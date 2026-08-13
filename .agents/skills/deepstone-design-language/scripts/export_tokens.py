#!/usr/bin/env python3
"""Validate Deepstone tokens and export CSS or a normalized JSON theme."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parent.parent
TOKEN_PATH = SKILL_DIR / "assets" / "tokens.json"
REQUIRED_GROUPS = {"color", "gradient", "typography", "space", "radius", "border", "layout", "component", "motion"}
HEX_RE = re.compile(r"^#[0-9A-Fa-f]{6}$")


def load_tokens() -> dict:
    with TOKEN_PATH.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    missing = REQUIRED_GROUPS - data.keys()
    if missing:
        raise ValueError(f"Missing token groups: {', '.join(sorted(missing))}")
    for name, token in data["color"].items():
        value = token.get("value")
        if not isinstance(value, str) or not HEX_RE.match(value):
            raise ValueError(f"Invalid color token color.{name}: {value!r}")
    return data


def css_name(group: str, name: str) -> str:
    cooked = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", name).lower()
    return f"--ds-{group}-{cooked}"


def css_value(group: str, value: object) -> str:
    if group in {"space", "radius", "border", "component"} and isinstance(value, (int, float)):
        return f"{value}px"
    if group == "motion" and isinstance(value, (int, float)):
        return f"{value}ms"
    return str(value)


def css_token_value(group: str, name: str, value: object) -> str:
    if group == "typography" and name.endswith("Px") and isinstance(value, (int, float)):
        return f"{value}px"
    if group != "layout" or not isinstance(value, (int, float)):
        return css_value(group, value)
    if name == "documentMarginMm":
        return f"{value}mm"
    if name == "slideSafeMarginPercent":
        return f"{value}%"
    if name == "webColumns":
        return str(value)
    return f"{value}px"


def export_css(data: dict) -> str:
    lines = [":root {"]
    for group in sorted(REQUIRED_GROUPS):
        for name, token in data[group].items():
            lines.append(f"  {css_name(group, name)}: {css_token_value(group, name, token['value'])};")
    lines.append("}")
    return "\n".join(lines) + "\n"


def normalized_theme(data: dict) -> str:
    theme = {
        group: {name: token["value"] for name, token in data[group].items()}
        for group in sorted(REQUIRED_GROUPS)
    }
    theme["meta"] = data.get("meta", {})
    return json.dumps(theme, ensure_ascii=False, indent=2) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--format", choices=("css", "json", "validate"), default="validate")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    data = load_tokens()
    if args.format == "validate":
        output = "Deepstone tokens valid\n"
    elif args.format == "css":
        output = export_css(data)
    else:
        output = normalized_theme(data)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output, end="")


if __name__ == "__main__":
    main()
