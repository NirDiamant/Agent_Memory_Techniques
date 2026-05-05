#!/usr/bin/env python3
"""Validate prose style for Agent_Memory_Techniques.

Rules enforced:
- No em dashes (U+2014) or en dashes (U+2013) anywhere in prose.
- No banned marketing words in prose.

Scope: README.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md, CONTENT_STANDARDS.md,
       ROADMAP.md, SESSION_SUMMARY.md, all files under docs/, all per-technique
       READMEs, and all markdown cells inside the 30 notebooks under all_techniques/.

Code cells, code blocks inside markdown (fenced ```), URLs, HTML tags, and
image paths are skipped so we don't false-positive on legitimate code content.

Exit 0 if clean, 1 if any violation. Prints file:line:snippet for each hit.
"""
import json
import os
import re
import sys
import glob

BANNED_WORDS = [
    r"\bsimply\b",
    r"\bjust\b",
    r"\bobviously\b",
    r"\btrivial(?:ly)?\b",
    r"\bleverage\b",
    r"\bleveraging\b",
    r"\butilize(?:s|d)?\b",
    r"\bparadigm\b",
    r"\brobust(?:ly|ness)?\b",
    r"\bseamlessly?\b",
    r"\bcutting[- ]edge\b",
    r"\bno fluff\b",
    r"\bno BS\b",
]
BANNED_RE = re.compile("|".join(BANNED_WORDS), re.IGNORECASE)

# Characters we ban anywhere in prose.
EM_DASH = "—"  # —
EN_DASH = "–"  # –

# Lines inside fenced code blocks are skipped for banned-words but still
# checked for dashes (dashes in code are rare and usually mistakes in prose
# copy-pasted into examples; if a code block legitimately needs one, rework).


def repo_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def iter_prose_lines_markdown(text):
    """Yield (lineno, line) for prose lines. Strips fenced code blocks for
    banned-word checks but keeps them for dash checks.

    Returns tuples: (lineno, line, in_code_block)
    """
    in_code = False
    for i, line in enumerate(text.splitlines(), start=1):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code = not in_code
            yield (i, line, True)
            continue
        yield (i, line, in_code)


SKIP_FILE_MARKER = "validate-style: ignore-file"


def check_text(path, text, hits):
    if SKIP_FILE_MARKER in text:
        return
    for lineno, line, in_code in iter_prose_lines_markdown(text):
        # Dash checks everywhere.
        if EM_DASH in line:
            hits.append((path, lineno, "em-dash", line.rstrip()))
        if EN_DASH in line:
            hits.append((path, lineno, "en-dash", line.rstrip()))
        if in_code:
            continue
        # Banned word check skips fenced code blocks.
        # Also skip inline code spans (content between backticks).
        prose = re.sub(r"`[^`]*`", "", line)
        # Skip URLs and HTML tags. Replace with a space so adjacent
        # tag content stays separated (otherwise '<b>word</b><br>next'
        # becomes 'wordnext' and the word boundary check misses banned
        # words that sit against a tag on either side).
        prose = re.sub(r"https?://\S+", " ", prose)
        prose = re.sub(r"<[^>]+>", " ", prose)
        m = BANNED_RE.search(prose)
        if m:
            hits.append((path, lineno, f"banned:{m.group(0).lower()}", line.rstrip()))


def markdown_files():
    root = repo_root()
    paths = []
    for name in [
        "README.md",
        "CONTRIBUTING.md",
        "CODE_OF_CONDUCT.md",
        "CONTENT_STANDARDS.md",
        "ROADMAP.md",
        "SESSION_SUMMARY.md",
    ]:
        p = os.path.join(root, name)
        if os.path.exists(p):
            paths.append(p)
    paths.extend(sorted(glob.glob(os.path.join(root, "docs", "**", "*.md"), recursive=True)))
    paths.extend(sorted(glob.glob(os.path.join(root, "all_techniques", "*", "*.md"))))
    return paths


def notebooks():
    root = repo_root()
    return sorted(glob.glob(os.path.join(root, "all_techniques", "*", "*.ipynb")))


def check_notebook(path, hits):
    with open(path) as f:
        nb = json.load(f)
    for i, c in enumerate(nb["cells"]):
        if c.get("cell_type") != "markdown":
            continue
        src = c.get("source", "")
        if isinstance(src, list):
            src = "".join(src)
        # Tag hits with the cell index so the user can locate them.
        cell_hits = []
        check_text(f"{path}#cell{i}", src, cell_hits)
        hits.extend(cell_hits)


def main(argv):
    hits = []
    # Allow passing specific files; if none, scan defaults.
    if len(argv) > 1:
        for path in argv[1:]:
            if path.endswith(".ipynb"):
                check_notebook(path, hits)
            else:
                with open(path) as f:
                    check_text(path, f.read(), hits)
    else:
        for path in markdown_files():
            with open(path) as f:
                check_text(path, f.read(), hits)
        for path in notebooks():
            check_notebook(path, hits)

    if not hits:
        print("style: OK (no em/en dashes or banned words found)")
        sys.exit(0)

    # Group by file for readability.
    from collections import defaultdict

    by_file = defaultdict(list)
    for path, lineno, kind, line in hits:
        by_file[path].append((lineno, kind, line))

    print(f"style: {len(hits)} violations across {len(by_file)} files")
    for path, rows in sorted(by_file.items()):
        print(f"\n{path}")
        for lineno, kind, line in rows:
            trimmed = line.strip()[:120]
            print(f"  line {lineno} [{kind}]: {trimmed}")
    sys.exit(1)


if __name__ == "__main__":
    main(sys.argv)
