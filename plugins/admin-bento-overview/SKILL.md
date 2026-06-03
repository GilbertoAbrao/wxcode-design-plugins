---
name: admin-bento-overview
description: |
  Light-mode bento-grid admin aesthetic: neutral canvas (#f6f7f9), white tiles,
  hairline borders (#e8eaee), and a multi-accent palette — indigo (#6366f1),
  teal (#14b8a6), amber (#f59e0b), rose (#f43f5e) — each assigned to a tile or
  component role. Archetype = sticky header (brand mark + period chips + avatar)
  + headerless full-width CSS grid of asymmetrically-spanned tiles: hero metric
  tile (large numeral + sparkline), area-chart tile, KPI pills, activity feed,
  donut chart, mini-table, and system-status tile. No sidebar. Built for
  at-a-glance operational overviews that need visual hierarchy through tile
  proportions, not navigation depth.
triggers:
  - "bento grid dashboard"
  - "bento ops"
  - "mosaic dashboard"
  - "asymmetric dashboard"
  - "light-mode bento admin"
  - "multi-accent tile dashboard"
  - "indigo teal amber rose admin"
  - "ops home screen"
  - "painel bento claro"
  - "モザイクダッシュボード"
example_prompt: "Apply this light bento-grid admin aesthetic to my domain"
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

# Bento Overview — Visual Archetype

This plugin contributes a **look** (light neutral canvas, multi-accent bento
tiles, asymmetric grid proportions) and a **structure** (sticky header + full-
width bento grid + list / form / detail screens). It does **not** contribute a
domain — the subject matter comes from the Knowledge Base and the user's prompt.
Treat the example below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property; hardcode the neutral light ramp.

- **Canvas / surfaces:** page `#f6f7f9`; tile background `#ffffff`; header
  `#ffffff`; hairline border `#e8eaee`; hover tint `#f8fafc`; muted row
  divider `#f1f5f9`.
- **Text ramp:** primary `#1e293b`, body `#334155`, secondary `#64748b`,
  muted `#94a3b8`.
- **Multi-accent tokens:**
  - `--c-indigo: #6366f1` / `--c-indigo-d: #4f46e5` / `--c-indigo-lt: #eef2ff`
  - `--c-teal: #14b8a6` / `--c-teal-d: #0d9488` / `--c-teal-lt: #f0fdfa`
  - `--c-amber: #f59e0b` / `--c-amber-d: #d97706` / `--c-amber-lt: #fffbeb`
  - `--c-rose: #f43f5e` / `--c-rose-d: #e11d48` / `--c-rose-lt: #fff1f2`
  - `--c-green: #22c55e` / `--c-green-lt: #f0fdf4`
  All chromatic fills and strokes in inline SVG use `var(--c-*)` or
  `currentColor`. No hex literals for chromatic values outside the `:root` block.
- **Accent role assignment:** indigo → hero tile accent strip, period-chip
  active state, "view all" links; teal → chart axis/fill, activity-feed border,
  chart-tab active; amber → KPI tile icon / mini-table header left border;
  rose → KPI tile icon / status-tile border when degraded.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`.
  No external font loads. Base 14px / line-height 1.5. Tile micro-labels 10–11px
  uppercase, `letter-spacing: 0.07em`, muted. Hero figure 42px / weight 800 /
  `letter-spacing: −0.04em`. KPI values 26px / weight 800. `font-variant-numeric:
  tabular-nums` on every numeric cell.
- **Density & radius:** tile border-radius 14px; control radius 6–8px; pill
  radius 20px; tile padding 18–20px; grid gap 14px; header height 52px.
- **Borders & shadows:** 1px hairlines only — no drop-shadows on tiles. Teal
  top border (3px) on activity tile; rose top border (3px) on status tile when
  degraded.
- **Delta chips:** up = green-lt background / #16a34a text; down = rose-lt
  background / rose-d text.
- **Motion:** `.15s` background/border hover transitions. No bouncy easing.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Sticky header** (52px, white, 1px bottom border): brand SVG monogram +
  wordmark → period selector chips (Today / 7D / 30D / Custom; active chip
  filled indigo) → flex spacer → timestamp or sub-label → notification icon
  button (with rose dot when active) → avatar circle. No sidebar.
- **Bento grid** (`display: grid; grid-template-columns: repeat(12, 1fr);
  grid-auto-rows: 88px; gap: 14px; padding: 20px 24px`). Tile spans are the
  visual hierarchy; vary them deliberately:
  - **Hero tile** (col-span 5, row-span 2): dominant metric — large numeral,
    hero-sub copy, delta chip, inline SVG sparkline. Indigo gradient left-edge
    accent strip (5px, absolutely positioned).
  - **Chart tile** (col-span 7, row-span 3): title + period tabs, inline SVG
    area chart with grid lines, axis labels, area fill. Teal axis and fill.
  - **KPI tile × 2** (col-span 3–4, row-span 1 each): micro-label + large
    value + delta chip + icon chip. One amber-accented, one rose-accented.
  - **Activity feed tile** (col-span 5, row-span 3): title + list of 5–6
    timestamped events, each with a severity dot (green / amber / rose / teal)
    + description + elapsed time. Teal 3px top border.
  - **Donut tile** (col-span 4, row-span 3): title + centered inline SVG donut
    (3–4 slices, center label) + 2-column legend with swatches and values.
    Indigo / teal / amber slices.
  - **Mini-table tile** (col-span 6–8, row-span 3): title + "View all" link +
    `<table>` with uppercase header row (light-slate bg, amber left border),
    5 dense rows (entity name, dimension, numeric value, status pill), no
    outer border.
  - **Status tile** (col-span 3–4, row-span 1–2): title + 4 service rows
    (`[dot] [name] [uptime %]`). Rose 3px top border if any service is degraded.
- **List screen:** header (title + "New" button), toolbar (search pill + filter
  chips with counts), full-width tile holding a `<table>` (same column pattern
  as mini-table but full list) + pager footer.
- **Form screen:** header (breadcrumb + title + cancel/save), sectioned tiles
  holding labelled fields in a 2-col grid. **Rules as inline validation only:**
  required mark (`*`), helper text under each field, inline error on invalid
  fields, submit disabled until valid. No rules panel.
- **Detail screen:** breadcrumb + detail header (title + status pill + edit
  button) + meta grid tile (3-col label/value cells) + related-data tile (a
  compact table or activity feed pattern).

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key metrics,
status states, record columns, form fields and their rules, and detail fields —
and map them onto the archetype above. If no KB/domain is supplied (standalone),
use the Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules
become inline field validation. Do NOT render build/implementation notes or
designer controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent
> (entities, metrics, states, columns, fields) drawn from the KB + prompt.

```
Domain (illustrative): a SaaS platform operational overview for a logistics company.

Header          → brand monogram "LX" + wordmark "Lumex Ops"; period chips Today /
                  7D (active) / 30D / Custom; avatar "PN" (Priya Nair).

Hero tile       → "Shipments Dispatched" — 8,241 (past 7 days); +14.2% vs last week;
                  sparkline trending upward. Indigo accent strip.

Chart tile      → "Delivery Volume" — area chart (Mon–Sun); series: On Time (teal),
                  Delayed (amber); period tabs 24H / 7D (active) / 30D / YTD.

KPI tiles (2):
  • Avg Transit Time 2.4 d (amber icon, ▲−0.3d improvement).
  • Exception Rate   1.8% (rose icon, ▼+0.2pp degradation).

Activity feed   → "Recent Events" — 6 timestamped events:
  success: Route LX-904 optimised, saving 37 km — 4 min ago.
  warn:    Carrier APEX-3 reported 2-hour delay on EMEA corridor — 22 min ago.
  info:    New carrier Brightline activated, webhook verified — 1 hr ago.
  error:   48 manifests failed customs validation — Incident #5812 open — 1 hr ago.
  success: Nightly warehouse sync completed (12 sites, 3 min 41 s) — 4 hr ago.
  info:    Priya Nair added Elena Sorokina to on-call rotation — 6 hr ago.
  Teal top border.

Donut tile      → "Channel Mix" — Web 46% (indigo), Mobile 30% (teal),
                  Partner API 15% (amber), In-store 9% (rose); centre label "8,241".

Mini-table tile → "Top Routes by Volume" — 5 rows:
  Route / Origin-Dest / Volume (7D) / On-time % / Status pill (Active /
  Scaling / Watch / At risk).

Status tile     → "Platform Health" — 4 services:
  API Gateway 99.97% (ok), Manifest Processor 99.84% (ok),
  Customs Connector 96.10% (warn), EMEA Router 83.40% (error).
  Rose top border (degraded service present).

List screen     → "All Shipments" — search + filter chips (status, carrier, region);
  columns: Shipment ID / Carrier / Origin / Destination / ETA / Status pill.
  Pager.

Form screen     → "New Shipment": origin hub (required select), destination hub
  (required select), carrier (required select), cargo type (required), weight kg
  (required, > 0), scheduled pickup (required, not in the past), priority. Rules as
  inline validation; "Create Shipment" disabled until valid.

Detail screen   → one shipment: breadcrumb "Shipments › LX-00842"; header (LX-00842
  + "In Transit" pill + Edit button); meta grid (carrier, origin, destination,
  weight, ETA, owner, created); related tile "Route Events" (compact activity feed).
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
5. One inline `<style>`, semantic HTML5, `tabular-nums` on figures, no external
   assets, no CDNs — self-contained.

## Output contract

```
<artifact identifier="admin-bento-overview" type="text/html" title="Bento Overview">
<!doctype html>...</artifact>
```
