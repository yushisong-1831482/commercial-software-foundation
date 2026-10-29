# Commercial Software Foundation v1.0

Reusable **engineering governance starter** for commercial web apps using Codex Remote + Codex Cloud + GitHub + Cloudflare. This is not a deployable application and does not automatically configure branch protection, Cloudflare previews, production approval, databases, or monitoring.

## Start a new project
1. Create a **separate private repository** for the product.
2. Copy root `AGENTS.md`, `docs/`, `templates/`, and `.github/pull_request_template.md` into it.
3. Copy the relevant `projects/<domain>/DOMAIN_RULES.md` into the new repository as `docs/DOMAIN_RULES.md`, and adjust AGENTS.md to refer to that path.
4. Fill in `docs/PRODUCT.md` and `docs/ARCHITECTURE.md` before implementation.
5. Inspect actual framework and deployment mechanism; adapt `.github/workflows/ci.yml` only if the project is Node/npm. Otherwise create a stack-appropriate CI workflow.
6. Configure GitHub branch protection/rulesets and required CI checks manually with approval.
7. Configure isolated Cloudflare previews, staging/test secrets, production approvals as required, and deployment monitoring.
8. Add real automated tests for critical business rules and journeys; run them before the first commercial launch.

## Operating model
- Codex Remote and Cloud work on separate branches.
- Every task follows AGENTS.md self-check and produces a report.
- Every PR runs CI, gets preview and human review when appropriate, then merges to protected main.
- Production deployment must follow verified Cloudflare integration and approved release policy.

## Critical caveats
- AGENTS.md is an instruction mechanism, not a security boundary or guaranteed execution engine.
- GitHub Actions does not enforce passing checks until branch protection/rulesets are configured.
- A Cloudflare preview deployment is not proof of test success.
- The sample CI file will fail until matching package scripts exist; adapt before use.
- Legal compliance, security posture, payment correctness, and operational readiness require actual implementation, tests, configuration, and review.
