# Building the documents locally

Requires TeX Live (or equivalent) with `pdflatex`, `biber`, and `latexmk`.
The repository is self-contained: the ModernCV class, its themes, and all
section/bibliography inputs travel with it, including the shared preamble in
`shared/`.

```sh
# Portfolio (including full evidence PDFs) and standalone CV, artifacts to ./build:
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex main-cv.tex

# Static checks (no TeX installation needed):
python3 tests/check_latex.py

# Remove the generated build directory, including driver logs and metadata:
# Run from the repository root.
rm -rf build/
```

Both roots must build with no errors; `tests/check_latex.py` must pass with
no failures (one known warning: the dateless `software.bib` entry).
## Overleaf

Import the whole repository, including `shared/` and the vendored ModernCV files.
Select **pdfLaTeX** and set the main document to `main.tex` (portfolio) or
`main-cv.tex` (CV), not `shared/preamble.tex` or an individual narrative section.
The inputs use relative paths. Local and CI builds do not replace an Overleaf
smoke test with the selected project's TeX Live version.

Each root loads `shared/preamble` and then selects its literal theme with
`\moderncvcolor{purple}` or `\moderncvcolor{black}`. If an older Overleaf copy
reports an undefined `\KPIModerncvColor` followed by missing `moderncvcolor.sty`,
sync both roots and `shared/preamble.tex` together and recompile from scratch.
The missing unsuffixed filename is a consequence of the undefined color command;
do not create an empty `moderncvcolor.sty` to hide it. The real theme files are
`moderncvcolorpurple.sty` and `moderncvcolorblack.sty`, both included here.

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

## Diagnostic acceptance test

Run `RUN_LATEX_INTEGRATION=1 python3 -m unittest discover -s tests -p 'test_*.py'`
with TeX installed. The fourth test copies the repository into a temporary
directory, injects an undefined control sequence, and verifies nonzero status,
source-error visibility and retained native/summary logs without altering sources.
Normal output labels dependency checks, actual latexmk rule passes, log audits
and successful outputs; verbose output additionally streams full native messages.
