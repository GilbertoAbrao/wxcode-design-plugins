---
name: admin-savory-pos
description: |
  Warm light-mode service admin aesthetic: near-white canvas (#faf8f5), amber
  accent (#f59e0b) with tomato alert tones (#ef4444) on white cards,
  dark sidebar (#1c1917) with grouped nav sections, 240px left sidebar
  (entity switcher + grouped nav + staff footer) + 60px sticky topbar +
  4 KPI tiles with inline sparklines and delta chips + a 3-column live state
  board (New / Active / Completed) + a bottom 2-column grid (ranked item list
  with inline bar + area-fill SVG trend chart) + wide dense records table with
  status pills. Built for high-turnover operational back-offices that need to
  scan live status at a glance.
triggers:
  - "warm light-mode admin"
  - "amber accent service dashboard"
  - "dark sidebar light content admin"
  - "live state board dashboard"
  - "kanban-style service dashboard"
  - "grouped-nav sidebar admin"
  - "service back-office aesthetic"
  - "painel quente modo claro"
example_prompt: "Apply this warm light-mode service admin aesthetic to my domain"
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

# Savory Service Admin — Visual Archetype

This plugin contributes a **look** (warm light-mode, amber accent, dark sidebar,
clean white cards) and a **structure** (grouped-nav sidebar + topbar + KPI tiles
+ live state board + bottom grid + records table, plus list / form / detail
screens). It does **not** contribute a domain — the subject matter comes from the
Knowledge Base and the user's prompt. Treat the example below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property; neutral near-white and gray values may be hardcoded.

- **Canvas / surfaces:** page `#faf8f5` (warm off-white); card `#ffffff`; sidebar
  `#1c1917` (near-black warm); border `#ece6df`; card shadow `0 1px 4px
  rgba(0,0,0,.07), 0 2px 8px rgba(0,0,0,.04)`.
- **Text ramp:** primary `#1e293b`, secondary `#64748b`.
- **Accent:** `--amber: #f59e0b`; `--amber-light: #fef3c7`; `--amber-mid: #fcd34d`.
  Primary CTAs, active nav, key figures, inline bars, sparkline strokes.
- **Alert / cancel tone:** `--tomato: #ef4444`; `--tomato-light: #fee2e2`.
  Overdue/error states, cancel status pills, late progress bars.
- **Positive tone:** `--green: #22c55e`; `--green-light: #dcfce7`.
  Completed state, paid pills, positive delta chips, live-dot animation.
- **Sidebar text:** `--sidebar-text: #d6d3d1`; active item `color:#fff`,
  `background: rgba(245,158,11,.12)`, amber left bar `3px`. Inactive items
  70% opacity on their SVG glyph.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
  sans-serif`. Base 14px. `font-variant-numeric: tabular-nums` on every numeric
  cell. Uppercase 10px, `letter-spacing: .08–.12em` for section labels and column
  headers. Big KPI figures 26px / weight 800 / line-height 1. Currency units 14px
  / weight 600 at the baseline.
- **Density & radius:** card radius 10px; control radius 8px; pill radius 20px;
  sidebar nav item padding 9px 18px; card padding 18px; KPI tile 16px 18px; table
  row 10px 12px.
- **Borders:** 1px `#ece6df` on cards and table rows; 1px `rgba(255,255,255,.1)`
  on sidebar elements. No drop shadows on the sidebar; only card surfaces carry
  the warm shadow.
- **Motion:** `pulse` keyframe (opacity 1 → 0.4 → 1, 2s) on the live-state dot.
  Hover transitions `.12s` on background. Progress bars width transition `.4s ease`.
  Default easing gentle; never bouncy.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns described by shape and behavior — not meaning.

- **Left sidebar (240px, sidebar-bg, sticky full-height):** brand mark (amber
  square glyph) + name + sub-label → **entity switcher** pill (green dot + label
  + caret) → **grouped nav sections** (section label in uppercase 9px + nav items
  each with inline SVG + label + optional count badge). Active item: amber 3px
  left bar + amber-tinted background, glyph at full opacity. Footer: staff avatar
  (amber circle with initials) + name + role + "end period" link.
- **Top bar (60px, white, 1px bottom border, sticky):** page title left → flexible
  **search input** (icon-prefixed, surface background) → **period indicator chip**
  (amber-light background) → notification icon button with tomato dot → manager
  avatar.
- **Main content (page bg, 24px padding, vertical flow):** page header (title +
  sub-line on left, ghost + primary buttons on right), then the region stack.
- **KPI tile row (4 tiles, equal grid):** each tile = white card with warm shadow,
  uppercase micro-label, large tabular figure (+ currency unit at baseline if
  applicable), an inline SVG sparkline (64×32px, amber stroke, gradient fill),
  and a meta row with a delta chip (green ▲ / tomato ▼ pill) + sub-line. The
  table-occupancy variant swaps the sparkline for a small donut ring SVG.
- **Live state board (full-width, 3 columns equal):** each column = surface-bg
  panel with border + radius. Column header: state dot (amber / tomato / green) +
  uppercase label + count badge. Each row card = white card with shadow: record
  ID + location + elapsed time top-row → item summary text → optional elapsed
  progress bar (green/amber/tomato fill) → footer (total + primary action
  button or state text). Action buttons: amber "primary" or green-light "positive".
- **Bottom 2-column grid (55fr / 45fr):**
  - **Left — ranked items list:** white card, card header with title + link. Rows:
    `[rank badge] [name] [qty label] [value label] [thin inline amber bar]`. Bars
    scale to the max value; rank badges amber-light square.
  - **Right — trend chart card:** white card, card header. Y-axis labels column
    (right-aligned 10px muted) beside SVG chart area (polyline + area-fill +
    horizontal grid lines + data dots). X-axis labels row below. Bottom strip with
    two key-figure cells (label + value, value in amber).
- **Wide records table:** white card, card header with title + "View all" link;
  sticky uppercase header row; dense rows with **status pills** (paid green /
  pending amber / cancelled tomato); amber hyperlinks for IDs; last column
  right-aligned; hover row tint; no visible footer pagination on the dashboard
  variant.
- **Records list screen:** the records-table archetype as its own page — search
  input + filter chips row + count, the same dense table, and a pager.
- **Record form screen:** sectioned white cards of labelled fields; **rules appear
  as inline validation** — required marks (`*`), helper text under the field, and
  inline error messages on invalid fields, with the primary submit disabled-until-
  valid. No rules/checklist/validation-status panel.
- **Record detail screen:** breadcrumb, header band (ID + status pill + key
  actions), meta grid of label/value pairs in a white card, and one or more
  related-data sub-panels below.

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key metrics,
state labels, ranked-item list columns, record table columns, form fields and
their rules, and detail fields — and map them onto the archetype above. If no
KB/domain is supplied (standalone), use the Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules
become inline field validation. Do NOT render build/implementation notes or
designer controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent
> (entities, metrics, states, columns, fields) drawn from the KB + prompt.

```
Domain (illustrative): a multi-venue restaurant group back-office.

Entity switcher     → venue: "Brasero Centrale" (green active dot).
Period indicator    → active shift: "Dinner shift · 6:00 PM – 11:00 PM".
Sidebar sections    → OVERVIEW (Dashboard, Live Orders), SERVICE (Tables,
                      Reservations, Kitchen Display), MENU (Menu Items, Inventory),
                      REPORTS (Sales Analytics, End-of-Day Report).

KPI tiles (4):
  • Today's Sales  € 4,830  (amber sparkline, ▲ 12.4% vs yesterday).
  • Orders Served  183      (green sparkline,  ▲ 8.1% vs yesterday).
  • Avg Ticket     € 26.4   (amber sparkline,  ▲ 3.6% vs last week).
  • Tables Occupied 22 / 28 (donut ring,       78% occupancy).

Live state board   → "Live Orders Board" — 3 columns:
  NEW     — incoming order cards with Accept button.
  COOKING — in-prep cards with elapsed-time progress bar + late warning.
  SERVED  — awaiting-payment cards with Mark Paid button.

Ranked list (left) → "Top-Selling Items Today" — 6 rows of
  [rank] [dish name] [qty sold] [revenue] [amber bar].

Trend chart (right) → "Hourly Sales (€)" — last 8 hours amber polyline
  + area fill. Bottom strip: peak hour value + running total in amber.

Records table      → "Recent Orders": Order # / Table / Items / Total /
  Status pill (Paid green / Pending amber / Cancelled tomato).

List screen        → all orders, search + filter chips (status, period),
  paginated dense table.

Form screen        → "New Reservation": guest name (required), party size
  (required, > 0), date (required, not in the past), time slot (required
  select), special requests. Rules as required marks + helper text + inline
  errors; "Confirm Reservation" disabled until valid.

Detail screen      → one order: breadcrumb, header (order# + status pill +
  actions), meta grid (table, items, total, server, placed-at, paid-at),
  itemised sub-table + activity log.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, state labels, ranked-item columns, record table columns, form
   fields + rules, detail fields — from the KB + prompt. Standalone: use the
   Example instantiation above.
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
<artifact identifier="admin-savory-pos" type="text/html" title="Service Admin">
<!doctype html>...</artifact>
```
