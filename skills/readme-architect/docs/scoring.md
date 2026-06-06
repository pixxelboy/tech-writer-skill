# README Scoring

Every README generated with README Architect should be scored before final delivery.

A generated README should only be considered successful if its final score is at least `9.0`.

README Architect does not copy templates. It learns patterns, detects project context, and composes the most useful README for that repository. The scoring model therefore measures both writing quality and whether the selected README structure fits the repository type.

## Criteria

### Pattern Fit, 0-10

Does the README structure match the repository type?

High score:

- mobile apps prioritize screenshots, platform support, device/simulator setup, permissions, and release flow
- CLIs prioritize install, quick usage, commands, flags, examples, and config
- libraries prioritize package install, minimal code example, API, compatibility, and examples
- SaaS products prioritize product story, demo, features, architecture, database/configuration, and deployment
- open-data projects prioritize data sources, pipeline, schema, update frequency, reproducibility, and attribution

Low score:

- same generic section order for every repository
- library README buries the first code example
- CLI README lacks command examples
- visual product README lacks screenshots/demo section despite available assets

### Evidence Grounding, 0-10

Are claims backed by repository evidence?

High score:

- features cite source files, routes, tests, docs, screens, commands, or schemas
- setup commands come from manifests, CI, Makefiles, lockfiles, or docs
- integrations are backed by dependency/config/env/source evidence
- missing facts are marked TODO

Low score:

- invented features
- unsupported integrations
- fake setup/deployment commands
- architecture diagram not grounded in code

### Visual Readability, 0-10

Is the README scannable and visually strong?

High score:

- strong hero sentence
- useful badges
- screenshots or demo links where available
- Mermaid diagrams for complex architecture/data flow
- tables for features, commands, APIs, roadmap, or config when helpful
- clean section hierarchy

Low score:

- wall of text
- repeated headings
- no visual hierarchy
- ignores available screenshots

### Developer Onboarding, 0-10

Can a developer install, run, test, and contribute?

High score:

- prerequisites are explicit
- package manager is correct
- environment variables are documented
- install/dev/build/test commands are present
- database/services setup is documented when applicable
- contribution path and local checks are clear

Low score:

- wrong package manager
- missing env vars
- no local run path
- no test/build instructions
- no contributor guidance

### Product Story, 0-10

Does the README clearly explain why the project matters?

High score:

- concrete one-sentence positioning
- user/audience is clear
- problem is specific
- differentiation is grounded in repository evidence
- no generic marketing filler

Low score:

- vague “platform” language
- unclear audience
- repeated value claims
- hype without proof

### Technical Accuracy, 0-10

Are commands, architecture, integrations, and setup details correct?

High score:

- commands are verified or clearly marked inferred/TODO
- architecture matches observed components
- environment/config docs match repository files
- package/runtime compatibility matches metadata

Low score:

- commands do not exist
- architecture mismatches source layout
- cloud/provider claims without config
- unsupported compatibility claims

## Score format

```yaml
overall_score: 9.2
criteria:
  pattern_fit:
    description: "Does the README structure match the repository type?"
    score: 9
  evidence_grounding:
    description: "Are claims backed by repository evidence?"
    score: 10
  visual_readability:
    description: "Is the README scannable and visually strong?"
    score: 9
  developer_onboarding:
    description: "Can a developer install, run, and contribute?"
    score: 9
  product_story:
    description: "Does the README clearly explain why the project matters?"
    score: 9
  technical_accuracy:
    description: "Are commands, architecture, integrations, and setup details correct?"
    score: 10
strengths:
  - README structure fits the detected project pattern.
  - Commands are grounded in package scripts and CI.
improvements:
  - Missing screenshots.
  - Roadmap is inferred from TODOs rather than maintainer-provided planning docs.
```

## Overall score

Use a weighted average unless the user asks otherwise:

```text
overall = (
  pattern_fit * 1.25 +
  evidence_grounding * 1.5 +
  visual_readability * 1.0 +
  developer_onboarding * 1.25 +
  product_story * 1.0 +
  technical_accuracy * 1.5
) / 7.5
```

Evidence grounding and technical accuracy carry the highest weight. A beautiful README with hallucinated claims should not score highly.

## Revision rules

- If `overall_score < 9.0`, revise the README or explain what repository evidence is missing.
- If `evidence_grounding < 9`, revise before final output.
- If `pattern_fit < 9`, reconsider project classification and section order.
- If `developer_onboarding < 9`, improve setup/config/test/contribution sections or mark precise TODOs.
