# GitHub configuration and verification

Git read access to the supplied repository was verified. GitHub API returned Forbidden in this environment; repository visibility, account-wide repository listing, creation rights, rulesets, Actions runs and PR creation are not verified. A Git read does not establish API administration privileges.

An authorized administrator should:
1. Open repository Settings → General and verify Private visibility. Create missing product repositories with Private selected; do not make an existing private repository public.
2. Settings → Rules → Rulesets → New branch ruleset: target main, set Active, require a pull request and at least one approval, dismiss stale approvals, require approval after the latest push where supported, require resolved conversations, block deletions and force pushes, restrict updates/direct pushes without granting broad bypass rights.
3. After the first CI run, select the actual `foundation` check under required status checks and require branches to be current. Require product checks once they exist. Do not type an assumed check name without observing it.
4. Inspect plan support for private repositories. If enforcement is unavailable, document the limitation and use an account/plan that supports the required controls before treating main as protected. Workflow YAML is not enforcement.
5. Settings → Environments → production: configure permitted main branch and required human reviewers, prevent self-review where supported. Verify these features are enforced on the plan before storing production secrets.
6. Verify with an unprivileged collaborator's disposable branch/PR that failed checks, missing review and direct updates are rejected; never probe by force-pushing main. Record API/UI evidence and review bypass actors.

Use feature/*, fix/* and chore/* branches. No automatic merges. Remote and Cloud work on separate branches; transfer work by pushed commits and PRs.
