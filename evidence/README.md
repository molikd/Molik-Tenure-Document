# Supplementary evidence

Assembly issue: [hail-local #53](https://github.com/molikd/hail-local/issues/53).
Broader portfolio tracker: [#4](https://github.com/molikd/Molik-Tenure-Document/issues/4).

The portfolio ends with its source notes, a linked supplementary-material index,
and 27 complete PDF documents (506 source pages). `supplements-2026.tex` controls
order. Each page has its evidence mark, document number, source page position,
and portfolio page number, outside the source image. Narrative marks such as
G1 link to the source notes; the notes link to individual PDFs such as G1.1.
The standalone CV does not include this material.

`supplements.json` records each document's mark, title, path, source locator,
page count, SHA-256 digest and interpretation limits. The issue-attachment PDFs
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
Include every source page. Rebuild both roots, run the static and unit
checks, verify source hashes/page counts and links, and inspect the rendered
labels and source pages. Do not replace source PDFs to add labels.
