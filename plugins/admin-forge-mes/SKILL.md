---
name: admin-forge-mes
description: |
  Industrial dark-mode Manufacturing Execution System (MES) admin dashboard archetype.
  Shop-floor focus: plant switcher + shift indicator in slim top navbar, icon-only left
  rail, four KPI tiles (OEE %, units output today, downtime minutes, scrap rate %),
  production lines status board with state pills (Running / Idle / Down), an inline SVG
  output trend chart, a work-orders table with WO numbers / product codes / due dates /
  status, and a downtime/alerts side panel. Dark backgrounds (#0c0f14 / #141922 /
  #1d2530), orange accent (#f97316), steel secondary (#64748b). Use when the brief
  mentions MES, shop-floor, OEE, production lines, or manufacturing operations.
triggers:
  - "mes dashboard"
  - "manufacturing execution"
  - "shop floor dashboard"
  - "oee dashboard"
  - "production lines"
  - "manufacturing admin"
  - "factory dashboard"
  - "industrial dashboard"
  - "dark industrial"
  - "downtime monitoring"
  - "painel de manufatura"
  - "制造执行系统"
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
  example_prompt: "Build me an industrial dark-mode MES admin dashboard for a discrete manufacturing plant — plant switcher navbar, OEE / output / downtime / scrap KPI tiles, production lines status board, output trend chart, work-orders table, downtime alerts panel."
---

# Forge MES Admin Skill

Produce the canonical dark industrial Manufacturing Execution System admin layout for discrete manufacturing plants.

## Workflow

1. Read the active DESIGN.md (if present); otherwise use orange (#f97316) accent on near-black canvas (#0c0f14).
2. Extract from the brief: plant name, active shift, production lines (3–6), product codes, KPI targets for OEE / output / downtime / scrap, work-order list.
3. Layout:

   - **Top navbar (52px, #141922 bg, 1px #2a3340 bottom border)**:
     - LEFT: forge-hammer SVG wordmark + plant switcher dropdown (chevron icon).
     - CENTER: search input (dark pill, magnifier icon, placeholder "Search WO, product, line…").
     - RIGHT: shift badge (e.g. "Shift B · 06:00–14:00"), notification bell with orange dot, avatar circle with operator initials.

   - **Left icon rail (56px wide, #0c0f14 bg, 1px #2a3340 right border)**:
     Five icon-only nav items (dashboard/grid, production/layers, work-orders/clipboard, reports/bar-chart, settings/gear). Active icon filled orange. Hover tooltip label on the right.

   - **Main content area (#0c0f14 bg, 16px padding)**:

     - **KPI tile row (4 tiles, gap-4)**:
       Each tile: #141922 bg, 1px #2a3340 border, 8px radius, 16px padding.
       - OEE %: gauge-circle SVG, big number in orange, delta chip (green ▲ / red ▼), label "Overall Equipment Effectiveness".
       - Units Today: factory-output SVG, count in white, vs-target micro text.
       - Downtime Min: clock-alert SVG, count in amber when >0, "this shift" sub-label.
       - Scrap Rate %: warning-triangle SVG, number red when above threshold, "ppm" context label.

     - **2-column main grid (7/5 ratio, gap-4)**:

       - LEFT (7 cols): **Production Lines Status Board** — card #141922, title "Production Lines", 5 line rows each:
         `[Line name] [state pill: Running=#22c55e bg-tint | Idle=#f59e0b bg-tint | Down=#ef4444 bg-tint] [units/hr] [thin progress bar orange] [operator count icon]`.
         Below the board: **Output Trend Chart** — inline SVG polyline (hourly output last 8 hours), axis labels, orange stroke, #1d2530 bg, grid lines at 25%/50%/75%.

       - RIGHT (5 cols): **Downtime & Alerts Panel** — card #141922, title "Alerts · This Shift", list of 6 alert rows:
         `[severity dot: red/amber/blue] [line tag] [description] [elapsed time]`. Below: a "Recent Downtime" mini-table (line, reason code, start, duration). Orange "Acknowledge All" ghost button at bottom.

     - **Work Orders Table** (full width below grid, card #141922):
       Header: "Work Orders — Active" + "Export CSV" ghost button + "+ New WO" orange CTA.
       8 rows, columns: WO# / Product Code / Description / Qty (pcs) / Due Date / Status pill (In Progress=orange-tint / Queued=steel / Completed=green / On Hold=red-tint).
       Subtle row hover (#1d2530), sticky header, pagination hint "Showing 8 of 34".

4. Color tokens: all chromatic colors as :root CSS custom properties (--accent, --accent-light, --state-running, --state-idle, --state-down, --state-queued, --state-completed, --delta-up, --delta-down). SVG fills/strokes use var(--token) or currentColor. Neutral dark bgs/borders/grays hardcoded.
5. Typography: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif. font-variant-numeric: tabular-nums on all numeric cells. Uppercase letter-spaced micro-labels for tile captions.
6. One inline `<style>`, semantic HTML5, zero external assets, zero CDNs, self-contained.

## Output contract

```
<artifact identifier="admin-forge-mes" type="text/html" title="Forge MES Admin">
<!doctype html>...</artifact>
```
