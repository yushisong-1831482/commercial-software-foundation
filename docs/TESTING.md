# Test strategy and release gates

## Test pyramid
1. Unit: domain rules, money calculations, date/time rules, permissions.
2. Integration: DB constraints/migrations, external API adapters, webhooks, queue retries.
3. E2E: critical customer journeys, errors, accessibility smoke, mobile viewport.
4. Security: access-control and tenant-isolation tests, dependency and secret checks.

## Mandatory PR gate
- Formatting/lint: PASS
- Typecheck (if applicable): PASS
- Unit tests: PASS
- Integration tests (where configured): PASS
- Production build: PASS
- Critical E2E tests: PASS when applicable and configured
- No critical security findings without documented remediation/approval

All checks must report PASS, FAIL, or NOT RUN with reason. A missing test suite is not a pass. Establish minimum critical-path coverage before commercial release; do not invent arbitrary coverage guarantees.

## Test isolation
- Synthetic data and sandbox providers only. Never execute destructive tests against production.
- Seed fixtures reproducibly and clean up after tests.
- For every defect, add a regression test when feasible.

## Human acceptance
- Review Cloudflare preview, especially mobile UI and real business workflows, before merge.
