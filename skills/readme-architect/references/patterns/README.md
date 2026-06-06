# README Best-Practice Pattern Library

README Architect does not copy templates. It learns patterns, detects project context, and composes the most useful README for that repository.

This directory contains reusable README composition patterns. The patterns are not complete READMEs and are not copied from any external template. They describe section priorities, evidence requirements, visual conventions, and anti-patterns for different project types.

## How patterns are used

1. Inspect repository evidence.
2. Classify the project type from observable signals.
3. Load `universal.yml`.
4. Load the closest project-specific pattern.
5. Compose a README outline that fits the repository, audience, and available evidence.
6. Generate content only from verified repository facts.
7. Mark missing information with TODOs.
8. Score pattern fit and evidence grounding before final output.

## Available patterns

| Pattern | Use for |
| --- | --- |
| `universal.yml` | Components shared by nearly all high-quality READMEs |
| `mobile-app.yml` | Android, iOS, React Native, Expo, Flutter, Swift, Kotlin apps |
| `web-app.yml` | Frontend-heavy web applications and dashboards |
| `saas.yml` | Multi-user products with auth, billing, deployment, or database workflows |
| `cli.yml` | Command-line tools and developer utilities |
| `library.yml` | Importable packages, SDKs, frameworks, and reusable modules |
| `chrome-extension.yml` | Browser extensions with manifests, permissions, background/content scripts |
| `desktop-app.yml` | Electron, Tauri, native macOS/Windows/Linux apps |
| `api-platform.yml` | REST, GraphQL, OpenAPI, service backends, API-first platforms |
| `open-data-project.yml` | Datasets, scraping/import pipelines, civic data, reproducible data workflows |

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
