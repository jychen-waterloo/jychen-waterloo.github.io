# jychen-waterloo.github.io

## LeetCode Tracker Workflow

- Source files remain in `leetcode/ledger.jsonl` (session log) and `leetcode/practice_pool.md` (mastery snapshot).
- Run `python3 leetcode/scripts/sync_sqlite.py` to sync those files into `leetcode/tracker.db`.
- The SQLite DB contains:
  - `ledger_entries`: every row from the JSONL ledger (one solve per line).
  - `practice_pool`: rows from the Markdown practice pool table.
- Example query:
  ```sql
  SELECT date, lc_id, title, time_min
  FROM ledger_entries
  WHERE date >= '2026-02-15'
  ORDER BY date DESC;
  ```

Use the DB for fast filtering/statistics, then continue publishing human-readable summaries from the Markdown/JSONL files.
