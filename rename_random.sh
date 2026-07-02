#!/usr/bin/env bash
#
# rename_random.sh — renames every file in the current directory to a
# random alphanumeric name, preserving each file's extension.
#
# Usage:
#   ./rename_random.sh              # rename with 8-char random names
#   ./rename_random.sh 12           # rename with 12-char random names
#   ./rename_random.sh --dry-run    # preview without renaming anything
#   ./rename_random.sh 12 --dry-run # combine length + dry run
#
# Notes:
#   - Only renames files in the CURRENT directory (not subdirectories).
#   - Skips hidden files (dotfiles) and skips itself if run from this folder.
#   - Keeps the original extension (e.g. "photo.jpg" -> "aB3xZ9kQ.jpg").
#   - Checks for name collisions and re-rolls if a name is already taken.

set -euo pipefail

LENGTH=8
DRY_RUN=false
SCRIPT_NAME="$(basename "$0")"

for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=true ;;
    ''|*[!0-9]*) ;;   # ignore anything that isn't a plain number
    *) LENGTH="$arg" ;;
  esac
done

randstr() {
  tr -dc 'A-Za-z0-9' </dev/urandom | head -c "$LENGTH"
}

count=0

for f in *; do
  [ -f "$f" ] || continue              # only regular files
  [ "$f" = "$SCRIPT_NAME" ] && continue # don't rename the script itself

  if [[ "$f" == *.* && "$f" != .* ]]; then
    ext="${f##*.}"
    base="${f%.*}"
  else
    ext=""
  fi

  newname="$(randstr)"
  [ -n "$ext" ] && newname="${newname}.${ext}"

  while [ -e "$newname" ]; do
    newname="$(randstr)"
    [ -n "$ext" ] && newname="${newname}.${ext}"
  done

  if $DRY_RUN; then
    echo "Would rename: $f -> $newname"
  else
    mv -- "$f" "$newname"
    echo "Renamed: $f -> $newname"
  fi
  count=$((count+1))
done

echo "Done. $count file(s) processed."
