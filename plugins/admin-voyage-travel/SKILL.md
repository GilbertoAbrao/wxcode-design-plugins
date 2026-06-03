---
name: admin-voyage-travel
description: |
  Airy light-mode admin aesthetic: white-and-pale-blue canvas (#f6fafc), sky-blue
  primary accent (#0ea5e9), coral secondary accent (#fb7185), clean sidebar
  navigation with grouped nav sections and a region/entity switcher pill, 60px
  topbar with centered search and date-range chip, 4 KPI cards with sparklines
  and delta badges, a two-column content grid (primary board + breakdown chart),
  a dense records table with status pills, and a circular donut side panel.
  Built for airy, open-space operational dashboards that surface key figures
  at a glance without visual clutter.
triggers:
  - "airy light-mode admin"
  - "sky-blue accent dashboard"
  - "coral accent admin"
  - "clean sidebar operations"
  - "open-space admin dashboard"
  - "light operations console"
  - "painel claro com sidebar"
  - "white canvas admin"
example_prompt: "Apply this airy light-mode admin aesthetic to my domain"
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

# Voyage Admin — Visual Archetype

This plugin contributes a **look** (airy light-mode, sky-and-coral palette, clean open
spacing) and a **structure** (sidebar with grouped nav + entity-switcher, topbar with
search + date-range, 4 KPI cards, a two-column main grid, a records table, and a donut
side panel). It does **not** contribute a domain — the subject matter comes from the
Knowledge Base and the user's prompt. Treat the example below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom property;
neutrals are hardcoded slate values.

- **Canvas / surfaces:** page `#f6fafc`; card / panel `#ffffff`; dividers `#e2eaf0`;
  subtle hover row `#f8fafc`; accent-tinted hover `#f0f9ff` (sky-bg); coral-tinted
  `#ffe4e6` (coral-bg).
- **Text ramp:** primary `#1e293b`; secondary `#64748b`; muted / micro-labels `#94a3b8`.
- **Primary accent:** `--sky: #0ea5e9`; hover variant `--sky-lt: #38bdf8`;
  tinted bg `--sky-bg: #f0f9ff`; border tint `#bae6fd`. Drives nav active state,
  CTAs, metric values, chart strokes, date-chip border.
- **Secondary accent:** `--coral: #fb7185`; light `--coral-lt: #fda4af`;
  tinted bg `--coral-bg: #ffe4e6`. Drives alert dots, cancelled/negative pills,
  notification dots, downward-trend sparklines.
- **Status ramp (as tokens):** `--green: #22c55e` / bg `--green-bg: #dcfce7` (confirmed /
  on-track); `--amber: #f59e0b` / bg `--amber-bg: #fef9c3` (pending / warning); coral
  (cancelled / negative); muted grey for neutral. All pill backgrounds use the tinted bg
  token.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`.
  Base 14px. Micro-labels 10px / `font-weight:700` / `text-transform:uppercase` /
  `letter-spacing:.07em` / color `#94a3b8`. Big KPI figures 26px / weight 800 / `#1e293b`.
  Card titles 14px / 700. Nav items 13px / 500–600. Mono face `"Courier New", monospace`
  for reference codes and IDs.
- **Density & radius:** relaxed — card padding 18–20px, row padding 12–13px, grid gaps
  16–20px; card radius 12px; pill radius 20px; avatar radius 50%; icon chip radius 10px;
  search/date-chip radius 20px.
- **Borders & shadows:** 1px `#e2eaf0` card borders; subtle `box-shadow:
  0 2px 12px rgba(14,165,233,.07)` on KPI cards; 1px bottom on topbar; 1px right on
  sidebar; no drop shadows elsewhere (flat, airy feel).
- **Motion:** gentle only — `.1s–.12s` background/color hover transitions, `.3s` bar-width
  transitions. No bounce; ease-out. Keep all transitions sub-150ms.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Left sidebar** (240px, white, 1px right border, scrollable): brand mark (icon chip +
  wordmark + sub-line) → **entity / region switcher pill** (sky-tinted, sky border, globe
  glyph + label + chevron) → grouped nav sections (each group: uppercase 10px muted label
  + N nav items). Nav item: left 3px border (transparent → sky accent on active), sky-bg
  row on active, icon glyph (16px) + label; optional count badge (coral pill) on alert
  items. Bottom: agent footer row (avatar + name + role + logout icon link).
- **Top bar** (60px, white, 1px bottom border): **page title block** (bold title +
  breadcrumb muted) → **centered search pill** (full-rounded, 320px, icon + placeholder,
  #f8fafc bg) → right cluster: **date-range chip** (sky border, calendar glyph + label +
  caret) + bell icon with coral dot + **avatar** (gradient circle + name label + caret).
- **KPI card row** (4 equal columns, gap 16px): each card = white, 12px radius, sky-tinted
  shadow, relative-positioned. Structure: absolute icon chip (sky-bg, top-right) → uppercase
  metric label → large tabular figure → footer: delta badge (green/coral/amber pill with arrow
  glyph) + comparison text + mini sparkline SVG (60×24px, 8-point polyline, sky stroke).
- **Two-column content grid** (primary ~60%, secondary ~38%, gap 20px):
  - **Primary — primary-entity board:** titled card, "View all →" sky link. Rows of
    `[icon chip] [entity name + sub-line] [pax / count] [state pill]`. State pills:
    green / amber / coral. Hover row #f8fafc.
  - **Secondary — breakdown chart:** titled card + period label. Rows of `[category label]
    [value (sky, 700)] [horizontal bar (sky fill, #e2eaf0 track)]`. Bar widths proportional
    to max value.
- **Bottom two-panel row** (primary ~65%, secondary ~33%):
  - **Records table card:** titled, ghost export button. Sticky uppercase header. Dense rows:
    mono reference ID + avatar+name customer cell + text columns + numeric column + status pill.
    Hover: sky-bg. No pager needed if rows < 10, otherwise add one.
  - **Donut side panel:** titled card. Inline donut SVG (sky + amber + border segments,
    center text 18px/800 + uppercase sub-label) + legend rows (dot + label + right-aligned
    value). Below: N category rows, each: label / value / horizontal fill bar (sky, 6px tall).
- **Records list screen:** search + filter chips toolbar (full-rounded search, chip group
  with count bubbles), then the records-table archetype as the primary content, with a
  footer pager.
- **Record form screen:** sectioned cards of labeled fields; **rules appear as inline
  validation** — required marks (`*`), helper text under the field, and inline error messages
  on invalid fields; primary submit disabled-until-valid. No rules/checklist/validation-status
  panel.
- **Record detail screen:** breadcrumb → header band (title + status pill + key actions) →
  meta-grid card (N columns of label/value pairs) → two-column related-data row (entity
  sub-list + activity feed).

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS domain's
equivalent of the archetype slots — its primary entities, key metrics, status states, record
list/columns, form fields and their rules, and detail fields — and map them onto the archetype
above. If no KB/domain is supplied (standalone), use the Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules become inline
field validation. Do NOT render build/implementation notes or designer controls — every screen
is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode this is
> IGNORED — replace every label with the real domain's equivalent (entities, metrics, states,
> columns, fields) drawn from the KB + prompt.

```
Domain (illustrative): a travel agency operations platform.

Entity switcher pill → region: "EMEA Region".
Agent footer         → Ops Manager, avatar gradient sky→coral.
Nav groups           → OVERVIEW (Dashboard, Analytics), OPERATIONS (Bookings,
                       Itineraries, Fleet, Suppliers), CLIENTS (Guests, Corporate,
                       Loyalty), SETTINGS (Settings). Active: Dashboard.

KPI cards (4):
  • Bookings Today: 84  ▲ +12% vs yesterday (sky sparkline).
  • Occupancy Rate: 73% ▲ +4 pts vs last week (sky sparkline).
  • Revenue (MTD): $214,800 ▲ +8% vs last month (sky sparkline).
  • Avg Lead Time: 18 days ▼ −2 days vs last month (coral sparkline, delta-down).

Primary board (left) → "Active Itineraries" — rows of flag icon + trip name /
  dates + pax count + status pill (Confirmed green, Pending amber, Cancelled coral).
  6 trips: Amalfi & Capri Escape, Kyoto Cherry Blossom Tour, Sahara Dunes Expedition,
  Fjords of Norway Voyage, Patagonia Trekking Route, Zanzibar Island Escape.

Breakdown chart (right) → "Top Destinations · May 2026" — 6 rows:
  Italy 38, Japan 31, Morocco 24, Norway 22, Argentina 17, Tanzania 14.

Records table → "Recent Bookings": Ref # (mono) / Customer (avatar+name) /
  Destination / Travel Dates / Pax / Total / Status. 7 rows; refs VGT-XXXXX.
  States: Confirmed (green), Pending (amber), Cancelled (coral).

Donut side panel → "Room & Seat Occupancy": Booked 73% (sky) / Held 9% (amber) /
  Available 18% (border). 3 property rows: Villa Adriatica 88%, Ryokan Higashiyama 74%,
  Riad Al-Andalus 61%.

List screen     → all records, search + filter chips (status facet), paginated table.

Form screen     → "New Booking": customer name (required), destination (required select),
  travel dates (required, not in the past), pax count (required, > 0), total value
  (required, > 0), notes. Rules: required marks + helper text + inline errors;
  "Create Booking" disabled until valid.

Detail screen   → one booking: breadcrumb → header (Ref # + status pill + Edit / Cancel
  actions) → meta grid (customer, destination, dates, pax, total, agent, created) →
  two-column: itinerary details sub-table + activity feed.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual language
   tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities, key metrics,
   status states, record columns, form fields + rules, detail fields — from the KB + prompt.
   Standalone: use the Example instantiation above.
3. Build each screen in the Visual language + Layout archetype above, imitating the example
   set in `assets/` (dashboard, list, form, detail) and the `assets/template.html` seed —
   with fresh content for the real domain, NOT the example labels.
4. Express domain rules as INLINE field validation (required marks, helper text, inline
   errors, disabled-until-valid submit). Never render rules/checklist/validation-status/
   build-note panels or designer/demo controls.
5. One inline `<style>`, semantic HTML5, no external assets, no CDNs — self-contained.

## Output contract

```
<artifact identifier="admin-voyage-travel" type="text/html" title="Voyage Admin">
<!doctype html>...</artifact>
```
