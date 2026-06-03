---
name: admin-bloom-nonprofit
description: |
  Warm-optimistic light-mode admin aesthetic: page canvas #f7fbf9, white card
  surfaces, emerald accent (#10b981) with coral counter-accent (#fb7185), soft
  #e4ede9 dividers, Inter type, 14px body with 10px uppercase micro-labels,
  12px rounded status badges. Archetype = left sidebar (entity/program switcher
  + grouped nav + user footer) + topbar (search + period tabs + notification
  dot + avatar) + 4 KPI cards with sparklines + 2-column mid-row (progress list
  + donut segment panel) + full-width trend chart + full-width records table
  with type pills. Built for warm, human-scale operational consoles where
  progress and growth must read at a glance.
triggers:
  - "warm light-mode admin"
  - "emerald accent admin"
  - "optimistic admin dashboard"
  - "soft green coral admin"
  - "progress-bar dashboard"
  - "sidebar nav admin"
  - "donut segment panel"
  - "painel claro otimista"
example_prompt: "Apply this warm light-mode admin aesthetic to my domain"
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

# Bloom Admin — Visual Archetype

This plugin contributes a **look** (warm light-mode, emerald + coral accents,
soft card surfaces) and a **structure** (entity/program-switcher sidebar +
period-tab topbar + KPI cards + progress list + donut panel + trend chart +
records table, plus list / form / detail screens). It does **not** contribute
a domain — the subject matter comes from the Knowledge Base and the user's
prompt. Treat the example below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property; hardcode only the slate neutral ramp.

- **Canvas / surfaces:** page `#f7fbf9`; card `#ffffff`; divider / border
  `#e4ede9`; hover row `#f9fdfb`.
- **Text ramp:** primary `#1e293b`, secondary `#64748b`, muted `#94a3b8`.
- **Accent (emerald):** `--accent: #10b981`, `--accent-light: #d1fae5`,
  `--accent-dark: #059669`, `--accent-mid: #34d399`. Primary CTAs, active nav
  indicator, progress fills, chart strokes, positive deltas.
- **Counter-accent (coral):** `--coral: #fb7185`, `--coral-light: #ffe4e8`,
  `--coral-dark: #e11d48`. Secondary CTAs, recurring-type pills, negative
  deltas, alert states.
- **Warm-neutral accent (amber):** `--amber: #f59e0b`, `--amber-light: #fef3c7`,
  `--amber-dark: #92400e`. Warning / ending-soon states.
- **Status badges (as tokens):** active `--accent-light / --accent-dark`;
  ending/warning `--amber-light / --amber-dark`; paused `#f1f5f9 / #64748b`.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
  sans-serif`. Base 14px / `line-height: 1.5`. Micro-labels 10px / uppercase /
  `letter-spacing: .06em` / muted. KPI figures 26px / weight 700. Nav items
  13px / weight 500. Table cells 13px. Use `font-variant-numeric: tabular-nums`
  on every numeric cell.
- **Density & radius:** comfortable — sidebar 260px, topbar 60px, card padding
  18–20px, cell padding 10–11px vertical / 20px horizontal; card radius 12px,
  control radius 8px, pill radius 20px, progress bar 6px tall / 3px radius.
- **Borders & shadows:** 1px hairlines at `var(--border)` do all separation;
  no drop shadows on cards (flat, airy feel). Inset hover background `#f9fdfb`.
- **Motion:** subtle — `.15s` background / border / color hover transitions,
  `.4s` width transitions on progress bars.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Left sidebar** (260px, white, 1px right border, sticky full-height):
  - **Entity / scope switcher** at top: avatar circle (accent fill, initial
    letter) + name + caret; below it, a row of 2–3 program/filter chips
    (active chip: `--accent-light` bg + `--accent-dark` text).
  - **Grouped nav**: 3–4 labeled groups of icon + label items; active item
    has `--accent-light` background, `--accent-dark` text + weight 600, and a
    3px left accent bar. Optional badge counts on items use coral-light pills.
  - **User footer** (pinned bottom, 1px top border): small avatar circle +
    name + role label + sign-out icon button.
- **Topbar** (60px, white, 1px bottom border, sticky):
  left: page title + date subtitle; center: search pill with magnifier icon;
  right: period-tab selector (3 tabs, active underlined accent) + notification
  button with amber dot + avatar circle.
- **KPI cards** (4-column equal grid): each card = white panel, uppercase
  micro-label, large tabular figure, inline 7-point SVG sparkline, footer with
  delta chip (up: accent-light; down: coral-light) + context label.
- **Mid-row (2 columns — free width + 320px fixed):**
  - **Left — progress list**: titled card, table of rows showing
    `[entity name + badge] [progress bar with fill pct] [amount A] [amount B] [deadline / status]`.
    Badge variants: active (emerald), ending-soon (amber), paused (slate).
  - **Right — segment / distribution panel**: titled card, inline SVG donut
    chart (4 arcs, gap between arcs, center label showing total + unit),
    legend below (color dot + segment name + count + percentage).
- **Full-width trend chart**: titled card, legend with 2 swatch items, inline
  SVG dual-area chart (two filled polylines, 50% opacity, gridlines in border
  color, x-axis month labels below).
- **Bottom row (free width + 320px fixed):**
  - **Left — records table**: titled card, dense rows of
    `[avatar circle + name] [dimension] [amount] [type pill] [date]`. Sticky
    uppercase header with sort-hint carets. Hover row `#f9fdfb`.
  - **Right — quick-stats list**: titled card, rows of
    `[label + value] [icon chip]` — accent / coral / amber icon chip colors.
- **List screen**: the records-table archetype as its own page — toolbar with
  search input + filter chips (facet label + chip row with counts) + result
  count, the same dense table, footer with result count + pager.
- **Form screen**: sectioned cards of labeled fields; **rules appear as inline
  validation** — required marks (`*`), helper text under the field, inline
  error messages on invalid fields, primary submit disabled-until-valid. No
  rules / checklist / validation-status panel.
- **Detail screen**: breadcrumb + header band (entity ID + status badge + key
  actions) + meta grid (3-col label/value cells) + one or more related-data
  sub-panels (the progress-list row pattern or a mini-table) + activity feed.

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
Domain (illustrative): a nonprofit organization's fundraising operations admin.

Entity switcher  → org: "Bloom Foundation" with program chips (All Programs /
                   Food & Hunger / Education).
Topbar period    → This Month / This Quarter / This Year.
Nav groups       → OVERVIEW (Dashboard, Campaigns), DONORS (Donor List,
                   Segments, Import), FINANCE (Revenue, Grants, Reports),
                   SETTINGS (Team, Integrations).

KPI cards (4):
  • Total Raised — $1.24M · ↑14% vs last quarter · 7-pt sparkline (emerald).
  • Active Donors — 4,821 · ↑9% · 7-pt sparkline (emerald).
  • Active Campaigns — 12 · ↑2 new this quarter · flat sparkline.
  • Recurring Gifts — $38.9k/mo · ↑7% monthly average · sparkline (coral).

Progress list (left mid) → "Active Campaigns" — rows of
  [campaign name + badge (Active/Ending Soon/Paused)]
  [progress bar fill + pct] [raised $] [goal $] [days left].

Segment donut (right mid) → "Donor Segments" — 4 arcs:
  Major Donors ≥$5k (emerald) 148 · 3%
  Mid-Level $500–$4.9k (accent-mid) 812 · 17%
  General <$500 (coral) 3,204 · 66%
  Lapsed >12 mo (amber) 657 · 14%
  Center label: "4,821 / donors".

Trend chart → "Trend — Last 12 Months" + legend (primary series: accent;
  secondary series: coral). Dual area chart, 12 monthly data points.

Records table → "Recent Transactions": donor avatar + name / dimension /
  amount / type pill (Primary / Recurring) / date. 8 rows.

Quick stats (right bottom) → rows: Avg. Transaction / Retention Rate /
  New this period / Lapsed (re-engage) / Active Grants / Pending Pledges.

List screen   → all records, search + filter chips (status, type), paginated.

Form screen   → "New Record": primary code (required), description, quantity
  (required, > 0), dimension select (required), due/close date (required, not
  in the past), priority select. Rules: required marks + helper text + inline
  errors; submit disabled until valid.

Detail screen → one record: breadcrumb + header (ID + status badge + Edit /
  secondary actions) + 3-col meta grid (code / dimension / amount / date /
  owner / created) + related items sub-table + activity feed.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, status states, record columns, form fields + rules, detail
   fields — from the KB + prompt. Standalone: use the Example instantiation
   above.
3. Build each screen in the Visual language + Layout archetype above, imitating
   the example set in `assets/` (dashboard, list, form, detail) and the
   `assets/template.html` seed — with fresh content for the real domain, NOT
   the example labels.
4. Express domain rules as INLINE field validation (required marks, helper text,
   inline errors, disabled-until-valid submit). Never render
   rules / checklist / validation-status / build-note panels or designer/demo
   controls.
5. One inline `<style>`, semantic HTML5, `tabular-nums` on figures, no external
   assets, no CDNs — self-contained.

## Output contract

```
<artifact identifier="admin-bloom-nonprofit" type="text/html" title="Bloom Admin">
<!doctype html>...</artifact>
```
