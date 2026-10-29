# Commercial Software Foundation

Reusable engineering standards and project preparation for Codex Remote, Codex Cloud, GitHub, and Cloudflare. No commercial application is implemented or deployed.

## Validate locally
Requires Python 3.12 or newer; no third-party dependencies.

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

## Prepare an independent product
```sh
python3 scripts/initialize_project.py logistics-crosscheck /tmp/logistics-crosscheck
python3 /tmp/logistics-crosscheck/scripts/validate.py
```
Use `language-platform` for the other product. The destination must not exist. The generator copies standards and the selected proposal, never credentials, Git history, or another product's data. Review proposals and initialise a separate private GitHub repository before application development. See [initialization](templates/PROJECT_INITIALIZATION.md).

## Review and release
Requirement → dedicated branch → implementation → self-check → PR → CI → isolated preview → review → approved merge → controlled release → monitoring.

The root is the maintained foundation. The nested `commercial-software-foundation/` directory preserves the original supplied starter for provenance. See [execution report](docs/IMPLEMENTATION_REPORT.md), [deployment](docs/DEPLOYMENT.md), and [operations](docs/OPERATIONS.md). Workflow files alone do not enforce branch protection. Product proposals require owner decisions before implementation.
