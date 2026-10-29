# Environment inventory

For each variable document name, purpose, required environments, secret/nonsecret classification, owner, destination, rotation and validation. Enter values only in approved secret stores.

Cloudflare deployment commonly needs CLOUDFLARE_ACCOUNT_ID (nonsecret) and CLOUDFLARE_API_TOKEN (secret). Scope tokens to the selected product/account and minimum deployment permissions. Do not configure these until architecture and deployment approval are settled. Preview and production use distinct bindings and credentials; previews use synthetic data. No credentials are required for foundation validation.
