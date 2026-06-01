---
name: admin-volt-energy
description: |
  Dark-mode energy utility grid operations control-room dashboard.
  Deep navy canvas (#0a0e14), amber (#fbbf24) + cyan (#22d3ee) accents,
  slim top navbar with region switcher, left icon rail, 4 KPI tiles
  (current load MW / generation MW / active outages / grid efficiency),
  a regions/sites status board with state pills (Online/Degraded/Offline),
  a dual-series inline SVG load/generation chart, an alerts table, and
  a sites side panel. Use when the brief mentions energy, utilities,
  grid operations, power management, SCADA-style dashboards, or any
  infrastructure operations control room.
triggers:
  - "energy dashboard"
  - "grid operations"
  - "utility dashboard"
  - "power grid admin"
  - "control room dashboard"
  - "SCADA dashboard"
  - "electricity operations"
  - "infrastructure operations"
  - "painel de energia"
  - "dashboard de energia"
  - "能源管理后台"
od:
  mode: prototype
  surface: web
  scenario: operations
  preview:
    type: html
    entry: index.html
  design_system:
    requires: true
    sections: [color, typography, layout, components]
  craft:
    requires: [pixel-discipline, laws-of-ux]
  example_prompt: "Build me a dark-mode energy grid operations dashboard — control-room style, KPI tiles for load/generation/outages/efficiency, regional sites status board, dual-series load chart, alerts table."
---

# Volt Energy Admin Skill

Produce a dark-mode utility grid operations dashboard that reads like a
control room — purposeful, data-dense, zero visual noise.

## Design tokens (all chromatic values as CSS custom properties)

```css
:root {
  --bg-root:    #0a0e14;
  --bg-panel:   #121822;
  --bg-card:    #1a2230;
  --border:     #28323f;
  --accent-amber: #fbbf24;
  --accent-cyan:  #22d3ee;
  --text-hi:    #e4ecf4;
  --text-muted: #8794a4;
  --state-online:   #34d399;
  --state-degraded: #fbbf24;
  --state-offline:  #f87171;
}
```

Every chromatic fill/stroke in SVGs and status pills must reference these
vars or `currentColor`. Neutrals (backgrounds, borders) may be hardcoded.

## Workflow

1. Read the active DESIGN.md if present; otherwise use the token set above.
2. Extract from the brief: operator name, grid regions, site names,
   live figures for load/generation/outages/efficiency.
3. Layout (single-file HTML, all CSS inline, no external CDNs or fonts):

### Top navbar (48px, bg-panel)
- Left: lightning-bolt SVG logo + "VOLT ENERGY" wordmark.
- Center: region switcher pill group (North Grid / South Grid / West Corridor).
- Right: search icon input (collapsed), bell icon with alert count badge
  in amber, avatar initials circle.

### Left icon rail (52px wide, bg-root, fixed)
Icons only — no labels. Active icon gets an amber left-bar accent.
Icons (inline SVG): Dashboard, Regions, Alerts, Schedule, Reports, Settings.

### Main content area (calc(100% - 52px) offset)

**4 KPI tiles** (grid 4-up, bg-card, border, 8px radius):
- Current Load: bold MW figure, tiny cyan inline sparkline, delta from
  yesterday.
- Generation: bold MW figure, tiny amber inline sparkline, delta.
- Active Outages: count in amber if > 0 else green, severity note.
- Grid Efficiency: percentage, progress arc SVG, colour-coded.

**Regions / Sites status board** (bg-card, full width below KPIs):
Table columns: Site | Source | Output (MW) | State pill.
State pills: Online (green), Degraded (amber), Offline (red).
Invent 8–10 realistic sites across 3 regions with varied states.

**Lower two-column grid (7/5)**:
- LEFT (7 cols): Load vs Generation chart card — title + live timestamp,
  two legends (Load in cyan, Generation in amber), dual-line inline SVG
  with 24 time-slots, horizontal gridlines, X-axis hour labels.
- RIGHT (5 cols): Active Alerts table — cols: ID / Site / Severity / Message / Status.
  Severity chips: Critical (red bg), High (amber bg), Info (muted).
  Status chips: Open (red outline), Acknowledged (amber outline), Resolved (green outline).
  5–7 invented alert rows.

**Sites side panel** (right-hand drawer style, 280px, bg-panel):
Site detail card for the "focused" site: name, region, installed capacity,
current output, uptime %, last inspection date, operator name, and a
tiny status timeline bar.

4. Typography: system font stack only —
   `"Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`.
   All numeric figures use `font-variant-numeric: tabular-nums`.
   Section labels in uppercase with letter-spacing: 0.08em.
5. One inline `<style>`, semantic HTML5, no external assets.

## Output contract

```
<artifact identifier="admin-volt-energy" type="text/html" title="Volt Energy Admin">
<!doctype html>...</artifact>
```
