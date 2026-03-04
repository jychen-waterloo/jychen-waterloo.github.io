#!/usr/bin/env bash
set -euo pipefail

# Publish LeetCode progress from workspace source -> GitHub repo mirror.
# Usage:
#   bash leetcode/scripts/publish_progress.sh                    # sync + rebuild sqlite
#   bash leetcode/scripts/publish_progress.sh --push             # sync + rebuild + git push
#   bash leetcode/scripts/publish_progress.sh --push --force     # bypass push cooldown guard

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SRC="$ROOT/../leetcode"
DST="$ROOT/leetcode"
DO_PUSH=""
FORCE_PUSH="false"
for arg in "$@"; do
  case "$arg" in
    --push) DO_PUSH="--push" ;;
    --force) FORCE_PUSH="true" ;;
  esac
done

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

  # Guardrail: avoid accidental back-to-back pushes unless explicitly forced.
  LAST_PUSH_FILE="$ROOT/.last_publish_push_ts"
  NOW_TS="$(date +%s)"
  if [[ "$FORCE_PUSH" != "true" && -f "$LAST_PUSH_FILE" ]]; then
    LAST_TS="$(cat "$LAST_PUSH_FILE" 2>/dev/null || echo 0)"
    if [[ "$LAST_TS" =~ ^[0-9]+$ ]]; then
      DELTA=$((NOW_TS - LAST_TS))
      if (( DELTA < 300 )); then
        echo "Refusing push: last publish push was ${DELTA}s ago (<300s cooldown)." >&2
        echo "If this is intentional, rerun with: --push --force" >&2
        exit 2
      fi
    fi
  fi

  if [[ -n "$(git status --porcelain leetcode)" ]]; then
    git add leetcode
    git commit -m "sync leetcode progress"
    git push origin main
    date +%s > "$LAST_PUSH_FILE"
    echo "Committed and pushed to origin/main."
  else
    echo "No git changes to push."
  fi
fi
