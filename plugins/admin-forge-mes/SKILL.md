---
name: admin-forge-mes
description: |
  Dark industrial-grade admin aesthetic: near-black canvas (#0c0f14), raised
  panels (#141922 / #1d2530), molten-orange accent (#f97316) on a steel-grey
  neutral ramp, Inter type with tabular-nums on every figure, dense 14px rows,
  8–10px radii, hairline #2a3340 borders, and crisp status pills. Archetype =
  entity-switcher navbar + icon rail + 4 KPI tiles + 2-column status board (rows
  of label / state pill / metric / progress / count) with an alerts side panel +
  full-width records table with status pills. Built for high-density operational
  consoles that have to read at a glance on a wall display.
triggers:
  - "dark industrial admin"
  - "near-black admin dashboard"
  - "dense data terminal"
  - "status-board dashboard"
  - "orange accent dark admin"
  - "operations control console"
  - "wall-display dashboard"
  - "painel escuro industrial"
example_prompt: "Apply this dark industrial admin aesthetic to my domain"
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

# Forge Admin — Visual Archetype

This plugin contributes a **look** (dark industrial, molten-orange accent, dense
tabular data) and a **structure** (entity-switcher navbar + icon rail + KPI tiles
+ status board + alerts panel + records table, plus list / form / detail screens).
It does **not** contribute a domain — the subject matter comes from the Knowledge
Base and the user's prompt. Treat the example below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property; hardcode the neutral dark ramp.

- **Canvas / surfaces:** page `#0c0f14`; raised panel `#141922`; inset / hover
  `#1d2530`; hairline border `#2a3340`; stronger hover border `#3a4455`.
- **Text ramp:** primary `#e6ebf2`, secondary `#c5cdd7`, muted `#8b96a5`, faint
  `#64748b`.
- **Accent:** `--accent: #f97316` (molten orange), `--accent-light: #fb923c`,
  `--accent-dim: rgba(249,115,22,.14)`. Primary CTAs, active nav, key figures,
  progress fills, chart strokes.
- **Status ramp (as tokens):** `--state-running #22c55e`, `--state-idle #f59e0b`,
  `--state-down #ef4444`, `--state-queued #64748b`, `--state-completed #22c55e`,
  `--state-hold #ef4444`, each with a `…-dim` tint at ~13–15% alpha for pill
  backgrounds. Deltas: `--delta-up #4ade80`, `--delta-down #f87171`. Severity:
  `--sev-critical #ef4444`, `--sev-warn #f59e0b`, `--sev-info #38bdf8`.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
  sans-serif`. Base 14px. `font-variant-numeric: tabular-nums` on **every** numeric
  cell. Micro-labels are 10–11px, `text-transform: uppercase`, `letter-spacing`
  ~.5px, muted. Big figures 28px / weight 800 / `letter-spacing: -.5px`. IDs and
  codes in a mono face (`"Courier New", monospace`).
- **Density & radius:** compact 11px vertical row padding, 14–16px panel padding,
  14px grid gaps; panel radius 10px, control radius 6–8px, pill radius 10–12px,
  progress bars 4px tall / 2px radius.
- **Borders & shadows:** 1px hairlines do the separation work; no drop shadows on
  panels (flat, terminal feel). 1px inner row dividers `#1d2530`.
- **Motion:** subtle only — `.12s–.15s` background/border hover transitions, a
  2s pulse on the live-status dot, `.4s ease` width transitions on progress bars.
  Default easing stays gentle; never bouncy.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Top navbar** (52px, surface bg, 1px bottom border, sticky): brand wordmark →
  **entity switcher** (pill button with leading glyph + chevron) → flexible
  **search** pill → **live status badge** (dot + short label) → icon button with
  notification dot → avatar.
- **Left icon rail** (56px, page bg, 1px right border): 4–5 icon-only nav items
  (active item filled accent on an accent-dim chip; hover lifts to surface bg), a
  flex spacer, then a settings item pinned to the bottom. Each item carries a
  native `title` tooltip.
- **Main content** (page bg, ~20px padding, vertical flow): a **page header**
  (title + sub-line on the left, ghost + primary buttons on the right), then the
  region stack below.
- **KPI tile row** (4 tiles, equal grid): each tile = surface panel with an icon
  chip + a delta chip on top, a big tabular figure, and an uppercase micro-label
  with a sub-line. Figures and icon chips recolor by state (orange / amber / red).
- **2-column grid (7fr / 5fr):**
  - **Left — status board:** a titled panel whose rows are
    `[label + sub] [state pill] [current / target metric over a thin progress bar]
    [count with glyph]`. Optionally followed by a second panel holding an inline
    **SVG trend chart** (polyline + area-fill + dotted gridlines + axis labels).
  - **Right — alerts / side panel:** a titled panel listing rows of
    `[severity dot] [tag chip] [description] [elapsed time]`, then a small
    sub-table (`label / reason / start / duration`), and a full-width ghost action
    button at the foot.
- **Full-width records table:** titled panel with ghost + primary header actions,
  a sticky uppercase header, dense rows with **status pills**, a mono ID column, a
  two-line code/name cell, right-aligned numerics, and a footer with a result
  count + pager.
- **Records list screen:** the records-table archetype as its own page —
  search + filter chips + a count, the same dense table, and a pager.
- **Record form screen:** sectioned cards of labelled fields; **rules appear as
  inline validation** — required marks (`*`), helper text under the field, and
  inline error messages on invalid fields, with the primary submit
  disabled-until-valid. No rules/checklist/validation-status panel.
- **Record detail screen:** a header band (title + status pill + key actions), a
  meta grid of label/value pairs, and one or more related-data sub-panels (the
  status-board row pattern or a mini-table) below.

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key metrics,
status states, record list/columns, form fields and their rules, and detail
fields — and map them onto the archetype above. If no KB/domain is supplied
(standalone), use the Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules
become inline field validation. Do NOT render build/implementation notes or
designer controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent
> (entities, metrics, states, columns, fields) drawn from the KB + prompt.

```
Domain (illustrative): a discrete-manufacturing Manufacturing Execution System.

Entity switcher  → plant: "Ironclad — Plant 1 · Sector A".
Live status badge → active shift: "Shift B · 06:00–14:00".
Rail items       → Dashboard, Production Lines, Work Orders, Reports, (Settings).

KPI tiles (4):
  • OEE 84.7% (orange figure, ▲3.1%, "Overall Equipment Effectiveness",
    "Target 85.0% · Availability 91%").
  • Units Output Today 14,382 (▲218, "Target 16,000 · 89.9% attained").
  • Downtime Minutes 47 (amber, ▲14 min, "This shift · 3 incidents").
  • Scrap Rate 2.1% (red, ▼0.4%, "Threshold 1.8% · 297 pcs scrapped").

Status board (left)  → "Production Lines" — rows of
  [Line A-01 · Stamping · Bay 1] [Running] [348/360 u/hr + bar] [3 ops].
  States used: Running / Idle / Down. Followed by an "Output Trend" SVG chart
  (units/hr, last 8 hours).

Alerts panel (right) → "Alerts · This Shift" — rows of
  [severity dot] [C-01] [Hydraulic press fault — E-Stop triggered] [23 min ago],
  a "Recent Downtime" sub-table (line / reason / start / min) and an
  "Acknowledge All Alerts" button.

Records table        → "Work Orders — Active": WO# / Product Code / Description /
  Qty (pcs) / Line / Due Date / Status pill (In Progress / Queued / Completed /
  On Hold).

List screen          → all work orders, search + filter chips (status, line),
  paginated.

Form screen          → "New Work Order": product code (required), description,
  quantity (required, > 0), line (required select), due date (required, not in
  the past), priority. Rules shown as required marks + helper text + inline
  errors; "Create Work Order" disabled until valid.

Detail screen        → one work order: header (WO# + status pill + actions),
  meta grid (product, line, qty, due, owner, created), and a "Routing &
  Operations" related sub-table + recent activity.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, status states, record columns, form fields + rules, detail fields
   — from the KB + prompt. Standalone: use the Example instantiation above.
3. Build each screen in the Visual language + Layout archetype above, imitating
   the example set in `assets/` (dashboard, list, form, detail) and the
   `assets/template.html` seed — with fresh content for the real domain, NOT the
   example labels.
4. Express domain rules as INLINE field validation (required marks, helper text,
   inline errors, disabled-until-valid submit). Never render
   rules/checklist/validation-status/build-note panels or designer/demo controls.
5. One inline `<style>`, semantic HTML5, `tabular-nums` on figures, no external
   assets, no CDNs — self-contained.

## Output contract

```
<artifact identifier="admin-forge-mes" type="text/html" title="Forge Admin">
<!doctype html>...</artifact>
```
