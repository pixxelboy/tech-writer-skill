#!/usr/bin/env python3
"""Validate README Architect repository structure and skill metadata."""
from __future__ import annotations

import re
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "patterns/README.md",
    "patterns/universal.yml",
    "patterns/mobile-app.yml",
    "patterns/web-app.yml",
    "patterns/saas.yml",
    "patterns/cli.yml",
    "patterns/library.yml",
    "patterns/chrome-extension.yml",
    "patterns/desktop-app.yml",
    "patterns/api-platform.yml",
    "patterns/open-data-project.yml",
    "skills/readme-architect/SKILL.md",
    "skills/readme-architect/templates/default.md",
    "skills/readme-architect/templates/mobile-app.md",
    "skills/readme-architect/templates/saas.md",
    "skills/readme-architect/templates/library.md",
    "skills/readme-architect/templates/cli.md",
    "skills/readme-architect/examples/example-input.md",
    "skills/readme-architect/examples/example-output.md",
    "skills/readme-architect/docs/philosophy.md",
    "skills/readme-architect/docs/scoring.md",
    "skills/readme-architect/docs/architecture.md",
    "skills/readme-architect/docs/pattern-library.md",
    "skills/readme-architect/docs/source-inspiration.md",
]
PROJECT_PATTERN_FILES = [
    "patterns/mobile-app.yml",
    "patterns/web-app.yml",
    "patterns/saas.yml",
    "patterns/cli.yml",
    "patterns/library.yml",
    "patterns/chrome-extension.yml",
    "patterns/desktop-app.yml",
    "patterns/api-platform.yml",
    "patterns/open-data-project.yml",
]
REQUIRED_PATTERN_KEYS = {
    "project_type",
    "description",
    "priority_sections",
    "recommended_sections",
    "avoid",
    "visuals",
    "required_evidence",
    "readme_strategy",
}


def parse_frontmatter(text: str) -> dict:
    assert text.startswith("---\n"), "SKILL.md must start with YAML frontmatter"
    match = re.search(r"\n---\n", text[4:])
    assert match, "SKILL.md frontmatter must close with ---"
    raw = text[4 : 4 + match.start()]
    if yaml:
        data = yaml.safe_load(raw)
    else:
        data = {}
        for line in raw.splitlines():
            if ":" in line and not line.startswith(" "):
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip()
    assert isinstance(data, dict), "frontmatter must parse to a mapping"
    return data


def load_yaml(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if yaml:
        data = yaml.safe_load(text)
        assert isinstance(data, dict), f"{path} must parse to a YAML mapping"
        return data
    # Lightweight fallback: only validates obvious top-level keys.
    return {line.split(":", 1)[0]: True for line in text.splitlines() if line and not line.startswith(" ") and ":" in line}


def main() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    assert not missing, f"Missing files: {missing}"

    skill = (ROOT / "skills/readme-architect/SKILL.md").read_text(encoding="utf-8")
    fm = parse_frontmatter(skill)
    assert fm.get("name") == "readme-architect"
    assert fm.get("description"), "description is required"
    assert len(fm["description"]) <= 1024, "description too long"
    assert len(skill) <= 100_000, "SKILL.md too large"
    assert "Understand first. Document second." in skill
    assert "README Architect does not copy templates" in skill
    assert "Pattern Selection Workflow" in skill
    assert "README Quality Scoring Engine" in skill
    assert "pattern_fit" in skill
    assert "evidence_grounding" in skill
    assert "Self-Critique Pass" in skill

    universal_text = (ROOT / "patterns/universal.yml").read_text(encoding="utf-8")
    universal = load_yaml(ROOT / "patterns/universal.yml")
    assert "sections" in universal, "universal.yml must define sections"
    for required_section in ["hero", "why", "features", "getting_started", "usage", "license"]:
        assert re.search(rf"^  {required_section}:", universal_text, re.MULTILINE), f"universal.yml missing {required_section}"

    for rel in PROJECT_PATTERN_FILES:
        data = load_yaml(ROOT / rel)
        text = (ROOT / rel).read_text(encoding="utf-8")
        missing_keys = REQUIRED_PATTERN_KEYS - set(data)
        assert not missing_keys, f"{rel} missing keys: {sorted(missing_keys)}"
        assert re.search(r"^priority_sections:\n- ", text, re.MULTILINE), f"{rel} must define priority sections"
        assert re.search(r"^required_evidence:\n- ", text, re.MULTILINE), f"{rel} must define required evidence"

    template_dir = ROOT / "skills/readme-architect/templates"
    for template in template_dir.glob("*.md"):
        text = template.read_text(encoding="utf-8")
        assert "{{score}}" in text, f"{template.name} must include scoring placeholder"
        assert "{{project_name}}" in text, f"{template.name} must include project name placeholder"

    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "repository-aware agent skill" in root_readme
    assert "Supported project types" in root_readme
    assert "Pattern library" in root_readme

    print("README Architect structure validation passed.")


if __name__ == "__main__":
    main()
