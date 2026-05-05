#!/usr/bin/env python3
"""Validate Jupyter notebook cell structure for Agent_Memory_Techniques.

Rules enforced:
- No code cell has more than MAX_LINES source lines.
- Every code cell is preceded by a non-empty markdown cell.

Exit 0 if every target passes, 1 otherwise. Prints a report either way.

Usage:
  python utils/validate_cells.py                  # scan all notebooks under all_techniques/
  python utils/validate_cells.py path/one.ipynb   # scan specific notebooks
"""
import json
import os
import sys
import glob

MAX_LINES = 60


def check_notebook(path):
    with open(path) as f:
        nb = json.load(f)
    cells = nb["cells"]
    long_cells = []
    no_md = []
    for i, c in enumerate(cells):
        if c.get("cell_type") != "code":
            continue
        src = c.get("source", "")
        if isinstance(src, list):
            src = "".join(src)
        lines = src.count("\n") + 1 if src else 0
        if lines > MAX_LINES:
            long_cells.append((i, lines))
        prev = cells[i - 1] if i > 0 else None
        ok = False
        if prev and prev.get("cell_type") == "markdown":
            psrc = prev.get("source", "")
            if isinstance(psrc, list):
                psrc = "".join(psrc)
            if psrc.strip():
                ok = True
        if not ok:
            no_md.append(i)
    return long_cells, no_md


def default_targets():
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return sorted(glob.glob(os.path.join(here, "all_techniques", "*", "*.ipynb")))


def main(argv):
    targets = argv[1:] if len(argv) > 1 else default_targets()
    total_long = 0
    total_no_md = 0
    any_fail = False
    print(f"{'notebook':<50} {'long':>5} {'no-md':>6}")
    for path in targets:
        long_cells, no_md = check_notebook(path)
        name = os.path.basename(os.path.dirname(path))
        total_long += len(long_cells)
        total_no_md += len(no_md)
        flag = " FAIL" if (long_cells or no_md) else ""
        print(f"{name:<50} {len(long_cells):>5} {len(no_md):>6}{flag}")
        if long_cells or no_md:
            any_fail = True
            for idx, ln in long_cells:
                print(f"  long cell #{idx}: {ln} lines (limit {MAX_LINES})")
            if no_md:
                print(f"  no-md-above at cells: {no_md}")
    print()
    print(f"TOTAL long={total_long} no-md={total_no_md}")
    sys.exit(1 if any_fail else 0)


if __name__ == "__main__":
    main(sys.argv)
