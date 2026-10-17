#!/usr/bin/env python3
"""Create a control entry from the template, with the next free CTL ID.

Usage:
  python3 new_control.py <controls-folder> --title "Quarterly admin access review"
                         --objectives CCO-15 [CCO-22 ...] [--owner "IT lead"]
                         [--frequency quarterly] [--source "SOC 2 2026 CC6.2"]

Writes <controls-folder>/CTL-NNNN-<slug>.md from
controls-and-evidence/assets/control-entry-template.md and prints the path.
Fill in the description, coverage, evidence, and testing sections afterward,
then rebuild the index with build_register_index.py.
"""
import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.normpath(os.path.join(HERE, "..", "..", "controls-and-evidence", "assets", "control-entry-template.md"))


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:50]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder")
    ap.add_argument("--title", required=True)
    ap.add_argument("--objectives", nargs="+", required=True)
    ap.add_argument("--owner", default="TBC")
    ap.add_argument("--frequency", default="TBC")
    ap.add_argument("--source", default="TBC")
    a = ap.parse_args()
    bad = [o for o in a.objectives if not re.fullmatch(r"CCO-\d{2}", o)]
    if bad:
        sys.exit(f"Objectives must look like CCO-15: {bad}")
    os.makedirs(a.folder, exist_ok=True)
    used = [int(m.group(1)) for n in os.listdir(a.folder) for m in [re.match(r"CTL-(\d{4})", n)] if m]
    cid = f"CTL-{(max(used) + 1 if used else 1):04d}"
    t = open(TEMPLATE, encoding="utf-8").read()
    t = t.replace("id: CTL-NNNN", f"id: {cid}")
    t = re.sub(r'^title: .*$', f'title: {a.title}', t, count=1, flags=re.M)
    t = re.sub(r'^objectives: .*$', f'objectives: {", ".join(a.objectives)}', t, count=1, flags=re.M)
    t = re.sub(r'^owner: .*$', f'owner: {a.owner}', t, count=1, flags=re.M)
    t = re.sub(r'^frequency: .*$', f'frequency: {a.frequency}', t, count=1, flags=re.M)
    t = re.sub(r'^source: .*$', f'source: {a.source}', t, count=1, flags=re.M)
    t = t.replace("# Control: <name>", f"# Control: {a.title}")
    path = os.path.join(a.folder, f"{cid}-{slugify(a.title)}.md")
    if os.path.exists(path):
        sys.exit(f"Already exists: {path}")
    open(path, "w", encoding="utf-8").write(t)
    print(path)


if __name__ == "__main__":
    main()
