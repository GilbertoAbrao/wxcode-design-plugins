---
name: admin-carbon-devops
description: |
  Dark-mode CI/CD operations dashboard for DevOps and platform engineering teams.
  Terminal-inspired aesthetic: near-black backgrounds, green accent, monospace build
  IDs and commit SHAs. Layout: slim top navbar with repo/env switcher + search +
  avatar, left icon rail for section navigation, 4 KPI tiles (deploys today / build
  success rate / open incidents / MTTR), a pipeline board with per-run stage chips
  (Build / Test / Deploy each pass or fail), a deploy-frequency inline SVG chart,
  a builds table with status pills, and an incidents side panel. Use when the brief
  mentions CI/CD, pipelines, deployments, DevOps, platform engineering, or a
  developer-facing operations console.
triggers:
  - "devops dashboard"
  - "ci/cd admin"
  - "pipeline dashboard"
  - "deployment dashboard"
  - "platform engineering"
  - "build health"
  - "dark ops dashboard"
  - "terminal admin"
  - "painel devops"
  - "运维控制台"
od:
  mode: prototype
  surface: web
  scenario: operations
  preview:
    type: html
    entry: example.html
  design_system:
    requires: true
    sections: [color, typography, layout, components]
  craft:
    requires: [pixel-discipline, laws-of-ux]
  example_prompt: "Build me a dark-mode DevOps admin dashboard for CI/CD pipelines — top navbar with repo/env switcher, left icon rail, KPI tiles for deploys and build health, pipeline board with stage chips, deploy frequency chart, builds table, and incident panel."
---

# Carbon DevOps Admin Skill

Produce a dark-mode CI/CD operations dashboard with a terminal-inspired developer aesthetic.

## Palette (CSS custom properties on :root)
- `--accent`: #22c55e (green primary)
- `--accent-hi`: #4ade80 (green hover/highlight)
- `--blue`: #3b82f6 (secondary accent, links, info)
- `--blue-hi`: #60a5fa
- `--warn`: #f59e0b (warning amber)
- `--danger`: #ef4444 (failure red)

Hardcoded neutrals (not tokens): bg `#0b0d10`, surface `#14171c`, raised `#1c2128`, border `#262c34`, text `#e6edf3`, muted `#8b949e`.

## Typography
- Body: system stack — `-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`
- Monospace (build IDs, SHAs, branch names): `ui-monospace, "SF Mono", Menlo, "Cascadia Code", monospace`
- No external font loads.

## Workflow
1. Read active DESIGN.md if present; otherwise use the Carbon DevOps palette above.
2. Extract from the brief: repo names, environment names (production / staging / canary), KPI figures, pipeline names, team names, incident labels.
3. Layout construction:

### Top Navbar (48px, bg #14171c, border-bottom #262c34)
- LEFT: hamburger icon + repo selector dropdown (name + branch badge) + environment pill switcher (prod / staging).
- CENTER: search bar (placeholder "Jump to pipeline, commit, branch…").
- RIGHT: bell icon with incident count badge + avatar circle with initials.

### Left Icon Rail (48px wide, bg #14171c, border-right #262c34)
- Stacked icon buttons (SVG only, no labels): Dashboard / Pipelines / Deploys / Incidents / Settings. Active item has green left-bar indicator and slightly lighter bg.

### Main Content Area (dark bg #0b0d10, padding 24px)

#### 4 KPI Tiles (grid, 4 columns)
Each tile: bg #14171c, border #262c34, border-radius 8px, padding 20px.
- Tile contents: small uppercase muted label, large number (white), delta chip below (green up / red down), small inline SVG sparkline in the top-right corner area.
- Tiles: "Deploys Today", "Build Success Rate", "Open Incidents", "MTTR".

#### Pipeline Board (full width, bg #14171c, border #262c34, radius 8px)
- Header: "Pipeline Runs" title + "View all" link in blue.
- 5 pipeline run rows, each: pipeline name (monospace) + commit SHA chip + author + branch + timestamp + three stage chips (Build / Test / Deploy) each colored pass (green outline) or fail (red outline) or running (amber + spinner dot) + a run-duration badge.

#### Two-column grid (chart left 2/3 + incidents right 1/3)
- LEFT: "Deploy Frequency" card — inline SVG bar chart (7 days, bars colored green for successful deploys, red for rollbacks, labels Mon–Sun, y-axis deploy counts). Card header: title + "Last 7 days" subtitle.
- RIGHT: "Active Incidents" card — list of 4 incidents each with severity pill (P1/P2/P3 colored red/amber/blue), service name, short description, opened-ago timestamp.

#### Builds Table (full width, bg #14171c, border #262c34, radius 8px)
- Header: "Recent Builds" + filter tabs (All / Passing / Failing / Cancelled).
- 7 rows: build ID (monospace #) / branch / commit SHA (monospace truncated) / triggered-by / status pill / duration / actions link.
- Status pills: Passed (green bg), Failed (red bg), Running (amber bg + dot), Cancelled (muted bg).

4. SVG rules: all chromatic fills/strokes use `var(--token)` or `currentColor`; neutrals hardcoded.
5. Animations: subtle fade-in on page load (opacity 0→1, 300ms ease-out). Status dot for "Running" pulses with a CSS keyframe.
6. One inline `<style>`, semantic HTML, no external assets, no CDNs, no lorem ipsum — invent repo names, SHAs, authors, figures.

## Output contract

```
<artifact identifier="admin-carbon-devops" type="text/html" title="Carbon DevOps Admin">
<!doctype html>...</artifact>
```
