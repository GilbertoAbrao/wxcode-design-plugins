---
name: admin-coral-billing
description: |
  Clean-fintech SaaS billing operations dashboard: coral accent
  (#f43f5e / #fb7185) on white/#f8f9fb surfaces, slate-blue nav
  (#475569), left sidebar with workspace switcher + grouped nav,
  topbar with global search + period selector + avatar, 4 KPI cards
  (MRR / active subscriptions / churn rate / ARPU), inline SVG
  revenue/MRR trend chart, plan-breakdown bar chart, paginated
  invoices table with status pills, and a dunning/failed-payments
  side panel. Choose this archetype when the brief mentions billing,
  subscriptions, invoices, revenue ops, or payment recovery.
triggers:
  - "billing dashboard"
  - "subscription admin"
  - "invoice management"
  - "revenue operations"
  - "MRR dashboard"
  - "dunning panel"
  - "failed payments"
  - "SaaS billing"
  - "coral fintech"
  - "painel de faturamento"
  - "账单管理后台"
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
  example_prompt: "Build me a billing admin dashboard for a SaaS product — left sidebar, topbar with period picker, MRR and subscription KPIs, revenue trend chart, plan breakdown, invoices table with status pills, failed-payment dunning panel."
---

# Coral Billing Admin Skill

Produce a clean-fintech billing operations dashboard. Coral accent
conveys urgency for failed-payment states; slate-blue grounds
navigation. Every money figure uses tabular-nums so columns align.

## Design tokens (always emit as :root custom properties)

```
--coral:        #f43f5e   /* primary accent, buttons, active states */
--coral-light:  #fb7185   /* hover, tints, chart fill */
--coral-muted:  #fff1f2   /* accent chip backgrounds */
--slate:        #475569   /* sidebar nav labels, headings */
--slate-light:  #64748b   /* secondary text */
--green:        #16a34a   /* paid status, positive delta */
--green-muted:  #f0fdf4   /* paid pill bg */
--amber:        #d97706   /* pending status, warning */
--amber-muted:  #fffbeb   /* pending pill bg */
--red:          #dc2626   /* failed status, dunning */
--red-muted:    #fef2f2   /* failed pill bg */
--surface:      #f8f9fb   /* page background */
--card:         #ffffff   /* card, sidebar, topbar backgrounds */
--border:       #e6e9ef   /* dividers, card borders */
```

Chromatic hex literals MUST NOT appear in CSS rules or inline SVG
fill/stroke attributes. Use var(--token) or currentColor everywhere.
Neutrals (#111827, #374151, #6b7280, #9ca3af, #f3f4f6) may be
hardcoded. White (#ffffff) and #f8f9fb may be hardcoded.

## Fonts

Inline system stack only — no @import, no Google Fonts:
```css
font-family: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
```
Money and numeric columns: `font-variant-numeric: tabular-nums;`

## Layout

```
┌─────────────────────────────────────────────────────────────────┐
│  Sidebar 240px  │  Main area                                     │
│                 │  ┌─────────────────────────────────────────┐  │
│  [logo + name]  │  │ Topbar 56px (search | period | avatar)  │  │
│  ─────────────  │  └─────────────────────────────────────────┘  │
│  WORKSPACE      │  ┌─────────────────────────────────────────┐  │
│  switcher pill  │  │ Page heading + period badge + actions   │  │
│                 │  └─────────────────────────────────────────┘  │
│  OVERVIEW       │  ┌──────┬──────┬──────┬──────┐               │
│  • Dashboard    │  │ MRR  │ Subs │Churn │ ARPU │  (4 KPI cards)│
│  • Revenue      │  └──────┴──────┴──────┴──────┘               │
│  • Invoices ●   │  ┌────────────────────┬────────────────────┐  │
│  • Subscriptions│  │ MRR Trend (SVG)    │ Plan Breakdown     │  │
│                 │  │                    │ (bar chart SVG)    │  │
│  BILLING        │  └────────────────────┴────────────────────┘  │
│  • Plans        │  ┌─────────────────────────────┬──────────┐   │
│  • Coupons      │  │ Invoices Table              │ Dunning  │   │
│  • Tax Rates    │  │ (7 rows + pagination)       │ Panel    │   │
│                 │  └─────────────────────────────┴──────────┘   │
│  SETTINGS       │                                                │
│  • Team         │                                                │
│  • Integrations │                                                │
│  • Billing Keys │                                                │
└─────────────────┴────────────────────────────────────────────────┘
```

### Sidebar (240 px, fixed)
- Background: var(--card). Right border: 1px solid var(--border).
- Top: 20px padding. Logo mark (inline SVG coral diamond) + product
  name "Vaultly" in 15px semibold slate.
- Workspace switcher pill below logo: company name + chevron, 8px
  radius, border 1px solid var(--border), 32px tall.
- Nav sections: uppercase 10px label (#9ca3af letter-spacing 0.08em),
  then items 36px tall, 8px radius, icon 16px + 10px gap + label 13px.
  Active: background var(--coral-muted), left 3px bar var(--coral),
  label color var(--coral). Hover: #f8f9fb.
- Badge on "Invoices": small pill "12" in var(--coral) bg white.
- Bottom: user avatar row pinned at bottom.

### Topbar (56 px, sticky)
- Background: var(--card). Border-bottom: 1px solid var(--border).
- Left: search input 260px wide, placeholder "Search invoices, customers…"
  with inline SVG magnifier icon inside.
- Center-right: period selector tabs — This Month | Last Month | Q2 2025 | YTD.
  Active tab: var(--coral) text + bottom border 2px var(--coral).
- Right: notification bell (inline SVG, coral dot for 3 unread) + avatar.

### Page heading strip
- Left: "Billing Overview" 20px bold #111827 + period badge.
- Right: "Export CSV" ghost button + "New Invoice" coral CTA button.

### 4 KPI cards (grid 4-col)
Cards: white, border 1px var(--border), 12px radius, 20px padding,
subtle shadow 0 1px 4px rgba(0,0,0,0.05).

| Card | Label | Value | Delta | Sparkline |
|---|---|---|---|---|
| MRR | Monthly Recurring Revenue | $148,320 | +8.4% green | inline SVG 12-pt line |
| Active Subs | Active Subscriptions | 2,847 | +124 green | inline SVG bar |
| Churn Rate | Monthly Churn | 1.9% | −0.3pp green | inline SVG line |
| ARPU | Avg Revenue / User | $52.10 | +2.1% green | inline SVG line |

Each delta chip: 20px tall, 6px radius, background green-muted / red-muted.
Sparkline SVG: 80×32px, stroke var(--coral-light), no fill, 1.5px stroke.

### MRR Trend chart card (left, ~60% width)
- Title "MRR Trend" + subtitle "Monthly recurring revenue — last 12 months".
- Period tabs: 6M | 12M | YTD.
- Inline SVG area chart: 560×200 viewBox, gradient fill from
  var(--coral-light) alpha 0.18 to transparent, stroke var(--coral)
  2px, 6 y-axis grid lines (#e6e9ef 1px), x-axis month labels (Jan–Dec
  abbreviated). Plot 12 invented monthly values between $108k–$148k.

### Plan Breakdown card (right, ~40% width)
- Title "Revenue by Plan".
- 4 horizontal bars for plans: Enterprise, Growth, Starter, Free.
  Bar track: #f3f4f6. Fill: var(--coral), var(--coral-light), #f97316
  (orange), #94a3b8. Labels: plan name left, revenue amount + % right.
  Invented values summing to ~$148k.

### Invoices table card (main area, left ~65%)
- Header: "Recent Invoices" + count badge "2,847" + "View All →" link.
- Columns: Invoice # | Customer | Plan | Amount | Due Date | Status.
- 7 rows with invented data. Status pills: Paid (green), Pending
  (amber), Failed (red — coral-adjacent). Hover row: #f8f9fb tint.
- Footer: pagination row "Showing 1–7 of 2,847" + Prev/Next buttons.

### Dunning / Failed Payments panel (right ~35%)
- Header "Dunning Queue" + badge "8 at risk" in var(--red-muted) /
  var(--red) text.
- 5 failed-payment cards, each: customer avatar initial + name, plan,
  amount, days overdue, "Retry Now" coral ghost button + "Write Off"
  text link.
- Footer note: "8 subscriptions at risk · $3,240 ARR exposure".

## Output contract

```
<artifact identifier="admin-coral-billing" type="text/html" title="Coral Billing Admin">
<!doctype html>...</artifact>
```

Emit a single self-contained HTML file. All CSS in one `<style>` block.
No external assets, no CDN links. Keep under 30 KB. Use semantic
landmark elements: `<aside>`, `<nav>`, `<main>`, `<header>`, `<section>`,
`<table>`. Every chromatic color through a CSS custom property.
