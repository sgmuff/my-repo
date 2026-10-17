#!/usr/bin/env python3
"""Package the suite for Claude Desktop (and claude.ai).

Usage:
  python3 skills/package_desktop.py [--out dist/claude-desktop]

Claude Code loads the skills from this folder, where each skill reaches the
shared files through ../_shared/. Claude Desktop installs each skill on its
own, so a skill can't see its neighbors. This script builds one zip per
skill with its own copy of _shared/ as shared/, rewrites the paths to match,
adds a Claude Desktop note to the bundled conventions, validates each
SKILL.md, and writes <out>/<skill>.zip. The repo stays the single source:
edit the skills here and rebuild.
"""
import argparse
import os
import re
import shutil
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
SHARED = os.path.join(HERE, "_shared")
SKIP_DIRS = {"__pycache__", "evals", ".git"}
SKIP_FILES = {".DS_Store"}
TEXT = (".md", ".py", ".json", ".txt", ".csv")

DESKTOP_NOTE = """## Running in Claude Desktop

This copy of the suite is packaged for Claude Desktop and claude.ai. Each skill is installed on its own and carries its own copy of the shared files in `shared/`. Where this file or a skill differs from the notes below, the notes win:

- **Where deliverables go:** there's no repository. Save deliverables in the session's outputs folder (`/mnt/user-data/outputs/compliance/` in claude.ai and Claude Desktop), with the layout in §8, and give the user the files to download. Records don't carry over between conversations. When a skill needs earlier records (RoPA entries, the AI inventory, the control library, past assessments), ask the user to upload their `compliance/` folder or the files concerned.
- **Scripts:** run them with Python in the code execution environment, using paths relative to the skill folder. If code execution is off, do the step by hand and say so.
- **Other skills:** the rest of the suite is installed as separate skills, so their folders aren't visible. Refer to them by name. If the user says one isn't installed, say what it does and what to do meanwhile.
- **Connected tools:** use the connectors the user has enabled, such as Jira or Atlassian; otherwise use the fallbacks in `connectors.md`. Never connect to a calendar or create calendar events.
- **Writing style:** if the `writing-style` skill isn't installed, follow the essentials in §2.

"""


def skills():
    for name in sorted(os.listdir(HERE)):
        if os.path.isfile(os.path.join(HERE, name, "SKILL.md")):
            yield name


def ignore(_, names):
    return [n for n in names if n in SKIP_DIRS or n in SKIP_FILES or n.endswith(".pyc")]


def rewrite(text, rel_dir, is_py):
    """Point shared paths at <skill>/shared from a file in rel_dir (relative to the skill root)."""
    depth = 0 if rel_dir in ("", ".") else rel_dir.count(os.sep) + 1
    up = "../" * depth
    if not rel_dir.startswith("shared"):
        text = re.sub(r"(?:\.\./)+_shared/", up + "shared/", text)
        text = re.sub(r"(?:\.\./)+_shared`", up + "shared`", text)
    text = re.sub(r"(?<![\w./])_shared/", "shared/", text)
    if is_py:
        text = text.replace('"..", "..", "_shared"', '"..", "shared"')
        text = text.replace('"..", "..", "controls-and-evidence", "assets"', '"..", "..", "assets"')
    return text


def build(skill, stage):
    root = os.path.join(stage, skill)
    shutil.copytree(os.path.join(HERE, skill), root, ignore=ignore)
    if skill != "writing-style":
        shutil.copytree(SHARED, os.path.join(root, "shared"), ignore=ignore)
    for dirpath, _, names in os.walk(root):
        rel_dir = os.path.relpath(dirpath, root)
        for n in names:
            if not n.endswith(TEXT):
                continue
            p = os.path.join(dirpath, n)
            with open(p, encoding="utf-8") as f:
                old = f.read()
            new = rewrite(old, "" if rel_dir == "." else rel_dir, n.endswith(".py"))
            if rel_dir == "shared" and n == "conventions.md":
                new = new.replace("\n## Contents\n", "\n" + DESKTOP_NOTE + "## Contents\n", 1)
            if new != old:
                with open(p, "w", encoding="utf-8") as f:
                    f.write(new)
    return root


def check(root, skill):
    """Return a list of problems: frontmatter limits and links that don't resolve."""
    problems = []
    text = open(os.path.join(root, "SKILL.md"), encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    meta = dict(re.findall(r"^(\w[\w-]*): (.*)$", m.group(1), re.M)) if m else {}
    if meta.get("name") != skill:
        problems.append(f"name is {meta.get('name')!r}, expected {skill!r}")
    d = meta.get("description", "")
    if not d or len(d) > 1024 or "<" in d or ">" in d:
        problems.append(f"description missing, over 1024 characters, or has angle brackets ({len(d)})")
    for dirpath, _, names in os.walk(root):
        for n in names:
            if not n.endswith(".md"):
                continue
            body = open(os.path.join(dirpath, n), encoding="utf-8").read()
            for link in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", body):
                if link.startswith(("http", "mailto:")) or link.startswith("../assessments/"):
                    continue
                if not os.path.exists(os.path.normpath(os.path.join(dirpath, link))):
                    problems.append(f"broken link in {os.path.relpath(os.path.join(dirpath, n), root)}: {link}")
            if re.search(r"(?:\.\./)+_shared|(?<![\w./])_shared/", body):
                problems.append(f"unrewritten _shared path in {os.path.relpath(os.path.join(dirpath, n), root)}")
    return problems


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(HERE), "dist", "claude-desktop"))
    a = ap.parse_args()
    stage = os.path.join(a.out, "build")
    shutil.rmtree(stage, ignore_errors=True)
    os.makedirs(stage)
    failed = False
    for skill in skills():
        root = build(skill, stage)
        problems = check(root, skill)
        if problems:
            failed = True
            print(f"FAIL {skill}")
            for p in problems:
                print(f"  {p}")
            continue
        zpath = os.path.join(a.out, f"{skill}.zip")
        with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
            for dirpath, _, names in os.walk(root):
                for n in sorted(names):
                    full = os.path.join(dirpath, n)
                    z.write(full, os.path.relpath(full, stage))
        print(f"ok   {skill}.zip ({os.path.getsize(zpath) // 1024} KB)")
    shutil.rmtree(stage)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
