# Operations

Each product needs a named operational owner and escalation contact before launch. Record environment inventory, deployment identifiers, provider status sources, and dependency update ownership separately for each product.

Use structured error events with correlation IDs, release SHA, severity and redaction. Exclude uploads, learner records, tokens, payment payloads, and customer identifiers from routine logs. Choose an error reporting vendor only after privacy, residency and cost review.

Before commercial release configure synthetic availability checks, deployment smoke checks, actionable alerts with an acknowledged escalation route, and tested alert delivery. No monitoring service is provisioned by this foundation.

Inventory data stores and object storage; agree backup frequency, retention, encryption, access, RPO and RTO with the owner. These are undecided business targets, not guarantees. Restore into an isolated environment, validate record counts and referential integrity, measure recovery, and record evidence before launch and after material changes.

Review dependency updates regularly, investigate advisories, and schedule security reviews around changes to authentication, billing, imports, tenancy and personal data. Use sandbox providers for recovery drills.
