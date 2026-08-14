# Natural-Language Generation Contract

Use this contract for every new DeepStone artifact. The user may speak naturally; never require them to fill a form unless a missing decision would materially change the result.

## 1. Parse intent

Convert the request into this internal model:

```json
{
  "project": {"title": "", "client": "", "audience": "", "purpose": ""},
  "deliverables": ["html", "docx", "pptx", "pdf"],
  "language": "zh-CN|zh-TW|en|bilingual",
  "key_message": "",
  "content_units": [
    {"id": "U01", "role": "headline|argument|proof|detail|action|appendix", "source": "user|file|inference", "text": ""}
  ],
  "constraints": {"length": null, "deadline": null, "must_include": [], "must_not_invent": true}
}
```

Infer safe defaults. Ask only when audience, output format, or a legally meaningful content choice cannot be inferred. Never invent client facts, metrics, testimonials, dates, citations, or results.

## 2. Build one canonical content map

For multi-format work, create one content map before laying out any file. Give every unit a stable ID and role. Reuse meaning and evidence across formats, but rewrite length and sequencing for the medium.

- `headline`: one sentence-level takeaway.
- `argument`: the reasoning that supports the takeaway.
- `proof`: sourced metric, quote, table, image, or factual example.
- `detail`: supporting explanation that can move to notes or an appendix.
- `action`: requested decision or next step.
- `appendix`: necessary reference content that interrupts the main narrative.

## 3. Initialize the deliverable workspace

For new work, run:

```bash
python scripts/init_deliverable.py OUTPUT_DIR \
  --title "PROJECT TITLE" \
  --formats html,docx,pptx,pdf \
  --language zh-CN \
  --audience "AUDIENCE" \
  --purpose "PURPOSE" \
  --key-message "KEY MESSAGE"
```

The command is non-destructive: it refuses to overwrite existing scaffold files. It copies the official logos, fonts, tokens, editable starters, the brief manifest, content map, and QA checklist.

## 4. Generate natively by format

- HTML: edit the starter into semantic responsive HTML/CSS/JS. Keep local font and asset paths in the complete source folder. After final edits, run `scripts/build_standalone_html.py OUTPUT_DIR/index.html` to create a client-ready `{Project}_{Document}_DeepStone_Standalone.html`. Deliver the named standalone file as the primary artifact and keep the source folder as its editable companion; do not convert the page to an image or discard the source folder.
- DOCX: use the Documents workflow and named Word styles. The bundled DOCX is a style/layout reference, not a text container to blindly replace.
- PPTX: use the Presentations workflow and editable text/shapes. The bundled PPTX is a master-like reference. Keep one takeaway per slide.
- PDF: generate from the semantically correct source. Never make PDF the only editable source unless the request explicitly requires it.

When multiple formats are requested, do not finish one and mechanically convert it into all others. Adapt the shared content map independently.

## 5. Apply the DeepStone signature

Mandatory in every format:

- official color or white logo selected by background;
- for Word/PDF document pages, exactly one logo at the upper-right, right-edge aligned to the page margin;
- mandatory client-document first-page copy: `{项目名称} · {年份}` above the title, `Reinventing Real-World Value Onchain` immediately above the main title, and a localized lower-right confidentiality statement: `仅供授权客户参考` for Chinese-only documents; `For Authorized Clients Only` for English and Chinese-English bilingual documents;
- EB Garamond for Latin and Swei B2 Serif CJKtc for Chinese;
- in DOCX, semantic heading styles plus explicit brand-font attributes on every heading/display run so Office theme fonts cannot override the visual system;
- Figma-calibrated tokens from `assets/tokens.json`;
- editorial whitespace and exact alignment;
- one dominant message per page, slide, or screen section;
- approved dark-band or editorial-text gradient only where the medium supports it reliably;
- solid navy fallback in Word/PPT/PDF when gradients would rasterize text or reduce editability.

## 6. Verify before delivery

Render every applicable output, inspect it visually, and update `qa-checklist.json` with `pass`, `fail`, or `not_applicable` plus a short evidence note.

Delivery is incomplete when:

- a file was not opened/rendered after generation;
- a font silently fell back;
- the logo was recreated as text;
- content overflow or blank pages remain;
- different formats contradict one another;
- an unsourced fact or metric appears;
- the output merely screenshots another format.
- an HTML request lacks either the complete editable source folder or a meaningfully named standalone HTML;
- the standalone filename is generic (`index.html` or `Standalone.html`), still depends on a missing local presentation asset, or does not visually match the source HTML.

## 7. Delivery report

Return links to each artifact and summarize:

1. what was generated;
2. which source content and assumptions were used;
3. which QA checks passed;
4. any remaining provisional item or font-installation requirement.

For HTML, return the meaningfully named standalone file first and clearly label it as the file to forward. Return the complete source folder or `index.html` second as the editable source.

## Natural-language examples

- “把附件整理成一份面向董事会的 10 页中文 PPT，再做一个两页 Word 摘要和 PDF；数据不要改。”
- “用 DeepStone 设计语言做一个双语官网首页，主信息是我们的 RWA 发行服务，循环模块必须可以暂停。”
- “把这个客户方案统一成 DeepStone 风格，输出 Word 和 PDF，并保留客户原有 Logo。”
- “根据下面的访谈纪要做英文投资者简报；没有数字的地方不要自行补数字。”
