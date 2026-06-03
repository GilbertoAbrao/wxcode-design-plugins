---
name: admin-ember-campaigns
description: |
  Vibrant-but-clean light-mode admin aesthetic: white/#fafafa canvas, rose-pink
  accent (#e11d48 / #ec4899) on a slate neutral ramp, secondary indigo (#4f46e5)
  for chart contrast, border #ececf0. Left sidebar (240px) with brand icon + nav
  sections + footer cluster, sticky topbar with search + date-range button + bell
  + avatar, 4 KPI cards with inline SVG sparklines + delta chips, a 7/5 split
  middle row (multi-series SVG line chart + conversion funnel bars), and a
  full-width records table with channel chips and status pills. Built for clean,
  modern analytics consoles with vibrant accent hits on a white canvas.
triggers:
  - "vibrant light-mode admin"
  - "rose-pink admin dashboard"
  - "sidebar analytics admin"
  - "clean funnel dashboard"
  - "sparkline KPI cards"
  - "modern analytics console"
  - "white canvas admin panel"
  - "painel admin vibrante"
example_prompt: "Apply this vibrant rose-accent light-mode admin aesthetic to my domain"
od:
  mode: prototype
  surface: web
  scenario: analytics
  preview:
    type: html
    entry: example.html
  design_system:
    requires: true
    sections: [color, typography, layout, components]
  craft:
    requires: [pixel-discipline, laws-of-ux]
---

# Ember Admin — Visual Archetype

This plugin contributes a **look** (vibrant-but-clean, rose-pink accent, white
canvas, slate neutrals) and a **structure** (left sidebar with nav sections +
brand + footer, sticky topbar, KPI card row with sparklines, 7/5 chart/funnel
split, full-width records table with typed chips and status pills). It does
**not** contribute a domain — the subject matter comes from the Knowledge Base
and the user's prompt. Treat the example below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. All chromatic values as `:root` CSS custom properties.

- **Canvas / surfaces:** page `#fafafa`; cards/sidebar `#ffffff`; border
  `#ececf0`; light hover `#f8fafc`; accent-tinted hover `#fff7f8`.
- **Text ramp:** primary `#0f172a`, secondary `#334155`, muted `#64748b`, faint
  `#94a3b8`.
- **Accent ramp:** `--color-accent: #e11d48` (rose-600), `--color-accent-soft:
  #ec4899` (pink-500), `--color-accent-bg: #fff1f5`. Primary CTAs, active nav
  border, key figures, sparkline strokes, button fills.
- **Secondary accent:** `--color-indigo: #4f46e5`, `--color-indigo-soft:
  #6366f1`, `--color-indigo-bg: #eef2ff`. Chart series 2 and typed-chip fills.
- **Tertiary accent:** `--color-sky: #0ea5e9`, `--color-sky-bg: #f0f9ff`.
  Chart series 3 and typed-chip fills.
- **Amber accent:** `--color-amber: #d97706`, `--color-amber-bg: #fffbeb`.
  Typed chips and "paused" state.
- **Semantic states:** `--color-success: #16a34a` / `--color-success-bg:
  #f0fdf4`; `--color-warning: #d97706` / `--color-warning-bg: #fffbeb`;
  `--color-danger: #dc2626` / `--color-danger-bg: #fef2f2`. Delta chips,
  status pills, funnel connectors.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
  sans-serif`. Base 14px. `font-variant-numeric: tabular-nums` on **every**
  numeric cell. KPI values 26–28px / weight 800 / `letter-spacing: -.5px`.
  Micro-labels 10–10.5px / uppercase / `letter-spacing: .65px` / muted.
- **Density & radius:** 12px card radius, 8px control radius, 20px pill radius;
  8px gaps within cells, 16–24px content padding, 16px grid gaps.
- **Borders & shadows:** 1px `#ececf0` borders on cards and sidebar; subtle
  `box-shadow: 0 2px 8px rgba(0,0,0,.04)` on cards. No heavy elevation.
- **Motion:** `.15s` background/color hover transitions; `.3s` width transitions
  on funnel bars. Ease-out only; never bouncy.
- **Buttons:** primary = rose gradient (`#e11d48 → #ec4899`), white text,
  radius 8px; ghost = white bg, `#ececf0` border, slate text, rose on hover.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns described by shape — not meaning.

- **Left sidebar** (240px fixed, white, 1px right border, full-height flex
  column): **brand strip** (icon chip + wordmark + tagline), **nav** (grouped
  sections each with an uppercase micro-label + nav items carrying icon + label
  + optional count badge; active item gets rose left-border + accent-bg +
  accent text), **footer cluster** (avatar + name/role + full-width CTA button).
- **Sticky topbar** (60px, white, 1px bottom border): page title + breadcrumb
  → flex spacer → **search pill** (icon + input) → **date-range button**
  (calendar icon + label) → **bell icon** (with notification dot) → **avatar
  chip**.
- **Main content** (page bg, 24px padding, flex-column gap 24px): **page
  header** (H1 + sub-line left; ghost + primary buttons right), then region
  stack.
- **KPI card row** (4 equal cards): each card = white panel with an uppercase
  micro-label, a big tabular figure, a 52×26 inline SVG sparkline (polyline +
  area fill), and a delta chip (arrow + ±% in a tinted pill) + period label.
- **7/5 split middle row:**
  - **Left (7) — multi-series line chart:** white panel with card header
    (title + legend chips), inline SVG with gridlines, y-axis labels, x-axis
    labels, 3 polyline series + area fills in accent / indigo / sky; data dots
    on peaks.
  - **Right (5) — conversion funnel:** white panel, stacked funnel rows each
    with `[step label] [count]` meta row + a proportionally-wide fill bar
    (gradient-colored by step order), connector lines showing drop-off %;
    aggregate rate summary chip at the foot.
- **Full-width records table:** white panel with card header (title + sub-line
  left; view-all link + primary button right), sticky uppercase header,
  dense tbody rows with 1px dividers, tinted hover, and per-row **channel
  chip** (indigo/rose/sky/amber by type) + **status pill** (green/amber/red);
  a two-line name/desc cell and right-aligned tabular numerics.
- **List screen:** records-table archetype as its own page — toolbar with
  search + filter chips + count, same dense table, footer pager.
- **Form screen:** sectioned cards of labelled fields; **rules as inline
  validation** — required marks (`*`), helper text under the field, inline
  error messages on invalid fields; primary submit disabled-until-valid. No
  rules/checklist/validation-status panel.
- **Detail screen:** breadcrumb + header band (title + status pill + key
  actions), meta grid of label/value pairs, one or more related-data sub-panels
  (funnel/performance rows or a mini-table) below.

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
Domain (illustrative): a digital marketing campaign management platform.

Sidebar brand    → flame icon chip + "Ember" wordmark + "Campaigns" tagline.
Nav sections     → Overview (Dashboard, Analytics), Campaigns (All Campaigns,
                   Audiences, Creatives), Reports (Performance, Attribution,
                   Export), Settings (Integrations, Team).
Active item      → "All Campaigns" with badge "8".
Footer cluster   → avatar "SM" + "Sofia Morales / Marketing Lead" + "Upgrade
                   to Pro" CTA button.

Topbar           → page title "Campaigns" + breadcrumb Home › Campaigns;
                   search "Search campaigns…"; date-range "May 1 – May 31, 2026".

KPI tiles (4):
  • Total Reach 4.2M (▲+12.4%, "vs last month").
  • Avg. CTR 3.81% (▲+0.6pp).
  • Total Spend $84.3K (▼−$3.1K).
  • ROAS 5.2× (▲+0.4×).

Middle left — "Campaign Performance" SVG chart (3 series: Impressions /
  Clicks / Conversions; legend chips in rose / indigo / sky; week x-axis).

Middle right — "Conversion Funnel" (4 steps: Impressions → Clicks → Leads →
  Customers; each step = meta row + fill bar; drop-off connector; overall
  conversion rate chip at foot).

Records table    → "Active Campaigns": Name/desc | Channel chip (Paid
  Search/Social/Email/Display) | Impressions | Clicks | Spend | Status pill
  (Live/Paused/Ended). 8 rows of invented copy.

List screen      → all campaigns, search + filter chips (channel, status),
  paginated.

Form screen      → "New Campaign": name (required), channel (required select),
  objective (required select), budget (required, > 0), start date (required),
  end date (required, after start), target audience (helper text). Rules shown
  as required marks + helper text + inline errors; "Create Campaign" disabled
  until valid.

Detail screen    → one campaign: breadcrumb + header (campaign name + status
  pill + "Edit" + "Pause" actions), meta grid (channel, objective, budget,
  start, end, owner, created), "Performance" mini-chart + "Recent Activity"
  timeline.
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
4. Express domain rules as INLINE field validation (required marks, helper
   text, inline errors, disabled-until-valid submit). Never render
   rules/checklist/validation-status/build-note panels or designer/demo
   controls.
5. One inline `<style>`, semantic HTML5, `tabular-nums` on figures, no external
   assets, no CDNs — self-contained.

## Output contract

```
<artifact identifier="admin-ember-campaigns" type="text/html" title="Ember Admin">
<!doctype html>...</artifact>
```
