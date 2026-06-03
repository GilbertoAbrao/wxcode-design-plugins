---
name: admin-slate-commerce
description: |
  Clean light-mode admin aesthetic: warm white canvas (#ffffff / #f9fafb), emerald
  accent (#10b981) for positive states and primary actions, amber (#f59e0b) for
  caution states, Inter type with tabular figures, 10px radii, subtle card shadows,
  and warm slate neutrals. Archetype = fixed sidebar (entity switcher + sectioned nav
  + user footer) + topbar (search + date-range selector + notification bell + avatar)
  + 4 KPI cards with inline sparklines + a metric bar chart + a ranked items panel +
  a full-width records table with status badges. Built for bright, data-dense
  back-office consoles that feel calm and trustworthy at a glance.
triggers:
  - "clean light-mode admin"
  - "warm white admin dashboard"
  - "emerald accent admin"
  - "light admin with sidebar"
  - "calm data-dense back-office"
  - "sparkline KPI cards"
  - "amber emerald admin"
  - "painel admin claro"
example_prompt: "Apply this clean light-mode admin aesthetic to my domain"
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
    requires: [pixel-discipline, typographic-rhythm]
---

# Slate Admin — Visual Archetype

This plugin contributes a **look** (clean light-mode, emerald primary accent, amber
caution, warm neutral surfaces, dense tabular data) and a **structure** (fixed sidebar
with entity switcher + topbar + KPI card row + metric chart + ranked items panel +
records table, plus list / form / detail screens). It does **not** contribute a
domain — the subject matter comes from the Knowledge Base and the user's prompt. Treat
the example below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property.

- **Canvas / surfaces:** page `#f9fafb`; card / panel `#ffffff`; hover row `#f3f4f6`;
  hairline border `#e5e7eb`.
- **Text ramp:** primary `#111827`, secondary `#6b7280`, muted `#9ca3af`.
- **Accent — emerald:** `--accent: #10b981`; light tint `--accent-light: #d1fae5`;
  dark `--accent-dark: #059669`; deep `--accent-deep: #065f46`. Primary CTAs, active
  nav indicator, positive metric figures, progress fills, chart bars.
- **Accent — amber:** `--accent-am: #f59e0b`; light `--accent-am-light: #fef3c7`;
  warn text `--accent-am-warn: #92400e`. Caution states, notification dots, warn
  deltas.
- **Status tokens:** `--badge-success` `#d1fae5` / `#059669`; `--badge-warn`
  `#fef3c7` / `#92400e`; `--badge-neutral` `#f1f5f9` / `#475569`; `--badge-danger`
  `#fee2e2` / `#b91c1c`. Each badge = background + text color pair.
- **Delta chips:** positive on `--accent-light` / `--accent-dark`; negative on
  `--badge-danger`; warn on `--accent-am-light` / `--accent-am-warn`.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`.
  Base 14px. `font-variant-numeric: tabular-nums` on every numeric cell and figure.
  Page titles 18px / weight 700 / `letter-spacing: -.4px`. Big KPI figures 26px /
  weight 800 / `letter-spacing: -.5px`. Column headers 11px / weight 700 /
  `text-transform: uppercase` / `letter-spacing: .5px`. IDs in a mono face
  (`"Courier New", monospace`).
- **Density & radius:** sidebar 240px fixed; topbar 60px; KPI cards 18px padding;
  table rows 12px vertical padding; card radius 10px; control radius 6px; badge
  radius 20px.
- **Borders & shadows:** 1px `#e5e7eb` hairlines; card shadow
  `0 1px 3px rgba(0,0,0,.07), 0 1px 2px rgba(0,0,0,.04)`. No heavy drop shadows.
- **Sparklines:** inline SVG polyline + area-fill at 10% opacity; 56×28 px viewport;
  emerald for positive trend, danger red for downward KPIs.
- **Motion:** `.1s–.15s` background/color hover transitions. Never bouncy.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Fixed sidebar** (240px, card bg, 1px right border): brand mark + name at top →
  **entity switcher** (border-box with label + sub-label + chevron) → sectioned nav
  groups (section micro-label + nav items: icon + label + optional badge) → user
  footer (avatar + name/role + logout icon) pinned at the bottom.
- **Topbar** (60px, card bg, 1px bottom border): page title on the left → flexible
  spacer → **search pill** (icon + input) → **range selector** (calendar icon + label
  + chevron) → **notification button** (bell + amber dot) → avatar ring.
- **Main content** (page bg, 24px padding, vertical flow):
  - **KPI card row** (4 equal cards): each = label row (uppercase label + sparkline
    SVG) + big tabular figure + delta chip + sub-line. Card bg, 10px radius, subtle
    shadow.
  - **Two-column grid (1fr / 320px):**
    - **Left — metric bar chart:** titled card with a legend, inline SVG bar chart
      (12 bars with Y-axis labels, current period highlighted in accent, prior
      period muted, future bars in `#e2e8f0`), tooltip bubble on the active bar.
    - **Right — ranked items panel:** titled card with rows of `[thumb] [name +
      sub-label] [bar fill] [metric figure]`. Progress bar 5px tall.
  - **Full-width records table:** titled card with header action link, sticky
    uppercase header, dense rows with avatar chip + name, mono ID column, right-
    aligned numerics, status badges, and row hover. Footer with pager when needed.
- **Records list screen:** the records-table archetype as its own page — search +
  filter chips + result count, same dense table, pager.
- **Record form screen:** sectioned cards of labelled fields; **rules appear as
  inline validation** — required marks (`*`), helper text under the field, and
  inline error messages on invalid fields, with the primary submit disabled-until-valid.
  No rules/checklist/validation-status panel.
- **Record detail screen:** a header band (title + status badge + key actions), a
  meta grid of label/value pairs (3 columns), and one or more related-data sub-panels
  (ranked rows or a mini-table) below.

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS domain's
equivalent of the archetype slots — its primary entities, key metrics, status states,
record list/columns, form fields and their rules, and detail fields — and map them
onto the archetype above. If no KB/domain is supplied (standalone), use the Example
instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules
become inline field validation. Do NOT render build/implementation notes or designer
controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent
> (entities, metrics, states, columns, fields) drawn from the KB + prompt.

```
Domain (illustrative): a retail back-office managing stores, orders, and products.

Entity switcher  → store: "Harborview Goods · harborviewgoods.com".
Topbar range     → "May 1 – May 31, 2025".
Nav sections     → Main (Dashboard, Orders [badge 14], Products, Customers)
                   Insights (Analytics, Reports) · System (Settings).

KPI cards (4):
  • Revenue $84,320 (↑ 12.4% vs Apr, emerald sparkline).
  • Orders 1,247 (↑ 8.1%, emerald sparkline).
  • Avg Order Value $67.62 (↑ 3.9%, amber sparkline, warn chip).
  • Refunds $3,180 (↑ 2.3%, danger sparkline, negative chip).

Metric bar chart → "Monthly Revenue Jan–Dec 2025 · USD"; May bar highlighted
  emerald, prior-year bars in accent-light, future bars in #e2e8f0. Tooltip: "$84,320".

Ranked items panel → "Top Products" — rows of
  [colored-shape thumb] [product name · SKU] [progress bar] [revenue].
  Top 5 items with revenue figures.

Records table → "Recent Orders": Order # (mono, emerald) / Customer (avatar + name) /
  Date / Items / Amount (tabular) / Status badge (Delivered emerald, Processing
  amber, Pending slate, Refunded rose).

List screen      → all records, search + filter chips (by status), paginated,
  same table columns.

Form screen      → "New Order": customer (required select), date (required),
  items (required, ≥ 1), shipping address (required), notes. Rules shown as
  required marks + helper text + inline errors; "Create Order" disabled until valid.

Detail screen    → one record: header (ID + status badge + actions), meta grid
  (customer, date, items, amount, shipping, created), and a line-items sub-table +
  activity feed.
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
<artifact identifier="admin-slate-commerce" type="text/html" title="Slate Admin">
<!doctype html>...</artifact>
```
