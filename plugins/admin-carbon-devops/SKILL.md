---
name: admin-carbon-devops
description: |
  Near-black terminal admin aesthetic: deep carbon canvas (#0b0d10), green accent
  (#22c55e), blue secondary (#3b82f6), monospace IDs and codes on every key cell,
  amber warning and red danger pills. Archetype = repo-switcher navbar with env
  pill switcher + search + icon rail, 4 KPI tiles with sparklines, a pipeline
  board (rows of name / code chip / stage chips / duration), a two-column grid
  (inline SVG bar chart left + severity-feed side panel right), and a dense
  records table with status pills. Built for high-density operational consoles
  that show state changes at a glance.
triggers:
  - "terminal admin"
  - "dark carbon admin"
  - "near-black green accent dashboard"
  - "monospace ops console"
  - "green accent dark admin"
  - "dense pipeline board"
  - "status-pill records table"
  - "dark developer console"
example_prompt: "Apply this dark carbon terminal admin aesthetic to my domain"
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
---

# Carbon Admin — Visual Archetype

This plugin contributes a **look** (dark carbon, green accent, monospace data,
dense tabular UI) and a **structure** (entity-switcher navbar + icon rail + KPI
tiles + pipeline board + chart + side panel + records table, plus list / form /
detail screens). It does **not** contribute a domain — the subject matter comes
from the Knowledge Base and the user's prompt. Treat the example below as
illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property; hardcode the neutral dark ramp.

- **Canvas / surfaces:** page `#0b0d10`; raised panel `#14171c`; inset / hover
  `#1c2128`; hairline border `#262c34`; stronger hover `#30363d`.
- **Text ramp:** primary `#e6edf3`, muted `#8b949e`, faint `#6e7681`.
- **Accent (green):** `--accent: #22c55e`, `--accent-hi: #4ade80`,
  `--accent-dim: color-mix(in srgb, #22c55e 12%, transparent)`. Active nav,
  primary CTA, positive state chips, passing status, delta-up.
- **Blue secondary:** `--blue: #3b82f6`, `--blue-hi: #60a5fa`. Links, info
  chips, search focus ring, secondary accent cells.
- **State ramp (as tokens):** `--state-pass: #22c55e`, `--state-fail: #ef4444`,
  `--state-run: #f59e0b` (amber / in-progress), `--state-skip: #6e7681`,
  each with a `…-dim` tint at ~12% alpha for pill backgrounds. Deltas:
  `--delta-up: #4ade80`, `--delta-down: #f87171`. Severity: `--sev-p1: #ef4444`,
  `--sev-p2: #f59e0b`, `--sev-p3: #3b82f6`.
- **Typography:** body `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
  sans-serif`; base 13px. Monospace (IDs, codes, hashes, branch names):
  `ui-monospace, "SF Mono", Menlo, "Cascadia Code", monospace`. Big figures
  28px / weight 700 / `letter-spacing: -.5px`. Micro-labels 10px, `text-transform:
  uppercase`, `letter-spacing: .08em`, muted. `font-variant-numeric: tabular-nums`
  on every numeric cell.
- **Density & radius:** 13px base, 11px vertical cell padding, 16–20px panel
  padding, 12px grid gaps; panel radius 8px, control radius 6px, pill radius
  10–12px, progress 4px / 2px radius.
- **Borders & shadows:** 1px hairlines do the separation work; no drop shadows
  on panels (flat terminal feel). 1px inner row dividers `#1c2128`.
- **Motion:** `.15s` background/border hover transitions, `.3s ease-out` page
  fade-in, `2s ease-in-out` pulse keyframe on in-progress/running dots.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Top navbar** (48px, panel bg, 1px bottom border, sticky): hamburger icon →
  **entity-switcher** (name + code badge, dropdown) → **env pill switcher**
  (2–3 pills, active one green-outlined) → flexible **search** input → icon
  button with incident/notification dot → avatar circle.
- **Left icon rail** (48px, panel bg, 1px right border): 5 icon-only nav items
  stacked (active item has green left-bar `::before` + green `color-mix` chip;
  hover lifts to inset bg), flex spacer, then a settings item pinned to the
  bottom. Each item carries a native `title` tooltip.
- **Main content** (page bg, ~20px padding, flex column, 16px gap): a **page
  header** (title + subtitle left, ghost + primary CTA right), then the region
  stack below.
- **KPI tile row** (4 tiles, equal grid, 12px gap): each tile = panel with a
  muted uppercase micro-label, a big tabular figure (white or accent-colored),
  a delta chip (green ▲ or red ▼), and a tiny inline SVG sparkline in the
  top-right corner. Figures recolor by state (green / amber / red).
- **Pipeline board / status board** (full-width panel): a titled card header
  with a "View all" link; rows of `[name chip] [code/sha chip] [author] [branch]
  [timestamp] [stage chips: Build / step-2 / step-3 each pass / fail / running]
  [duration badge]`. Stage chip: green-outline for pass, red-outline for fail,
  amber-outline + pulse dot for running.
- **Two-column grid (2fr / 1fr):**
  - **Left — chart card:** inline SVG bar chart (N bars, labeled axis), card
    header with title + period subtitle.
  - **Right — severity feed / side panel:** a titled panel listing rows of
    `[severity dot] [tag/code chip] [description] [elapsed time]`.
- **Full-width records table:** titled panel with filter tabs (All / State-A /
  State-B / …), dense rows with mono ID column, branch/code column, SHA column,
  triggered-by, status pill, duration, action link; footer with result count +
  pager.
- **Records list screen:** the records-table archetype as its own page — search
  input + filter chips + count, the same dense table, pager.
- **Record form screen:** sectioned cards of labelled fields; **rules appear as
  inline validation** — required marks (`*`), helper text under the field, and
  inline error messages on invalid fields, with the primary submit
  disabled-until-valid. No rules/checklist/validation-status panel.
- **Record detail screen:** a header band (ID + status pill + key actions), a
  meta grid of label/value pairs, and one or more related-data sub-panels (a
  stage-steps list or mini-table + an activity / log feed) below.

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key metrics,
status states, stage names, record columns, form fields and their rules, and
detail fields — and map them onto the archetype above. If no KB/domain is
supplied (standalone), use the Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules
become inline field validation. Do NOT render build/implementation notes or
designer controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent
> (entities, metrics, states, stage names, columns, fields) drawn from the KB
> + prompt.

```
Domain (illustrative): a software continuous-integration and delivery system.

Entity switcher  → repo: "acme-api / main".
Env pill switcher → "prod" (active) / "staging" / "canary".
Rail items       → Dashboard, Pipelines, Deploys, Incidents, (Settings).

KPI tiles (4):
  • Deploys Today   42  (▲7 from yesterday  · sparkline).
  • Build Success   94.2%  (▼1.3% from last week · sparkline).
  • Open Incidents  3  (▲1 · sparkline, figure red).
  • MTTR            8 min  (▼2 min from last week · sparkline).

Pipeline board   → "Pipeline Runs" — 5 rows of
  [acme-api/build · #1847] [sha:3f2a] [alice] [feat/auth] [2 min ago]
  [Build ✓] [Test ✓] [Deploy ⟳] [1m 23s].
  Stage chip states: pass (green outline), fail (red outline),
  running (amber outline + pulse dot).

Two-column grid:
  Left   → "Deploy Frequency" — 7-bar SVG chart (Mon–Sun, green = success,
            red = rollback, y-axis = count, labeled).
  Right  → "Active Incidents" — 4 rows of
            [P1 dot] [SVC-AUTH] [Token refresh timeout] [23 min ago].

Records table    → "Recent Builds" — filter tabs All / Passing / Failing /
  Cancelled. 7 rows: Build ID (mono) / Branch / SHA (mono) /
  Triggered by / Status pill / Duration / Action.
  Status pills: Passed (green), Failed (red), Running (amber), Cancelled (muted).

List screen      → all pipeline runs, search + filter chips (status, repo),
  paginated.

Form screen      → "New Pipeline Trigger": repo (required select), branch
  (required text), environment (required select), run mode (required radio),
  label (optional). Rules shown as required marks + helper text + inline errors;
  "Trigger Pipeline" disabled until valid.

Detail screen    → one build: header (build ID + status pill + actions),
  meta grid (repo, branch, SHA, triggered by, started, duration),
  "Stage Steps" related table + "Build Log" activity feed.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, status states, stage/step names, record columns, form fields +
   rules, detail fields — from the KB + prompt. Standalone: use the Example
   instantiation above.
3. Build each screen in the Visual language + Layout archetype above, imitating
   the example set in `assets/` (dashboard, list, form, detail) and the
   `assets/template.html` seed — with fresh content for the real domain, NOT
   the example labels.
4. Express domain rules as INLINE field validation (required marks, helper text,
   inline errors, disabled-until-valid submit). Never render
   rules/checklist/validation-status/build-note panels or designer/demo controls.
5. Use `ui-monospace` for IDs, codes, hashes, and branch names.
   `font-variant-numeric: tabular-nums` on every numeric cell.
6. One inline `<style>`, semantic HTML5, no external assets, no CDNs —
   self-contained.

## Output contract

```
<artifact identifier="admin-carbon-devops" type="text/html" title="Carbon Admin">
<!doctype html>...</artifact>
```
