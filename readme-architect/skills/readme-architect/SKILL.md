---
name: readme-architect
description: Use when generating, rewriting, auditing, or improving README.md files for software repositories. Inspect repository evidence first, classify project type, compose an adaptive README from best-practice patterns, avoid copied templates and hallucinated claims, score pattern fit/evidence grounding, self-critique, and revise before final output.
version: 1.1.0
author: README Architect contributors
license: MIT
metadata:
  hermes:
    tags: [readme, documentation, open-source, technical-writing, repository-analysis, pattern-library]
    related_skills: [codebase-inspection, requesting-code-review, writing-plans]
---

# README Architect

## Overview

README Architect generates world-class `README.md` files from software repositories. It behaves like a senior staff engineer, technical writer, product marketing manager, developer advocate, and open-source maintainer working together.

The operating principles are strict:

> Understand first. Document second.

> README Architect does not copy templates. It learns patterns, detects project context, and composes the most useful README for that repository.

Never write a README from guesses. Every feature, command, architecture claim, integration, supported platform, screenshot, and setup step must be backed by repository evidence or clearly marked as missing.

## When to Use

Use this skill when the user asks to:

- generate a README for a repository
- rewrite or improve an existing README
- make a project GitHub-ready
- document architecture, onboarding, features, or setup
- create README sections for a mobile app, SaaS product, web app, CLI, library, browser extension, desktop app, API platform, or open-data project
- audit README quality and produce a score
- create a README that feels comparable to strong open-source projects such as Next.js, Supabase, FastAPI, Home Assistant, Payload CMS, Appwrite, LangChain, or Cal.com

Do not use this skill for:

- API reference documentation only
- changelogs or release notes only
- marketing landing pages disconnected from the repository
- speculative product copy without source evidence

## Non-Negotiable Rules

1. **Evidence Rule:** Every feature, command, integration, architecture claim, and support statement must be backed by repository evidence. If uncertain, write a TODO instead of inventing.
2. **Adaptive README Rule:** Do not generate the same structure for every project. Choose the structure based on project type, evidence, audience, and likely user intent.
3. **Anti-Copying Rule:** Do not copy external README templates verbatim. Use external examples only as pattern inspiration.
4. **Do not trust filenames alone.** Validate claims by reading manifests, source files, scripts, docs, tests, or config.
5. **Do not overwrite blindly.** If an existing `README.md` exists, show the draft or ask before replacing unless the user explicitly requested overwrite.
6. **Verify commands when practical.** Prefer commands found in manifests, Makefiles, docs, or CI. If a command cannot be verified safely, label it as inferred.
7. **Avoid AI voice.** No generic hype, repeated claims, hollow buzzwords, or filler introductions.
8. **Revise after scoring.** The first draft is not final. Score it, critique it, fix the highest-impact weaknesses, then deliver.

## Pattern Selection Workflow

1. Inspect repository evidence.
2. Classify project type.
3. Load the universal README pattern from `patterns/universal.yml`.
4. Load the most relevant project-specific pattern from `patterns/<type>.yml`.
5. Compose a README structure for this repository, not a static template.
6. Generate content from repository evidence.
7. Mark missing information as TODO.
8. Score the README, including pattern fit and evidence grounding.
9. Improve before final output.

Pattern composition examples:

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

Borrow sections across patterns when evidence supports it. Example: a SaaS repository with a CLI admin tool may use the SaaS pattern as primary and add a CLI commands section.

## Pattern Library

The pattern library lives at repository root under `patterns/`:

- `universal.yml` — shared README components and quality gates
- `mobile-app.yml` — mobile screenshots, device/simulator install, permissions, release/distribution
- `web-app.yml` — demo, screenshots, local dev, framework/deployment evidence
- `saas.yml` — product story, auth/billing/database/deployment, integrations
- `cli.yml` — install, one-line usage, commands, flags, examples, shell completion
- `library.yml` — package install, minimal code, API, compatibility, examples
- `chrome-extension.yml` — manifest, permissions, load-unpacked install, privacy
- `desktop-app.yml` — platform support, screenshots, packaging, distribution
- `api-platform.yml` — quick request, auth, endpoints/schema, local server, deployment
- `open-data-project.yml` — sources, pipeline, schema, update frequency, reproducibility, attribution

Read `docs/pattern-library.md` and `docs/source-inspiration.md` when adapting patterns or explaining how this skill works.

## Repository Understanding Engine

Before writing, build an evidence map. Inspect at least the following categories when they exist.

### 1. Project metadata

Look for:

- `package.json`
- `pnpm-lock.yaml`, `yarn.lock`, `package-lock.json`, `bun.lockb`
- `pyproject.toml`, `requirements.txt`, `setup.py`, `setup.cfg`, `uv.lock`, `poetry.lock`
- `Cargo.toml`, `Cargo.lock`
- `go.mod`, `go.sum`
- `pom.xml`, `build.gradle`, `settings.gradle`, `gradle.properties`
- `.csproj`, `.sln`
- `composer.json`
- `Gemfile`

Extract:

- project name
- package name
- description
- language/runtime
- framework dependencies
- scripts and commands
- entry points
- license metadata
- package publishing metadata

### 2. Runtime, build, and deployment

Inspect:

- `Dockerfile`, `docker-compose.yml`, `compose.yml`, `compose.yaml`
- `Makefile`, `justfile`, `Taskfile.yml`
- `.github/workflows/*`
- `.gitlab-ci.yml`
- `.circleci/config.yml`
- `vercel.json`, `netlify.toml`, `railway.toml`, `fly.toml`, `render.yaml`
- Kubernetes manifests, Helm charts, Terraform, Pulumi, CloudFormation

Extract install/build/test/start commands, environment variables, deployment targets, CI checks, containerized services, databases, and dependent services.

### 3. Architecture

Inspect top-level and source directories:

- `src/`, `app/`, `pages/`, `routes/`, `api/`, `server/`, `backend/`, `frontend/`
- `components/`, `screens/`, `features/`, `modules/`, `services/`, `lib/`, `utils/`
- `cmd/`, `internal/`, `pkg/`
- `models/`, `schemas/`, `migrations/`, `db/`, `prisma/`
- `tests/`, `test/`, `__tests__/`, `spec/`

Detect frontend framework, backend framework, database, auth provider, third-party integrations, service boundaries, API surface, state management, jobs/workers, hosting, and cloud providers.

### 4. Feature extraction

Features must be backed by evidence. Useful evidence includes routes, pages, screens, controllers, handlers, API endpoint names, module names plus source content, tests, existing docs, UI strings, CLI command definitions, migrations/schema files, examples, and fixtures.

Bad feature extraction:

```text
The project has analytics, collaboration, and AI-powered workflows.
```

Good feature extraction:

```text
- Resume analysis workflow — backed by `src/app/analyze/page.tsx`, `src/lib/resume/analyzer.ts`, and `tests/resume-analyzer.test.ts`.
- Stripe billing portal — backed by `src/app/api/stripe/portal/route.ts` and `STRIPE_SECRET_KEY` in `.env.example`.
```

### 5. Screenshot discovery

Inspect `assets/`, `images/`, `screenshots/`, `docs/`, `public/`, and platform-specific resource directories. Include screenshots only when image files exist. Prefer relative paths.

If screenshots are expected but missing, write:

```markdown
## Screenshots

TODO: Add screenshots showing the main product flow.
```

## Project Classifier

Classify by evidence, not intuition. Multiple labels can be present, but choose one primary type for README structure.

```yaml
mobile_app:
  signals:
    - AndroidManifest.xml
    - build.gradle
    - Kotlin/Swift files
    - ios/
    - android/

cli:
  signals:
    - bin/
    - commander
    - click
    - argparse
    - yargs
    - console_scripts

library:
  signals:
    - package exports
    - src/index.*
    - pyproject package
    - published package metadata

web_app:
  signals:
    - Next.js
    - Vite
    - React
    - Vue
    - Svelte
    - Astro

saas:
  signals:
    - auth
    - billing
    - dashboard
    - API routes
    - database migrations

chrome_extension:
  signals:
    - manifest.json
    - background script
    - content script
    - permissions

desktop_app:
  signals:
    - Electron
    - Tauri
    - SwiftUI macOS
    - native desktop app config

api_platform:
  signals:
    - OpenAPI
    - REST routes
    - GraphQL schema
    - server framework

open_data_project:
  signals:
    - datasets
    - data pipeline
    - CSV/JSON generation
    - scraping/import scripts
```

Tie-breakers:

- Prefer the primary user-facing artifact. A Next.js SaaS with auth/billing is usually `saas`, not just `web_app`.
- Prefer `cli` when the main package entry point is executable and examples are terminal-first.
- Prefer `library` when the main consumption path is import/API usage.
- Prefer `api_platform` when programmatic API access is the product.
- Prefer `open_data_project` when data provenance, schema, and reproducibility are central.

## Evidence Map Format

Before drafting, produce a compact evidence map:

```yaml
project:
  name: "..."
  primary_type: "mobile_app | web_app | saas | library | cli | chrome_extension | desktop_app | api_platform | open_data_project | default"
  secondary_types: []
  description_source: "package.json | pyproject.toml | inferred from ..."
  license: "MIT | Apache-2.0 | TODO"

pattern_selection:
  universal_pattern: "patterns/universal.yml"
  primary_pattern: "patterns/<type>.yml"
  borrowed_sections: []
  rationale: "..."

stack:
  languages: []
  frontend: []
  backend: []
  database: []
  auth: []
  deployment: []
  integrations: []

commands:
  install: []
  dev: []
  build: []
  test: []
  lint: []
  start: []

features:
  - name: "..."
    evidence: ["path", "path:line if available"]
    confidence: "high | medium | low"

architecture:
  components:
    - name: "..."
      evidence: []
  data_flow: []

screenshots:
  - path: "..."

missing:
  - "Deployment docs not found"
  - "Roadmap not found"
```

Only high- and medium-confidence claims should appear in the README. Low-confidence observations belong in TODOs or are omitted.

## README Structure Composition

Do not start from a fixed section list. Compose based on the primary pattern:

- **Mobile app:** Hero → screenshots → features → install on device/simulator → configuration → permissions → architecture → roadmap
- **CLI:** Hero → install → quick usage → commands → examples → configuration → development → license
- **Library:** Hero → install → minimal code example → API overview → advanced usage → compatibility → contributing
- **SaaS:** Hero → product story → demo/screenshots → features → architecture → local setup → database/configuration → deployment
- **Open-data project:** Hero → data sources → pipeline → schema → usage → update frequency → reproducibility → license/attribution
- **API platform:** Hero → quick request → auth → endpoints/schema → architecture → local development → deployment
- **Chrome extension:** Hero → screenshots → load unpacked → permissions → architecture → privacy → release packaging
- **Desktop app:** Hero → screenshots → platform support → install/run → features → packaging → architecture

When the repository has insufficient evidence for a recommended section, include a targeted TODO or skip the section if it would distract.

## Product Storytelling

Answer four questions with concrete language:

- **What:** What does this project do?
- **Why:** Why was it built?
- **Who:** Who is it for?
- **Differentiation:** What makes it meaningfully different?

Bad:

```text
A powerful platform for civic engagement.
```

Good:

```text
CitizenEye helps citizens understand how elected representatives vote, monitor upcoming legislation, and take action before decisions become law.
```

Rules:

- Prefer one precise sentence over three vague sentences.
- Use domain nouns found in the repo.
- Avoid “powerful”, “seamless”, “robust”, “AI-powered”, “next-generation”, unless the repo proves the specific capability.
- Do not claim scale, security, production-readiness, or enterprise support unless evidence exists.

## Visual Quality

Use visual elements when they improve scanning:

- Mermaid diagrams for architecture/data flow
- badges for license, CI, package version, release, platform, framework, or package registry
- screenshot galleries when screenshots exist
- feature tables for evidence-rich features
- command/API tables for CLI/API/library projects
- roadmap tables
- project structure trees

Keep diagrams honest. Use TODO nodes when boundaries are unclear.

## Getting Started Rules

Commands must come from evidence where possible:

- package manager lockfile determines package manager preference
- `package.json.scripts` determines JS commands
- `Makefile` targets can be used when present
- `.env.example` determines configuration variables
- CI files indicate verified test/build commands
- Docker/Compose files indicate container setup

When uncertain, say so:

```markdown
TODO: Confirm the production start command.
```

Do not invent:

- `npm install` if the repo clearly uses `pnpm`
- `npm run dev` if no dev script exists
- Docker commands if no Dockerfile/compose evidence exists
- cloud deployment steps without provider config

## README Quality Scoring Engine

After drafting, score the README. The final README is successful only if `overall_score >= 9.0`. If the repository lacks evidence, the score should reflect that honestly.

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
  - README structure fits the detected SaaS project pattern.
  - Commands are grounded in package scripts and CI.
improvements:
  - Missing screenshots.
  - Roadmap is inferred from TODOs rather than maintainer-provided planning docs.
```

Scoring guidance:

- 10 = excellent, evidence-backed, polished, immediately useful
- 8 = strong, minor gaps remain
- 6 = usable but incomplete
- 4 = substantial omissions or uncertainty
- 2 = misleading, thin, or hard to use
- 0 = absent or unusable

Revision rules:

- If `overall_score < 9.0`, revise or explain what repository evidence is missing.
- If `evidence_grounding < 9`, revise before final output.
- If `pattern_fit < 9`, reconsider project classification and section order.
- If `developer_onboarding < 9`, improve setup/config/test/contribution sections or mark precise TODOs.

## Self-Critique Pass

Ask and answer these before final delivery:

1. Is anything hallucinated?
2. Does the README structure fit the detected project type?
3. Is onboarding complete?
4. Are commands verified from repository evidence or clearly marked?
5. Is the value proposition concrete?
6. Is architecture understandable?
7. Are screenshots available and included?
8. Is the project approachable for new contributors?
9. Is there repeated or generic content?
10. Are TODOs explicit where repository evidence is missing?
11. Does the result feel composed for this repository rather than copied from a generic template?

Then revise the README to fix the highest-impact issues.

## Output Modes

### Draft mode

Use when the user wants review before write:

- Show evidence summary
- Show project classification and selected pattern
- Show generated README
- Show score and self-critique
- Ask whether to write the file

### Write mode

Use when the user explicitly asks to create or replace `README.md`:

- Backup or preserve existing README when appropriate
- Write the README
- Report changed path
- Include score and unresolved TODOs

### Audit mode

Use when improving an existing README:

- Score current README
- Identify pattern mismatch and evidence gaps
- Rewrite or patch sections
- Score revised README

## Open Source Excellence Sections

Generate these when applicable:

- `Contributing`
- `Development Setup`
- `Roadmap`
- `Support`
- `Acknowledgements`
- `License`

Do not claim open-source maturity that is not present. If no contributing docs exist, include a simple contributor path and TODOs.

## Common Pitfalls

1. **Writing before inspecting.** This causes hallucinated features and fake commands. Always build an evidence map first.
2. **Using one structure for everything.** A CLI README and mobile app README should not have the same section order.
3. **Copying external templates.** Pattern inspiration is allowed; verbatim template copying is not.
4. **Over-marketing.** Strong READMEs are specific, not loud. Replace hype with concrete outcomes.
5. **Skipping screenshots.** For UI projects, missing screenshots materially weakens the README. Search for them and include them when present.
6. **Using the wrong package manager.** Respect lockfiles and CI. `pnpm` repos should not get `npm` instructions unless evidence supports both.
7. **Treating every module as a feature.** A feature is user-meaningful behavior, not just a folder name.
8. **Pretending TODOs are weakness.** TODOs are better than hallucination. They tell maintainers exactly what evidence is missing.
9. **Forgetting contributors.** Public GitHub projects need development setup, tests, contribution workflow, license, and support expectations.
10. **Making diagrams too detailed.** Architecture diagrams should orient readers, not mirror every file.

## Verification Checklist

Before final response:

- [ ] Repository was inspected before writing
- [ ] Evidence map was created
- [ ] Project type was classified with evidence
- [ ] Universal and project-specific patterns were considered
- [ ] README structure fits project type and audience
- [ ] README contains no unsupported claims
- [ ] Setup commands are verified or marked TODO/inferred
- [ ] Screenshots were searched and included if found
- [ ] Architecture is explained with a diagram when useful
- [ ] Open-source sections are present when applicable
- [ ] Scoring YAML includes pattern fit and evidence grounding
- [ ] Overall score is at least 9.0 or gaps are explained
- [ ] Self-critique was performed
- [ ] Final README was revised after critique
