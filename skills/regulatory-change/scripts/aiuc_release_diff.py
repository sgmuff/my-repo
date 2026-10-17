#!/usr/bin/env python3
"""Compare a new AIUC-1 release with the suite's reference file.

Usage:
  curl -sL https://standard.aiuc-1.com/llms.txt -o /tmp/aiuc-llms.txt
  python3 aiuc_release_diff.py /tmp/aiuc-llms.txt [--reference ../../_shared/references/aiuc-1.md]

Parses the requirement list in AIUC's llms.txt index ("A001: Title" links,
with "[Retired]" markers) and the requirement tables in aiuc-1.md, then
prints requirements added, retired, renamed, and newly reinstated. It
doesn't edit anything; the regulatory-change skill proposes the edits.
Mandatory/optional status and capability tags live on the domain pages,
so check those for changes too.
"""
import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_REF = os.path.normpath(os.path.join(HERE, "..", "..", "_shared", "references", "aiuc-1.md"))


def from_index(text):
    reqs = {}
    for m in re.finditer(r"\[([A-F]\d{3}): (\\?\[Retired\] )?([^\]]+)\]", text):
        reqs[m.group(1)] = {"title": m.group(3).strip(), "retired": bool(m.group(2))}
    return reqs


def from_reference(text):
    reqs = {}
    for m in re.finditer(r"^\| ([A-F]\d{3}) \| ([^|]+?) \| (Mandatory|Optional) \|", text, re.M):
        reqs[m.group(1)] = {"title": m.group(2).strip(), "retired": False}
    retired = re.search(r"\*\*Retired requirements.*?\n\n(\|.*?)\n\n", text, re.S)
    if retired:
        for m in re.finditer(r"^\| ([A-F]\d{3}) \| ([^|]+?) \|", retired.group(1), re.M):
            if m.group(1) != "Retired":
                reqs[m.group(1)] = {"title": m.group(2).strip(), "retired": True}
    return reqs


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("index")
    ap.add_argument("--reference", default=DEFAULT_REF)
    a = ap.parse_args()
    new = from_index(open(a.index, encoding="utf-8").read())
    old = from_reference(open(a.reference, encoding="utf-8").read())
    if not new:
        sys.exit("No requirements found in the index; its format may have changed.")
    added = sorted(k for k in new if k not in old and not new[k]["retired"])
    retired = sorted(k for k in new if new[k]["retired"] and k in old and not old[k]["retired"])
    reinstated = sorted(k for k in new if not new[k]["retired"] and k in old and old[k]["retired"])
    renamed = sorted(k for k in new if k in old and not new[k]["retired"] and not old[k]["retired"]
                     and norm(new[k]["title"]) != norm(old[k]["title"]))
    missing = sorted(k for k in old if k not in new)
    active = sum(1 for v in new.values() if not v["retired"])
    print(f"Release index: {len(new)} requirements ({active} active). Reference: {len(old)} rows.")
    for label, ids in (("Added", added), ("Retired", retired), ("Reinstated", reinstated), ("Renamed", renamed), ("Missing from the index", missing)):
        print(f"\n{label}: {len(ids)}")
        for k in ids:
            if label == "Renamed":
                print(f"  {k}: '{old[k]['title']}' -> '{new[k]['title']}'")
            else:
                print(f"  {k}: {(new.get(k) or old.get(k))['title']}")
    if not any((added, retired, reinstated, renamed, missing)):
        print("\nNo requirement-level changes found. Check the changelog for control-level changes.")


if __name__ == "__main__":
    main()
