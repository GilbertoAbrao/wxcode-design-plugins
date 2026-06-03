---
name: admin-cargo-fleet
description: |
  Industrial-clean light-mode admin aesthetic: white/slate canvas (#f8f9fb / #ffffff),
  dark-navy sidebar (#1a2235), orange-amber accent family (#ea580c / #f59e0b), crisp
  status pills on slate borders, system sans-serif at 13–14px, compact cards with
  1px borders and shallow shadows. Archetype = branded sidebar (entity switcher +
  grouped nav) + topbar (search pill + context filter + avatar) + 4 KPI cards +
  2-column middle (Kanban-column status board + abstract network visualization) +
  full-width records table with status pills, plus list / form / detail screens.
triggers:
  - "industrial-clean light admin"
  - "orange-amber accent dashboard"
  - "white-slate admin panel"
  - "dark-navy sidebar admin"
  - "kanban-board status admin"
  - "network-visualization dashboard"
  - "painel clean laranja"
example_prompt: "Apply this industrial-clean light admin aesthetic to my domain"
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

# Cargo Fleet Admin — Visual Archetype

This plugin contributes a **look** (industrial-clean light mode, orange-amber
accent, dark-navy sidebar) and a **structure** (sidebar with entity switcher +
grouped nav, topbar with search, 4 KPI cards, Kanban status board, network
visualization, records table, plus list / form / detail screens). It does **not**
contribute a domain — the subject matter comes from the Knowledge Base and the
user's prompt. Treat the example below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property.

- **Canvas / surfaces:** page `#f8f9fb`; card/surface `#ffffff`; border
  `#e6e9ee`; sidebar `#1a2235`; sidebar text (inactive) `#94a3b8`; sidebar
  text (active) `#ffffff`.
- **Text ramp:** primary `#1e293b`, muted `#64748b`.
- **Accent family:** `--accent: #ea580c` (deep orange), `--accent-hover: #c2410c`,
  `--accent-light: #fff7ed`; `--amber: #f59e0b`, `--amber-light: #fffbeb`.
  CTAs, active nav bar, key figures, sparkline strokes, progress fills.
- **Status ramp (as tokens):** `--success: #16a34a` / `--success-light: #f0fdf4`;
  `--danger: #dc2626` / `--danger-light: #fef2f2`; `--warn: #d97706`. State pill
  backgrounds use the corresponding `*-light` tint; pill text uses the base color.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
  sans-serif`. Base 14px body. KPI values 26px / weight 800 / `letter-spacing:
  -.02em`. KPI labels, table headers, nav group labels: 10px / uppercase /
  `letter-spacing: .07–.10em`. Record IDs in monospace (`"SF Mono", "Consolas",
  monospace`). `font-variant-numeric: tabular-nums` on every numeric cell.
- **Density & radius:** topbar 60px, sidebar 240px. Card padding 18–20px.
  Panel radius 10px (`--radius-md`), control radius 6px (`--radius-sm`), pill
  radius 20px. Compact table rows: 10px vertical padding.
- **Borders & shadows:** 1px `var(--border)` for all card outlines and dividers.
  Shallow card shadow `0 1px 4px rgba(0,0,0,.06)`; hover lift
  `0 4px 12px rgba(0,0,0,.10)`. Active sidebar item: `rgba(234,88,12,.15)` bg +
  3px left border in `var(--accent)`.
- **Motion:** `.15s` background/border hover transitions, subtle hover lift
  `translateY(-1px)` on Kanban cards, node pulse animation 2s ease-in-out
  infinite. No bouncy easing.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Left sidebar** (240px, dark-navy, sticky full-height): brand mark (inline
  SVG glyph + wordmark + sub-label) → **entity switcher** (a selector block
  showing current entity + caret) → **grouped nav** (2–4 groups; each group
  has an uppercase micro-label + 2–4 items). Active item: 3px left orange bar
  + accent-dim bg overlay. Footer: avatar chip + user name + role label.
- **Top bar** (60px, white, 1px bottom border, sticky): page title + breadcrumb
  → **search pill** (magnifier icon + text input, rounded) → spacer →
  **context filter** (pill-select with caret) → notification bell with dot →
  avatar circle + name.
- **KPI card row** (4 equal cards, 1fr grid): each card = 1px bordered white
  surface with a top row of uppercase micro-label + icon chip, a big tabular
  figure, a delta chip (green▲ / red▼ / amber▲) + sparkline SVG, and
  optionally a thin progress bar across the card bottom.
- **2-column middle grid (7fr / 5fr):**
  - **Left — Kanban status board:** white panel with a header (title + action
    link) and 3–4 columns; each column has an uppercase colored label + count
    badge + 2–3 item cards. Each item card: ID (monospace) + route/description
    line + sub-detail + time label; colored left-border stripe for the column
    state.
  - **Right — network visualization:** white panel with a header + an abstract
    SVG graph (nodes as circles + curved arc paths, colored by state; animated
    traveler dot along one arc). Legend row: active / busy / idle dots.
- **Full-width records table:** white panel with header (title + count badge +
  ghost + primary buttons), sticky uppercase thead, dense rows with **status
  pills**, monospace ID column, route/description cell, carrier/detail columns,
  and alternating row tints. Footer with result count + pager links.
- **Records list screen:** the table archetype as its own page — search input +
  filter chips + record count, same dense table, pager.
- **Record form screen:** sectioned white cards with labeled fields; **rules
  appear as inline validation** — required marks (`*`), helper text below the
  field, inline error messages on invalid fields, primary submit
  disabled-until-valid. No rules/checklist/validation-status panel.
- **Record detail screen:** a header band (title + status pill + primary / ghost
  actions), a meta grid of label/value pairs, one or more related sub-panels
  (status-board row pattern or a mini-table) below.

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
Domain (illustrative): a logistics and fleet operations platform.

Entity switcher    → active hub: "North Central".
Sidebar groups     → DISPATCH (Overview, Live Map, Status Board),
                     FLEET (Vehicles, Drivers, Maintenance),
                     WAREHOUSE (Inventory, Dock Schedule),
                     SETTINGS (Integrations, Users, Alerts).
Context filter     → region selector: All Regions / North / South / East / West.

KPI cards (4):
  • In Transit: 847 (▲+12% vs yesterday), sparkline in orange.
  • On-Time Rate: 94.2% (▲+1.4pp this week), sparkline in green.
  • Active Fleet: 312 vehicles (▼−3 offline), sparkline in slate.
  • Warehouse Util.: 78% (▲+6% capacity), progress bar at 78%.

Status board (left, Kanban)  → "Shipment Status Board" — 4 columns:
  Pending (24), Loading (11), In Transit (847), Delivered (1,204).
  Each card: shipment ID / origin→dest / carrier / ETA or completion.
  Column colors: Pending=slate, Loading=amber, In Transit=orange,
  Delivered=green (left border stripe per column).

Network visualization (right) → "Route Network" — abstract SVG graph
  of 8 invented hub nodes (Veron, Kalsted, Omdra, Pelholt, Trisca,
  Nuvex, Brekka, Gorfen) connected by bezier arcs. Active=orange,
  Busy=amber, Idle=slate. Animated traveler dot on the primary arc.
  Legend: Active Route / Busy / Idle.

Records table        → "Active Shipments" (847): Shipment ID / Origin→Dest /
  Carrier / Vehicle ID / ETA / Status pill
  (Pending / Loading / In Transit / Delayed / Delivered).

List screen          → all records, search + filter chips (status, region),
  paginated, same dense table.

Form screen          → "New Record": ID field (auto), origin (required select),
  destination (required select), carrier (required), vehicle (required select),
  scheduled date (required, not in the past), priority. Required marks + helper
  text + inline errors; submit disabled until valid.

Detail screen        → one record: header (ID + status pill + Edit / Archive
  actions), meta grid (origin, dest, carrier, vehicle, ETA, created), and a
  "Route Log" related sub-table + timeline of events.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, status states, record columns, form fields + rules, detail
   fields — from the KB + prompt. Standalone: use the Example instantiation above.
3. Build each screen in the Visual language + Layout archetype above, imitating
   the example set in `assets/` (dashboard, list, form, detail) and the
   `assets/template.html` seed — with fresh content for the real domain, NOT
   the example labels.
4. Express domain rules as INLINE field validation (required marks, helper text,
   inline errors, disabled-until-valid submit). Never render
   rules/checklist/validation-status/build-note panels or designer/demo controls.
5. One inline `<style>`, semantic HTML5, `tabular-nums` on figures, no external
   assets, no CDNs — self-contained.

## Output contract

```
<artifact identifier="admin-cargo-fleet" type="text/html" title="Cargo Fleet Admin">
<!doctype html>...</artifact>
```
