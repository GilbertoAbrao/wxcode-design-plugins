---
name: admin-meridian-people
description: |
  Warm-professional light-mode admin aesthetic: off-white canvas (#f8f8fb),
  indigo accent (#4f46e5 / #6366f1), white sidebar and cards with #e8e8ef
  hairline borders, soft 2–8px card shadows, Inter type, 12px radii on cards
  and 8px on controls, 11px uppercase micro-labels at 0.06–0.10em letter-
  spacing, large 26px tabular KPI figures, and multi-tone status pills
  (green / amber / indigo / red). Archetype = 240px fixed left sidebar
  (entity-switcher card + grouped nav sections + footer user row) + 60px
  topbar (title/breadcrumb + search + period-selector tabs + bell + avatar) +
  4 KPI tiles (number + delta chip + sparkline) + 2-column grid (area chart
  card + horizontal-bar breakdown card) + full-width records table with
  avatars and status pills + 320px right side panel (queued-approvals list).
triggers:
  - "light professional admin"
  - "indigo accent dashboard"
  - "warm light-mode admin"
  - "sidebar nav admin panel"
  - "soft-shadow card admin"
  - "period-selector topbar"
  - "avatar records table"
  - "approval side panel"
example_prompt: "Apply this warm light-mode indigo-accent admin aesthetic to my domain"
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

# Meridian Admin — Visual Archetype

This plugin contributes a **look** (warm light-mode, indigo accent, soft-shadow
cards) and a **structure** (fixed sidebar + topbar + KPI tiles + chart/breakdown
grid + records table + approval side panel, plus list / form / detail screens).
It does **not** contribute a domain — the subject matter comes from the Knowledge
Base and the user's prompt. Treat the example below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property; hardcode surface and text neutrals.

- **Canvas / surfaces:** page `#f8f8fb`; sidebar `#ffffff`; card `#ffffff`;
  hairline border `#e8e8ef`; inner row divider `#f1f1f5`; hover row `#fafafa`.
- **Text ramp:** primary `#1e1e2d`, secondary `#6b7280`, muted `#9ca3af`.
- **Accent:** `--color-accent: #4f46e5` (primary indigo), `--color-accent-mid: #6366f1`
  (hover / lighter), `--color-accent-bg: #eef2ff` (tint for backgrounds and
  active-nav highlights). Active nav: accent left-bar + accent-bg fill.
- **Status tokens:** `--color-success #16a34a` / `--color-success-bg #dcfce7`;
  `--color-warn #d97706` / `--color-warn-bg #fef3c7`; `--color-danger #dc2626` /
  `--color-danger-bg #fee2e2`; `--color-probation #4338ca` /
  `--color-probation-bg #e0e7ff`. Pills: colored text + tint background.
- **Category bar colors (token set for breakdown charts):**
  `--color-cat-a #6366f1`, `--color-cat-b #ec4899`, `--color-cat-c #f59e0b`,
  `--color-cat-d #10b981`, `--color-cat-e #8b5cf6`, `--color-cat-f #0ea5e9`.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`.
  Base 14px. Micro-labels: 10–11px `text-transform:uppercase` `letter-spacing:.06–.10em`
  color muted. KPI figures: 26px weight 700 color primary. Section headers:
  10px uppercase 0.10em muted. Links and active states: accent color.
- **Density & radius:** card radius 12px; control radius 8px; pill radius 99px;
  progress bar 6px tall / 99px radius; 24px content padding; 16px card gaps.
- **Shadows:** cards `0 2px 8px rgba(0,0,0,.04)`. No heavy drop shadows.
- **Motion:** `.12s` background/color hover transitions, ease. No bouncy easing.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Left sidebar** (240px, fixed, white, right hairline border, scrollable):
  top logo area → **entity-switcher card** (org avatar chip + name + sub-line +
  chevron, rounded box on page-bg) → **grouped nav sections** (10px uppercase
  section label + nav items with 13px label + icon; active item = left accent
  bar + accent-bg fill + accent text + weight 600; badge chips on items with
  counts) → **footer user row** (avatar circle + name + role + cog icon).
- **Top topbar** (60px, white, bottom hairline, flex): page-title/breadcrumb
  block (left) → search input with icon (center, 300px max) → period-selector
  tab group (MTD/QTD/YTD style, right-aligned, white active tab with shadow) →
  notification bell with badge dot → avatar + name.
- **KPI tile row** (4 tiles, equal grid, 16px gap): each tile = white card
  (12px radius, soft shadow) with uppercase micro-label + 26px figure + footer
  row holding a delta chip (color-coded up/down/warn pill) + a 60×32px inline
  SVG sparkline.
- **2-column grid (1fr / 300px, 16px gap, align start):**
  - **Left — area-chart card:** card-header (title + sub + tab group) →
    chart-legend row → full-width inline SVG (area fill gradient + polyline +
    Y-axis labels left + X-axis labels bottom + horizontal grid lines).
  - **Right — horizontal-bar breakdown card:** card-header (title + sub) →
    rows of `[color swatch] [category name] [bar track + fill] [count] [pct]`.
    Bar fill uses category color tokens; track is `#f1f1f5`.
- **Full-width records table** (below grid): white card; table-header with
  title + count badge + filter-pill row + primary CTA button; sticky uppercase
  thead on page-bg; dense rows (avatar circle + name/sub-line cell, role,
  category, status pill, date); colored status pills; footer with result count
  + pager.
- **Right side panel** (320px, 16px gap, align start): two stacked white cards.
  First card: **queued-approvals list** — panel title + date sub-line →
  `timeoff-item` rows of `[avatar circle] [name / sub-line / approve + decline
  action buttons] [day count]`. Second card: **secondary-approvals section** —
  section-header + count badge → `pending-item` rows of `[warn dot] [name /
  detail / submitted-when]` → "View all" accent-bg link.
- **Records list screen:** the records-table archetype as its own page —
  search + filter chips + count, same dense table with avatars, pager.
- **Record form screen:** sectioned cards of labelled fields; **rules appear as
  inline validation** — required marks (`*`), helper text under the field,
  inline error messages on invalid fields, submit disabled-until-valid. No
  rules/checklist/validation-status panel.
- **Record detail screen:** breadcrumb → header band (name + status pill +
  actions) → meta grid (label/value pairs, 3 columns) → related sub-panels
  (horizontal-bar mini breakdown or a mini activity log).

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key metrics,
status states, record list/columns, form fields and their rules, category
breakdown dimensions, and detail fields — and map them onto the archetype above.
If no KB/domain is supplied (standalone), use the Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules
become inline field validation. Do NOT render build/implementation notes or
designer controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent
> (entities, metrics, states, columns, fields) drawn from the KB + prompt.

```
Domain (illustrative): a people-operations admin for a mid-sized organisation.

Entity switcher     → organisation: "NorthVault Group · 847 members".
Topbar title        → "People Dashboard" / breadcrumb "NorthVault / Overview".
Sidebar sections    → OVERVIEW (Dashboard, Headcount, Attendance),
                      TALENT (Recruitment, Onboarding, Performance),
                      PEOPLE (Directory, Time Off, Payroll),
                      SETTINGS (Roles & Permissions, Integrations).

KPI tiles (4):
  • Total Headcount 847  (↑ +12 this month — sparkline upward).
  • Attendance Rate 94.3% (↓ −0.8 pp — sparkline slight dip).
  • Open Roles 23  (+ 5 new listings — sparkline stepped up).
  • Turnover (12 mo) 8.2%  (↓ −1.1 pp — sparkline trending down).

Area-chart card  → "Headcount Growth" (12 months Jun–May);
                   area fill accent-bg gradient, line accent, monthly labels.

Breakdown card   → "By Department" — 6 bars: Sales 211, Engineering 182,
                   Operations 97, Design 64, Finance 58, Product 48.

Records table    → "Employees": Name (avatar + email) / Role / Department /
                   Status pill (Active · On Leave · Probation · Terminated) /
                   Start Date. 8 rows; "+ Add" primary CTA; All / Active /
                   On Leave / Probation filter pills; pagination.

Side panel 1     → "Time Off Today": 4 entries with avatar, name, leave type,
                   day count, Approve / Decline buttons.
Side panel 2     → "Pending Approvals" (count badge): 3 entries with warn dot,
                   name, detail line, submitted-when; "View all requests" link.

List screen      → all records, search + filter chips (e.g. department /
                   status), paginated dense table.

Form screen      → "New Record": Name (required), Email (required, valid
                   format), Role (required), Department (required select),
                   Start Date (required, not in the past), Contract type.
                   Rules shown as required marks + helper text + inline errors;
                   "Create" disabled until valid.

Detail screen    → one record: breadcrumb → header (name + status pill +
                   Edit / Archive actions) → meta grid (role, department,
                   start date, manager, location, contract) → related panel
                   (e.g. leave balance breakdown or activity log).
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, status states, category breakdown dimensions, record columns,
   form fields + rules, detail fields — from the KB + prompt. Standalone: use
   the Example instantiation above.
3. Build each screen in the Visual language + Layout archetype above, imitating
   the example set in `assets/` (dashboard, list, form, detail) and the
   `assets/template.html` seed — with fresh content for the real domain, NOT
   the example labels.
4. Express domain rules as INLINE field validation (required marks, helper text,
   inline errors, disabled-until-valid submit). Never render
   rules/checklist/validation-status/build-note panels or designer/demo controls.
5. One inline `<style>`, semantic HTML5, no external assets, no CDNs —
   self-contained.

## Output contract

```
<artifact identifier="admin-meridian-people" type="text/html" title="Meridian Admin">
<!doctype html>...</artifact>
```
