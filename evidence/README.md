# Supplementary evidence

Assembly issue: [hail-local #53](https://github.com/molikd/hail-local/issues/53).
Broader portfolio tracker: [#4](https://github.com/molikd/Molik-Tenure-Document/issues/4).

The portfolio ends with its source notes, a linked supplementary-material index,
and 29 included PDF documents (497 source pages selected from 30 retained
originals totaling 563 pages). `supplements-2026.tex` controls
order. Each page has its evidence mark, document number, source page position,
and portfolio page number, outside the source image. Narrative tags display plain-language labels such as
`[EVIDENCE: Funding and proposal records]`. Tags in the Statement are unlinked;
tags in the detailed sections link to the corresponding source notes; the notes link to individual PDFs such as G1.1.
The standalone CV does not include this material.

`supplements.json` records each document's mark, title, path, source locator,
original page count, SHA-256 digest and interpretation limits. Optional
`included_pages` lists select intact source pages in ascending order; an empty
list retains the original but omits it from assembly. Without that field, the
whole PDF is included. The issue-attachment PDFs
were copied from the retained September 15 review files; proposal PDFs came
from the candidate-supplied OneDrive ZIPs and FFAR application. Original files
are preserved byte-for-byte. The KPI appendix uses the reviewed August 31
snapshot, not a newer or locally re-saved report.

The source index preserves distinctions between submissions, awards, drafts,
AI-generated notes, proposed services and completed outcomes. Including a
source does not independently validate every statement it contains. Missing
mailbox exports, Word/Excel originals and official current-year records remain
tracked in issue #4. The superseded recommendation form and duplicate unsigned
records are not included as current evidence. Full proposal packages may
contain personal and collaborator information; retain the portfolio's existing
reviewer-access controls.

To add a PDF, retain the original, append its metadata to `supplements.json`,
add its index line and `\evidencepdf` call to `supplements-2026.tex`, and link it
from the appropriate evidence note. Use a stable suffix under the existing
mark. Name evidence files descriptively with words joined by `_` and a single
terminal `.pdf` (no other `.` in the name), e.g. `<filename_with_words>.pdf`.
Include every source page unless a documented contribution-based excerpt or
redundancy decision is recorded in the manifest. For an excerpt, use the same
explicit page list in the optional argument to `\evidencepdf`; original page
numbers must remain visible. Omitted sources have no appendix destination and
are linked directly from the source notes. Rebuild both roots, run the static and unit
checks, verify source hashes/page counts and links, and inspect the rendered
labels and source pages. Do not replace source PDFs to add labels.

D1.4 is the candidate-supplied July 15, 2026 Research Weekly newsletter, added
September 23. It preserves all five pages and confirms publication of the
open-access/open-data article on pages 3–4; authorship is candidate-confirmed.

September 28 selections and their rationale are documented in the
[issue #32 verification](../planning/2026-issue-32-verification.md). G1.7 is
retained but not embedded; G2.1 includes pages 1–2 and N2.1 includes pages 2–7
and 18–19. G2.2 remains complete. No source PDF was rewritten.


October 15 post-cutoff supplement: U1.1 retains all 28 pages of the publisher
accepted manuscript for *How to write (and review) a Genome Report*. U1 records
direct source observations for seven additional developments. Private mailbox,
Teams and working-document exports remain outstanding; observations are labeled
rather than presented as embedded original evidence. See
[the discovery report](../planning/2026-10-15-update-discovery-report.md).

October 16: P1.4 adds the candidate-supplied 24-page 2026 evaluation, retained
byte-identical with its digital signature. Both signatures appear on the ratings
page (5); the supervisor acknowledgment line on page 14 is blank. The 2025
evaluation remains included. See the final submission review for remaining items.

The signed original is retained separately from `evidence/2026/evaluation_2026_packet_display.pdf`.
The latter is generated using `qpdf --flatten-annotations=all` to preserve the
visible digital signature during LaTeX inclusion. It is a display derivative,
not a cryptographically signed original; its hash is recorded in the manifest.
