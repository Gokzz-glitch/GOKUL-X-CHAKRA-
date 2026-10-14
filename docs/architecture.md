# Architecture

- Python 3.10+ command-line interface with no third-party runtime dependencies.
- SQLite stores memory records in a per-user local data directory.
- CHAKRA_MEMORY_DB or the global --db option can select another database path.
- Records have a type, title, body, tags, source, timestamps, and optional archive timestamp.
- Search covers title, content, tags, and source.

The source may live in Google Drive sync. The active SQLite database defaults to local application data and is excluded from Git. Export to a synced folder only when the user explicitly requests a readable backup.
