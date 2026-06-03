---
name: admin-volt-energy
description: |
  Deep-navy control-room admin aesthetic: near-black canvas (#0a0e14), raised
  panels (#121822 / #1a2230), amber (#fbbf24) + cyan (#22d3ee) dual-accent on a
  steel-blue neutral ramp, Inter type with tabular-nums on every figure, dense
  13px rows, 8px radii, hairline #28323f borders, and crisp status pills.
  Archetype = entity-switcher navbar (region pills) + icon rail + 4 KPI tiles +
  full-width status board (rows of label / source tag / metric / state pill) +
  2-column lower grid: a dual-series SVG trend chart (cyan + amber lines) with an
  alerts table + a focused entity side panel with detail rows and a progress bar.
  Built for real-time operational consoles that must read at a glance.
triggers:
  - "deep navy control-room admin"
  - "dual-accent dark admin"
  - "amber cyan dark dashboard"
  - "navy operations console"
  - "real-time status board"
  - "control-room style admin"
  - "dual-series trend chart admin"
  - "painel escuro naval operacional"
example_prompt: "Apply this deep-navy control-room admin aesthetic to my domain"
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

# Volt Admin — Visual Archetype

This plugin contributes a **look** (deep navy, dual amber + cyan accent, dense
tabular data) and a **structure** (region-switcher navbar + icon rail + KPI tiles
+ status board + dual-series trend chart + alerts panel + entity side panel, plus
list / form / detail screens). It does **not** contribute a domain — the subject
matter comes from the Knowledge Base and the user's prompt. Treat the example
below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property; hardcode the neutral dark ramp.

- **Canvas / surfaces:** page `#0a0e14`; raised panel `#121822`; inset / card
  `#1a2230`; hairline border `#28323f`; hover row tint `rgba(255,255,255,.025)`.
- **Text ramp:** primary `#e4ecf4`, muted `#8794a4`.
- **Dual accent:** `--accent-amber: #fbbf24` (primary CTAs, active-state markers,
  alert severity, delta figures); `--accent-cyan: #22d3ee` (trend series, output
  figures, input focus, secondary highlights).
- **Status ramp (tokens):** `--state-online #34d399`, `--state-degraded #fbbf24`,
  `--state-offline #f87171`, each with a ~12–14% alpha tint for pill backgrounds
  (`rgba(52,211,153,.12)` / `rgba(251,191,36,.14)` / `rgba(248,113,113,.13)`).
  Severity: `--sev-critical` (offline tint), `--sev-high` (amber tint), `--sev-info`
  (muted tint). Alert status: open (offline outline), acknowledged (amber outline),
  resolved (online outline).
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`.
  Base 13px. `font-variant-numeric: tabular-nums` on **every** numeric cell.
  Micro-labels: 10px, `text-transform: uppercase`, `letter-spacing: .08em`, muted.
  Big KPI figures: 28px / weight 700 / `letter-spacing: -.5px`. IDs in monospace.
- **Density & radius:** compact 10px vertical row padding, 16px panel padding,
  12–16px grid gaps; panel radius 8px, control radius 6px, pill radius 4px,
  sparkline and progress elements minimal (≤4px height).
- **Borders & shadows:** 1px hairlines do the separation work; no drop shadows
  on panels (flat control-room terminal feel). 1px inner row dividers `#28323f`.
- **Motion:** `.15s` background/border hover transitions; 2s ease-in-out pulse
  on the live-status dot. Gentle only — never bouncy.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Top navbar** (48px, panel bg, 1px bottom border, fixed): logo glyph → brand
  wordmark → **region/entity switcher** (pill group, active pill raised on card bg)
  → right: search input pill → notification bell with amber badge dot → avatar
  initials circle.
- **Left icon rail** (52px, page bg, 1px right border, fixed): 3–5 icon-only nav
  items (active item amber `currentColor`; amber left-bar 3px before pseudo); a
  separator; footer items; optional spacer for bottom-pinned settings.
- **Main content** (page bg, ~20px padding, vertical flow): a **page header**
  (title + sub-line left, live-status dot + ghost + primary buttons right), then
  the region stack below.
- **KPI tile row** (4 tiles, equal grid): each tile = card panel with an icon/label
  row, a big tabular figure, and a bottom row of delta chip + sparkline or arc SVG.
  Figures recolor by state (cyan / amber / offline-red / online-green).
- **Full-width status board:** a titled panel whose rows are
  `[region badge + entity name] [source/type tag] [metric value + unit] [state pill]`.
  Column headers uppercase micro-labels; rows hover-tinted; state pills
  online/degraded/offline.
- **2-column lower grid (auto / 320px):**
  - **Left — dual-series trend chart:** a titled card with timestamp + legend
    (two items, one cyan dot + one amber dot), a full-width inline SVG chart:
    horizontal gridlines, area fills under each line, x-axis time labels, y-axis
    labels. Two `<polyline>` series — cyan + amber.
  - **Right (stacked):** (a) **alerts table** — titled card with a count badge,
    columns `[ID] [entity name + message] [severity pill] [status pill]`; (b)
    **entity side panel** — titled card with entity name + sub-line, a divider,
    label/value detail rows (`[key] [value]`), a progress bar fill + label.
- **Records list screen:** a search pill toolbar + filter chips + count, then the
  status-board table pattern paginated.
- **Record form screen:** sectioned cards of labelled fields; **rules appear as
  inline validation** — required marks (`*`), helper text under the field, and
  inline error messages on invalid fields, with primary submit disabled-until-valid.
  No rules/checklist/validation-status panel.
- **Record detail screen:** a breadcrumb → header band (entity name + status pill
  + key actions) → meta grid of label/value pairs → one or more related-data
  sub-panels (status-board row pattern or a mini-table + a timeline list).

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
Domain (illustrative): a regional electric-grid operations center.

Region switcher     → zones: "North Grid", "South Grid", "West Corridor".
Live status badge   → "Live · 14:32 UTC".
Rail items          → Dashboard, Regions, Alerts, Schedule, Reports, (Settings).

KPI tiles (4):
  • Current Load   4,821 MW (cyan figure, ▲3.2% vs yesterday, sparkline).
  • Generation     5,103 MW (amber figure, ▲1.7% capacity, sparkline).
  • Active Issues  7       (offline-red figure, "2 critical, 5 minor, since 09:14 UTC").
  • Efficiency     94.3%   (green figure, ▲0.4% this week, arc progress SVG).

Status board (full-width) → "Site Monitoring — All Regions" — rows of
  [region badge + site name] [source tag (Gas Turbine / Wind / Solar / Hydro / BESS)]
  [output MW] [state pill: Online / Degraded / Offline].
  9 representative sites across 3 regions.

Lower left: dual-series trend chart → "Load vs. Generation — Last 24 Hours"
  (cyan = load, amber = generation; 24 time slots; area fills; x-axis hour labels).

Lower right (stacked):
  Alerts table → "Active Alerts" with count badge — rows:
    [ID] [site name + short message] [severity: Critical/High/Info] [status: Open/ACK/Resolved].
  Side panel  → "Site Detail" for a focused site: name + region/type sub-line,
    divider, rows of (Installed Capacity / Current Output / Utilisation / Uptime /
    Last Inspection / Site Operator), progress bar (30-day uptime).

List screen   → all sites with search + filter chips (status, region), paginated table.

Form screen   → "New Site": name (required), region (required select), source type
  (required select), installed capacity MW (required, > 0), operator name (required),
  commissioning date (required, not in the future), notes. Rules as required marks +
  helper text + inline errors; "Add Site" disabled until valid.

Detail screen → one site: header (name + status pill + actions), meta grid
  (region, source type, capacity, current output, utilisation, uptime, operator,
  last inspection), and a "Recent Events" related list + activity timeline.
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
<artifact identifier="admin-volt-energy" type="text/html" title="Volt Admin">
<!doctype html>...</artifact>
```
