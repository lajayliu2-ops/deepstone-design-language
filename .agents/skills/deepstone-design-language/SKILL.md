---
name: deepstone-design-language
description: Create or restyle client-facing HTML pages, Word documents, PowerPoint decks, and PDFs in the Deepstone visual language. Use when the user asks for a Deepstone-style website, proposal, report, presentation, one-pager, case study, brochure, PDF, design system, branded artifact, or asks to apply the same design language across formats from a natural-language brief.
---

# Deepstone Design Language

Apply one shared visual grammar across HTML, DOCX, PPTX, and PDF. Treat the bundled token file as authoritative; adapt its expression to the target medium without changing the brand character.

## Workflow

1. Parse the brief into audience, purpose, deliverable, content hierarchy, required sections, language, and output format.
2. Read `references/design-system.md` completely.
3. Read `references/brand-assets.md` completely.
4. Read `references/generation-contract.md` completely. Use its canonical content model for one or multiple formats.
5. Read `references/format-mappings.md` for the requested output format.
6. Read `references/brief-and-qa.md` when the brief is incomplete and again before final verification.
7. Load `assets/tokens.json`. Use token names, not ad-hoc visual values.
8. For a new deliverable, run `scripts/init_deliverable.py` to seed a safe output folder, brand assets, brief manifest, content map, QA checklist, and optional starter artifacts. Skip only when editing an existing user file.
9. Select one composition pattern from the format mapping. Do not invent a new visual direction unless the user explicitly asks.
10. Produce the artifact with the matching document, presentation, PDF, or site tooling and follow that tool's own render-and-verify workflow.
11. Render the result and inspect it visually. Revise until it passes the Deepstone QA gates and update the generated `qa-checklist.json`.

## Non-negotiables

- Preserve the Deepstone signature: editorial whitespace, dark navy anchors, restrained royal-blue emphasis, thin rules, modular information blocks, precise alignment, EB Garamond for Latin text, and Swei B2 Serif CJKtc for Chinese text.
- In document-style Word and PDF pages, place the DeepStone logo once per page at the upper-right, aligned to the right page margin. Use the white logo on dark pages and the color logo on light pages; never place the document logo at upper-left.
- For every client-facing document, proposal, report, presentation, and exported PDF, apply the mandatory first-page cover copy defined in `references/design-system.md`: project name plus year above the title, `Reinventing Real-World Value Onchain` immediately above the main title, and `仅供授权客户参考` in the lower-right confidentiality position.
- Use one dominant message per page, slide, or screen section.
- Keep decoration subordinate to information. Never add generic gradients, floating blobs, glassmorphism, excessive shadows, or random iconography.
- Use no more than one primary accent color and one optional status color in a composition.
- Keep content containers square or lightly rounded. Buttons are the intentional exception and use the Figma-calibrated 100px pill radius.
- Use photography or diagrams only when they add evidence or meaning.
- Maintain accessible color contrast, readable type sizes, and reduced-motion behavior.
- Never detach visual style from content hierarchy: hierarchy comes before ornament.

## Format routing

- HTML or website: generate semantic, responsive HTML/CSS. Run `scripts/export_tokens.py --format css` when a CSS variable file is useful.
- Word/DOCX: use the Documents workflow. Use section bands, rules, tables, and restrained callouts rather than web-like cards everywhere.
- PowerPoint/PPTX: use the Presentations workflow. Build slide masters/layouts conceptually from the shared tokens; prioritize projection readability.
- PDF: create from the most semantically suitable source—HTML for screen-first reports, DOCX for editorial documents, or PPTX for landscape decks—then render and inspect every page.
- Multiple formats: create a shared content outline first, then adapt layout independently per medium. Do not merely screenshot or paste one format into another.

## Required output behavior

When important brand assets are missing, use a clearly labeled placeholder and continue. State which inputs are provisional. Do not block on optional assets.

For each delivered artifact, report:

- format and file path;
- content or assumptions used;
- provisional visual values, if any;
- render/QA result;
- any missing brand assets that would materially improve fidelity.

## Resources

- `assets/tokens.json`: machine-readable source of truth.
- `assets/logos/`: official color and white/inverse DeepStone logos. Use the color version on light surfaces and the white version on navy/dark surfaces.
- `assets/fonts/`: bundled EB Garamond and Swei B2 Serif CJKtc font files plus their OFL licenses.
- `references/design-system.md`: visual grammar and component rules.
- `references/brand-assets.md`: mandatory logo and font usage.
- `references/format-mappings.md`: HTML, Word, PPT, and PDF adaptations.
- `references/generation-contract.md`: deterministic natural-language-to-artifact contract and multi-format content model.
- `references/brief-and-qa.md`: brief schema, prompt examples, and QA gates.
- `scripts/export_tokens.py`: validate tokens and export CSS or a normalized theme manifest.
- `scripts/init_deliverable.py`: create a reusable project scaffold from a natural-language brief.
- `assets/templates/`: editable HTML, DOCX, and PPTX starters plus a PDF visual reference.
