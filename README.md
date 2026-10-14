# CHAKRA

Repository name: GOKUL-X-CHAKRA-.

Dedicated startup project workspace with a local persistent memory utility.

The only confirmed product context is that the founder is building a startup called CHAKRA. Industry, product, customers, and business model remain unknown until provided.

## Structure

- docs/ — product context, architecture, decisions.
- memory/ — memory workflow guidance.
- references/ — source documents and research.
- scripts/ — small maintenance utilities.
- src/chakra_memory/ — Python CLI and SQLite storage.

## Install and use

Requires Python 3.10+. From this directory:

    python -m pip install -e .
    chakra-memory init
    chakra-memory add --kind fact --title "Startup name" --content "I am building a startup called CHAKRA." --source "Founder, 2026-10-14"
    chakra-memory search "startup"
    chakra-memory list

The active database defaults to %LOCALAPPDATA%/Chakra/memory.sqlite3 on Windows and the local user data directory on other systems. Set CHAKRA_MEMORY_DB to choose another local path. Keep the active DB outside Google Drive sync. Use chakra-memory export --output PATH for a readable export.

## GitHub

This workspace uses the existing private repository Gokzz-glitch/GOKUL-X-CHAKRA-.