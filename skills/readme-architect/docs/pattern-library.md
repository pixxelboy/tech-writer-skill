# Pattern Library

README Architect does not copy templates. It learns patterns, detects project context, and composes the most useful README for that repository.

The pattern library turns README generation into an adaptive process. A mobile app should not read like a package library. A CLI should not bury the first useful command below a long product essay. An open-data project should foreground sources, schema, freshness, and attribution.

## Pattern files

The root `patterns/` directory contains YAML patterns:

- `universal.yml` defines shared README components: hero, badges, demo, why, features, architecture, getting started, configuration, usage, project structure, roadmap, contributing, and license.
- Project-specific files define section priorities, recommended sections, anti-patterns, visual conventions, evidence requirements, and strategy.

## Workflow

1. Build an evidence map from repository files.
2. Classify the project type.
3. Load `patterns/universal.yml`.
4. Load the most relevant project-specific pattern.
5. Compose a custom outline.
6. Fill sections from repository evidence.
7. Use TODOs for missing evidence.
8. Score pattern fit and evidence grounding.
9. Revise before final output.

## Composition examples

```text
Mobile app:
Hero → screenshots → features → install → architecture → roadmap

CLI:
Hero → install → quick usage → commands → examples → configuration

Library:
Hero → install → minimal code example → API → advanced usage → contributing

SaaS:
Hero → product story → demo → features → architecture → deployment

Open-data project:
Hero → data sources → pipeline → schema → usage → update frequency → contribution
```

## Pattern selection rules

- Choose one primary pattern.
- Add secondary sections only when evidence supports them.
- Do not include every possible section.
- Prioritize the reader's first successful outcome.
- Prefer concrete examples over abstract explanation.
- Use screenshots/demos early for visual products.
- Use install/quick-start early for developer tools.
- Use data provenance early for open-data projects.

## Evidence requirements

Each pattern specifies `required_evidence`. Do not write a section unless the repository supports it, or the section is explicitly marked TODO.

Examples:

- Do not document shell completion unless completion scripts or CLI docs exist.
- Do not claim App Store availability unless release links/config exist.
- Do not claim Stripe billing unless Stripe code/env/config exists.
- Do not claim real-time data updates unless schedules, cron jobs, or docs prove it.

## Scoring impact

The pattern library adds these scoring dimensions:

```yaml
pattern_fit:
  description: "Does the README structure match the repository type?"
  score: 0-10

evidence_grounding:
  description: "Are claims backed by repository evidence?"
  score: 0-10

visual_readability:
  description: "Is the README scannable and visually strong?"
  score: 0-10

developer_onboarding:
  description: "Can a developer install, run, and contribute?"
  score: 0-10

product_story:
  description: "Does the README clearly explain why the project matters?"
  score: 0-10
```

A generated README should only be considered successful if its final score is at least `9.0`.
