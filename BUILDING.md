# Building the documents locally

Requires TeX Live (or equivalent) with `pdflatex`, `biber`, and `latexmk`.
The repository is self-contained: the ModernCV class, its themes, and all
section/bibliography inputs travel with it, including the shared preamble in
`shared/`.

```sh
# Portfolio (49 pages) and standalone CV (6 pages), artifacts to ./build:
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex main-cv.tex

# Static checks (no TeX installation needed):
python3 tests/check_latex.py

# Clean generated files (sources are never modified by a build):
latexmk -C -outdir=build
```

Both roots must build with no errors; `tests/check_latex.py` must pass with
no failures (one known warning: the dateless `software.bib` entry).
Overleaf: import the whole repository; both roots compile there unchanged
because all inputs, including `shared/`, are relative paths.
