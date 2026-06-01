---
name: admin-meadow-agri
description: |
  Original agriculture farm-management admin dashboard archetype: light
  mode, natural palette with accent green (#16a34a / #22c55e) and
  earth-amber (#a16207), white and #f7faf5 surfaces, #e6ece1 borders.
  Left sidebar with farm/region switcher and nav, topbar with search,
  season badge and avatar, 4 KPI cards, fields status board, inline-SVG
  yield forecast chart, sensors table, and weather plus tasks side
  panel. Use when the brief involves agriculture, farming, crop
  management, precision-agriculture IoT, or agri-ops dashboards.
triggers:
  - "farm dashboard"
  - "agriculture admin"
  - "crop management"
  - "agri ops"
  - "field management"
  - "precision agriculture"
  - "farm management system"
  - "soil sensor dashboard"
  - "painel agrícola"
  - "农业管理后台"
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
  example_prompt: "Build me a farm management admin dashboard — left sidebar with farm/region switcher, 4 KPI cards (active fields, yield forecast, avg soil moisture, tasks due), a fields status board, a yield forecast chart, a sensors table, and a weather plus tasks side panel."
---

# Meadow Agri Admin Skill

Produce a farm-operations admin dashboard with a natural, grounded
visual identity — calm greens, earthy ambers, and generous whitespace
that mirrors the openness of agricultural landscapes.

## Workflow

1. Read the active DESIGN.md (if present); otherwise use the default
   palette: accent `#16a34a` (active) / `#22c55e` (hover), earth-amber
   `#a16207`, surface `#f7faf5`, border `#e6ece1`, text `#1e293b`.
2. Extract from the brief: farm name, region set, crop types, the 4
   KPIs, table records (fields or plots), sensor types, and tasks.
3. Layout — single HTML file, all CSS inline, no external resources:

### Left Sidebar (240px)
- Brand area: leaf/sprout SVG mark + "Meadow Agri" wordmark.
- Farm/region switcher: dropdown showing current farm name + chevron.
- Nav groups: OVERVIEW (Dashboard, Map View), CROPS (Fields, Harvest
  Plan), SENSORS (Live Readings, Alerts), OPERATIONS (Tasks, Reports),
  SETTINGS (Team, Integrations). Active item: green left-bar + tinted
  `rgba(22,163,74,0.08)` background.

### Top Bar (56px)
- Left: page title "Operations Dashboard".
- Center: search input with magnifier SVG icon.
- Right: season badge (e.g. "Growing Season 2026"), notification bell,
  avatar circle with operator initials.

### 4 KPI Cards (full-width grid, 4 cols)
Each card: icon SVG top-right, uppercase micro-label, large number,
delta chip or sub-label. Cards:
  1. **Active Fields** — count (e.g. 42), icon grid.
  2. **Yield Forecast** — tonnes (e.g. 1,840 t), icon chart-up.
  3. **Avg Soil Moisture** — percentage (e.g. 61%), icon droplet.
  4. **Tasks Due** — count (e.g. 7), icon clipboard.

### Fields Status Board (left, ~60% width)
Table: Field / Crop / Stage / Health / Area (ha). 7–8 rows with
invented field names (e.g. North Paddock, River Bend, Sunridge A).
Stage values: Germination, Vegetative, Flowering, Grain Fill, Harvest.
Health pills: Healthy (green), Moderate (amber), Attention (red).

### Yield Forecast Chart (below fields board)
Inline SVG area chart: x-axis weeks W1–W8, y-axis tonnes. Two series:
Forecast (green fill) and Target (amber dashed line). Grid lines,
axis labels, legend — all SVG, no canvas, no library.

### Sensors Table (below chart)
Columns: Sensor ID / Field / Metric / Reading / Status. 6 rows.
Metrics: Soil Temp, Soil Moisture, pH, N-Level, Humidity, Lux.
Status pills: Online (green), Warning (amber), Offline (slate).

### Weather + Tasks Panel (right, ~38% width)
- **Weather card**: 5-day forecast mini-strip — day, weather SVG icon,
  high/low temp. Current conditions hero: icon, temp, condition label.
- **Tasks card**: 5 to-do items with checkbox SVGs, priority dot
  (green/amber/red), task text, assignee initials chip. One "Add task"
  ghost CTA at bottom.

## Typography & Color rules
- Font: inline system stack — "Inter", system-ui, -apple-system,
  "Segoe UI", Roboto, sans-serif.
- Every chromatic color via a `:root` CSS custom property; SVG
  fill/stroke chromatic via `var(--token)` or `currentColor`.
- Neutral values (white, #f7faf5, #e6ece1, slate grays) may be
  hardcoded. No chromatic hex literals in rules or inline SVG.

## Output contract

```
<artifact identifier="admin-meadow-agri" type="text/html" title="Meadow Agri Admin">
<!doctype html>...</artifact>
```
