#!/usr/bin/env python3
"""Find where a provision, requirement, or term is cited.

Usage:
  python3 find_citations.py <pattern> <folder> [<folder> ...] [--regex]

Searches *.md files for the pattern (plain text by default, case-insensitive)
and prints each hit as path:line with a snippet, grouped by file, then a
count per folder. Use it to see which reference files, skills, and
deliverables a change touches, for example:

  python3 find_citations.py "Art. 33" ../_shared/references ../../compliance
  python3 find_citations.py "C011|C012|D002" ../../compliance --regex
"""
import argparse
import os
import re
import sys


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pattern")
    ap.add_argument("folders", nargs="+")
    ap.add_argument("--regex", action="store_true")
    a = ap.parse_args()
    pat = re.compile(a.pattern if a.regex else re.escape(a.pattern), re.I)
    totals = {}
    for folder in a.folders:
        if not os.path.isdir(folder):
            print(f"(skipping {folder}: not a folder)", file=sys.stderr)
            continue
        totals[folder] = 0
        for dirpath, _, names in os.walk(folder):
            for n in sorted(names):
                if not n.endswith(".md"):
                    continue
                p = os.path.join(dirpath, n)
                try:
                    lines = open(p, encoding="utf-8").read().split("\n")
                except (OSError, UnicodeDecodeError):
                    continue
                hits = [(i + 1, l) for i, l in enumerate(lines) if pat.search(l)]
                if hits:
                    print(f"\n{p} ({len(hits)})")
                    for ln, l in hits[:20]:
                        s = l.strip()
                        print(f"  {ln}: {s[:160]}{'…' if len(s) > 160 else ''}")
                    if len(hits) > 20:
                        print(f"  … {len(hits) - 20} more")
                    totals[folder] += len(hits)
    print("\nTotals:")
    for f, c in totals.items():
        print(f"  {f}: {c}")


if __name__ == "__main__":
    main()
