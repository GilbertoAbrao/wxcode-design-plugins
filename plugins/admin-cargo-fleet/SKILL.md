---
name: admin-cargo-fleet
description: |
  Industrial-clean logistics and fleet operations admin: light mode with
  orange-amber accent (#ea580c / #f59e0b), white/slate surfaces, status
  greens/reds. Left sidebar with hub/region switcher and grouped nav;
  topbar with search, region filter dropdown, and avatar; 4 KPI cards
  (in-transit count, on-time rate, active fleet, warehouse utilization);
  a Kanban-style shipment status board (Pending / Loading / In Transit /
  Delivered columns with draggable-looking cards); an original abstract
  route/region SVG visualization (nodes + arcs, no real map copy); and
  an active shipments data table with status pills. Use when the brief
  involves logistics, freight, cargo, fleet management, trucking,
  warehouse ops, or supply-chain dashboards.
triggers:
  - "cargo fleet"
  - "logistics dashboard"
  - "fleet management"
  - "shipment tracker"
  - "freight admin"
  - "trucking dashboard"
  - "warehouse operations"
  - "supply chain admin"
  - "painel logístico"
  - "物流管理后台"
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
  example_prompt: "Build me an industrial-clean cargo fleet admin dashboard — left sidebar with hub/region switcher, topbar with search and region filter, 4 KPI cards (in transit, on-time rate, active fleet, warehouse utilization), a shipment status board (Pending / Loading / In Transit / Delivered), a route/region visualization, and an active shipments table."
---

# Cargo Fleet Admin Skill

Produce an industrial-clean logistics and fleet operations admin layout
anchored to the orange-amber accent family with white/slate surfaces.

## Design tokens

| Token | Value | Usage |
|---|---|---|
| `--accent` | `#ea580c` | primary CTAs, active nav bar, focus rings |
| `--accent-light` | `#fff7ed` | active nav bg, card tints |
| `--amber` | `#f59e0b` | secondary highlights, ETA warnings |
| `--success` | `#16a34a` | on-time status, delivered pill |
| `--danger` | `#dc2626` | delayed status, critical alerts |
| `--warn` | `#d97706` | in-transit warning, loading pill |
| `--surface` | `#ffffff` | card bg |
| `--bg` | `#f8f9fb` | page canvas |
| `--border` | `#e6e9ee` | dividers, card outlines |
| `--text` | `#1e293b` | primary body text |
| `--muted` | `#64748b` | secondary labels, timestamps |
| `--sidebar-bg` | `#1a2235` | sidebar dark navy |
| `--sidebar-text` | `#94a3b8` | inactive sidebar labels |
| `--sidebar-active` | `#ffffff` | active sidebar label |

All chromatic colors must be CSS custom properties on `:root`; no hex
literals in CSS rules or inline SVG chromatic fills — use `var(--token)`
or `currentColor`.

## Workflow

1. Read the active DESIGN.md if present; otherwise apply the token table
   above directly.
2. Extract from the brief: company/hub name, region list (default:
   North, South, East, West, Central), primary fleet type (trucks,
   vans, containers — default trucks).
3. Layout (single HTML file, all CSS inline):

   **Left sidebar (240px, dark navy `#1a2235`)**
   - Brand mark at top: a small inline SVG truck/hexagon icon + company
     name in white.
   - Hub/region switcher: a dropdown-style selector showing current hub
     with a small caret; visually distinct section above the nav.
   - Nav groups: DISPATCH (Overview, Live Map, Status Board), FLEET
     (Vehicles, Drivers, Maintenance), WAREHOUSE (Inventory, Dock
     Schedule), SETTINGS (Integrations, Users, Alerts).
   - Active item: 3px left orange bar + `--accent-light` tinted bg
     (use semi-transparent overlay since sidebar is dark — render as
     `rgba(234,88,12,0.15)` bg + white text).
   - Footer: avatar + user name + role label in small text.

   **Top bar (60px, white, `--border` bottom)**
   - Left: page title "Status Board" + breadcrumb "Fleet Ops / Status Board".
   - Center: search input with magnifier SVG icon, placeholder
     "Search shipments, carriers, routes…".
   - Right: region filter pill-select (All Regions / North / South /
     East / West), notification bell with amber dot, avatar circle.

   **KPI cards row (4 cards)**
   - White cards, 10px radius, subtle shadow `0 1px 4px rgba(0,0,0,0.06)`.
   - Card 1 "In Transit": count ~847, delta +12% vs yesterday, inline
     SVG truck icon in orange.
   - Card 2 "On-Time Rate": 94.2%, delta +1.4pp, inline SVG
     checkmark-circle in green.
   - Card 3 "Active Fleet": 312 vehicles, delta −3 offline, inline SVG
     fleet icon in slate.
   - Card 4 "Warehouse Util.": 78%, progress bar across card bottom
     (orange fill), inline SVG warehouse icon in amber.
   - Each card: small uppercase muted label, big bold number, delta
     chip (green ▲ / red ▼), tiny inline sparkline SVG (5–7 points).

   **Two-column middle section (7/5 grid)**
   - LEFT (7 cols): **Shipment Status Board** — 4 Kanban columns
     (Pending / Loading / In Transit / Delivered). Column header has
     label + count badge. Each column holds 2–3 shipment cards showing:
     shipment ID, origin→dest abbreviation, carrier name, ETA or
     completion time, status color-dot. Cards have white bg, subtle
     border, hover lift. Pending = slate, Loading = amber, In Transit
     = orange, Delivered = green column accent dots.
   - RIGHT (5 cols): **Route Network Visualization** — an original
     abstract SVG (450×320 or similar) showing stylized nodes (city
     hub circles) connected by curved arc paths. Nodes are colored by
     status (active = orange, idle = slate, busy = amber). Animate
     a small circle traveling along one arc with a CSS animation.
     Label 6–8 node cities with short invented names (Veron, Kalsted,
     Omdra, Pelholt, Trisca, Nuvex, Brekka, Gorfen). Add legend:
     Active Route / Idle / Busy. No real map geography — purely
     abstract topological graph.

   **Active Shipments table (full width)**
   - Header: "Active Shipments" title + count badge + "Export CSV"
     ghost button + "New Shipment" orange primary button.
   - 8 rows, columns: Shipment ID, Origin → Destination, Carrier,
     Vehicle ID, ETA, Status pill.
   - Status pills: Pending (slate bg), Loading (amber bg), In Transit
     (orange bg), Delayed (red bg), Delivered (green bg) — white text.
   - Alternating row tint (`#f8f9fb` on odd rows), hover highlight.
   - Invented data: realistic shipment IDs (SHP-20481, etc.), city
     pairs, carrier names (Veron Freight, Kaldex Logistics, etc.).

4. Typography: system font stack only — `"Inter", system-ui,
   -apple-system, "Segoe UI", Roboto, sans-serif`. No external font
   loads. Uppercase tracking for KPI labels. Orange for active
   links and primary actions only.

5. One inline `<style>` block, semantic HTML5, zero external CDNs,
   zero external fonts, no lorem ipsum, all copy invented, target
   10–30 KB total.

## Output contract

```
<artifact identifier="admin-cargo-fleet" type="text/html" title="Cargo Fleet Admin">
<!doctype html>...</artifact>
```
