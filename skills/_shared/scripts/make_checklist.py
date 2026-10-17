#!/usr/bin/env python3
"""Generate a blank assessment table from a framework reference file.

Usage:
  python3 make_checklist.py <framework> <kind> [--references <dir>]

framework: nist-pf | ai-rmf | iso-42001 | aiuc-1
kind:      profile  (Current and Target Profile rows, for program-assessment)
           soa      (Statement of Applicability rows, for controls-and-evidence;
                     aiuc-1 and iso-42001 only)

Reads the reference file's own tables, so every subcategory, control, or
requirement appears exactly once and nothing is retyped. Prints Markdown to
stdout; redirect it into the deliverable.
"""
import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_REFS = os.path.normpath(os.path.join(HERE, "..", "references"))

FILES = {
    "nist-pf": "nist-privacy-framework.md",
    "ai-rmf": "nist-ai-rmf.md",
    "iso-42001": "iso-42001.md",
    "aiuc-1": "aiuc-1.md",
}


def rows(framework, text):
    out = []
    if framework == "nist-pf":
        for m in re.finditer(r"^\| ((?:ID|GV|CT|CM|PR)\.[A-Z]{2}-P\d+) \| (.+?) \|$", text, re.M):
            out.append((m.group(1), m.group(2)))
    elif framework == "ai-rmf":
        for m in re.finditer(r"^\| ((?:GOVERN|MAP|MEASURE|MANAGE) \d+\.\d+) \| (.+?) \| (.+?) \| .*\|$", text, re.M):
            out.append((m.group(1), m.group(2)))
    elif framework == "iso-42001":
        for m in re.finditer(r"^\| ((?:A\.)?\d+(?:\.\d+)*) \| (.+?) \| .*\|$", text, re.M):
            out.append((m.group(1), m.group(2)))
    elif framework == "aiuc-1":
        for m in re.finditer(r"^\| ([A-F]\d{3}) \| (.+?) \| (Mandatory|Optional) \| (.*?) \| .*\|$", text, re.M):
            out.append((m.group(1), f"{m.group(2)} ({m.group(3)}; {m.group(4) or 'no tag'})"))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("framework", choices=FILES)
    ap.add_argument("kind", choices=["profile", "soa"])
    ap.add_argument("--references", default=DEFAULT_REFS)
    a = ap.parse_args()
    if a.kind == "soa" and a.framework not in ("aiuc-1", "iso-42001"):
        sys.exit("soa is only for aiuc-1 and iso-42001")
    path = os.path.join(a.references, FILES[a.framework])
    if not os.path.exists(path):
        sys.exit(f"Reference file not found: {path}")
    items = rows(a.framework, open(path, encoding="utf-8").read())
    if not items:
        sys.exit("No rows found; the reference file's table format may have changed.")
    if a.kind == "profile":
        print("| ID | Outcome | In Target Profile? (why) | Current state | Evidence (IDs or links) | Status | Gap | Priority |")
        print("|---|---|---|---|---|---|---|---|")
        for i, d in items:
            print(f"| {i} | {d} | | | | | | |")
    else:
        print("| ID | Requirement or control | Applies? | Justification for any exclusion | Opted in (optional items) | Company controls (CTL IDs) | Evidence (EV IDs) | Status |")
        print("|---|---|---|---|---|---|---|---|")
        for i, d in items:
            print(f"| {i} | {d} | | | | | | |")
    print(f"\n{len(items)} rows from {FILES[a.framework]}", file=sys.stderr)


if __name__ == "__main__":
    main()
