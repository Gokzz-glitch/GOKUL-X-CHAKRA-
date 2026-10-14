# CHAKRA

Repository name: GOKUL-X-CHAKRA-.

Dedicated startup project workspace with a local persistent memory utility.

Founder-confirmed direction: CHAKRA is an AI-in-healthcare startup currently focused on colonoscopy polyps related to colorectal cancer. The repositories and Drive materials describe ChakraModel research and prototypes; they do not by themselves establish the startup's finalized product, clinical claims, regulatory status, buyer, or business model.

## Structure

- docs/ — product context, architecture, decisions.
- memory/ — memory workflow guidance.
- references/ — source documents and research.
- scripts/ — small maintenance utilities.
- src/chakra_memory/ — Python CLI and SQLite storage.

## Imported project context

- [Product context](docs/product-context.md) records founder-confirmed direction and open product questions.
- [GitHub review](docs/github-context-review.md) and [Drive review](docs/drive-context-review.md) preserve source-attributed findings, maturity labels, and conflicting evidence.
- [Squad spreadsheet review](docs/spreadsheet-context-review.md) captures CHAKRA-relevant tasks and dataset notes from the shared team workbook, with status caveats.
- The current readable memory export is in `memory/CHAKRA-memory-backup-2026-10-14.md`; the live SQLite database stays in local application data.

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
## Tests

Run the CLI smoke suite with:

    python -m unittest discover -s tests -v
