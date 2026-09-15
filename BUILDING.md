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
latexmk -C -outdir=build main.tex main-cv.tex
```

Both roots must build with no errors; `tests/check_latex.py` must pass with
no failures (one known warning: the dateless `software.bib` entry).
Overleaf: import the whole repository; both roots compile there unchanged
because all inputs, including `shared/`, are relative paths.

## Logged build and troubleshooting

The preferred command is `python3 scripts/build.py`. Add `--verbose` to stream
full subprocess output, or specify `main.tex` or `main-cv.tex` to build one root.
The driver runs static checks, records tool versions, and invokes latexmk (which
manages LaTeX/biber passes). `build/*-build.log` retains commands, output, elapsed
time and exit status. Native `.log`/`.blg` files remain alongside each PDF;
`*-diagnostics.txt` summarizes actionable errors and layout warnings with log
line numbers. TeX's `-file-line-error` also supplies source locations.

Missing dependencies return status 2; failed checks/builds or missing expected
artifacts return a nonzero status. Layout warnings remain visible but nonfatal:
the current template has existing header/CV overflow warnings. Do not suppress
new warnings merely to obtain green CI. Never infer success from an old PDF
when the current command failed. Diagnostic tests run with
`python3 -m unittest discover -s tests -p 'test_*.py'`.

CI uses the action-supported frozen TeX Live 2024 image and the same driver.
Local validation used TeX Live 2026. Versions are recorded rather than
claiming bit-identical output across OS/font/toolchain versions. CI retains logs
for 14 days even after failure, but does not upload evidence PDFs. Logs can
contain source excerpts and should be reviewed before external sharing. A job
that never starts (for example an Actions billing limit) has no compiler log and
requires an account-level fix, not a LaTeX workaround.

## Dependency and PDF review decisions

Keep the vendored ModernCV for this review cycle: changing its major version
requires a separate layout migration. Preserve vendor licenses and comment local
interfaces rather than rewriting upstream files. Both roots share the preamble;
CV-specific identity fields stay in the CV until content owners reconcile them.
Bibliography loading intentionally differs between roots; filters use keywords.

Each root supplies PDF author/title metadata. The document has selectable text
and hyperlinks but is **not a certified tagged PDF/PDF-UA document**. Embedded
signed PDFs retain their original accessibility limitations. A future tagged-PDF
migration needs dedicated reading-order and assistive-technology review. Keep
signed evidence byte-identical, and compare page renderings after macro changes.
