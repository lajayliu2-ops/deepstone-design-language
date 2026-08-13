# Brief Schema and QA

## Minimum brief

Infer what is safe and ask only for missing information that materially changes the result.

```yaml
project:
  title: ""
  client: ""
  deliverable: html | docx | pptx | pdf | multi
  audience: ""
  purpose: inform | persuade | propose | report | explain
content:
  source_material: []
  required_sections: []
  key_message: ""
  calls_to_action: []
brand:
  logo: "assets/logos/deepstone-logo-color.png"
  inverse_logo: "assets/logos/deepstone-logo-white.png"
  primary_color_override: null
  fonts: ["EB Garamond", "Swei B2 Serif CJKtc"]
  imagery: []
constraints:
  language: zh-CN | en | bilingual
  page_or_slide_target: null
  deadline: null
  accessibility: WCAG-AA
```

If the user supplies only a short prompt, proceed with placeholders for missing logo or imagery and clearly identify them.

## Natural-language examples

- “用 Deepstone 风格把这份市场报告做成 12 页中文 PPT，面向董事会。”
- “根据以下文案生成一个 Deepstone 风格的双语官网首页 HTML。”
- “把客户方案整理成正式的 Word 提案，并同时导出 PDF。”
- “将这个 PPT、Word 和网页统一成同一套 Deepstone 设计语言。”
- “做一份 Deepstone 风格的案例研究，不要添加我没有提供的数据。”

## Content integrity

- Never invent customer names, facts, metrics, quotes, citations, or case studies.
- Label sample content as sample content.
- Separate evidence from interpretation.
- Preserve legally or financially meaningful wording unless the user authorizes rewriting.
- For bilingual work, maintain semantic parity; do not let translation change the hierarchy.

## Visual QA gates

An artifact passes only when all applicable gates are true.

### Shared

- Uses only defined or explicitly overridden tokens.
- Uses the official DeepStone logo asset, never a text recreation.
- Uses EB Garamond for Latin and Swei B2 Serif CJKtc for Chinese; any fallback is disclosed.
- Contains a clear message hierarchy.
- Has one primary accent and no decorative visual noise.
- Uses consistent alignment, radius, rule, and icon styles.
- Meets accessible contrast and readable minimum type sizes.
- Contains no invented evidence.
- Has been rendered and visually inspected.
- Every client-facing document cover uses `{项目名称} · {年份}`, `Reinventing Real-World Value Onchain`, and `仅供授权客户参考` in their prescribed positions.
- Every Word/PDF document page uses exactly one DeepStone logo at the upper-right, aligned to the right page margin, with the correct light/dark asset.

### HTML

- Works at desktop, tablet, and mobile widths.
- Has no horizontal overflow.
- Keyboard focus is visible.
- Motion has pause/reduced-motion behavior.
- Print output is intentional if PDF export is expected.

### DOCX

- Named styles are used consistently.
- Heading and display runs explicitly declare EB Garamond for Latin and Swei B2 Serif CJKtc for East Asian text; no Office theme-font attributes remain on those runs.
- Rendered Heading 1/2, callout titles, numbered-step titles, bullets, and body text form one coordinated serif system with no unexplained sans-serif fallback.
- When a PDF render is available for QA, its font inventory identifies EB Garamond rather than a substituted Latin family.
- The right-aligned header or first-page cover anchor contains one logo only; there is no upper-left or duplicate logo.
- No unintended blank pages, split headings, clipped tables, or isolated captions.
- Page numbers and TOC are correct when present.

### PPTX

- Every slide has one takeaway.
- No text overflow or undersized body copy.
- Alignment remains consistent at thumbnail scale.
- Charts state units, sources, and conclusions.

### PDF

- Every page has been rendered.
- The logo is consistently upper-right on every document page and uses the correct color variant.
- Text remains selectable and fonts render correctly.
- Links, page breaks, bookmarks, and image quality are acceptable.

## Fidelity notes

Core v1.0 values have been calibrated from the editable Figma node context. For future Figma revisions, re-check:

- named color styles and variable modes beyond the calibrated homepage;
- any changed font weights, line heights, or bilingual overrides;
- frame grids and responsive breakpoints;
- component variants and radii;
- motion timings and easing;
- logo clear space and minimum sizes if the official brand manual changes.
