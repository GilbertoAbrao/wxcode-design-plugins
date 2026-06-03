---
name: admin-vault-treasury
description: |
  Premium dark-mode finance admin aesthetic: deep-navy canvas (#0a0f1e),
  raised navy panels (#121a2e / #1b2640), amber-gold accent (#f59e0b /
  #fbbf24) on a cool-navy neutral ramp, Inter type with tabular-nums on
  every figure, calm green (#34d399) for positive signals and coral red
  (#f87171) for negative, 8–10px radii, 1px #243049 borders. Archetype =
  labeled rail nav (220px, grouped items with active amber left-bar) +
  60px topbar (entity switcher + period tabs + avatar) + 4 KPI cards with
  inline SVG sparklines + 2-column grid (7fr area chart / 5fr allocation
  donut with legend) + full-width records table with +/- colored amounts
  and status pills. Built for calm, high-clarity operational consoles that
  communicate financial magnitude at a glance.
triggers:
  - "deep navy admin"
  - "amber-gold dark admin"
  - "finance ops dark admin"
  - "labeled rail nav dark dashboard"
  - "premium dark-mode admin"
  - "area chart donut dashboard"
  - "cool navy console"
  - "painel escuro navy dourado"
example_prompt: "Apply this deep navy amber-gold admin aesthetic to my domain"
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

# Vault Admin — Visual Archetype

This plugin contributes a **look** (deep navy, amber-gold accent, sparkline
KPI cards, area-chart + donut mid-row, signed-amount records table) and a
**structure** (labeled rail nav + topbar entity/period switcher + KPI row +
2-column chart grid + records table, plus list / form / detail screens).
It does **not** contribute a domain — the subject matter comes from the
Knowledge Base and the user's prompt. Treat the example below as
illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS
custom property; hardcode the cool-navy neutral ramp.

- **Canvas / surfaces:** page `#0a0f1e`; raised panel `#121a2e`; inset /
  hover `#1b2640`; deep hover `#1e2e4a`; hairline border `#243049`.
- **Text ramp:** primary `#e5e9f0`, secondary `#c5cdd7`, muted `#8b97ad`,
  faint `#4e5e7a`.
- **Accent:** `--accent: #f59e0b` (amber-gold), `--accent-hi: #fbbf24`,
  `--accent-dk: #b45309`. Active states, links, accent marks, CTA
  backgrounds.
- **Semantic signals:** `--green: #34d399` (positive / settled), `--red:
  #f87171` (negative / rejected), `--amber: #f59e0b` (pending / warning).
  Each has a pill-background tint at ~12–14% alpha.
- **Donut / chart palette:** 5 named tokens `--slice-1…5` in the amber /
  green / blue / violet / orange family.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
  sans-serif`. Base 14px. `font-variant-numeric: tabular-nums` on **every**
  numeric cell. Micro-labels 10px, uppercase, letter-spacing ~.1em, muted.
  Big KPI figures 26px / weight 700 / letter-spacing -.03em.
- **Density & radius:** 18–20px panel padding, 16px card gaps; panel radius
  10px, control radius 8px, pill radius 20px.
- **Borders & shadows:** 1px hairlines separate surfaces; no drop shadows
  (clean terminal feel). Tinted hover row `#1b2640`.
- **Motion:** subtle only — `.12s` background/border hover transitions.
  Default easing, never bouncy.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Labeled rail nav** (220px fixed, panel bg, 1px right border): brand
  mark + wordmark at top (1px bottom border); scrollable nav body with
  **grouped sections** — each group has a micro-label section header, then
  nav items of `[icon] [label]` with optional numeric badge. Active item:
  amber left-bar (2px) + inset bg + amber-hi text. Bottom slot: bottom-
  border divider, then a user-identity nav item.
- **Top bar** (60px, panel bg, 1px bottom border, sticky):
  **entity switcher** (dot + name + chevron, inset pill) →
  **period selector tabs** (segmented: MTD / QTD / YTD / Custom) →
  flex spacer →
  icon buttons (notification with red dot, search) →
  **avatar group** (gradient circle + name + role sub-line).
- **Main content** (page bg, 24px padding, scrollable vertical flow):
  a **page header** (title + sub-line left, ghost + primary buttons right),
  then the region stack below.
- **KPI card row** (4 tiles, equal grid): each card = panel bg, 1px border,
  10px radius, 3px amber left accent strip. Layout: micro-label → big tabular
  figure → footer row of `[delta chip (▲/▼)] [inline SVG 5-point sparkline]
  [sub text]`. Sparklines use the signal-color of the delta (green/red/amber).
- **2-column grid (7fr / 5fr):**
  - **Left — time-series area chart card:** card-header with title + sub +
    period tab strip (1M / 3M / 6M / YTD); legend row (color dot + label per
    series); inline SVG area chart (gridlines, axis labels, area fills with
    alpha gradient, polyline strokes, data-point dots). Two or three series.
  - **Right — allocation donut card:** card-header title + sub; inline SVG
    donut (background ring + colored segments, rotated from –90°); centered
    total label overlaid; legend rows below of
    `[color dot] [name] [amount] [percent]`, separated by thin borders.
- **Full-width records table card:** card-header with title + sub + "View
  all" link; sticky uppercase header; dense rows with **signed-amount cells**
  (green for positive, red for negative, `tabular-nums`), a date column
  (muted), counterparty / entity name (medium weight), type label (muted),
  right-aligned amount, and status pill; tinted hover; footer with result
  count + pager buttons.
- **Records list screen:** the records-table archetype as its own page —
  search pill + filter chips + count header, same dense table, pager.
- **Record form screen:** sectioned cards of labeled fields; **rules appear
  as inline validation** — required marks (`*`), helper text under the
  field, and inline error messages on invalid fields, primary submit
  disabled-until-valid. No rules/checklist/validation-status panel.
- **Record detail screen:** breadcrumb + header band (ID + status pill +
  key actions), a 3-column meta grid of label/value pairs, and one or more
  related-data sub-panels (a mini-table or status-row list + an activity
  feed) below.

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key
metrics, signal states, record columns and amounts, form fields and their
rules, and detail fields — and map them onto the archetype above. If no
KB/domain is supplied (standalone), use the Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain
rules become inline field validation. Do NOT render build/implementation
notes or designer controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In
> WXCode this is IGNORED — replace every label with the real domain's
> equivalent (entities, metrics, states, columns, fields) drawn from the
> KB + prompt.

```
Domain (illustrative): a corporate treasury management system.

Entity switcher   → entity: "Halcyon Group — HQ".
Period tabs       → MTD / QTD (active) / YTD / Custom.
Rail groups       → Overview (Dashboard, Cash Position, Cashflow) /
                    Transactions (Payments, Transfers, FX & Hedging) /
                    Management (Bank Accounts, Forecasting, Reports).

KPI cards (4):
  • Total Cash Balance $84.7M (▲ +4.2%, green sparkline, "vs prev quarter").
  • Total Inflows $31.2M (▲ +8.6%, green sparkline, "Apr–Jun 2026").
  • Total Outflows $19.8M (▼ +2.1%, red sparkline, "Apr–Jun 2026").
  • Projected Runway 127 d (▲ +9 days, amber sparkline, "at current burn").

Area chart (left) → "Cashflow Analysis" — dual series: Inflows (green) /
  Outflows (red) + Net Position (amber dashed), 6 month labels, area fills.

Donut (right)     → "Cash Allocation" by account / currency:
  USD Operating 45.1% / EUR Hedge 21.9% / GBP Reserves 14.6% /
  JPY Liquidity 11.0% / Other 7.3%; center label "$84.7M Total".

Records table     → "Recent Transactions": Date / Counterparty / Type /
  Amount (+green / –red) / Status pill (Settled / Pending / Rejected).

List screen       → all transactions, search + filter chips (status, type),
  paginated.

Form screen       → "New Payment": counterparty (required), payment type
  (required select), amount (required, > 0), currency (required select),
  value date (required, not in the past), reference / note. Rules shown as
  required marks + helper text + inline errors; "Submit Payment" disabled
  until valid.

Detail screen     → one transaction: breadcrumb + header (ID + status pill
  + actions), meta grid (counterparty, type, amount, currency, date, owner,
  created), and a "Settlement Details" mini-table + activity feed below.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's
   Visual language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary
   entities, key metrics, signal states, record columns, form fields +
   rules, detail fields — from the KB + prompt. Standalone: use the
   Example instantiation above.
3. Build each screen in the Visual language + Layout archetype above,
   imitating the example set in `assets/` (dashboard, list, form, detail)
   and the `assets/template.html` seed — with fresh content for the real
   domain, NOT the example labels.
4. Express domain rules as INLINE field validation (required marks, helper
   text, inline errors, disabled-until-valid submit). Never render
   rules/checklist/validation-status/build-note panels or designer/demo
   controls.
5. One inline `<style>`, semantic HTML5, `tabular-nums` on figures, no
   external assets, no CDNs — self-contained.

## Output contract

```
<artifact identifier="admin-vault-treasury" type="text/html" title="Vault Admin">
<!doctype html>...</artifact>
```
