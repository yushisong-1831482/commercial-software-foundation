# Security and privacy baseline

- Threat-model authentication, authorization, multi-tenant access, uploads, payment and external integrations before release.
- Enforce authorization server-side on every resource operation; deny by default. Test horizontal and vertical privilege escalation.
- Validate input; parameterize queries; protect against XSS, CSRF where applicable, SSRF, injection, unsafe file uploads, and insecure redirects.
- Store secrets only in approved environment secret stores; never in repo or client bundles. Separate secrets by environment and project.
- Minimize collected personal data; document purpose, retention, access, deletion, and breach response. Verify applicable Australian privacy obligations.
- Use TLS, least-privilege service accounts, secure session handling, rate limits and abuse controls.
- Record audit events for security-sensitive and financial changes; redact personal data from routine logs.
- Scan dependencies and secrets in CI; triage findings rather than suppressing them without rationale.
- Document backup schedule, restoration tests, and incident escalation contacts before commercial launch.
