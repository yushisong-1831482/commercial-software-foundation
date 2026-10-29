# Logistics Cross-Check — commercial domain guardrails

## Business goal
Reconcile shipment, order, carrier, warehouse, invoice, and/or freight-charge records. Exact data sources and matching policy MUST be specified by owner before implementation.

## Non-negotiable domain rules
- Preserve raw source records and provenance (source, import time, original identifier, version/hash); never silently overwrite originals.
- Define canonical IDs and explicit matching rules. Distinguish exact matches, probable matches, mismatches, missing records, and duplicates.
- Reconciliation must be reproducible: same inputs + rules version -> same outcome.
- Handle duplicate uploads/webhooks idempotently; record exceptions rather than silently dropping data.
- Use decimal/fixed-precision money and explicit currency, tax, units, time zone, rounding and exchange-rate source/date. Never use binary floating-point for financial totals.
- Keep a human-review queue for ambiguous matches, discrepancies, and overrides. Log reviewer, timestamp, reason, before/after values.
- Never auto-charge, refund, delete shipments, or finalize a disputed financial discrepancy without approved business rules and permissions.
- Separate customer/tenant data and enforce row/resource authorization on the server.
- Support partial import failure, retries, rollback/replay, reconciliation snapshots, export, and audit history.

## Minimum acceptance tests
- Exact match, mismatch, duplicate, missing side, late-arriving record, partial shipment, currency/unit conversion, rounding, conflicting IDs, repeated import, unauthorized tenant access, and human override audit.

## Decisions needed from owner
- Which systems and APIs? What constitutes a match? Tolerances? Charge categories? Multi-currency? Who approves exceptions? Retention period? Required exports? Data volume/SLA?
