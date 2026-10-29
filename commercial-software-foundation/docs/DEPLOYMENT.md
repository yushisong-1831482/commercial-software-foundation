# GitHub + Cloudflare deployment policy

## Intended flow
feature branch -> PR -> automated CI -> Cloudflare preview (if configured) -> human review -> protected main -> production deploy -> smoke test/monitor -> rollback if needed.

## Before implementation
- Inspect whether the app uses Cloudflare Pages, Workers Git integration, or Wrangler-based deployment. Do not assume.
- Verify production branch, build commands, secrets, domains, database bindings, and current deployment triggers.
- Check that PR preview uses nonproduction bindings and credentials. A preview URL is NOT proof tests passed.
- Configure GitHub required checks through branch protection/rulesets; GitHub Actions alone cannot prevent merging.
- Determine whether the hosting integration deploys immediately on merge; if manual production approval is required, configure an appropriate deployment gate rather than assuming PR approval alone is sufficient.

## Production change checklist
- CI green and reviewed PR; migrations compatible with rollback; verified backups; release notes; smoke checks; monitoring and rollback steps.
- Never log live secrets or customer data in deployment output.
- For incident: stop rollout, assess impact, rollback code if safe, account for irreversible schema/data changes, and document root cause.
