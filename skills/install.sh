#!/usr/bin/env bash
# Symlink each skill folder in this directory, plus _shared, into ~/.claude/skills
# so Claude Code loads them and edits in the repo take effect immediately.
# Existing folders that aren't symlinks are left alone and reported.
set -euo pipefail

src="$(cd "$(dirname "$0")" && pwd)"
dest="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
mkdir -p "$dest"

for dir in "$src"/*/; do
  name="$(basename "$dir")"
  [[ -f "$dir/SKILL.md" || "$name" == "_shared" ]] || continue
  target="$dest/$name"
  if [[ -L "$target" ]]; then
    ln -sfn "${dir%/}" "$target"
    echo "updated  $name"
  elif [[ -e "$target" ]]; then
    echo "skipped  $name (a real folder already exists at $target; move it aside to link this one)"
  else
    ln -s "${dir%/}" "$target"
    echo "linked   $name"
  fi
done
