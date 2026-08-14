# Brand Assets

These rules are mandatory for every Deepstone artifact.

## Logo

- Light background: use `assets/logos/deepstone-logo-color.png`.
- Navy or dark background: use `assets/logos/deepstone-logo-white.png`.
- Preserve the original aspect ratio of 742:229.
- Never typeset, redraw, trace, stretch, crop, recolor, or separate the Latin and Chinese portions.
- Keep clear space of at least 12% of the logo height on every side.
- Minimum rendered width: 120px on screen, 32mm in documents, or 1.25in in presentations.
- Alt text: `DeepStone Tech 深石科技`.
- Word/PDF document pages: place the logo once at the upper-right. Align its right edge with the page's right content margin and keep at least the standard clear space from the top edge and nearby text. Do not pair it with a second logo elsewhere on the same page.
- Word/PDF covers: white logo on navy/dark; color logo on light. Word/PDF interior pages: color logo on light; white logo only when the entire top area behind it is dark.
- This document-only upper-right rule does not override website navigation or presentation-master placement.

The inverse asset was made with a lossless color-only transformation: every visible RGB pixel is white while the original alpha channel and geometry remain unchanged.

## Fonts

### Latin

- Family: `EB Garamond`.
- Regular/body: 400.
- Medium emphasis: 500.
- Headings: 600.
- Italics: use the bundled italic variable font.
- Office-compatible static faces: use bundled `EBGaramond-Regular.ttf` and `EBGaramond-SemiBold.ttf` for Word/LibreOffice rendering; keep the family name `EB Garamond` in the document.

### Chinese

- Family: `Swei B2 Serif CJKtc`.
- Figma-calibrated website body, navigation, and hero: Medium 500 using the bundled Medium file.
- Regular 400 is available for denser office documents where Medium would reduce legibility.
- Headings/emphasis: 600 using the bundled SemiBold file.

### Mixed-language text

Apply EB Garamond as the Latin font and Swei B2 Serif CJKtc as the East Asian font within the same style/run where the file format supports separate script fonts. For CSS, list EB Garamond first and Swei second; the browser will fall through to the CJK font for Chinese glyphs.

## Font delivery

- HTML editable source folder: reference bundled Regular, Medium, and SemiBold local fonts with `@font-face`; do not depend on a CDN in final deliverables.
- HTML standalone delivery: run `scripts/build_standalone_html.py` after final source edits so the official logo, fonts, images, local stylesheets, icons, and scripts are embedded as data or inline content. Preserve the source folder separately; never make the standalone file the only editable source.
- DOCX/PPTX: set the exact font family in styles and include the bundled static Office faces and CJK fonts next to the deliverable when embedding is unavailable. For DOCX headings and display text, also set explicit `ascii`, `hAnsi`, `cs`, and `eastAsia` run-font attributes and remove theme-font attributes; do not rely on style inheritance alone.
- PDF: embed fonts whenever supported and inspect the final PDF for substitution.
- Licenses: retain both OFL files in `assets/fonts/` whenever fonts are redistributed.
