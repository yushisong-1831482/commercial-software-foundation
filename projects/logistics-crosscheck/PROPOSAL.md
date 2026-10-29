# Logistics Cross-Check proposal — approval required

## Product requirements and MVP boundary
Goal: reliable reconciliation with immutable source evidence and explainable results. No source systems, matching rules, tolerances, prices or features are approved. Candidate MVP: authenticated import of two agreed datasets, explicit validation, deterministic reconciliation and human discrepancy review, followed by an auditable export. Confirm users, tenancy, formats, volumes, retention and acceptance examples before selecting this scope. Exclude automatic financial action and probabilistic matching unless separately approved.

## Architecture proposal
Keep parsers, canonical normalization, versioned rules, reconciliation execution and review API as separate modules. Persist raw files in private object storage with digest/provenance; use a transactional relational store for normalized records, runs and audit events. Large imports may require a queue and a separate runtime if CPU/memory exceeds Workers limits. Framework, database and Cloudflare model remain undecided pending representative import benchmarks and residency requirements.

## Conceptual database design
Proposed entities: organisation, membership, import, source_record, normalized_record, rules_version, reconciliation_run, result, review_action and audit_event. Preserve original bytes and hashes. Scope every business key and query to the authorized organisation if multi-tenant. Enforce unique import idempotency keys and transactional run state. Store currency with decimal/fixed precision and explicit rounding policy. Retention must not silently destroy audit evidence. This is a conceptual model, not migration SQL.

## API proposal
Candidate authenticated operations: create import, upload through restricted signed access, validate import, start a reconciliation with explicit input/rules versions, retrieve run/results, submit reviewed resolution with reason and version precondition, export authorized results. Resource ownership is checked server-side. Mutations use idempotency keys; retries return prior results. Return bounded validation errors without raw customer data; paginate results. Exact paths and contracts require approved use cases.

## Rules specification and decision register
For each approved rule record ID/version, input fields, normalization, keys, precedence, units, currencies, rounding, tolerance, missing/duplicate handling, expected examples and reviewer authority. Same source versions plus rules version must yield identical results. No guessed tolerance or exchange rate. Ambiguity goes to review, never silent acceptance. Owner must supply synthetic examples of exact, duplicate, conflicting, missing and partial records before rule implementation.

## Testing strategy
Use synthetic fixtures. Test decimal calculations, repeated import, partial failures, replay, conflicting identifiers, missing sides, late arrivals, concurrency, audited overrides, malicious uploads, authorization and tenant isolation. Verify provenance and record counts end to end. No tests exist for application logic because no application is implemented.

## Deployment and recovery
Select Pages for a static UI only; evaluate Workers for supported APIs after limits/dependency validation. Preview needs independent storage, sandbox credentials and private access; public preview requires approval. No production bindings. Agree operational owner, RPO/RTO, backup retention and restore evidence before launch. See foundation deployment policy.
