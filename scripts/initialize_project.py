"""Create a separate proposal-stage product directory without overwriting files."""
import argparse
from pathlib import Path
import shutil

PRODUCTS = ("logistics-crosscheck", "language-platform")


def initialize(product, destination):
    if product not in PRODUCTS:
        raise ValueError("Unsupported product")
    root = Path(__file__).resolve().parents[1]
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=False)
    for name in ("AGENTS.md", ".gitignore"):
        shutil.copy2(root / name, destination / name)
    for name in ("docs", "templates", "scripts", "tests", ".github"):
        shutil.copytree(root / name, destination / name,
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    shutil.copy2(root / "projects" / product / "DOMAIN_RULES.md",
                 destination / "docs" / "DOMAIN_RULES.md")
    shutil.copy2(root / "projects" / product / "PROPOSAL.md",
                 destination / "docs" / "PRODUCT_PROPOSAL.md")
    (destination / "README.md").write_text(
        f"# {product}\n\nProposal stage; no business features approved.\n"
        "Read docs/PRODUCT_PROPOSAL.md and docs/DOMAIN_RULES.md.\n"
        "Validate: python3 scripts/validate.py\n"
        "Test: python3 -m unittest discover -s tests -v\n"
        "The initializer is maintained in the foundation repository.\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("product", choices=PRODUCTS)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    initialize(args.product, args.destination)
