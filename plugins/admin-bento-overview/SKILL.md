---
name: admin-bento-overview
description: |
  Bento-grid operations dashboard archetype: light mode, multi-accent
  palette (indigo, teal, amber, rose) on a neutral canvas. Distinctive
  layout is a CSS grid with asymmetric tile spans — NOT a sidebar+table.
  Tiles: hero metric (large), area chart (wide), 2–3 KPI pills, activity
  feed, donut chart, compact mini-table, system status. Use when the
  brief calls for an "ops overview", "command center", "home screen",
  or explicitly asks for a bento or mosaic grid layout.
triggers:
  - "bento grid dashboard"
  - "bento ops"
  - "operations overview"
  - "command center dashboard"
  - "mosaic dashboard"
  - "asymmetric dashboard"
  - "ops home screen"
  - "painel de operações"
  - "运营总览"
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
  example_prompt: "Build me a business operations overview dashboard using a bento-grid layout — asymmetric tile sizes, hero metric, SVG chart, KPI tiles, activity feed, donut, mini-table, and status tile."
---

# Bento Ops Overview Skill

Produce the bento-grid operations overview layout — a mosaic of
asymmetrically-sized tiles on a neutral canvas, each tile potentially
carrying its own accent color from the multi-accent palette.

## Palette tokens (always emit as :root custom properties)
```
--c-indigo: #6366f1
--c-indigo-lt: #eef2ff
--c-teal: #14b8a6
--c-teal-lt: #f0fdfa
--c-amber: #f59e0b
--c-amber-lt: #fffbeb
--c-rose: #f43f5e
--c-rose-lt: #fff1f2
```
All chromatic fills/strokes in inline SVG must use `var(--c-*)` or
`currentColor`. No hex literals for chromatic colors in CSS rules
or SVG attributes — only in the :root block.

## Workflow
1. Read the active DESIGN.md if present; otherwise use the palette above.
2. Extract from the brief: org/product name, reporting period, primary
   metric (GMV, ARR, throughput, processed events — whatever fits the
   domain), secondary KPIs (4–6: latency, error-rate, active users,
   conversion, uptime, etc.). Invent plausible figures if none given.
3. Layout rules:
   - **Header (44px)**: brand logo mark (inline SVG monogram) + product
     name on the left; period selector chips (Today / 7D / 30D / Custom)
     in the center; notification icon + avatar on the right. No sidebar.
   - **Bento grid**: CSS Grid, `grid-template-columns: repeat(12, 1fr)`,
     `gap: 16px`. Tile spans are the point; vary them deliberately:
       • **Hero tile** (col-span 5, row-span 2): dominant metric, large
         numeral, sparkline (inline SVG), trend chip, subtitle copy.
         Accent: indigo gradient strip on the left edge.
       • **Chart tile** (col-span 7, row-span 2): title + period tabs,
         inline SVG area chart with grid lines and axis labels.
         Accent: teal axis/fill.
       • **KPI tile × 2** (col-span 3, row-span 1 each): compact label +
         value + delta pill. One accented amber, one rose.
       • **Activity feed tile** (col-span 3, row-span 2): 5–6 timestamped
         events with dot indicator (colored per severity). Teal accent.
       • **Donut tile** (col-span 3, row-span 2): inline SVG donut with
         3–4 slices, legend below. Indigo/teal/amber slices.
       • **Mini-table tile** (col-span 6, row-span 2): 5 rows, 4 columns
         (entity name, region, value, status pill). Header row with
         light slate background. Amber accent on header left border.
       • **Status tile** (col-span 3, row-span 1): system health summary
         — 4 services with colored dot (green/amber/rose) + uptime %.
         Rose accent on border if any service is degraded.
4. Typography: system font stack only — "Inter", system-ui, -apple-system,
   "Segoe UI", Roboto, sans-serif. No external font loads. Tile labels
   uppercase, letter-spacing 0.05em, 11px. Values at 28–36px bold.
5. Neutral palette hardcoded: canvas #f6f7f9, tile background #ffffff,
   border #e8eaee, text-primary #1e293b, text-secondary #64748b.
6. Single inline `<style>`, semantic HTML, no external CDNs, no lorem ipsum.

## Output contract

```
<artifact identifier="admin-bento-overview" type="text/html" title="Bento Ops Overview">
<!doctype html>...</artifact>
```
