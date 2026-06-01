---
name: admin-jetstream-airline
description: |
  Airline operations control center archetype: dark-mode (#0a0f1a canvas),
  slim top navbar with hub-switcher + global search + avatar, narrow left
  icon rail (collapsed-by-default), 4 KPI tiles (on-time performance,
  flights today, load factor, delayed), live flights status board with
  status pills, departures-by-hour inline SVG bar chart, full flights table,
  crew/aircraft availability side panel. Accent palette: indigo (#6366f1)
  + sky (#38bdf8). All chromatic values via CSS custom properties.
  Use when the brief references airline, aviation, airport operations,
  flight control, dispatch dashboard, or transport operations center.
triggers:
  - "airline admin"
  - "airline dashboard"
  - "aviation control center"
  - "flight operations"
  - "airport dashboard"
  - "dispatch control"
  - "airline ops"
  - "painel de operações aéreas"
  - "航空运营中心"
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
  example_prompt: "Build me a dark-mode airline operations control center — navbar with hub switcher, icon rail sidebar, 4 KPI tiles (on-time %, flights today, load factor, delayed), a live flights status board, departures-by-hour chart, flights detail table, and a crew/aircraft side panel."
---

# Jetstream Airline Admin Skill

Produce the canonical dark-mode airline operations control center — a purpose-built admin surface for flight dispatchers, hub controllers, and airline ops managers.

## Workflow

1. **Read the active DESIGN.md** (if present); otherwise use the Jetstream palette:
   - Backgrounds: `#0a0f1a` (deepest) / `#111a2b` (surface) / `#18243a` (card)
   - Borders: `#24314a`
   - Text primary: `#e4ecf6`, muted: `#8a98ad`
   - Accent indigo: `#6366f1`, accent sky: `#38bdf8`
   - Status: on-time green `#22c55e`, delayed amber `#f59e0b`, boarding sky `#38bdf8`, departed muted `#8a98ad`

2. **Extract from the brief**: airline name + IATA-style hub codes, KPI labels (default: on-time %, flights today, load factor, delayed count), route pairs, gate labels, aircraft types, crew names.

3. **Layout**:
   - **Top navbar (48px, `#111a2b`, `border-bottom: 1px solid #24314a`)**: leftmost hub-switcher pill (hub code + chevron), centered global search input (icon + placeholder), rightmost cluster (alert bell with badge, avatar circle + initials).
   - **Left icon rail (48px wide)**: fixed column of square icon buttons, active state: indigo background tint + sky icon. Icons: Dashboard, Flights, Routes, Gates, Crew, Aircraft, Reports, Settings. No text labels — pure icon navigation.
   - **Main content area** (fills remaining space, padding 24px, background `#0a0f1a`):
     - **Page header row**: title "Operations Center", hub + date line, "Export" ghost button, "New Flight" indigo primary button.
     - **4 KPI tiles** (2×2 on narrow, 1×4 on wide; `#18243a`, `border: 1px solid #24314a`, `border-radius: 10px`): each tile has a small inline SVG icon in a tinted circle, uppercase label, large tabular-nums figure, and a delta chip (arrow + percentage or count).
       - Tile 1 — On-Time Performance: e.g. 87.4%, icon: checkmark circle, delta: +2.1%
       - Tile 2 — Flights Today: e.g. 142, icon: plane, delta: +8 vs yesterday
       - Tile 3 — Load Factor: e.g. 91.2%, icon: seat grid, delta: −0.6%
       - Tile 4 — Delayed: e.g. 11, icon: clock-warning, delta: +3 vs avg
     - **Flights Board** (`#18243a` card, full width, `border-radius: 10px`): header "Live Flights Board" + "Refresh" ghost button. Table with columns: Flight # / Route / Gate / Dep. Time / Status pill. Status pills: On Time (green), Boarding (sky), Delayed (amber), Departed (gray). Show 8–10 rows with invented flight numbers (e.g. JS401, JS218) and IATA-style routes (e.g. KVX→ORD).
     - **Two-column grid** (chart 60% / side panel 40%):
       - LEFT: **Departures by Hour** card — title, inline SVG bar chart (24-bar histogram for 00:00–23:00, accent bars for peak hours, muted for off-peak, sky accent for current hour), x-axis labels every 3h, y-axis flight count.
       - RIGHT: **Crew & Aircraft** side panel — two stacked sub-cards:
         - *Crew Availability* (3 rows): name, role badge (Captain/F.O./Purser), hub, status dot (Available/On Duty/Rest).
         - *Aircraft Status* (3 rows): tail number, type (e.g. A320, B737), next departure, status pill.
     - **Flights Detail Table** (`#18243a` card, full width): header "All Flights" + search input + filter chips (All / Domestic / International). Columns: Flight / Aircraft / Origin → Dest / Dep Time / Status / Pax. 8 rows. Tinted hover, status pill column.

4. **Typography**: system font stack inline — `"Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`. All numeric figures: `font-variant-numeric: tabular-nums`. KPI numbers: 28–32px bold. Table cells: 13px. Labels: 11px uppercase letter-spacing 0.06em muted.

5. **SVGs**: all inline, no external. Icon SVGs: 16–20px, `stroke="currentColor"`, `fill="none"`, `stroke-width="1.5"`. Chart SVGs: `viewBox` scaled to container, fill via `var(--color-accent-indigo)` / `var(--color-accent-sky)`. No chromatic hex literals in inline SVG — use `var(--token)` or `currentColor`.

6. **CSS custom properties** (required at `:root`):
   ```css
   --color-accent-indigo: #6366f1;
   --color-accent-sky: #38bdf8;
   --color-status-on-time: #22c55e;
   --color-status-delayed: #f59e0b;
   --color-status-boarding: #38bdf8;
   --color-status-departed: #8a98ad;
   --color-text-primary: #e4ecf6;
   --color-text-muted: #8a98ad;
   ```
   Neutrals (backgrounds, borders, grays) hardcoded.

7. **Single `<style>` block**, semantic HTML5, all CSS inline, no external CDNs, no external fonts, no lorem ipsum. Target 10–30 KB total.

## Output contract

```
<artifact identifier="admin-jetstream-airline" type="text/html" title="Jetstream Airline Admin">
<!doctype html>...</artifact>
```
