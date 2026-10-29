# Architecture decision record and boundaries

## Baseline architecture
User -> Cloudflare-hosted UI/API -> application services -> project-specific data stores and external integrations.
GitHub -> PR -> CI -> isolated preview -> human acceptance -> protected main -> controlled production deployment -> monitoring.

## Decisions to record before choosing implementation
- Frontend and backend framework: TODO
- Cloudflare Pages vs Workers and deployment mechanism: TODO (inspect existing project)
- Database/storage provider, location, encryption and retention: TODO
- Authentication provider and authorization model: TODO
- Background jobs/queues, idempotency and retry policy: TODO
- Third-party APIs and webhooks, signature verification: TODO
- Environments: local, preview/staging, production: TODO
- Operational owner, availability target and recovery objectives: TODO

## Boundaries
- Separate repositories, secrets, service identities, databases, and production environments per commercial product.
- Preview/test must never connect to production data by default.
- External APIs are fallible; design for timeout, retries, duplicates, rate limits and partial failure.
- Document major architecture decisions with date, alternatives and rationale.
