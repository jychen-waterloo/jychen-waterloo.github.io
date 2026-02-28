#!/usr/bin/env bash
set -euo pipefail

# Publish LeetCode progress from workspace source -> GitHub repo mirror.
# Usage:
#   bash leetcode/scripts/publish_progress.sh            # sync + rebuild sqlite
#   bash leetcode/scripts/publish_progress.sh --push     # sync + rebuild + git push

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SRC="$ROOT/../leetcode"
DST="$ROOT/leetcode"
DO_PUSH="${1:-}"

if [[ ! -d "$SRC" ]]; then
  echo "Source leetcode dir not found: $SRC" >&2
  exit 1
fi

mkdir -p "$DST/notes"

cp "$SRC/ledger.jsonl" "$DST/ledger.jsonl"
cp "$SRC/practice_pool.md" "$DST/practice_pool.md"

# Sync notes directory (non-destructive for safety)
if command -v rsync >/dev/null 2>&1; then
  rsync -a "$SRC/notes/" "$DST/notes/"
else
  cp -r "$SRC/notes/." "$DST/notes/"
fi

python3 "$DST/scripts/sync_sqlite.py"

echo "Synced source files and rebuilt sqlite DB."

if [[ "$DO_PUSH" == "--push" ]]; then
  cd "$ROOT"
  if [[ -n "$(git status --porcelain leetcode)" ]]; then
    git add leetcode
    git commit -m "sync leetcode progress"
    git push origin main
    echo "Committed and pushed to origin/main."
  else
    echo "No git changes to push."
  fi
fi
