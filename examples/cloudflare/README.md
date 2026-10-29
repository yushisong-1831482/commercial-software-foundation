# Cloudflare configuration adoption

No deployable application exists. Do not activate a deployment workflow until stack, private preview access, bindings, artifact paths and approval controls are verified. Do not reuse Miro Living projects, tokens or DNS.

For a confirmed Workers app, commit a project-specific Wrangler configuration with workers_dev=false, preview_urls=false, explicit compatibility_date and isolated preview/production environments. Bindings must be environment-specific; do not rely on inherited production defaults. Use a locked Wrangler dependency. Verify configuration and bundling with `npx wrangler deploy --dry-run --env preview` before any release. This command is not yet runnable here because there is no Worker entrypoint or selected Wrangler version.

For static output, Pages is a candidate; for authenticated APIs, storage and queues evaluate Workers or a separate backend. Validate runtime compatibility, residency, pricing and limits first. Git integration may publish before quality gates, so prefer an explicitly gated Actions path when needed.

Deployment workflow design: a same-repository PR runs CI without credentials; only a reviewed, trusted revision can enter a reviewer-protected preview environment. Use synthetic bindings and Cloudflare Access; confirm that public preview URLs are disabled before upload. Never execute fork-controlled code with deployment secrets or use pull_request_target to check out untrusted code. Production uses manual dispatch from main, repeats required validation for the exact SHA, waits for an enforced production reviewer gate, then deploys that immutable artifact with minimum-permission token. Disable competing auto-deploy paths only with explicit production approval.

Actual deploy commands, account IDs and resource bindings belong in the independent product repository after architecture approval. Deployment configuration is guidance only; no preview or production deployment has occurred.
