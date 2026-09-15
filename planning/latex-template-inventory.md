# LaTeX template inventory and findings

Tracking issue: https://github.com/molikd/Molik-Tenure-Document/issues/7
Plan: `planning/latex-template-review.md`. Baseline: both roots build clean
(`latexmk -pdf main.tex main-cv.tex`), static checks pass with one known
warning (dateless `software.bib` entry).

The findings below describe the original inventory; completion is recorded at the end.

## Entry points and inputs

- `main.tex` — portfolio: cover page, `recommendation.pdf`, employment
  history, `achievements/goals/directed/nondirected/researchandcreative.tex`,
  `pd.pdf`, `evidence/2025/evaluation-signed.pdf`,
  `evidence/2025/reappointment-letter-signed.pdf`, then `cv.tex`.
- `main-cv.tex` — standalone CV: preamble plus `cv.tex` only.
- `cv.tex` is shared verbatim by both roots (personal data, experience,
  education, keyword-filtered bibliographies, grants, teaching).
- Bibliographies: `journal/conference/corresponding/whitepapers/talks/
  gradthesis/ugradthesis/software/internal.bib`, all loaded in `main.tex`;
  `main-cv.tex` loads the first seven only. Filtering is by bib `keywords=`;
  see below for dead category code.

## Custom macros

- `\portfoliotitle` (both roots, identical bodies): repeatable section
  header; required because moderncv's `\makecvtitle` allocates layout lengths
  with `\newcommand` and can run only once per document. Keep.
- `\Colorhref[color]{url}{text}` (both roots, identical): violet hyperlinks
  used throughout `cv.tex`. Keep; candidate for the shared preamble.
- `\cvdoublecolumn` (both roots): zero uses anywhere. Dead — remove.

## Findings (prioritized)

### P0 — dead code and files (safe removals, verified unreferenced)

1. `\DeclareBibliographyCategory` x9–10 plus the commented `\forcsvlist`
   categorization in both preambles: nothing ever populates the categories;
   every `\printbibliography` filters by `keywords=`. Remove.
2. `\cvdoublecolumn` in both roots: defined twice, used nowhere. Remove.
3. `evaluation.tex` (182 lines): no preamble, `\input` nowhere, superseded by
   `evidence/2025/evaluation-signed.pdf`. Remove in its own commit.
4. `plainyrrev.bst` (22K) + `vancouver.bst` (41K): BibTeX styles, unreachable
   under the biblatex/biber workflow; nothing references them (sources, tests,
   CI). Remove in its own commit.
5. `picture.jpg` (15K): only commented `\photo` references. Keep — documents
   the photo option and costs nothing.

### P1 — structural consolidation

6. Both roots duplicate ~95 preamble lines (documentclass, theme, geometry,
   xurl, biblatex setup + 7 shared resources, font/icon packages, `Colorhref`,
   `\portfoliotitle`). Extract `shared/preamble.tex` holding the common core;
   roots keep only what differs (theme color, `pdfpages`/spacing, the two
   extra bib resources + categories, personal data). `\input` with a
   subdirectory works on Overleaf. Verify with before/after builds and text
   comparison.
7. Extend `tests/check_latex.py` `root_sources()` to `shared/*.tex` so the
   extracted preamble stays under static checks.

### P2 — documented decisions (no change)

8. Keep vendored ModernCV v1.2.0 (2012): upstream is v2.x with visibly
   different styling; restyling mid-tenure-season is unacceptable risk, and
   vendoring keeps the Overleaf import self-contained and pinned. No upgrade.
9. Keep all bundled theme/color files: they are upstream's set;
   `moderncvcompatibility.sty` and `tweaklist.sty` are loaded by
   `moderncv.cls` itself. Deleting fragments of a vendored dependency saves
   nothing and risks breakage.
10. Keep `\usepackage{marvosym}` in both roots: `moderncv.cls` defines
    `\marvosymbol` via the `mvs` font family, which exists only when the
    package is loaded — it drives the contact icons. Likewise keep
    `fontawesome5`/`academicons` (active in `cv.tex` extrainfo).
11. Keep commented photo/social/mobile scaffolding: documents optional
    template features, zero build effect.
12. CI (`test.yml`: static checks + both-root `latexmk` builds) already covers
    this workstream — coordinate, do not duplicate. PDF metadata
    (`pdftitle`/`pdfauthor`) is unset; recorded as a limitation rather than
    changed, since per-root titles would complicate the shared preamble.

### P3 — deferred

- ModernCV v2 migration (post-tenure).
- `picture.jpg` removal if the photo option is definitively unwanted.
- Merging `evaluation.tex` prose anywhere (content workstream, not template).

## PR #8 reconciliation

Items 1–4 and 6–7 are implemented: dead definitions/files removed, common
preamble extracted and checked. Items 5 and 8–11 are intentional retention
decisions. Item 12 is superseded by the logged Python build driver and CI artifact
uploads; both roots now set author and distinct titles after ModernCV initializes
hyperref. Source headers document section ownership and presentation boundaries.

Existing font substitutions and over/underfull boxes remain baseline warnings.
Before/after comparison found identical rendered pixels and extracted text on
all 55 pages. BUILDING.md records navigation/accessibility limitations.
CI uses the action's supported frozen TeX Live 2024 image; local builds use 2026.
Hosted validation of that environment remains blocked by GitHub account billing.
