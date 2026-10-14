"""Command-line interface for the CHAKRA project memory."""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

from .db import connect, default_db_path

KINDS = ("fact", "decision", "lesson", "note", "goal")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="chakra-memory", description="Store and search local CHAKRA project memories.")
    parser.add_argument("--db", type=Path, help="database path (defaults to CHAKRA_MEMORY_DB or local user data)")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("init", help="initialize the local database")

    add = commands.add_parser("add", help="save a memory")
    add.add_argument("--kind", choices=KINDS, required=True)
    add.add_argument("--title", required=True)
    add.add_argument("--content", required=True)
    add.add_argument("--tag", action="append", default=[], help="repeat to add tags")
    add.add_argument("--source", default="", help="where the information came from")

    search = commands.add_parser("search", help="search active memories")
    search.add_argument("query")

    listing = commands.add_parser("list", help="list memories")
    listing.add_argument("--kind", choices=KINDS)
    listing.add_argument("--archived", action="store_true")

    show = commands.add_parser("show", help="show a memory by ID")
    show.add_argument("id")

    archive = commands.add_parser("archive", help="archive a memory by ID")
    archive.add_argument("id")

    export = commands.add_parser("export", help="export memories as Markdown")
    export.add_argument("--output", type=Path, help="output file; default is standard output")
    export.add_argument("--include-archived", action="store_true")
    return parser


def row_summary(row) -> str:
    tags = ", ".join(json.loads(row["tags"]))
    suffix = f" | tags: {tags}" if tags else ""
    return f"{row['id']} | {row['kind']} | {row['title']} | {row['created_at']}{suffix}"


def run(args: argparse.Namespace) -> int:
    db_path = args.db or default_db_path()
    if args.command == "init":
        with connect(db_path):
            pass
        print(f"Initialized local memory database: {db_path}")
        return 0

    with connect(db_path) as connection:
        if args.command == "add":
            memory_id, timestamp = uuid.uuid4().hex, now_iso()
            connection.execute(
                """INSERT INTO memories
                   (id, kind, title, content, tags, source, created_at, updated_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (memory_id, args.kind, args.title.strip(), args.content.strip(),
                 json.dumps(args.tag, ensure_ascii=False), args.source.strip(), timestamp, timestamp),
            )
            print(memory_id)
            return 0

        if args.command == "search":
            query = f"%{args.query.strip()}%"
            rows = connection.execute(
                """SELECT * FROM memories WHERE archived_at IS NULL
                   AND (title LIKE ? COLLATE NOCASE OR content LIKE ? COLLATE NOCASE
                     OR tags LIKE ? COLLATE NOCASE OR source LIKE ? COLLATE NOCASE)
                   ORDER BY created_at DESC""",
                (query, query, query, query),
            ).fetchall()
            for row in rows:
                print(row_summary(row))
            return 0 if rows else 1

        if args.command == "list":
            filters, values = [], []
            if args.kind:
                filters.append("kind = ?")
                values.append(args.kind)
            filters.append("archived_at IS NOT NULL" if args.archived else "archived_at IS NULL")
            rows = connection.execute(
                f"SELECT * FROM memories WHERE {' AND '.join(filters)} ORDER BY created_at DESC", values
            ).fetchall()
            for row in rows:
                print(row_summary(row))
            return 0

        if args.command == "show":
            row = connection.execute("SELECT * FROM memories WHERE id = ?", (args.id,)).fetchone()
            if row is None:
                print(f"Memory not found: {args.id}", file=sys.stderr)
                return 2
            print(row_summary(row))
            if row["source"]:
                print(f"Source: {row['source']}")
            print()
            print(row["content"])
            return 0

        if args.command == "archive":
            timestamp = now_iso()
            result = connection.execute(
                "UPDATE memories SET archived_at = ?, updated_at = ? WHERE id = ? AND archived_at IS NULL",
                (timestamp, timestamp, args.id),
            )
            if result.rowcount == 0:
                print(f"Active memory not found: {args.id}", file=sys.stderr)
                return 2
            print(f"Archived {args.id}")
            return 0

        if args.command == "export":
            where = "" if args.include_archived else " WHERE archived_at IS NULL"
            rows = connection.execute(
                "SELECT * FROM memories" + where + " ORDER BY created_at ASC"
            ).fetchall()
            lines = ["# CHAKRA Project Memory", ""]
            for row in rows:
                lines.extend([f"## {row['title']}", "", f"- Type: {row['kind']}", f"- ID: {row['id']}",
                              f"- Created: {row['created_at']}"])
                if row["source"]:
                    lines.append(f"- Source: {row['source']}")
                tags = json.loads(row["tags"])
                if tags:
                    lines.append(f"- Tags: {', '.join(tags)}")
                if row["archived_at"]:
                    lines.append(f"- Archived: {row['archived_at']}")
                lines.extend(["", row["content"], ""])
            output = "\n".join(lines)
            if args.output:
                args.output.parent.mkdir(parents=True, exist_ok=True)
                args.output.write_text(output, encoding="utf-8")
                print(args.output)
            else:
                print(output)
            return 0
    return 2


def main() -> None:
    args = make_parser().parse_args()
    try:
        raise SystemExit(run(args))
    except sqlite3.Error as exc:
        print(f"Memory database error: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
