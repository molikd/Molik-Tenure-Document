# David Molik's tenure portfolio

LaTeX sources, supporting evidence and review documentation for David Molik's
Kansas State University reappointment and tenure portfolio, with a standalone CV.

## Build

Install Python 3 and a TeX Live distribution providing `pdflatex`, `biber` and
`latexmk`. From the repository root:

```sh
python3 scripts/build.py
```

Outputs are `build/main.pdf` (portfolio) and `build/main-cv.pdf` (CV).
Use `--verbose` for full build output or supply a root such as `main-cv.tex`.
See [BUILDING.md](BUILDING.md) for dependencies, cleanup, diagnostic logs,
CI behavior, integration tests and accessibility limitations.

## Documentation

- [2026 manuscript status](planning/2026-draft-status.md): implemented narrative and remaining submission requirements.
- `evidence-2026.tex`: compiled source index linked from the narrative.
- [Supplementary evidence](evidence/README.md): PDFs with evidence labels, placed with the relevant summaries and annual records.


- [2026 evidence register](planning/2026-evidence-register.md): supporting sources and evidence tracking.
- [2026 review checklist](planning/2026-review-checklist.md): portfolio review and content updates.
- [Template inventory](planning/latex-template-inventory.md): source structure and dependency decisions.
- [Template review plan](planning/latex-template-review.md): technical scope and acceptance criteria.
- [Issue #4](https://github.com/molikd/Molik-Tenure-Document/issues/4): tenure content/evidence work.
- [Issue #7](https://github.com/molikd/Molik-Tenure-Document/issues/7): template maintenance and build review.

## Source layout

| Path | Purpose |
| --- | --- |
| `main.tex` | Portfolio entry point, section order and embedded evidence |
| `main-cv.tex` | Standalone CV entry point |
| `shared/preamble.tex` | Shared packages, bibliography setup and presentation macros |
| `cv.tex` | CV content shared by both outputs |
| `achievements.tex`, `goals.tex`, `directed.tex`, `nondirected.tex`, `researchandcreative.tex` | Portfolio narrative sections |
| `*.bib` | Bibliographic records, selected by keyword filters |
| `evidence/` and source PDFs | Supporting documents, including signed evidence |
| `scripts/`, `tests/`, `.github/workflows/` | Build driver, checks and CI |
| `moderncv*`, `tweaklist.sty` | Vendored template dependencies |

## Making changes

Edit narrative sections and bibliographic records for content updates; use the
shared preamble for presentation changes affecting both outputs. Root-specific
settings belong in the appropriate entry point. Keep signed evidence PDFs
byte-identical and review both generated documents after layout changes.
Proposed word maximums are planning guidance until they come into force.

```sh
python3 tests/check_latex.py
python3 -m unittest discover -s tests -p 'test_*.py'
```

The real LaTeX failure test is opt-in; its command is in [BUILDING.md](BUILDING.md).
Generated outputs and temporary files are ignored. Source PDFs and bibliography
files remain eligible for version control.

## Citation and attribution

Use [CITATION.cff](CITATION.cff) to cite this repository; include the commit used
when reproducibility matters. Cite individual publications through their own
bibliographic records rather than treating this repository as their publisher.

Bundled template files retain their original author and license notices. Those
notices apply to their respective files; this repository does not assign a new
blanket license to the portfolio or supporting evidence.
