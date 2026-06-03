---
name: admin-jetstream-airline
description: |
  Dark aerospace-grade admin aesthetic: near-black navy canvas (#0a0f1a),
  indigo (#6366f1) + sky-blue (#38bdf8) dual-accent on a cool-blue neutral
  ramp, slim 48px navbar with entity-switcher pill, 48px icon-only rail, 4 KPI
  tiles, a live-status board table with state pills, an inline SVG bar chart,
  a full-width records table with filter chips, and a resource side panel.
  Built for high-density operational consoles with a cool, precision-control feel.
triggers:
  - "dark navy admin"
  - "indigo sky admin"
  - "dual-accent control center"
  - "cool-dark operational dashboard"
  - "near-black navy dashboard"
  - "status-board control console"
  - "precision dark operations UI"
  - "painel escuro naval"
example_prompt: "Apply this dark navy precision-control aesthetic to my domain"
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

# Jetstream Admin — Visual Archetype

This plugin contributes a **look** (dark navy canvas, indigo + sky dual-accent,
cool-blue neutrals, precision-dense tabular data) and a **structure** (slim
navbar + icon rail + KPI tiles + live status board + bar chart + records table
+ resource side panel, plus list / form / detail screens). It does **not**
contribute a domain — the subject matter comes from the Knowledge Base and the
user's prompt. Treat the example below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property; hardcode the neutral navy ramp.

- **Canvas / surfaces:** page `#0a0f1a`; surface `#111a2b`; raised card `#18243a`;
  hairline border `#24314a`; hover-row tint `rgba(99,102,241,.04)`.
- **Text ramp:** primary `#e4ecf6`, muted `#8a98ad`.
- **Dual accent:**
  - `--accent-indigo: #6366f1` (indigo), `--accent-indigo-dim: rgba(99,102,241,.15)`.
    Primary CTAs, active nav chip, icon tints, bar chart fill.
  - `--accent-sky: #38bdf8` (sky blue), `--accent-sky-dim: rgba(56,189,248,.15)`.
    Current/highlight bars, boarding/active state, search focus ring.
- **Status tokens:** `--state-active #22c55e` (green), `--state-active-dim rgba(34,197,94,.1)`;
  `--state-warn #f59e0b` (amber), `--state-warn-dim rgba(245,158,11,.1)`;
  `--state-sky #38bdf8` (sky), `--state-sky-dim rgba(56,189,248,.1)`;
  `--state-muted #8a98ad`, `--state-muted-dim rgba(138,152,173,.08)`.
  Each state pill pairs a dim background + 1px border at ~20–25% alpha.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
  sans-serif`. Base 14px. `font-variant-numeric: tabular-nums` on **every**
  numeric cell. Micro-labels 10–11px, `text-transform: uppercase`,
  `letter-spacing` ~.06em, muted. KPI figures 28px / weight 700 / `letter-spacing: -.02em`.
  IDs and codes use tabular-nums on the same font stack (no mono shift needed).
- **Density & radius:** 48px navbar/rail; 11px vertical row padding; 16–18px
  panel padding; 14px grid gaps; card radius 10px; control radius 6–7px;
  pill radius 6px; progress bars 4px tall / 2px radius.
- **Borders & shadows:** 1px hairlines (`#24314a`) carry all separation; no
  drop shadows (flat precision feel). Inner row dividers `rgba(36,49,74,.5)`.
- **Motion:** `.15s` background/border hover transitions; 2s pulse on the
  live-status dot. Never bouncy.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Top navbar** (48px, surface bg, 1px bottom border, sticky): **entity-switcher pill**
  (live-status dot + short code + chevron) → **global search input** (icon + placeholder,
  grows with flex) → icon-only alert button with badge dot → avatar circle.
- **Left icon rail** (48px, surface bg, 1px right border): icon-only nav items
  (active: indigo-dim chip + sky icon; hover: card bg); divider line between main
  and utility items; settings pinned to flex-end. Each item has a `title` tooltip.
- **Main content** (page bg, ~20–24px padding, vertical flow): a **page header**
  (title + sub-line / context on left; ghost + primary buttons on right), then
  the region stack.
- **KPI tile row** (4 tiles, equal `repeat(4,1fr)` grid, collapses to 2×2 on
  narrow): each tile = card panel with icon-chip in tinted circle (recolored by
  meaning) + uppercase micro-label on top row; big tabular figure in the middle;
  delta chip (arrow + value) + context sub-line at the foot.
- **Live status board** (full-width card): titled panel with a live-pulse badge +
  ghost action button; a table of rows carrying
  `[identifier] [origin → dest] [location pill] [scheduled time] [state pill]`.
  State pills: active-green / sky-boarding / amber-warn / muted-departed.
- **Two-column grid (60% / 40%):**
  - **Left — bar chart card:** title + legend chips; an inline SVG histogram
    (N bars across a time axis, peak bars in indigo, off-peak in border color,
    current bar in sky; dotted gridlines + x/y axis labels).
  - **Right — resource side panel:** two stacked sub-cards separated by a
    hairline, each sub-card showing 3 rows of
    `[avatar / icon-chip] [name + sub-label] [status dot + label]`.
- **Full-width records table** (card): titled panel with search input + filter
  chips (All / facet A / facet B); a sticky uppercase column header; dense rows
  with status pills, right-aligned numerics, a two-part `current/capacity` cell;
  footer pager.
- **Records list screen:** the records-table archetype as its own page —
  search + filter chips + result count, the same dense table, pager.
- **Record form screen:** sectioned cards of labelled fields; **rules appear as
  inline validation** — required marks (`*`), helper text under the field,
  inline error messages on invalid fields, submit disabled-until-valid. No
  rules/checklist/validation-status panel.
- **Record detail screen:** breadcrumb + header band (identifier + state pill +
  key actions); 3-column meta grid of label/value pairs; related-data sub-panels
  (status-board row pattern or mini-table) below.

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
Domain (illustrative): a transport hub operations control center.

Entity switcher  → hub code: "KVX HUB" with live-status green dot.
Search           → placeholder "Search records, locations, resources…".
Rail items       → Dashboard, Records, Routes, Locations, Resources, Reports, Settings.

KPI tiles (4):
  • On-Time Rate 87.4% (green icon-chip, ▲+2.1%, "vs last week").
  • Total Today 142 (sky icon-chip, ▲+8, "vs yesterday").
  • Utilization 91.2% (indigo icon-chip, ▼−0.6%, "vs last week").
  • Delayed / Exception Count 11 (amber icon-chip, ▼+3, "vs rolling avg").

Live status board → "Live Status Board" with LIVE pulse badge — rows of
  [identifier] [origin → destination] [location pill] [scheduled time] [state pill].
  States: On Time (green) / Active (sky) / Delayed (amber) / Departed (muted).

Bar chart (left) → "Volume by Hour" — 24-bar histogram (00–23h); peak bars
  in indigo, current hour bar in sky, off-peak in border color; x-axis every 3h.

Resource side panel (right) → two sub-cards:
  Sub-card 1 (Personnel) — 3 rows: name, role + base, availability status.
  Sub-card 2 (Equipment) — 3 rows: ID/tail, type, next assignment + status.

Records table    → "All Records": identifier / equipment / origin→dest /
  scheduled time / status pill / capacity (current/total).
  Filter chips: All / Type A / Type B.

List screen      → all records, search + filter chips (status, type), paginated.

Form screen      → "New Record": primary identifier (required), description,
  quantity (required, > 0), location (required select), scheduled date
  (required, not in the past), priority. Rules as required marks + helper
  text + inline errors; submit disabled until valid.

Detail screen    → one record: breadcrumb + header (identifier + state pill +
  actions), meta grid (type, origin, destination, qty, scheduled, owner,
  created), and a "Route & Stops" sub-table + recent activity feed.
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
<artifact identifier="admin-jetstream-airline" type="text/html" title="Jetstream Admin">
<!doctype html>...</artifact>
```
