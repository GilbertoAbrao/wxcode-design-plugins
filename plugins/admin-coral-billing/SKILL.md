---
name: admin-coral-billing
description: |
  Clean light-mode SaaS admin aesthetic: white/near-white canvas (#f8f9fb), coral
  accent (#f43f5e / #fb7185) for urgency and primary actions, slate-blue neutrals
  (#475569) for navigation, soft-shadow cards with subtle 1px borders, and
  tabular-nums on every figure. Archetype = fixed left sidebar (logo + workspace
  switcher + grouped icon-nav) + sticky topbar (search pill + period tabs + avatar)
  + 4 KPI cards + 2-column mid-row (area-chart card + horizontal bar-chart card) +
  2-column bottom row (records table + items-at-risk side panel). Built for
  high-legibility operational consoles on light displays.
triggers:
  - "coral accent admin"
  - "clean light-mode admin"
  - "light SaaS dashboard"
  - "white card admin"
  - "pink-coral accent dashboard"
  - "slate sidebar admin"
  - "soft-shadow card layout"
  - "painel claro com destaque coral"
example_prompt: "Apply this clean coral-accent light-mode admin aesthetic to my domain"
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

# Coral Admin — Visual Archetype

This plugin contributes a **look** (clean light canvas, coral accent, slate-blue
navigation, soft-shadow cards, tabular figures) and a **structure** (fixed sidebar
+ topbar + KPI cards + area-chart + bar-chart + records table + side panel, plus
list / form / detail screens). It does **not** contribute a domain — the subject
matter comes from the Knowledge Base and the user's prompt. Treat the example below
as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property.

- **Canvas / surfaces:** page `#f8f9fb`; card / sidebar / topbar `#ffffff`; hover
  row `#f8f9fb`; border / divider `#e6e9ef`.
- **Text ramp:** primary `#111827`; body `#374151`; secondary `#6b7280`; muted
  `#9ca3af`. Neutral hardcoded values `#111827`, `#374151`, `#6b7280`, `#9ca3af`,
  `#f3f4f6` may appear directly in CSS.
- **Accent:** `--coral: #f43f5e`; `--coral-light: #fb7185`; `--coral-muted: #fff1f2`.
  Primary CTAs, active nav, count badges, chart strokes, form focus rings.
- **Nav neutral:** `--slate: #475569`; `--slate-light: #64748b`. Sidebar headings,
  secondary labels.
- **Status ramp (as tokens):** `--green: #16a34a`, `--green-muted: #f0fdf4`
  (positive / paid); `--amber: #d97706`, `--amber-muted: #fffbeb` (warning /
  pending); `--red: #dc2626`, `--red-muted: #fef2f2` (negative / failed / at-risk).
  Delta chips reuse these pairs.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`.
  Base 14px. `font-variant-numeric: tabular-nums` on **every** numeric cell and KPI
  figure. Micro-labels 10–11px, uppercase, `letter-spacing: .06–.08em`, muted.
  Section labels: 10px, uppercase, `letter-spacing: .08em`, `#9ca3af`. KPI values:
  24px / weight 700.
- **Density & radius:** nav items 36px tall, 8px radius; KPI cards 12px radius,
  20px padding; table rows 12px vertical cell padding; control height 34px; 6–8px
  control radius; pill radius 20px.
- **Borders & shadows:** 1px solid `var(--border)` on cards; `box-shadow: 0 1px 4px
  rgba(0,0,0,.05)` on cards (no heavy drops); 1px row dividers.
- **Motion:** `.10s–.15s` background/border hover transitions; gentle easing.
  Never bouncy.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns described by shape and behavior — not meaning.

- **Fixed left sidebar** (240px, card bg, 1px right border, full height): top logo
  mark + product name → **workspace switcher pill** (entity name + chevron, 8px
  radius, 32px tall) → grouped nav sections: each section has an uppercase 10px
  micro-label followed by 36px nav items (icon 16px + label 13px + optional count
  badge), active item = `var(--coral-muted)` bg + left 3px bar + coral label/icon,
  hover = surface bg. Bottom: user avatar row pinned at the bottom with a 1px
  top-border separator.
- **Sticky topbar** (56px, card bg, 1px bottom border): left search pill (260px,
  inline SVG magnifier inside, 8px radius) → center-right **period selector tabs**
  (flush `border-bottom: 2px` active indicator, coral when active) → right icon
  cluster: notification bell with coral dot + user avatar button.
- **Main content** (surface bg, 24px padding, vertical scroll): a **page heading**
  strip (title 20px + context badge left; ghost + primary buttons right), then the
  region stack below.
- **4 KPI cards** (equal 4-column grid, 14px gap): each card = white panel, 12px
  radius, 20px padding, soft shadow. Contents: uppercase micro-label → big tabular
  figure + inline sparkline SVG (80×32, 1.5px coral-light stroke) → footer row:
  delta chip (green/red background tint) + sub-text. No icon chips; accent on figure
  not icon.
- **Mid 2-column row (3fr / 2fr gap 14px):**
  - **Left — trend chart card:** title + subtitle + period toggle tabs (pill chips,
    active = coral-muted bg + coral text), then an inline SVG area chart (full card
    width, gradient fill from coral-light α18% to transparent, 2px coral stroke, 6
    hairline grid-lines `#e6e9ef`, x-axis category labels, y-axis scale labels).
  - **Right — breakdown bar chart card:** title + subtitle, then horizontal bars:
    each row = category label left / value + % right, a 4px-high bar track (`#f3f4f6`)
    with a colored fill, coral / coral-light / accent-variant / neutral for the four
    bars. Optional legend chips below.
- **Bottom 2-column row (3fr / 2fr gap 14px):**
  - **Left — records table card:** titled panel with count badge + "View All" link,
    a sticky uppercase header, dense rows with **status pills** (paid/pending/failed),
    a mono ID column, hover row highlight, footer: result count + pager
    (page buttons, active = coral bg white text).
  - **Right — items-at-risk panel:** titled panel with a count badge in red-muted,
    a subtitle, then item cards (avatar initials chip + name/tier + amount/elapsed
    row + two action buttons: ghost coral-border "Retry" + muted text "Write Off"),
    footer text summarizing total count and exposure metric.
- **Records list screen:** the records-table archetype as its own page — search pill
  + filter chips (with count badges) in a toolbar, the same dense table, and a
  pager below.
- **Record form screen:** white card sections, each section has an uppercase 10px
  section title with a small accent glyph; a field-grid (1fr 1fr, `.full` spans
  both). **Rules appear as inline validation** — required marks (`*` coral), helper
  text under the field, inline error message on invalid fields (`--red` text, 1px
  red border), submit disabled until valid. No rules/checklist/validation-status panel.
- **Record detail screen:** breadcrumb → header band (entity ID + status pill +
  action buttons) → meta grid (3-column label/value cells in a white card) → one
  or more related-data sub-panels (mini-table or item rows) below.

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS domain's
equivalent of the archetype slots — its primary entities, key metrics, period
dimensions, status states, record columns, form fields and their rules, and detail
fields — and map them onto the archetype above. If no KB/domain is supplied
(standalone), use the Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules
become inline field validation. Do NOT render build/implementation notes or
designer controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent
> (entities, metrics, period dimensions, states, columns, fields) drawn from the
> KB + prompt.

```
Domain (illustrative): a SaaS subscription and invoicing operations desk.

Workspace switcher  → "Nexum Corp" + chevron.
Live status         → period selector "This Month / Last Month / Q2 / YTD" in topbar.
Sidebar sections    → OVERVIEW (Dashboard, Revenue, Invoices ●12, Subscriptions);
                      BILLING (Plans, Coupons, Tax Rates);
                      SETTINGS (Team, Integrations, Billing Keys).

KPI cards (4):
  • Monthly Recurring Revenue  $148,320 · +8.4% · "vs prior period"
  • Active Subscriptions       2,847    · +124  · "new this period"
  • Monthly Churn Rate         1.9%     · −0.3pp · "improving"
  • Avg Revenue Per User       $52.10   · +2.1%  · "vs prior period"

Mid row left   → "Revenue Trend" area chart — period tabs 6M | 12M | YTD,
                 12-point polyline from $108k to $148k with gradient fill.
Mid row right  → "Revenue by Tier" horizontal bars — Enterprise 50%, Growth 30%,
                 Starter 15%, Free 5%.

Records table  → "Recent Invoices": Invoice # | Customer | Tier | Amount | Due Date
                 | Status pill (Paid / Pending / Failed). 7 rows + pagination.

Items-at-risk panel → "Recovery Queue · 8 at risk" — 5 item cards with customer
  name, tier, amount, days overdue, "Retry Now" + "Write Off" actions.
  Footer: "8 items at risk · $3,240 ARR exposure".

List screen    → all invoices: search pill + filter chips (status, tier),
                 paginated records table.

Form screen    → "New Invoice": entity/customer (required select), tier plan
  (required select), amount (required, > 0), due date (required, not past),
  billing cycle (required), notes. Rules shown as required marks + helper text +
  inline errors; "Create Invoice" disabled until valid.

Detail screen  → one invoice: breadcrumb → header (invoice # + status pill +
  actions), meta grid (customer, plan, amount, due date, issued by, created),
  and a "Line Items" mini-table + activity feed sub-panels.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities, key
   metrics, period dimensions, status states, record columns, form fields + rules,
   detail fields — from the KB + prompt. Standalone: use the Example instantiation
   above.
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
<artifact identifier="admin-coral-billing" type="text/html" title="Coral Admin">
<!doctype html>...</artifact>
```
