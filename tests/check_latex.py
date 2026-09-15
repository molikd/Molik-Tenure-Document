#!/usr/bin/env python3
"""Static checks for the tenure LaTeX sources.

Runs with stdlib-only Python 3; no TeX installation needed, so this doubles
as the fast CI job while latexmk handles full compilation. Fails (exit 1)
on anything that breaks the build or silently drops content; prints
non-failing warnings for items needing owner input.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []
warnings = []


def fail(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def root_sources():
    return sorted(ROOT.glob("*.tex")) + sorted(ROOT.glob("*.bib"))


# --- 1. Duplicate bibliography keys (biber errors out) ---------------------
keys = {}
for bib in sorted(ROOT.glob("*.bib")):
    text = bib.read_text(encoding="utf-8")
    for match in re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,", text):
        key = match.group(1)
        if key in keys:
            fail(f"duplicate bib key '{key}': {keys[key].name} and {bib.name}")
        keys[key] = bib

# --- 2. Per-entry field checks ----------------------------------------------
ENTRY_RE = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)(?=^@|\Z)", re.S | re.M)
for bib in sorted(ROOT.glob("*.bib")):
    text = bib.read_text(encoding="utf-8")
    for entry in ENTRY_RE.finditer(text):
        kind, key, body = entry.group(1).lower(), entry.group(2), entry.group(3)
        fields = re.findall(r"^\s*([A-Za-z-]+)\s*=", body, re.M)
        seen = set()
        for field in fields:
            lowered = field.lower()
            if lowered in seen:
                fail(f"{bib.name}: entry '{key}' has duplicate field '{field}'")
            seen.add(lowered)
        month = re.search(r"month\s*=\s*\{([^}]*)\}", body)
        if month and not re.fullmatch(r"\d+", month.group(1).strip()):
            fail(f"{bib.name}: entry '{key}' month must be an integer, "
                 f"got '{month.group(1)}'")
        if not re.search(r"^\s*(?:year|date)\s*=", body, re.I | re.M):
            warn(f"{bib.name}: entry '{key}' has no year/date "
                 f"(biber warns; ydnt sorting placement suffers)")

# --- 3. Every \cite key must exist -------------------------------------------
for source in root_sources():
    text = source.read_text(encoding="utf-8")
    for match in re.finditer(r"\\cite\{([^}]*)\}", text):
        for key in match.group(1).split(","):
            key = key.strip()
            if key and key not in keys:
                fail(f"{source.name}: citation '{key}' has no bib entry")

# --- 4. Codepoints pdflatex cannot handle ------------------------------------
# The kernel covers quotes/dashes; narrow nbsp (U+202F) and non-breaking
# hyphen (U+2011) are fatal. Extend this set if a new one bites.
BAD_CODEPOINTS = {0x202F: "narrow no-break space", 0x2011: "non-breaking hyphen"}
for source in root_sources():
    for number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
        for char in line:
            if ord(char) in BAD_CODEPOINTS:
                fail(f"{source.name}:{number}: {BAD_CODEPOINTS[ord(char)]} "
                     f"(U+{ord(char):04X}) breaks pdflatex")

# --- 5. Regression words: typos fixed in review must not return --------------
wordlist = ROOT / "tests" / "regression-words.txt"
words = []
for raw in wordlist.read_text(encoding="utf-8").splitlines():
    s = raw.strip()
    if not s or s.startswith("#"):
        continue
    words.append(s)
for source in root_sources():
    # .bib URLs/DOIs are identifiers, not prose; skip them here.
    if source.suffix == ".bib":
        continue
    text = source.read_text(encoding="utf-8")
    for word in words:
        if word in text:
            fail(f"{source.name}: forbidden string '{word}' is back")

# --- 6. Structural invariants --------------------------------------------------
main = (ROOT / "main.tex").read_text(encoding="utf-8")
if not re.search(r"^\\firstname\{", main, re.M):
    fail("main.tex: \\firstname must be active (moderncv fatals without it)")
if not re.search(r"^\\familyname\{", main, re.M):
    fail("main.tex: \\familyname must be active (moderncv fatals without it)")
if r"\begin{titlepage}" in main:
    fail("main.tex: titlepage environment does not exist in moderncv")
if re.search(r"^\s*\\makecvtitle\b", main, re.M):
    fail("main.tex: \\makecvtitle may only be called once per document; "
         "sections must use \\portfoliotitle")
for section in ["achievements", "goals", "directed", "nondirected",
                "researchandcreative", "cv"]:
    text = (ROOT / f"{section}.tex").read_text(encoding="utf-8")
    if re.search(r"^\s*\\makecvtitle\b", text, re.M):
        fail(f"{section}.tex: use \\portfoliotitle instead of \\makecvtitle")

for message in warnings:
    print(f"warning: {message}", file=sys.stderr)
if errors:
    print(f"{len(errors)} check(s) failed:", file=sys.stderr)
    for message in errors:
        print(f"  - {message}", file=sys.stderr)
    sys.exit(1)
print(f"all static checks passed ({len(warnings)} warning(s)).")
