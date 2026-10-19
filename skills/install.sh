#!/usr/bin/env bash
# Install the gov command, then symlink each skill folder in this directory, plus
# _shared, into ~/.claude/skills so Claude Code loads them and edits in the repo
# take effect immediately. Existing folders that aren't symlinks are left alone
# and reported.
set -euo pipefail

src="$(cd "$(dirname "$0")" && pwd)"
repo="$(dirname "$src")"

# gov, installed in editable mode so repo changes take effect without reinstalling.
if command -v uv >/dev/null 2>&1; then
  uv tool install --force --editable "$repo" >/dev/null
  echo "installed gov (uv tool)"
else
  python3 -m pip install --user --quiet --editable "$repo"
  echo "installed gov (pip --user)"
fi
command -v gov >/dev/null 2>&1 || echo "warning: gov isn't on PATH; add the install folder above to PATH"
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
