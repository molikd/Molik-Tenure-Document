# LaTeX template review plan

Tracking issue: https://github.com/molikd/Molik-Tenure-Document/issues/7

## Purpose

Review and modernize the underlying LaTeX/template code so the portfolio and standalone CV remain maintainable, reproducible and easy to update. This is a technical maintenance workstream separate from the tenure-content/evidence work in #4 and PR #6.

## Review scope

- [ ] Inventory the two entry points (`main.tex`, `main-cv.tex`), included sections, bibliography resources, custom macros and bundled ModernCV class/style files. Document intentional differences between outputs.
- [ ] Consolidate duplicated package, bibliography and identity configuration where appropriate while preserving output-specific styling and bibliography selection.
- [ ] Review custom section/title macros, repeated title handling, page breaks, spacing and long-link wrapping; replace fragile overrides with clear, documented interfaces.
- [ ] Audit unused packages, commented template scaffolding, legacy `.bst` files and bundled themes. Verify actual usage before removal; preserve third-party attribution/licenses.
- [ ] Compare the bundled ModernCV dependency with a supported upstream approach and document a compatibility/migration decision rather than upgrading blindly.
- [ ] Standardize LaTeX naming, formatting and file organization; keep content separate from presentation and avoid unrelated editorial changes.
- [ ] Review biblatex/biber resource loading, categories, sorting, citation keys and metadata validation without changing achievement classifications or publication facts.
- [ ] Document a reproducible local build for both roots, dependencies/engine choice, generated-output location and cleanup procedure.
- [ ] Review existing static checks and CI for meaningful regressions, reproducible dependencies, actionable log diagnostics and both document roots. Coordinate with the existing CI work carried by PR #6 rather than duplicating it.
- [ ] Review PDF navigation, metadata, text extraction, fonts and practical accessibility; explicitly document limitations of the chosen toolchain.

## Acceptance criteria

- Both documents build from a clean checkout using documented commands.
- No new undefined references/citations, missing assets, duplicate bibliography keys or unexplained warnings.
- Before/after visual review covers title pages, section headers, long URLs, bibliography pagination and embedded PDFs; intentional layout changes are documented.
- Signed evidence PDFs remain byte-identical. Portfolio claims, statuses and policy interpretation remain unchanged; proposed word maximums are not made mandatory.
- Meaningful checks cover changed failure modes, and remaining technical debt is recorded.

Start with an inventory and prioritized review findings. Implement subsequent fixes in small, reviewable commits after the review scope is established.
