# Decision 0001: local SQLite memory store

- Date: 2026-10-14
- Status: accepted
- Decision: use Python's built-in SQLite module for the first local memory utility.
- Reason: durable structured storage without a hosted service or third-party runtime dependency.
- Data location: keep the live database in local application data, outside Google Drive sync.
- Revisit when multi-device synchronization, shared team memory, or a hosted API is requested.
