---
name: admin-kaiadmin
description: |
  Light-canvas dark-sidebar admin aesthetic: frosted-white card surfaces on a
  pale blue-grey page (#f5f7fd), a fixed deep-navy sidebar (#1a2035) with white
  icon-label navigation, a sticky top header bar, a cobalt-blue primary accent
  (#1572e8) for buttons, badges, and active states, body text #5a5a5a, Public
  Sans 400/600/700 type scale, 10px card radius, subtle box-shadow cards, and
  status pills for every entity state. Archetype = fixed dark vertical sidebar
  (icon + label items, collapsible sub-nav, bottom user chip) + sticky top
  header (breadcrumb title + search field + icon actions + avatar) + 4-tile KPI
  row (icon chip + big figure + trend badge + sub-label) + 2-column dashboard
  grid (status overview panel + SVG inline chart panel) + full-width records
  table with status pills, plus list, advanced datatable, form, charts,
  widgets, and profile/settings screens.
triggers:
  - "light admin dark sidebar"
  - "navy sidebar blue accent admin"
  - "clean card admin dashboard"
  - "white card navy panel admin"
  - "blue accent enterprise dashboard"
  - "light canvas sidebar admin"
  - "admin painel lateral escuro"
  - "dashboard cards brancos acento azul"
  - "admin fundo claro sidebar navy"
  - "enterprise sidebar navigation blue"
example_prompt: "Apply this light-canvas dark-sidebar admin aesthetic to my domain"
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
    requires: [typographic-rhythm, state-coverage]
---

# Azure Rail Admin — Visual Archetype

This plugin contributes a **look** (light frosted-white content area, deep-navy
sidebar, cobalt-blue accent, Public Sans type, 10px radius cards with subtle
shadows) and a **structure** (fixed dark sidebar + sticky header + KPI tiles +
dashboard grid + records table, plus list, datatable, form, charts, widgets, and
profile screens). It does **not** contribute a domain — the subject matter comes
from the Knowledge Base and the user's prompt. Treat the example below as
illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Every chromatic value is a `:root` CSS custom property;
only true neutrals (#fff, #000 derivatives) may be hardcoded.

- **Page canvas:** `--page-bg: #f5f7fd` (pale blue-grey); content scrolls on this.
- **Sidebar:** `--sidebar-bg: #1a2035` (deep navy); `--sidebar-text: #a9b7d0`
  (muted slate); `--sidebar-active-bg: #1572e8` (blue chip); `--sidebar-active-text: #ffffff`.
  `--sidebar-hover-bg: rgba(255,255,255,.08)`. Width 260px fixed; top logo zone 60px.
- **Cards / panels:** `--card-bg: #ffffff`; `border-radius: 10px`;
  `box-shadow: 0 1px 4px rgba(0,0,0,.08), 0 4px 16px rgba(0,0,0,.04)`.
  Internal padding 20–24px. Card headings 15px / weight 600 / `#444`.
- **Primary accent:** `--accent: #1572e8` (cobalt blue); `--accent-hover: #1260c4`;
  `--accent-light: rgba(21,114,232,.12)` (icon chip + badge tint).
- **Text ramp:** `--text-primary: #444444`; `--text-body: #5a5a5a`;
  `--text-muted: #9daec5`; `--text-link: #1572e8`.
- **Status tokens:**
  - `--state-success: #31ce36`; `--state-success-bg: rgba(49,206,54,.13)`.
  - `--state-warning: #ffad46`; `--state-warning-bg: rgba(255,173,70,.13)`.
  - `--state-danger: #f25961`; `--state-danger-bg: rgba(242,89,97,.13)`.
  - `--state-info: #48abf7`; `--state-info-bg: rgba(72,171,247,.13)`.
  - `--state-secondary: #6c757d`; `--state-secondary-bg: rgba(108,117,125,.13)`.
- **Typography:** `"Public Sans", "Segoe UI", system-ui, -apple-system, sans-serif`.
  Base 14px; line-height 1.5. Headings: page title 20px/700; card title 15px/600;
  table header 11px/700 uppercase letter-spacing .5px; KPI figure 28px/700;
  sub-labels 12px/400 muted. Numeric columns use `font-variant-numeric: tabular-nums`.
- **Borders:** `--border: #ebecec` (1px dividers); `--border-focus: #1572e8` (focus ring).
- **Header bar:** `--header-bg: #ffffff`; height 60px; 1px bottom border `--border`;
  position sticky top 0; `z-index 100`.
- **Radius & spacing:** card 10px; button 5px; input 5px; pill 12px; table row 44px tall;
  section padding 24px; grid gap 20px.
- **Motion:** `.15s ease` background/color/border transitions on interactive elements;
  no bounce, no scale-zero transforms.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns described by shape and behavior — not meaning.

- **Fixed dark sidebar (260px):** top logo zone (brand mark + app label) → vertical
  nav list (icon glyph + label + optional sub-nav chevron, collapsible sub-items
  indented 12px) → bottom user chip (avatar + name + role, pinned). Active item
  gets a blue solid chip full-width; hover gets a translucent white wash.
- **Sticky header bar (60px, full width minus sidebar):** left — page breadcrumb /
  title; center — search input (icon + placeholder + pill border); right — icon
  action buttons (bell + grid + cog) with optional badge dot + avatar circle with
  dropdown indicator.
- **Main content area** (padding 24px, vertical flow on `--page-bg`):
  - **KPI tile row** (4 equal tiles): each tile = white card with a colored square
    icon chip (top-left) + a trend/delta pill (top-right) + a big tabular figure
    (center) + an uppercase sub-label + a supporting line of text.
  - **2-column dashboard grid (7fr / 5fr or 60/40):**
    - **Left — status overview panel:** titled white card with a summary bar or
      segmented ring, then a labeled-row list of
      `[color dot] [label] [count chip] [bar-fill percent]` stacked rows.
    - **Right — inline chart panel:** titled white card housing an SVG line/area
      chart with labeled axes, gridlines, and a small legend row; optionally a
      second smaller bar-chart panel stacked below.
  - **Full-width records table panel:** white card, card-title + count badge + header
    actions (search field + primary button), a sticky thead with sortable columns
    (11px/700 uppercase), dense tbody rows (44px, 1px row border) with status pills,
    a checkbox column, an action column (icon buttons), and a footer with result
    count + pagination controls.
- **List screen:** the records-table archetype as a full page — filter row (search
  input + select chips + date range) above the same table, pager below.
- **Advanced datatable screen:** adds column visibility toggle, row-select checkbox
  header, inline row editing (pencil icon → editable cell), bulk action bar (appears
  when rows selected), and per-row expand/collapse sub-row.
- **Form screen:** sectioned white cards of labelled fields; **domain rules appear
  as inline validation** — red asterisk on required labels, helper text beneath the
  field, and inline error message on the field border turning `--state-danger`;
  primary submit button disabled until required fields pass. No rules/checklist/
  validation-status panel.
- **Charts screen:** a row of two or three chart cards (line, bar, doughnut) in the
  same white-card shell, each with a card header + SVG or CSS chart body + optional
  legend row.
- **Widgets screen:** a mixed-grid of specialty cards — progress-ring widget,
  quick-stats strip, activity feed, mini-calendar block, icon-stat row — all in the
  same white-card + blue-accent skin.
- **Profile / settings screen:** two-column layout — left narrow card (avatar +
  name + role + quick stats) + right wider card (tabbed sections: personal info
  fields, password change, notification toggles, each section with inline-validated
  fields and a save button).

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key metrics,
status states, record list columns, form fields and their validation rules, chart
subjects, and settings sections — and map them onto the archetype above. If no
KB/domain is supplied (standalone), use the Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules
become inline field validation. Do NOT render build/implementation notes or
designer controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent
> (entities, metrics, states, columns, fields) drawn from the KB + prompt.

```
Domain (illustrative): a regional logistics and fleet-management console.

Sidebar nav items → Dashboard, Shipments, Fleet, Routes, Drivers, Reports, Settings.
Header breadcrumb → "Dashboard" or current section label.
Avatar            → dispatcher's initials chip.

KPI tiles (4):
  • Active Shipments 1,284 (▲ 47, "vs. yesterday", blue chip icon: box).
  • On-Time Delivery 94.2% (▲ 1.3%, green, icon: check-circle).
  • Vehicles En Route 86 (▼ 3, amber, icon: truck).
  • Incidents Today 5 (▲ 2, red, icon: alert-triangle).

Dashboard grid:
  Left — Shipment Status panel: segmented bar + labeled rows
    [blue dot] In Transit   [412] [████████░░ 82%]
    [green dot] Delivered   [718] [██████████ 100%]
    [amber dot] Delayed     [94]  [████░░░░░░ 18%]
    [red dot]   Failed      [12]  [█░░░░░░░░░  2%]
  Right — Delivery Rate chart: SVG line chart of on-time % over 7 days
    with gridlines + day labels; secondary mini bar-chart of daily volume below.

Records table → "Shipments — Active":
  Columns: ID (mono) / Origin / Destination / Driver / ETA / Status pill /
  Actions (eye + edit).
  Status pills: In Transit (blue) / Delayed (amber) / Failed (red) / Delivered (green).

List screen     → All shipments; filter by Status, Route, Date Range; paginated.
Datatable       → Fleet vehicles — column toggle, row inline edit (license plate,
  capacity), bulk "schedule maintenance" action, expand sub-row for trip log.
Form screen     → "New Shipment": origin (required), destination (required), driver
  (required select), cargo type, declared weight (required, > 0), pickup date
  (required, not in the past), notes. Required marks + helper text + inline errors;
  submit disabled until valid.
Charts screen   → Delivery rate line chart (7 days) + Volume by route bar chart +
  Shipment status doughnut.
Widgets screen  → On-time ring (94.2%), Active fleet strip, Recent alerts feed,
  Top routes mini-table, Daily volume mini bar.
Profile screen  → Left card: dispatcher avatar + name + role + 3 quick stats.
  Right card tabs: Personal Info (name, email, phone — inline validated), Change
  Password (current + new + confirm, strength meter inline), Notifications (toggles).
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities, key
   metrics, status states, record columns, form fields + rules, chart subjects,
   settings sections — from the KB + prompt. Standalone: use the Example
   instantiation above.
3. Build each screen in the Visual language + Layout archetype above, imitating the
   example set in `assets/` (dashboard, list, datatable, form, charts, widgets,
   profile) and the `assets/template.html` seed — with fresh content for the real
   domain, NOT the example labels.
4. Express domain rules as INLINE field validation (required asterisks, helper text,
   inline error messages, disabled-until-valid submit). Never render
   rules/checklist/validation-status/build-note panels or designer/demo controls.
5. One inline `<style>`, semantic HTML5, `tabular-nums` on figures, no external
   assets, no CDNs — self-contained.

## Output contract

```
<artifact identifier="admin-kaiadmin" type="text/html" title="Azure Rail Admin">
<!doctype html>...</artifact>
```
