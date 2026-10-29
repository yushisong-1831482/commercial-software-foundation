# Independent project initialization

1. Run `python3 scripts/initialize_project.py <logistics-crosscheck|language-platform> <new-directory>` from the foundation root. Never target an existing directory.
2. Review copied domain rules, product proposal and decision register with the owner. No business feature is approved by copying these files.
3. Create a private GitHub repository under the intended owner, then initialise Git in the generated directory and commit on `chore/initial-foundation`. If the repository exists, inspect it before copying anything.
4. Add an origin and push the dedicated branch; open a PR. Establish the default branch through the owner's approved bootstrap procedure; do not merge automatically.
5. Configure protection using `docs/GITHUB.md`; verify actual enforcement and repository privacy.
6. Select stack, lock dependencies, add actual lint/type/test/build commands and isolated integration fixtures. Extend CI to enforce them before feature implementation.
7. Select deployment architecture and gated release process, separate secrets/data/permissions/backups. Never copy Miro Living configuration.
8. Run foundation validation and product-specific tests; produce the self-check report. Publish the cloud environment only after review of saved setup configuration.
