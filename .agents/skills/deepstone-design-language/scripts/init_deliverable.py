#!/usr/bin/env python3
"""Create a non-destructive DeepStone deliverable scaffold."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = SKILL_DIR / "assets"
ALLOWED_FORMATS = {"html", "docx", "pptx", "pdf"}
TEMPLATE_MAP = {
    "html": ("deepstone-starter.html", "index.html"),
    "docx": ("deepstone-starter.docx", "DeepStone-template.docx"),
    "pptx": ("deepstone-starter.pptx", "DeepStone-template.pptx"),
    "pdf": ("deepstone-reference.pdf", "DeepStone-reference.pdf"),
}


def confidentiality_copy(language: str) -> str:
    """Chinese only for pure Chinese briefs; English for English or bilingual briefs."""
    normalized = language.strip().lower().replace("_", "-")
    chinese_only_tags = {"zh", "zh-cn", "zh-sg", "zh-tw", "zh-hk", "zh-hans", "zh-hant"}
    return "仅供授权客户参考" if normalized in chinese_only_tags else "For Authorized Clients Only"


def standalone_filename(title: str) -> str:
    """Create a recognizable, client-ready standalone HTML filename."""
    base = re.sub(r"[^\w]+", "_", title, flags=re.UNICODE).strip("_")
    base = base[:120].rstrip("_") or "DeepStone_Deliverable"
    if "deepstone" not in base.lower():
        base += "_DeepStone"
    return f"{base}_Standalone.html"


def write_new(path: Path, content: str) -> None:
    if path.exists():
        raise FileExistsError(f"Refusing to overwrite existing scaffold file: {path}")
    path.write_text(content, encoding="utf-8")


def copy_tree_missing(source: Path, target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)
    for item in source.iterdir():
        destination = target / item.name
        if destination.exists():
            continue
        if item.is_dir():
            shutil.copytree(item, destination)
        else:
            shutil.copy2(item, destination)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--title", required=True)
    parser.add_argument("--formats", default="html")
    parser.add_argument("--language", default="zh-CN")
    parser.add_argument("--audience", default="client stakeholders")
    parser.add_argument("--purpose", default="inform and persuade")
    parser.add_argument("--key-message", default="")
    args = parser.parse_args()

    formats = [value.strip().lower() for value in args.formats.split(",") if value.strip()]
    invalid = sorted(set(formats) - ALLOWED_FORMATS)
    if not formats or invalid:
        raise SystemExit(f"Formats must be one or more of {sorted(ALLOWED_FORMATS)}; invalid={invalid}")

    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    assets_out = output_dir / "assets"
    for name in ("logos", "fonts"):
        copy_tree_missing(ASSETS_DIR / name, assets_out / name)
    shutil.copy2(ASSETS_DIR / "tokens.json", assets_out / "tokens.json")

    template_dir = ASSETS_DIR / "templates"
    for format_name in formats:
        source_name, target_name = TEMPLATE_MAP[format_name]
        source = template_dir / source_name
        if source.exists() and not (output_dir / target_name).exists():
            shutil.copy2(source, output_dir / target_name)

    brief = {
        "schema": "deepstone-brief/v1",
        "project": {
            "title": args.title,
            "client": "",
            "audience": args.audience,
            "purpose": args.purpose,
        },
        "deliverables": formats,
        "language": args.language,
        "key_message": args.key_message,
        "content_units": [],
        "constraints": {"must_include": [], "must_not_invent": True},
        "brand": {
            "logo_color": "assets/logos/deepstone-logo-color.png",
            "logo_inverse": "assets/logos/deepstone-logo-white.png",
            "latin_font": "EB Garamond",
            "cjk_font": "Swei B2 Serif CJKtc",
            "tokens": "assets/tokens.json",
            "confidentiality": confidentiality_copy(args.language),
        },
    }
    if "html" in formats:
        brief["html_delivery"] = {
            "source_folder": ".",
            "source_entry": "index.html",
            "standalone_entry": standalone_filename(args.title),
            "standalone_required": True,
            "standalone_is_primary_delivery": True,
        }
    write_new(output_dir / "deepstone-brief.json", json.dumps(brief, ensure_ascii=False, indent=2) + "\n")

    content_map = """# Canonical content map\n\n| ID | Role | Source | Content | Format notes |\n|---|---|---|---|---|\n| U01 | headline | user |  |  |\n| U02 | argument | user |  |  |\n| U03 | proof | user/file |  |  |\n| U04 | action | user |  |  |\n"""
    write_new(output_dir / "content-map.md", content_map)

    checks = {
        "schema": "deepstone-qa/v1",
        "status_values": ["pending", "pass", "fail", "not_applicable"],
        "checks": [
            {"id": "brand.logo", "status": "pending", "evidence": ""},
            {"id": "brand.fonts", "status": "pending", "evidence": ""},
            {"id": "brand.confidentiality_language", "status": "pending", "evidence": ""},
            {"id": "content.no_invention", "status": "pending", "evidence": ""},
            {"id": "layout.hierarchy", "status": "pending", "evidence": ""},
            {"id": "layout.overflow", "status": "pending", "evidence": ""},
            {"id": "accessibility.contrast", "status": "pending", "evidence": ""},
            {"id": "render.visual_inspection", "status": "pending", "evidence": ""},
            {"id": "html.source_folder_preserved", "status": "pending" if "html" in formats else "not_applicable", "evidence": ""},
            {"id": "html.standalone_assets_embedded", "status": "pending" if "html" in formats else "not_applicable", "evidence": ""},
            {"id": "html.standalone_visual_parity", "status": "pending" if "html" in formats else "not_applicable", "evidence": ""},
            {"id": "html.client_ready_filename", "status": "pending" if "html" in formats else "not_applicable", "evidence": ""},
            {"id": "cross_format.semantic_parity", "status": "pending", "evidence": ""},
        ],
    }
    write_new(output_dir / "qa-checklist.json", json.dumps(checks, ensure_ascii=False, indent=2) + "\n")
    print(output_dir)


if __name__ == "__main__":
    main()
