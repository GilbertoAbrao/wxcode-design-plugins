---
name: admin-meadow-agri
description: |
  Light-mode natural admin aesthetic: white and #f7faf5 surfaces, #e6ece1
  borders, accent green (#16a34a / #22c55e) and earth-amber (#a16207) on a
  slate neutral ramp, Inter type with tabular figures, 12px soft card radii,
  generous whitespace, and gentle 1px separators. Archetype = 240px left
  sidebar (entity switcher + grouped nav sections) + full-width topbar with
  search + context badge + avatar + 4 KPI cards + left status board with
  inline SVG trend chart + IoT/telemetry readings table + right weather/
  context panel + task side card. Built for calm operational oversight
  interfaces that need to feel grounded rather than urgent.
triggers:
  - "light natural admin"
  - "green accent light dashboard"
  - "calm ops admin"
  - "white sidebar admin"
  - "earth-tone admin dashboard"
  - "soft light operational console"
  - "green-and-amber light admin"
  - "natural palette dashboard"
example_prompt: "Apply this light natural admin aesthetic to my domain"
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

# Meadow Admin — Visual Archetype

This plugin contributes a **look** (light natural, green accent, earth-amber,
generous whitespace, calm operational feel) and a **structure** (left sidebar
with entity switcher + grouped nav + 4 KPI cards + status board with trend
chart + telemetry table + side context panel, plus list / form / detail
screens). It does **not** contribute a domain — the subject matter comes from
the Knowledge Base and the user's prompt. Treat the example below as
illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property; neutral values may be hardcoded.

- **Canvas / surfaces:** page `#f7faf5`; card/panel `#ffffff`; inset/hover
  `#f1f5f9`; hairline border `#e6ece1`; subtle row divider `#f0f4ee`.
- **Text ramp:** primary `#1e293b`, secondary `#334155`, muted `#475569`,
  faint `#64748b`, micro `#94a3b8`.
- **Accent:** `--accent: #16a34a` (natural green), `--accent-hover: #22c55e`,
  `--accent-muted: rgba(22,163,74,0.10)`, `--accent-border: rgba(22,163,74,0.30)`.
  Primary CTAs, active nav item, key figures, progress fills, chart strokes.
- **Earth accent:** `--earth: #a16207`, `--earth-light: #fef3c7`,
  `--earth-border: #fde68a`. Secondary metric figures, season/context badges,
  weather icons.
- **Status ramp (as tokens):**
  `--state-healthy #16a34a`, `--state-healthy-bg #dcfce7`;
  `--state-moderate #d97706`, `--state-moderate-bg #fef3c7`;
  `--state-attention #dc2626`, `--state-attention-bg #fee2e2`;
  `--state-online #16a34a`, `--state-online-bg #dcfce7`;
  `--state-warning #d97706`, `--state-warning-bg #fef3c7`;
  `--state-offline #64748b`, `--state-offline-bg #f1f5f9`.
  Deltas: `--delta-up #16a34a / #dcfce7`, `--delta-down #dc2626 / #fee2e2`,
  `--delta-neutral #64748b / #f1f5f9`.
- **Chart tokens:** `--chart-primary: #16a34a`,
  `--chart-primary-fill: rgba(22,163,74,0.15)`,
  `--chart-secondary: #a16207`.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
  sans-serif`. Base 14px. `font-variant-numeric: tabular-nums` on every
  numeric cell. Micro-labels 10–11px, uppercase, `letter-spacing` ~0.06–0.08em,
  `#94a3b8`. Big figures 28px / weight 800 / `letter-spacing: -0.03em`.
- **Density & radius:** comfortable 11px vertical row padding, 18px panel
  padding, 14–16px grid gaps; card radius 12px, control radius 7–8px, pill
  radius 99px (full), badge radius 6px, progress bars 4px.
- **Borders & shadows:** 1px hairlines (`#e6ece1`) do the separation work;
  cards carry a soft `0 1px 4px rgba(0,0,0,0.04)` shadow (lift vs page).
- **Motion:** `.12s–.15s` background/border hover transitions. Default
  ease-out; never bouncy. No aggressive entrance animations.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns described by shape and behavior — not meaning.

- **Left sidebar** (240px, white, 1px right border, full-height): a brand
  area (logo SVG mark + wordmark + sub-label) → **entity switcher** (pill
  button with name + region sub-line + chevron) → **grouped nav sections**
  (uppercase 10px section label + nav items with leading 16px SVG glyph;
  active item = accent left-bar 3px + accent-muted background + accent text +
  weight 600; badge counts on certain items) → **user footer** pinned to
  bottom (small avatar + name + role label).
- **Topbar** (56px, white, 1px bottom border): page title left → **search
  pill** (flex-grow, magnifier SVG icon, placeholder) → spacer → **context
  badge** (earth-light/earth colors, short text) → icon notification button
  with dot → avatar circle.
- **Main content area** (page bg, 24px padding, vertical flex): a **page
  header row** (greeting/title + sub-line on the left; ghost + primary buttons
  on the right) → **KPI card row** (4 equal grid) → **2-column grid (1fr /
  300px)** containing the left stack and the right panel.
- **KPI card** (white, 1px border, 12px radius, soft shadow): absolute icon
  chip (top-right, 36×36, accent-muted bg + accent color); uppercase
  micro-label; big tabular figure with optional unit; delta chip or sub-label.
  Earth-variant icon chip for secondary-accent metrics.
- **Left stack:** one or more stacked cards: a **status board table**
  (card-header with title + action link; `<table>` with uppercase 10.5px
  header row, dense rows with state pills, progress indicators, numeric
  right-align) → an **inline SVG trend chart** card (two series — solid fill
  area + dashed line; dotted grid lines; x/y-axis labels; legend strip) → a
  **telemetry/readings table** (ID column in mono, field/location column,
  metric column, reading value column, status pill).
- **Right panel** (300px, flex column, 14px gap): a **context card** (hero
  strip with icon + big figure + label/sub-label; 5-item strip with icon +
  high/low or key sub-values) → a **task/action card** (card-header with
  count; rows of checkbox + priority-dot + label + assignee chip; ghost "add"
  CTA at the foot).
- **Records list screen:** search pill + filter chip row + result count, the
  dense status-board table pattern as a full-page table, pager.
- **Record form screen:** sectioned cards of labelled fields; **rules appear
  as inline validation** — required marks (`*`), helper text under the field,
  inline error messages on invalid fields, primary submit disabled until valid.
  No rules/checklist/validation-status panel.
- **Record detail screen:** breadcrumb → header band (title + status pill +
  key actions) → 3-col meta grid of label/value pairs → related-data
  sub-panels (readings sub-table or activity list).

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entity (entity
switcher label), key metrics (4 KPI figures + labels), status states for
status-board rows, telemetry/record list columns, form fields and their rules,
and detail fields — and map them onto the archetype above. If no KB/domain is
supplied (standalone), use the Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain
rules become inline field validation. Do NOT render build/implementation notes
or designer controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In
> WXCode this is IGNORED — replace every label with the real domain's
> equivalent (entities, metrics, states, columns, fields) drawn from the
> KB + prompt.

```
Domain (illustrative): a field-crop farm operations system.

Entity switcher  → farm: "Greenfield Station · Northern Valley Region".
Context badge    → active period: "Growing Season 2026".
Nav sections     → Overview (Dashboard, Map View), Crops (Fields, Harvest
                   Plan), Sensors (Live Readings, Alerts), Operations
                   (Tasks, Reports).

KPI cards (4):
  • Active Fields — 42 (▲+3 this season, green delta).
  • Yield Forecast — 1,840 t (▲+8.4% vs last yr, green delta).
  • Avg Soil Moisture — 61% (stable range, neutral delta).
  • Tasks Due — 7 (2 overdue, amber/red delta, earth-variant icon chip).

Status board (left) → "Fields Status" — rows of
  [field name] [crop badge with dot] [stage text] [Health pill] [area ha].
  States: Healthy / Moderate / Attention. Seven rows.
  Below: inline SVG area chart "Yield Forecast — 8-Week Outlook (tonnes)".
  Two series: Forecast (green fill) + Target (amber dashed line).

Telemetry table → "Sensor Readings" — Sensor ID (mono) / Field / Metric /
  Reading / Status pill (Online / Warning / Offline). Six rows.

Context card (right) → weather overview: hero (icon + 19°C + "Partly
  Cloudy" + location); 5-day forecast strip (day name + icon + hi/lo).

Task card (right) → "Tasks Due": 5 task rows (checkbox + priority dot +
  label + assignee initials chip); "Add task" ghost CTA.

List screen       → all records (e.g. fields list), search + filter chips
  (status, type), paginated dense table.

Form screen       → "New Record" (e.g. new field): entity name (required),
  description, area in ha (required, > 0), type/category (required select),
  assigned operator (required select), target date (required, not in the
  past), notes. Rules shown as required marks + helper text + inline errors;
  "Create" disabled until valid.

Detail screen     → one record (e.g. one field): breadcrumb → header
  (name + status pill + actions), 3-col meta grid (crop, area, stage, health,
  assigned, updated), related readings sub-table + recent activity.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entity,
   key metrics, status states, record columns, form fields + rules, detail
   fields — from the KB + prompt. Standalone: use the Example instantiation
   above.
3. Build each screen in the Visual language + Layout archetype above, imitating
   the example set in `assets/` (dashboard, list, form, detail) and the
   `assets/template.html` seed — with fresh content for the real domain, NOT
   the example labels.
4. Express domain rules as INLINE field validation (required marks, helper text,
   inline errors, disabled-until-valid submit). Never render
   rules/checklist/validation-status/build-note panels or designer/demo
   controls.
5. One inline `<style>`, semantic HTML5, `tabular-nums` on figures, no external
   assets, no CDNs — self-contained.

## Output contract

```
<artifact identifier="admin-meadow-agri" type="text/html" title="Meadow Admin">
<!doctype html>...</artifact>
```
