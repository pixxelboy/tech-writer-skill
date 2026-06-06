#!/usr/bin/env python3
"""Validate README Architect repository structure and skill metadata."""
from __future__ import annotations

import json
import re
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills/readme-architect"
PATTERN_NAMES = [
    "README.md",
    "universal.yml",
    "mobile-app.yml",
    "web-app.yml",
    "saas.yml",
    "cli.yml",
    "library.yml",
    "chrome-extension.yml",
    "desktop-app.yml",
    "api-platform.yml",
    "open-data-project.yml",
]
PROJECT_PATTERN_FILES = [
    "mobile-app.yml",
    "web-app.yml",
    "saas.yml",
    "cli.yml",
    "library.yml",
    "chrome-extension.yml",
    "desktop-app.yml",
    "api-platform.yml",
    "open-data-project.yml",
]
REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "SUBMISSION.md",
    "skills.sh.json",
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
REQUIRED_FILES += [f"patterns/{name}" for name in PATTERN_NAMES]
REQUIRED_FILES += [f"skills/readme-architect/references/patterns/{name}" for name in PATTERN_NAMES]
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
    return {line.split(":", 1)[0]: True for line in text.splitlines() if line and not line.startswith(" ") and ":" in line}


def assert_project_pattern(path: Path) -> None:
    data = load_yaml(path)
    text = path.read_text(encoding="utf-8")
    missing_keys = REQUIRED_PATTERN_KEYS - set(data)
    assert not missing_keys, f"{path} missing keys: {sorted(missing_keys)}"
    assert re.search(r"^priority_sections:\n- ", text, re.MULTILINE), f"{path} must define priority sections"
    assert re.search(r"^required_evidence:\n- ", text, re.MULTILINE), f"{path} must define required evidence"


def main() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    assert not missing, f"Missing files: {missing}"

    skill = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    fm = parse_frontmatter(skill)
    assert fm.get("name") == "readme-architect"
    assert fm.get("description"), "description is required"
    assert len(fm["description"]) <= 1024, "description too long"
    assert fm.get("version"), "version is required"
    assert fm.get("author"), "author is required"
    assert fm.get("license") == "MIT"
    platforms = fm.get("platforms", [])
    if isinstance(platforms, str):
        platforms = [item.strip() for item in platforms.strip("[]").split(",") if item.strip()]
    assert set(platforms) == {"linux", "macos", "windows"}
    assert "homepage: https://github.com/pixxelboy/tech-writer-skill" in skill
    assert "requires_toolsets: [file]" in skill
    assert len(skill) <= 100_000, "SKILL.md too large"
    assert "Understand first. Document second." in skill
    assert "README Architect does not copy templates" in skill
    assert "Pattern Selection Workflow" in skill
    assert "${HERMES_SKILL_DIR}/references/patterns/universal.yml" in skill
    assert "README Quality Scoring Engine" in skill
    assert "pattern_fit" in skill
    assert "evidence_grounding" in skill
    assert "Self-Critique Pass" in skill

    universal_text = (SKILL_DIR / "references/patterns/universal.yml").read_text(encoding="utf-8")
    universal = load_yaml(SKILL_DIR / "references/patterns/universal.yml")
    assert "sections" in universal, "universal.yml must define sections"
    for required_section in ["hero", "why", "features", "getting_started", "usage", "license"]:
        assert re.search(rf"^  {required_section}:", universal_text, re.MULTILINE), f"universal.yml missing {required_section}"

    for name in PROJECT_PATTERN_FILES:
        assert_project_pattern(ROOT / "patterns" / name)
        assert_project_pattern(SKILL_DIR / "references/patterns" / name)

    template_dir = SKILL_DIR / "templates"
    for template in template_dir.glob("*.md"):
        text = template.read_text(encoding="utf-8")
        assert "{{score}}" in text, f"{template.name} must include scoring placeholder"
        assert "{{project_name}}" in text, f"{template.name} must include project name placeholder"

    sidecar = json.loads((ROOT / "skills.sh.json").read_text(encoding="utf-8"))
    assert any("readme-architect" in group.get("skills", []) for group in sidecar.get("groupings", []))

    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "repository-aware agent skill" in root_readme
    assert "Supported project types" in root_readme
    assert "Pattern library" in root_readme

    print("README Architect structure validation passed.")


if __name__ == "__main__":
    main()
