#!/usr/bin/env python3
"""Build or refresh the LeetCode tracking SQLite database from existing sources.

Sources:
- leetcode/ledger.jsonl (append-only per-session logs)
- leetcode/practice_pool.md (current mastery snapshot)

Outputs:
- leetcode/tracker.db (SQLite database with two tables: ledger_entries, practice_pool)
"""
from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Iterable, List, Dict, Any

ROOT = Path(__file__).resolve().parents[2]
LEETCODE_DIR = ROOT / "leetcode"
LEDGER_PATH = LEETCODE_DIR / "ledger.jsonl"
POOL_PATH = LEETCODE_DIR / "practice_pool.md"
DB_PATH = LEETCODE_DIR / "tracker.db"


def load_ledger() -> List[Dict[str, Any]]:
    entries: List[Dict[str, Any]] = []
    if not LEDGER_PATH.exists():
        return entries
    with LEDGER_PATH.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON in ledger: {exc}\nLine: {line}") from exc
            entries.append(entry)
    return entries


def parse_markdown_table() -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    if not POOL_PATH.exists():
        return rows
    with POOL_PATH.open() as f:
        for line in f:
            line = line.strip()
            if not line.startswith("|") or line.startswith("| ---"):
                continue
            # Skip header row
            if line.lower().startswith("| # |"):
                continue
            parts = [cell.strip() for cell in line.split("|")]
            # format: ['', '#', 'Title', ... , 'Notes', '']
            if len(parts) < 9:
                continue
            rows.append({
                "lc_id": parts[1],
                "title": parts[2],
                "topics": parts[3],
                "difficulty": parts[4],
                "attempts": parts[5],
                "last_attempt": parts[6],
                "mastery": parts[7],
                "notes": parts[8],
            })
    # drop header separators by filtering rows where lc_id not digit
    cleaned: List[Dict[str, Any]] = []
    for row in rows:
        try:
            lc_id = int(row["lc_id"]) if row["lc_id"] else None
        except ValueError:
            continue
        if lc_id is None:
            continue
        cleaned.append({
            "lc_id": lc_id,
            "title": row["title"],
            "topics": row["topics"],
            "difficulty": row["difficulty"],
            "attempts": int(row["attempts"]) if row["attempts"] else None,
            "last_attempt": row["last_attempt"] or None,
            "mastery": row["mastery"],
            "notes": row["notes"],
        })
    return cleaned


def init_db(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()
    cur.execute("PRAGMA journal_mode=WAL;")
    cur.execute("PRAGMA foreign_keys=ON;")
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS ledger_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lc_id INTEGER,
            title TEXT,
            difficulty TEXT,
            topics TEXT,
            status TEXT,
            date TEXT,
            time_min REAL,
            result TEXT,
            approach TEXT,
            key_insight TEXT,
            mistakes TEXT,
            notes TEXT,
            notes_path TEXT,
            complexity TEXT,
            hints INTEGER,
            submissions INTEGER
        );
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS practice_pool (
            lc_id INTEGER PRIMARY KEY,
            title TEXT,
            topics TEXT,
            difficulty TEXT,
            attempts INTEGER,
            last_attempt TEXT,
            mastery TEXT,
            notes TEXT
        );
        """
    )
    conn.commit()


def refresh_tables(conn: sqlite3.Connection, ledger: List[Dict[str, Any]], pool: List[Dict[str, Any]]) -> None:
    cur = conn.cursor()
    cur.execute("DELETE FROM ledger_entries;")
    cur.execute("DELETE FROM practice_pool;")

    ledger_rows = [
        (
            entry.get("id"),
            entry.get("title"),
            entry.get("difficulty"),
            json.dumps(entry.get("topics")),
            entry.get("status"),
            entry.get("date"),
            entry.get("time_min"),
            entry.get("result"),
            entry.get("approach"),
            entry.get("key_insight"),
            entry.get("mistakes"),
            entry.get("notes"),
            entry.get("notes_path"),
            entry.get("complexity"),
            entry.get("hints"),
            entry.get("submissions"),
        )
        for entry in ledger
    ]
    cur.executemany(
        """
        INSERT INTO ledger_entries (
            lc_id, title, difficulty, topics, status, date, time_min, result,
            approach, key_insight, mistakes, notes, notes_path, complexity,
            hints, submissions
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """,
        ledger_rows,
    )

    pool_rows = [
        (
            row["lc_id"],
            row["title"],
            row["topics"],
            row["difficulty"],
            row["attempts"],
            row["last_attempt"],
            row["mastery"],
            row["notes"],
        )
        for row in pool
    ]
    cur.executemany(
        """
        INSERT INTO practice_pool (
            lc_id, title, topics, difficulty, attempts, last_attempt, mastery, notes
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """,
        pool_rows,
    )

    conn.commit()


def main() -> None:
    ledger = load_ledger()
    pool = parse_markdown_table()
    conn = sqlite3.connect(DB_PATH)
    try:
        init_db(conn)
        refresh_tables(conn, ledger, pool)
    finally:
        conn.close()
    print(f"Synced {len(ledger)} ledger entries and {len(pool)} practice pool rows into {DB_PATH}.")


if __name__ == "__main__":
    main()
