# Release checklist

- Approved scope and business rules; reviewed PR; required checks passed on the release SHA.
- Verify repository protection and production environment reviewer enforcement on the actual GitHub plan.
- Functional review of isolated preview; no production bindings or customer data.
- Security, accessibility, privacy and dependency findings resolved or explicitly accepted.
- Data migrations reversible/compatible; backup restoration evidence and rollback owner identified.
- Explicit production approval; deploy approved immutable SHA through gated workflow.
- Smoke checks, alert delivery and operational ownership verified; record deployment ID and rollback evidence.
