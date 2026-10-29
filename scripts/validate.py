"""Validate required documentation and local Markdown link targets."""
from pathlib import Path
import re
import sys

REQUIRED = ["AGENTS.md", "README.md", ".github/workflows/ci.yml",
            ".github/pull_request_template.md"] + [
    f"docs/{name}.md" for name in (
        "PRODUCT", "ARCHITECTURE", "SECURITY", "TESTING", "DEPLOYMENT",
        "OPERATIONS", "INCIDENT_RESPONSE")]


def validate(root):
    root = Path(root)
    errors = []
    for name in REQUIRED:
        path = root / name
        if not path.is_file() or not path.read_text().strip():
            errors.append(f"Missing or empty required file: {name}")
    for path in root.rglob("*.md"):
        if any(p in {".git", "node_modules", ".venv"} for p in path.parts):
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
            if ":" in target or target.startswith("#"):
                continue
            target = target.split("#", 1)[0]
            if target and not (path.parent / target).exists():
                errors.append(f"Broken link in {path.relative_to(root)}: {target}")
    return errors


if __name__ == "__main__":
    errors = validate(Path(__file__).resolve().parents[1])
    print("\n".join(errors) if errors else "PASS: required files and local links")
    sys.exit(bool(errors))
