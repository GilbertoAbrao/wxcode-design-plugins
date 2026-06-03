---
name: admin-verdant-clinic
description: |
  Calm light-mode admin aesthetic: near-white #f7faf9 canvas, white #ffffff cards
  with #e3ece9 hairline borders, emerald-to-teal accent (#10b981 / #0d9488),
  slate text hierarchy (#1e293b / #475569 / #94a3b8), three-tone status pills
  (emerald / amber / rose), soft 1px card shadow, 12px card radius, 8px control
  radius, 14px base type. Archetype = left sidebar (entity-switcher dropdown +
  sectioned nav groups + user chip) + 60px topbar (breadcrumb + search + date
  badge + avatar) + 4 KPI cards with inline sparklines + 2-column main grid (a
  schedule/board table + a side chart panel) + full-width records table.
triggers:
  - "calm light-mode admin"
  - "emerald-teal admin"
  - "clean white card dashboard"
  - "soft clinical admin aesthetic"
  - "light sidebar admin"
  - "teal accent operations panel"
  - "status-pill schedule dashboard"
  - "painel claro esmeralda"
example_prompt: "Apply this calm emerald-teal light-mode admin aesthetic to my domain"
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

# Verdant Admin — Visual Archetype

This plugin contributes a **look** (calm light-mode, emerald-to-teal accent, soft
card surfaces, tri-tone status pills) and a **structure** (entity-switcher sidebar
+ topbar + KPI cards + schedule/board table + side chart + records table, plus
list / form / detail screens). It does **not** contribute a domain — the subject
matter comes from the Knowledge Base and the user's prompt. Treat the example
below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property; only neutral near-whites and slate text may be hardcoded.

- **Canvas / surfaces:** page `#f7faf9`; cards / sidebar `#ffffff`; hover row /
  input bg `#f1f5f3`; hairline border `#e3ece9`; table header bg `#fafcfb`.
- **Text ramp:** primary `#1e293b`; secondary `#475569`; muted `#94a3b8`; deep
  `#0f172a` (big KPI figures).
- **Accent:** `--accent-emerald: #10b981`, `--accent-teal: #0d9488`,
  `--accent-emerald-dim: #ecfdf5`, `--accent-teal-dim: #ccfbf1`.
  Interactive hover shifts emerald → teal. Active nav item: `#ecfdf5` background +
  emerald left bar (`3px`, border-radius `0 3px 3px 0`).
- **Status pill tokens (3 tones):**
  - Stable / Completed / Success → `--status-stable-bg: #d1fae5`,
    `--status-stable-text: #065f46`.
  - Pending / In Progress / Warning → `--status-pending-bg: #fef3c7`,
    `--status-pending-text: #92400e`.
  - Urgent / Cancelled / Danger → `--status-urgent-bg: #fce7f3`,
    `--status-urgent-text: #9d174d`.
  - A 4th tone (informational / neutral) may use `--status-info-bg: #dbeafe`,
    `--status-info-text: #1e40af`.
- **Sparkline tokens:** `--spark-emerald: #10b981`, `--spark-teal: #0d9488`,
  `--spark-amber: #f59e0b`, `--spark-rose: #f43f5e`.
- **Chart bar tokens:** `--chart-bar-1: #10b981`, `--chart-bar-2: #0d9488`,
  `--chart-bar-3: #6ee7b7`, `--chart-bar-4: #14b8a6`.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
  sans-serif`. Base 14px / line-height 1.5. KPI values 28px / weight 800 /
  `letter-spacing: -.5px`. Table headers 10–10.5px / weight 700 / uppercase /
  `letter-spacing: .06–.08em`. Nav labels 13–13.5px / weight 500.
- **Density & radius:** 12px card radius, 8px control / pill / input radius, 7px
  nav-item radius. Card padding ~18–20px; row padding 10–11px. Grid gap 16px.
- **Shadows:** `0 1px 4px rgba(0,0,0,.05)` on cards. No shadow on topbar/sidebar
  — border-only separation.
- **Motion:** `.13–.15s` background / border / color hover transitions. No bounce.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns described by shape and behavior — not meaning.

- **Left sidebar (240px, white bg, 1px right border):** top logo area (icon mark +
  wordmark) → **entity-switcher dropdown** (label + chevron, rounded, hover
  border-color accent) → **sectioned nav groups** (each group: uppercase 10px
  micro-label + nav-item rows; active item gets emerald left-bar + dim bg + weight
  600; items may carry right-aligned count badges in status-pill colors) → footer
  chip (avatar circle + user name + role + sign-out icon button).
- **Top header bar (60px, white bg, 1px bottom border):** breadcrumb (muted
  parent / bold current) → **flex-1 search input** (icon-inset, focus border
  accent, max 360px) → right cluster: date/context badge + notification icon button
  (with dot indicator) + avatar circle.
- **Page header (inside scrollable body):** title (20px / 700) + subtitle on the
  left; ghost button + primary CTA on the right.
- **KPI card row (4 cards, equal grid):** each card = white, 12px radius, soft
  shadow, 1px border. Top: uppercase micro-label + icon chip (recolored by
  tone — emerald / teal / amber / rose). Below: big tabular figure. Footer: inline
  SVG sparkline (polyline or bars) + delta chip (`.up` / `.down` / `.flat`).
- **2-column main grid (1fr / ~340px side panel):**
  - **Left — schedule / board table:** card with header (title + subtitle +
    view-all link), then a full-width table. Columns: time/ID column (bold) /
    entity cell (avatar dot + name + sub-id) / type/category / badge slot /
    status pill. 8 rows minimum.
  - **Right — mini-chart panel:** card with header + legend chips (color dot +
    label), inline SVG grouped bar chart (N days × M series), day-label row below.
- **Full-width records table (lower section):** card header (title + subtitle +
  view-all link), a data table — columns: entity/ID cell (avatar dot + name +
  code) / numeric metric / category tag chip / timestamp / status pill. Tinted
  hover row. 8 rows minimum.
- **Records list screen:** search + filter chip toolbar (search input + active/all
  chip + state chips with counts), then the records-table component, then a
  footer with count + simple pager.
- **Record form screen:** one or more sectioned white cards (section-title line
  inside each card + a field grid). **Rules appear as inline validation only** —
  required marks (`*`), helper text under the field, and inline error messages on
  invalid fields. Submit button disabled until valid. No rules-summary /
  checklist / validation-status panel.
- **Record detail screen:** breadcrumb → detail header band (bold ID + status pill
  + action buttons) → meta grid card (3-column label/value pairs with sub-lines)
  → 2-column lower section (a related-data board / mini-table on the left +
  activity/timeline panel on the right).

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key metrics,
status states, record list/columns, form fields and their rules, and detail fields
— and map them onto the archetype above. If no KB/domain is supplied (standalone),
use the Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules
become inline field validation. Do NOT render build/implementation notes or
designer controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent
> (entities, metrics, states, columns, fields) drawn from the KB + prompt.

```
Domain (illustrative): a multi-department outpatient scheduling operation.

Entity switcher  → department: "General Practice".
Date badge       → current date.
Rail nav groups  → OVERVIEW (Dashboard, Schedule, Records), OPERATIONS
                   (Intake, Results, Prescriptions), ADMIN (Rooms, Staff, Reports),
                   SETTINGS.

KPI cards (4):
  • Primary-entity count today — big number, emerald sparkline, delta chip.
  • Appointment/session count — big number, teal bar-sparkline, delta chip.
  • Avg wait/processing time — number + unit suffix, amber trend, flat chip.
  • Capacity/occupancy rate — percentage, rose fill bar, delta chip.

2-column grid (left) → schedule board: columns Time / Entity / Type / Room-or-Slot
  / Status pill. States: Completed (stable), In Progress (pending), Waiting
  (pending), Urgent (urgent), Scheduled (info).

2-column grid (right) → occupancy/utilization mini-chart: 7-day × 4-series
  grouped bars with legend and day labels.

Records table → full-width: Entity name + ID / Age-or-numeric / Category tag /
  Last timestamp / Status pill.

List screen  → all records, search + filter chips (status, category), paginated.

Form screen  → "New Record": primary-entity lookup (required), category
  (required select), sub-type (required), slot/location (required select),
  scheduled time (required, not in the past), priority (select). Rules shown as
  required marks + helper text + inline errors; submit disabled until valid.

Detail screen → one record: header (ID + status pill + Edit / Cancel actions),
  meta grid (entity, category, location, scheduled, created, owner), and a
  "Related Sessions" mini-table + activity feed.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, status states, record columns, form fields + rules, detail fields
   — from the KB + prompt. Standalone: use the Example instantiation above.
3. Build each screen in the Visual language + Layout archetype above, imitating
   the example set in `assets/` (dashboard, list, form, detail) and the
   `assets/template.html` seed — with fresh content for the real domain, NOT the
   example labels.
4. Express domain rules as INLINE field validation (required marks, helper text,
   inline errors, disabled-until-valid submit). Never render
   rules/checklist/validation-status/build-note panels or designer/demo controls.
5. One inline `<style>`, semantic HTML5, no external assets, no CDNs —
   self-contained. Every chromatic color via `:root` CSS custom property.

## Output contract

```
<artifact identifier="admin-verdant-clinic" type="text/html" title="Verdant Admin">
<!doctype html>...</artifact>
```
