# README Architect Philosophy

README Architect exists to produce READMEs that maintainers would be comfortable publishing on serious open-source repositories.

## Pattern-aware, not template-bound

README Architect does not copy templates. It learns patterns, detects project context, and composes the most useful README for that repository. Best-practice examples are used to extract reusable documentation principles, not to reproduce a fixed structure or copied wording.

## Understand first. Document second.

The README is a derived artifact. It should be generated from repository evidence, not from the agent's assumptions about what similar projects usually do.

Evidence can come from:

- manifests and lockfiles
- source code
- scripts and build files
- CI/CD configuration
- existing docs
- tests
- screenshots and assets
- deployment configuration
- schema and migrations

When evidence is missing, the honest output is a TODO, not a confident invention.

## Accuracy beats completeness

A short accurate README is better than a complete-looking README with fake setup instructions or hallucinated product features.

Prefer:

```markdown
TODO: Add deployment instructions.
```

Over:

```markdown
Deploy to Vercel with one click.
```

unless `vercel.json`, framework conventions, or existing docs prove the claim.

## Specific beats impressive

Avoid generic language:

- powerful
- seamless
- robust
- next-generation
- cutting-edge
- all-in-one
- AI-powered

Replace it with concrete descriptions of user outcomes and technical behavior.

## The README has multiple audiences

A strong README serves:

- users deciding whether the project solves their problem
- developers trying to run it locally
- contributors trying to understand architecture
- maintainers who need clear support/contribution boundaries
- search/discovery systems that need accurate keywords and structure

## TODOs are part of the job

TODOs should be precise and useful:

```markdown
TODO: Add screenshots for the dashboard and settings flow.
TODO: Confirm whether `pnpm build` is the production build command.
TODO: Add license.
```

They should not be vague:

```markdown
TODO: Improve docs.
```
