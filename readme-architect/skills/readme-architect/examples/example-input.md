# Example input request

Use README Architect on this repository and generate a README draft. Do not overwrite the existing README until I approve it.

Repository evidence discovered by the agent:

```yaml
project:
  name: CitizenEye
  type: mobile-app
  description_source: inferred from app screens and docs
  license: TODO
stack:
  languages: [Kotlin]
  frontend: [Jetpack Compose]
  backend: []
  database: []
  auth: []
  deployment: []
  integrations: [Assemblée nationale public data]
commands:
  build: ["./gradlew assembleDebug"]
  test: ["./gradlew test"]
features:
  - name: Representative activity feed
    evidence: ["app/src/main/java/.../ActivityFeedScreen.kt"]
    confidence: high
  - name: Vote detail cards
    evidence: ["app/src/main/java/.../VoteDetailScreen.kt"]
    confidence: high
screenshots:
  - path: docs/screenshots/feed.png
  - path: docs/screenshots/vote-detail.png
missing:
  - License file not found
  - Deployment/release instructions not found
```
