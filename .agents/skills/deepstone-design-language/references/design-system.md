# Deepstone Design System

Status: `v1.3.1 Figma-calibrated core + localized confidentiality + client-ready standalone HTML delivery`. Core homepage colors, typography, layout, buttons, cards, gradients, and bilingual behavior were read from the source Figma nodes listed in `assets/tokens.json`. Tokens marked as derived remain adaptable where the Figma file has no named variable.

## 1. Brand character

Deepstone should feel analytical, international, composed, and quietly confident. Its work should resemble a strong advisory firm or research-led technology business—not a playful consumer startup.

Five attributes govern every visual decision:

1. Structured: visible grid, consistent alignment, meaningful grouping.
2. Editorial: generous margins, disciplined typography, intentional pacing.
3. Technical: thin rules, restrained diagrams, labeled evidence, precise data.
4. Premium: high contrast, few colors, few effects, excellent spacing.
5. Human: readable prose, real imagery, natural language, no sterile dashboard overload.

## 2. Color grammar

Read exact values from `../assets/tokens.json`.

- `ink`: primary text and high-authority anchors.
- `navy` and `navyDeep`: the two stops of the approved dark-band gradient.
- `royal`: the Figma-documented hover/link blue `#094197`.
- `blue`: the end stop of the approved editorial-heading gradient.
- `paper`: warm-white main canvas.
- `mist`: quiet alternate surface and table background.
- `line`: structural rules and dividers.
- `muted`: secondary copy and metadata.

Recommended area distribution per composition:

- 65–80% paper/white;
- 15–30% navy/ink anchors;
- 3–8% royal/blue accent;
- below 3% status colors.

Only two gradients are approved: `gradient.darkBand` for dark section surfaces and `gradient.editorialText` for selected editorial headings. Do not invent additional gradients or use the text gradient for body copy.

## 3. Typography

Typography is a system of ratios, not a collection of decorative font choices.

### Families

- Latin: **EB Garamond**. Use the bundled variable font for Regular through SemiBold emphasis.
- Chinese: **Swei B2 Serif CJKtc**. Use Regular for body and SemiBold for headings/emphasis.
- Do not substitute another typeface when the bundled fonts can be installed, linked, or embedded.
- Emergency fallback only: Georgia for Latin and Songti SC / SimSun for Chinese. Mark the output as provisional when fallback is used.
- Do not introduce a third display or body family.
- In Word, do not rely only on inherited Heading styles for brand typography. Keep semantic Heading 1–3 styles, and also write explicit Latin/East Asian run-font attributes on every heading, callout title, and other display run so Office theme fonts cannot replace the brand fonts.

### Hierarchy

- Web hero: 46px, 1.6 line height; EB Garamond Bold in English and Swei B2 Serif CJKtc Medium in Chinese.
- Web editorial section title: 40px, 1.6 line height.
- Web feature/news title: 24px, 1.6 line height.
- Web body: 15px for compact cards; 18px/30px for long-form news copy.
- Display outside the calibrated website: 2.3–3.4× body; weight 600; max 2–3 lines.
- H1: 1.8–2.4× body; weight 600.
- H2: 1.35–1.7× body; weight 600.
- H3: 1.05–1.25× body; weight 600.
- Body: weight 400; line height 1.45–1.65.
- Label/meta: 0.72–0.85× body; weight 500–600; optional slight tracking.

Sentence case is the default. Avoid all caps except short navigation labels, eyebrow text, or table labels. Avoid centered body paragraphs.

## 4. Spacing and grid

Use the 4-point base scale from the token file. Prefer these named steps:

- `xs` 4: icon gaps and micro-alignment.
- `sm` 8: label-to-value spacing.
- `md` 16: card padding on compact surfaces.
- `lg` 24: standard block spacing.
- `xl` 32: module padding.
- `2xl` 48: section gaps.
- `3xl` 64: large section padding.
- `4xl` 96: desktop hero or editorial opening space.

### Grids

- HTML desktop reference: 1440px canvas, 152px principal left/right anchor, approximately 1136px content width; map this proportionally to fluid containers.
- HTML tablet: 8 columns, 20px gutters.
- HTML mobile: 4 columns, 16px gutters and 20–24px outer margins.
- Documents: 1- or 2-column editorial grid. Do not force a 12-column web grid onto paper.
- Document logo anchor: upper-right on Word and PDF pages, with its right edge aligned to the document's right content margin. Keep the logo inside the top safe area and separate from titles or running text.
- Presentations: 12-column logical grid with fixed safe margins; align every object to the same anchors.

Whitespace is an active element. A page that feels slightly sparse is preferable to one that feels crowded.

## 5. Shape and effects

- Default content-container radius: 0–8px depending on medium.
- Primary and secondary web buttons: 46px high with a 100px pill radius, 14px type, 1px ink/white outline, and a 20px arrow box.
- Pills outside buttons remain reserved for tags, filters, and compact statuses.
- Rules: 1px or 0.75pt, neutral line color.
- Shadows: use only for actual elevation or layered media; never as default card decoration.
- Borders: prefer one thin border over shadow plus border.
- Icons: simple outline icons at one consistent stroke weight. Do not mix icon families.

## 6. Composition patterns

### Mandatory client-document cover copy

Apply this three-part copy system to the first page of every client-facing proposal, report, presentation, leave-behind, and PDF. Treat the wording as brand-controlled content, not a placeholder:

1. Top project identifier: `{项目名称} · {年份}`. Replace generic labels such as `Client Feasibility Proposal`, `Company Presentation`, or `Proposal`.
2. Brand proposition immediately above the main title: `Reinventing Real-World Value Onchain`. Do not replace it with `DeepStone`, a document type, or a client name.
3. Lower-right confidentiality statement: use `仅供授权客户参考` only when the document is Chinese-only. Use `For Authorized Clients Only` when the document is English or Chinese-English bilingual. Do not use product-positioning copy in this position.

Keep the official DeepStone logo separately in the cover header. On Word and PDF covers, anchor it at the upper-right; use the white asset on a navy/dark cover and the color asset on a light cover. The proposition complements the logo and never substitutes for the logo asset. This cover rule does not apply to ordinary website landing pages unless the page intentionally represents a document cover.

### A. Editorial hero

Eyebrow → concise headline → supporting statement → one primary action → optional evidence/visual. Use asymmetry, not arbitrary diagonals.

### B. Navy anchor band

Use for a strong opening, a section reset, or final CTA. Keep text concise and high contrast. Allow one accent element only.

### C. Evidence grid

Use 2–4 columns for metrics, services, or proof. Each item contains label, value/title, one sentence, and optional source. Keep baseline alignment consistent.

### D. Split narrative

Use 5/7 or 4/8 proportions. One side contains the argument; the other contains evidence, imagery, a diagram, or selected facts.

### E. Insight list

Use strong titles, metadata, thin separators, and one controlled thumbnail ratio. Avoid generic card grids when a list communicates hierarchy better.

### F. Closing statement

Use generous space, one decisive sentence, and a single action. Do not add a redundant feature grid near the end.

## 7. Components

### Navigation

Logo left, concise destinations, one clear action. Maximum two navigation tiers. Mobile navigation must retain hierarchy rather than showing every option at once.

### Buttons

- Primary: royal fill, white text.
- Secondary: transparent or paper fill, ink border/text.
- Inverse: white or paper on navy.
- Text link: no container; use underline or directional cue.

Use short verb-led labels. Do not place more than two competing buttons together.

### Cards and blocks

Cards require a semantic reason: containment, comparison, or interaction. Editorial content should often use whitespace and rules instead of boxes.

### Tables

Use quiet headers, aligned numbers, short labels, and subtle row separators. Avoid full-grid borders. Highlight only the decision-relevant column or row.

### Forms

Labels above fields, visible focus, clear error text, and 44px minimum touch targets. Use a single-column form unless comparison or short paired fields justify two columns.

### Charts and diagrams

Start with ink/navy and one royal accent. Use direct labels when possible. Remove unnecessary legends, 3D effects, and heavy grid lines. Always include units and sources.

## 8. Imagery

Prefer real environments, architectural detail, technical process, material texture, or calm abstract geometry. Crop decisively. Avoid handshake stock photos, generic laptop scenes, neon AI imagery, and decorative city skylines without relevance.

Image ratios:

- cinematic hero: 16:9 or 2:1;
- editorial feature: 4:3;
- card thumbnail: 3:2;
- portrait/profile: 4:5;
- logo/mark: preserve intrinsic ratio.

## 9. Motion

Motion should explain sequence or maintain rhythm.

- Micro transitions: 160–240ms.
- Section transitions: 320–480ms.
- Carousel/loop dwell: 4–7s per item.
- Easing: ease-out for entrances, ease-in-out for state changes.
- Avoid simultaneous motion in more than two regions.
- Provide pause controls for autoplaying content.
- Respect `prefers-reduced-motion`; replace motion with a stable key frame.

## 10. Anti-patterns

Reject these even when they look fashionable:

- unapproved gradients outside `gradient.darkBand` and `gradient.editorialText`;
- oversized rounded cards everywhere;
- glass panels and glowing outlines;
- decorative blobs, sparkles, or generic AI symbols;
- five equal CTAs;
- arbitrary centered layouts;
- fake charts or invented metrics;
- dense slides with paragraph-sized body copy;
- web components pasted unchanged into Word or PowerPoint;
- inconsistent icon families or illustration styles.
