# Format Mappings

Use this file after reading `design-system.md`. Preserve shared tokens and hierarchy while adapting composition to the medium.

## HTML

### Structure

- Use semantic landmarks: `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`.
- Use CSS custom properties exported from `assets/tokens.json`.
- Define local `@font-face` rules for bundled EB Garamond and Swei B2 Serif CJKtc assets. List EB Garamond first and Swei second so mixed-language text selects the intended glyph source.
- Use the official white logo in dark/navy navigation or hero regions and the official color logo on light surfaces.
- Use `gradient.darkBand` for approved dark sections and `gradient.editorialText` for selected 40px/24px editorial headings. Provide the corresponding solid navy fallback for print and reduced rendering environments.
- Match the calibrated desktop anchors: 1440px reference canvas, 152px principal margin, 46px pill buttons, 14px button labels, and 36px card padding. Convert these to fluid proportions rather than hard-coding a fixed desktop canvas.
- Use a responsive 12/8/4-column system and container queries or media queries where appropriate.
- Maintain a readable text measure of 55–75 characters for prose.
- Use one H1 per page and a valid heading hierarchy.
- For document-style HTML, use the mandatory cover copy: `{项目名称} · {年份}` in the top identifier, `Reinventing Real-World Value Onchain` above the H1, and the localized confidentiality statement at lower right: Chinese-only `仅供授权客户参考`; English and Chinese-English bilingual `For Authorized Clients Only`.

### Page sequence

Default corporate page:

1. Navigation
2. Editorial hero
3. Trust/evidence strip
4. Core offer or argument
5. Split narrative with evidence
6. Insights or proof
7. Closing navy CTA
8. Footer

Remove sections that do not serve the brief. Do not fill the sequence with invented content.

### Responsive behavior

- Stack split layouts below tablet width.
- Keep important actions visible without duplicating them excessively.
- Convert multi-column evidence blocks into a single readable sequence on mobile.
- Reduce display size and spacing proportionally; do not merely shrink the desktop canvas.
- Autoplay media must be muted, pausable, and replaced by a static frame under reduced-motion preferences.

### HTML QA

Check keyboard focus, contrast, responsive overflow, heading order, reduced motion, alt text, print styling, and real content length.

### HTML delivery

- Preserve the complete editable folder containing `index.html`, `assets/`, tokens, source media, brief, content map, and QA checklist.
- After the final source edit, run `python scripts/build_standalone_html.py OUTPUT_DIR/index.html`. The default output name is read from `deepstone-brief.json` or derived from the HTML title using `{Project}_{Document}_DeepStone_Standalone.html`.
- Treat the named standalone file as the primary file for individual sharing. It must embed all local presentation assets, including both DeepStone logo variants when referenced, EB Garamond, Swei B2 Serif CJKtc, images, local CSS, icons, and local JavaScript.
- Fail the standalone build when a referenced local asset is missing or a remote presentation asset remains. Use `--allow-remote-assets` only when the user explicitly accepts online dependencies.
- Render the source and named standalone versions at the same desktop and mobile widths and verify visual parity before delivery.

## Word / DOCX

### Page setup

- Default A4 portrait unless the user specifies another size.
- Margins: 18–22mm for reports; 24–28mm for formal proposals.
- Body: 9.5–11pt; leading 1.15–1.35 depending on density.
- Use a restrained header/footer with document title, section, date, and page number.
- Set Latin run fonts to `EB Garamond` and East Asian run fonts to `Swei B2 Serif CJKtc` in styles and direct runs. Include the bundled font files with delivery when font embedding is unavailable.
- Harden Heading 1–3 and all display/callout-title runs against Office theme fallback: set explicit `ascii`, `hAnsi`, and `cs` to `EB Garamond`, set `eastAsia` to `Swei B2 Serif CJKtc`, and remove `*Theme` font attributes. A heading style without matching direct run fonts does not pass QA.
- Use the official white logo on dark cover bands and the official color logo in light headers or covers.
- Place the logo once per page at the upper-right. In Word, use a right-aligned header for light interior pages; for a dark first-page cover, use a separate first-page header or a right-aligned logo inside the cover's top band so the inverse logo sits on dark. Do not duplicate the logo in both places.
- Align the logo's right edge to the 18–28mm right page margin selected for the document. Recommended rendered width: 34–48mm, reduced only when the page format requires it while respecting the 32mm minimum.
- Translate the approved dark gradient to a solid `color.navy` band when Word cannot render the gradient reliably; do not introduce a new Office theme color.
- On page one, use `{项目名称} · {年份}` above the title, `Reinventing Real-World Value Onchain` immediately above the main title, and the localized lower-right confidentiality statement: Chinese-only `仅供授权客户参考`; English and Chinese-English bilingual `For Authorized Clients Only`.

### Mapping

- HTML hero → cover or opening title block.
- Navy anchor band → full-width section divider or top/bottom band, not a heavy box on every page.
- Evidence grid → aligned table without visible outer grid or a two-column fact block.
- Cards → bordered callout, sidebar, or ruled subsection.
- CTA → next-step panel or final action page.
- Navigation → table of contents and running headers.

### Styles

Create named paragraph styles for Title, Subtitle, Heading 1–3, Body, Lead, Caption, Quote, Table Header, and Callout. Do not format paragraphs manually when a style can express the rule.

### Word QA

Check widow/orphan control, table splitting, page breaks, heading hierarchy, TOC accuracy, page numbers, image resolution, and whether every page has a deliberate visual anchor. Inspect rendered Heading 1/2, callout titles, numbered-step titles, bullets, and body copy together; reject any sans-serif or theme-font fallback.

## PowerPoint / PPTX

### Canvas and typography

- Default 16:9 widescreen.
- Safe margin: at least 5% of slide width.
- Slide title: typically 26–34pt.
- Body: typically 16–22pt; never below 14pt unless it is a source note.
- Source/footer: 9–11pt.
- Set Latin text to `EB Garamond` and Chinese text to `Swei B2 Serif CJKtc`. Include the bundled fonts with delivery if the deck cannot embed them.
- Place the white logo on navy slides and the color logo on paper/mist slides. Never recreate the logo with editable text.
- Use `color.navy` as the projection-safe fallback for `gradient.darkBand`; use `color.blue` or `color.navy` as a solid heading color instead of rasterizing gradient text.
- On slide one, use `{项目名称} · {年份}` in the top project identifier, `Reinventing Real-World Value Onchain` above the main title, and the localized confidentiality statement at lower right: Chinese-only `仅供授权客户参考`; English and Chinese-English bilingual `For Authorized Clients Only`.

### Slide grammar

Use a limited master set:

1. Navy cover
2. Section divider
3. Statement slide
4. Two-column argument/evidence
5. Metric or evidence grid
6. Chart with takeaway
7. Case study
8. Timeline/process
9. Closing action

Each slide must communicate one sentence-level takeaway. Titles should state the takeaway, not merely name the topic.

### Mapping

- Web sections become individual slides or short slide sequences.
- Long prose becomes speaker notes or a supporting document.
- Evidence cards become aligned metric blocks.
- Web navigation is removed; use section markers and progress cues sparingly.
- A table becomes a chart, a prioritized subset, or an appendix table depending on purpose.

### PowerPoint QA

Inspect every rendered slide at fit-to-window and thumbnail scale. Check projection readability, text overflow, alignment, contrast, chart labeling, and consistency of master-like elements.

## PDF

Choose the source format based on reading behavior:

- screen-first, interactive, or responsive report → HTML to PDF;
- formal editorial report or proposal → DOCX to PDF;
- landscape presentation or leave-behind deck → PPTX to PDF.

### PDF rules

- Define real page breaks; never rely on accidental browser pagination.
- Embed EB Garamond and Swei B2 Serif CJKtc whenever the PDF source path supports embedding. If a tool substitutes fonts, stop and fix the font path or disclose that the PDF is provisional.
- Use the raster logo assets at sufficient size; never typeset the logo from separate text.
- Place the logo once per portrait document page at the upper-right, aligned to the right page margin. Use a consistent top offset across pages of the same class; switch only the color/inverse asset according to the background.
- Preserve selectable text and working links.
- Include bookmarks for reports longer than ten pages when practical.
- Keep important tables and figures with their captions.
- Avoid color-dependent meaning; labels must remain understandable in grayscale.
- Preserve the source document's mandatory first-page cover copy exactly: `{项目名称} · {年份}`, `Reinventing Real-World Value Onchain`, and the applicable localized confidentiality statement. Chinese-only uses `仅供授权客户参考`; English and Chinese-English bilingual use `For Authorized Clients Only`.

### PDF QA

Render all pages to images. Check clipping, blank pages, orphan headings, broken links, raster quality, font substitution, and page-to-page rhythm.

## Cross-format adaptation

When one brief requests multiple formats:

1. Create a canonical content outline and evidence inventory.
2. Assign every content unit a role: headline, argument, proof, detail, action, or appendix.
3. Map roles separately to each format.
4. Reuse tokens and visual grammar, not pixel dimensions.
5. Verify that every format remains native to its medium.

The formats should feel like members of one family, not copies of one another.
