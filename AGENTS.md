# Commercial Software Foundation — Agent Rules

Applies to Codex Remote, Codex Cloud, and other coding agents operating in this repository. Project-specific rules may add stricter requirements, never relax security or production controls.

## 1. Mission and scope
- Build production-grade commercial software with verifiable correctness, privacy, maintainability, accessibility, and recoverability.
- Before coding, read `docs/PRODUCT.md`, `docs/ARCHITECTURE.md`, `docs/SECURITY.md`, `docs/TESTING.md`, `docs/DEPLOYMENT.md`, and the relevant `projects/*/DOMAIN_RULES.md` if present.
- If requirements are ambiguous, identify the decision and seek approval; do not invent business rules.
- Prefer small, reversible changes. Preserve existing design, behavior, and established conventions unless requested.

## 2. Non-negotiable controls
- Never access, modify, delete, or seed production customer data as part of testing.
- Never expose, log, commit, or transmit secrets, tokens, credentials, or personal data. Use least privilege.
- Never bypass authentication, authorization, tenant isolation, or audit logging for convenience.
- Never run destructive migrations, change production infrastructure, alter payment settings, or rotate credentials without explicit approval and a rollback plan.
- Do not merge PRs or deploy to production without the configured human approval and passing required checks.
- Cloud and Remote must use separate branches in existing isolated checkouts for concurrent tasks. Do not assume Cloud sees local uncommitted changes, tools, or secrets.
- Treat external input, uploaded files, third-party APIs, and AI-generated output as untrusted. Validate at system boundaries.

## 3. Definition of ready
Before implementation, identify: user story, acceptance criteria, affected data, security/privacy impact, failure modes, test plan, and rollout/rollback approach. For material changes, propose a plan first.

## 4. Mandatory self-check after EVERY code change
1. Inspect `git diff` and all changed files; confirm scope and absence of secrets.
2. Review logic, edge cases, authorization, data isolation, input validation, error handling, accessibility, and backward compatibility.
3. Run applicable repository commands for format/lint, typecheck, unit tests, integration tests, security checks, and production build. Use documented commands; do not fabricate results.
4. For affected critical user journeys, run available end-to-end/browser tests against isolated test data. Check responsive layouts and error/empty/loading states when UI changes.
5. Fix regressions introduced by the change and rerun affected checks. Never delete/weaken tests just to make CI pass.
6. If a check cannot run, record **NOT RUN** and the exact reason; never call it passed.
7. Produce a self-check report using `templates/SELF_CHECK_REPORT.md` with commands, outcomes, remaining risks, and evidence.

## 5. Git and review policy
- Work in `feature/*`, `fix/*`, or `chore/*` branches. Keep `main` deployable.
- Open a PR with scope, screenshots where applicable, tests, risk assessment, and rollback notes.
- CI must validate every PR. Required checks must be enforced through repository rulesets/branch protection; workflow files alone do not block merges.
- Human review is required for production-bound changes. Do not auto-merge.

## 6. Engineering expectations
- Keep business rules in testable domain modules, not scattered across UI code.
- Use explicit database migrations, constraints, indexes, and idempotency for retried operations.
- Use structured logging with redaction and correlation IDs; record sensitive actions in an audit trail without storing secrets.
- Define service ownership, environment configuration, rate limits, timeout/retry behavior, and backup/restore expectations.
- Prefer accessible, mobile-friendly interfaces. Do not claim compliance without evidence.

## 7. Completion format
Summarize: change, affected files, checks with PASS/FAIL/NOT RUN, security/data considerations, deployment impact, known limitations, PR link if any, and required human decisions.

## Shared execution rules
- Use the existing isolated cloud checkout; do not create worktrees unless explicitly requested.
- Never force-push protected branches, bypass checks, or automatically merge PRs.
- Avoid unrelated refactors and dependencies; document significant architectural decisions. Never silently change business logic.
- Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v` for foundation changes. Products must add actual stack commands before implementation.
- Follow `docs/DOMAIN_RULES.md` in generated product repositories.
