# Submission Notes

README Architect is prepared for Hermes Skills Hub / official review.

## Canonical skill path

```text
skills/readme-architect/
```

This follows the `hermes skills publish <skill-path> --to github --repo owner/repo` flow documented in the Hermes Agent developer guide.

## Self-contained bundle

The installable skill contains all runtime assets:

```text
skills/readme-architect/
├── SKILL.md
├── templates/
├── docs/
├── examples/
└── references/
    └── patterns/
```

The repository-root `patterns/` directory mirrors the bundled pattern library for easier browsing, but the skill does not depend on files outside its own directory.

## Validation

Run before submission:

```bash
python3 tests/validate_structure.py
hermes skills publish /absolute/path/to/skills/readme-architect --to github --repo NousResearch/hermes-agent
```

The publish command runs Hermes Skills Guard before creating a PR.
