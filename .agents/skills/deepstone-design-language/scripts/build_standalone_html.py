#!/usr/bin/env python3
"""Build a single-file DeepStone HTML with local presentation assets embedded."""

from __future__ import annotations

import argparse
import base64
import html as html_module
import json
import mimetypes
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


CSS_URL_RE = re.compile(r"url\(\s*(['\"]?)([^'\")]+)\1\s*\)", re.IGNORECASE)
STYLESHEET_RE = re.compile(
    r"<link\b(?=[^>]*\brel\s*=\s*(['\"])[^'\"]*stylesheet[^'\"]*\1)[^>]*>",
    re.IGNORECASE,
)
SCRIPT_RE = re.compile(
    r"<script\b(?P<before>[^>]*?)\bsrc\s*=\s*(?P<quote>['\"])(?P<url>[^'\"]+)(?P=quote)(?P<after>[^>]*)>\s*</script>",
    re.IGNORECASE,
)
SCRIPT_BLOCK_RE = re.compile(r"<script\b[^>]*>.*?</script>", re.IGNORECASE | re.DOTALL)
MEDIA_ATTR_RE = re.compile(
    r"(?P<prefix>\b(?:src|poster)\s*=\s*)(?P<quote>['\"])(?P<url>[^'\"]+)(?P=quote)",
    re.IGNORECASE,
)
SRCSET_RE = re.compile(
    r"(?P<prefix>\bsrcset\s*=\s*)(?P<quote>['\"])(?P<value>[^'\"]+)(?P=quote)",
    re.IGNORECASE,
)
HREF_RE = re.compile(r"\bhref\s*=\s*(['\"])([^'\"]+)\1", re.IGNORECASE)
REL_RE = re.compile(r"\brel\s*=\s*(['\"])([^'\"]+)\1", re.IGNORECASE)
TITLE_RE = re.compile(r"<title\b[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)


MIME_OVERRIDES = {
    ".css": "text/css",
    ".js": "text/javascript",
    ".mjs": "text/javascript",
    ".svg": "image/svg+xml",
    ".ttf": "font/ttf",
    ".otf": "font/otf",
    ".woff": "font/woff",
    ".woff2": "font/woff2",
}


class StandaloneBuilder:
    def __init__(self, source: Path, allow_remote_assets: bool = False) -> None:
        self.source = source.resolve()
        self.root = self.source.parent
        self.allow_remote_assets = allow_remote_assets
        self.cache: dict[Path, str] = {}
        self.embedded: set[Path] = set()

    @staticmethod
    def is_remote(url: str) -> bool:
        parsed = urlsplit(url.strip())
        return parsed.scheme.lower() in {"http", "https", "//"} or bool(parsed.netloc)

    @staticmethod
    def is_embedded_or_navigation(url: str) -> bool:
        value = url.strip().lower()
        return value.startswith(("data:", "blob:", "mailto:", "tel:", "javascript:", "#"))

    def resolve_local(self, url: str, base: Path) -> Path | None:
        value = url.strip()
        if self.is_embedded_or_navigation(value):
            return None
        if self.is_remote(value):
            if self.allow_remote_assets:
                return None
            raise ValueError(f"Remote presentation asset is not standalone: {value}")
        parsed = urlsplit(value)
        if parsed.scheme or parsed.netloc:
            return None
        candidate = (base / unquote(parsed.path)).resolve()
        try:
            candidate.relative_to(self.root)
        except ValueError as exc:
            raise ValueError(f"Asset escapes the deliverable folder: {value}") from exc
        if not candidate.is_file():
            raise FileNotFoundError(f"Referenced asset is missing: {value} -> {candidate}")
        return candidate

    def data_uri(self, path: Path) -> str:
        if path not in self.cache:
            mime = MIME_OVERRIDES.get(path.suffix.lower()) or mimetypes.guess_type(path.name)[0]
            if not mime:
                mime = "application/octet-stream"
            payload = base64.b64encode(path.read_bytes()).decode("ascii")
            self.cache[path] = f"data:{mime};base64,{payload}"
        self.embedded.add(path)
        return self.cache[path]

    def replace_css_urls(self, css: str, base: Path) -> str:
        def replace(match: re.Match[str]) -> str:
            original = match.group(2)
            path = self.resolve_local(original, base)
            return match.group(0) if path is None else f'url("{self.data_uri(path)}")'

        return CSS_URL_RE.sub(replace, css)

    def inline_stylesheet(self, match: re.Match[str]) -> str:
        tag = match.group(0)
        href = HREF_RE.search(tag)
        if not href:
            return tag
        path = self.resolve_local(href.group(2), self.root)
        if path is None:
            return tag
        css = self.replace_css_urls(path.read_text(encoding="utf-8"), path.parent)
        self.embedded.add(path)
        return f"<style data-standalone-source=\"{path.name}\">\n{css}\n</style>"

    def inline_script(self, match: re.Match[str]) -> str:
        path = self.resolve_local(match.group("url"), self.root)
        if path is None:
            return match.group(0)
        code = path.read_text(encoding="utf-8")
        self.embedded.add(path)
        attrs = f"{match.group('before')}{match.group('after')}".strip()
        attrs = f" {attrs}" if attrs else ""
        return f"<script{attrs} data-standalone-source=\"{path.name}\">\n{code}\n</script>"

    def replace_media_attr(self, match: re.Match[str]) -> str:
        path = self.resolve_local(match.group("url"), self.root)
        if path is None:
            return match.group(0)
        quote = match.group("quote")
        return f"{match.group('prefix')}{quote}{self.data_uri(path)}{quote}"

    def replace_srcset(self, match: re.Match[str]) -> str:
        rewritten: list[str] = []
        for candidate in match.group("value").split(","):
            parts = candidate.strip().split()
            if not parts:
                continue
            path = self.resolve_local(parts[0], self.root)
            if path is not None:
                parts[0] = self.data_uri(path)
            rewritten.append(" ".join(parts))
        quote = match.group("quote")
        return f"{match.group('prefix')}{quote}{', '.join(rewritten)}{quote}"

    def inline_icon_links(self, html: str) -> str:
        link_re = re.compile(r"<link\b[^>]*>", re.IGNORECASE)

        def replace(match: re.Match[str]) -> str:
            tag = match.group(0)
            rel = REL_RE.search(tag)
            href = HREF_RE.search(tag)
            if not rel or not href or "icon" not in rel.group(2).lower().split():
                return tag
            path = self.resolve_local(href.group(2), self.root)
            if path is None:
                return tag
            quote = href.group(1)
            new_href = f"href={quote}{self.data_uri(path)}{quote}"
            return tag[: href.start()] + new_href + tag[href.end() :]

        return link_re.sub(replace, html)

    @staticmethod
    def transform_outside_scripts(html: str, transform) -> str:
        """Apply an HTML rewrite without interpreting JavaScript as markup."""
        output: list[str] = []
        cursor = 0
        for match in SCRIPT_BLOCK_RE.finditer(html):
            output.append(transform(html[cursor : match.start()]))
            output.append(match.group(0))
            cursor = match.end()
        output.append(transform(html[cursor:]))
        return "".join(output)

    def assert_no_local_presentation_refs(self, html: str) -> None:
        unresolved: list[str] = []

        def inspect(url: str) -> None:
            value = url.strip()
            if self.is_embedded_or_navigation(value):
                return
            if self.is_remote(value) and self.allow_remote_assets:
                return
            unresolved.append(value)

        for match in SCRIPT_RE.finditer(html):
            inspect(match.group("url"))

        markup = SCRIPT_BLOCK_RE.sub("", html)
        for match in CSS_URL_RE.finditer(markup):
            inspect(match.group(2))
        for match in MEDIA_ATTR_RE.finditer(markup):
            inspect(match.group("url"))
        for match in STYLESHEET_RE.finditer(markup):
            href = HREF_RE.search(match.group(0))
            if href:
                inspect(href.group(2))

        if unresolved:
            preview = ", ".join(dict.fromkeys(unresolved))
            raise ValueError(f"Standalone HTML still contains presentation asset references: {preview}")

    def build(self) -> str:
        html = self.source.read_text(encoding="utf-8")
        html = self.transform_outside_scripts(
            html,
            lambda value: CSS_URL_RE.sub(
                lambda match: self.replace_css_urls(match.group(0), self.root), value
            ),
        )
        html = STYLESHEET_RE.sub(self.inline_stylesheet, html)
        html = SCRIPT_RE.sub(self.inline_script, html)
        html = self.transform_outside_scripts(
            html, lambda value: SRCSET_RE.sub(self.replace_srcset, value)
        )
        html = self.transform_outside_scripts(
            html, lambda value: MEDIA_ATTR_RE.sub(self.replace_media_attr, value)
        )
        html = self.inline_icon_links(html)
        marker = "<!-- DeepStone Standalone HTML: local presentation assets embedded. -->"
        if marker not in html:
            html = html.replace("<html", f"{marker}\n<html", 1)
        self.assert_no_local_presentation_refs(html)
        return html


def standalone_filename(title: str) -> str:
    """Create a recognizable, client-ready standalone HTML filename."""
    base = re.sub(r"[^\w]+", "_", title, flags=re.UNICODE).strip("_")
    base = base[:120].rstrip("_") or "DeepStone_Deliverable"
    if "deepstone" not in base.lower():
        base += "_DeepStone"
    return f"{base}_Standalone.html"


def default_output_path(source: Path) -> Path:
    brief_path = source.parent / "deepstone-brief.json"
    title = ""
    if brief_path.is_file():
        try:
            brief = json.loads(brief_path.read_text(encoding="utf-8"))
            title = str(brief.get("project", {}).get("title", "")).strip()
            configured = str(brief.get("html_delivery", {}).get("standalone_entry", "")).strip()
            if configured:
                return source.with_name(Path(configured).name)
        except (json.JSONDecodeError, OSError, TypeError, ValueError):
            pass
    if not title:
        match = TITLE_RE.search(source.read_text(encoding="utf-8"))
        if match:
            title = html_module.unescape(re.sub(r"<[^>]+>", "", match.group(1))).strip()
    if not title:
        title = source.parent.name or source.stem
    return source.with_name(standalone_filename(title))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Completed source HTML, normally index.html")
    parser.add_argument(
        "output",
        type=Path,
        nargs="?",
        help="Optional explicit output path. Default: client-ready name from deepstone-brief.json or the HTML title",
    )
    parser.add_argument(
        "--allow-remote-assets",
        action="store_true",
        help="Allow remote display assets to remain linked; local assets are still embedded",
    )
    args = parser.parse_args()

    source = args.source.resolve()
    if not source.is_file():
        raise SystemExit(f"Source HTML not found: {source}")
    output = args.output.resolve() if args.output else default_output_path(source)
    if output == source:
        raise SystemExit("Output must differ from source; keep the editable source HTML intact")

    builder = StandaloneBuilder(source, allow_remote_assets=args.allow_remote_assets)
    standalone = builder.build()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(standalone, encoding="utf-8")
    print(f"{output}\nembedded_files={len(builder.embedded)}\nbytes={output.stat().st_size}")


if __name__ == "__main__":
    main()
