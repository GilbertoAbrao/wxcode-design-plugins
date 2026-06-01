---
name: admin-aegis-insurance
description: |
  Institutional insurance carrier operations dashboard: light mode with
  navy (#1e3a8a / #2563eb) and teal (#14b8a6) accent palette, left
  sidebar with line-of-business switcher and section nav, topbar with
  search + period selector + avatar, 4 KPI cards (active policies /
  open claims / renewals due / loss ratio), a horizontal claims pipeline
  board (Filed → Review → Approved → Paid), a sortable policies table,
  a renewals-due side panel, and an inline SVG claims trend chart.
  Use when the brief targets an insurance carrier, underwriter, TPA,
  or claims management platform.
triggers:
  - "insurance admin"
  - "claims dashboard"
  - "policy management"
  - "carrier operations"
  - "insurance carrier"
  - "claims pipeline"
  - "renewals dashboard"
  - "loss ratio"
  - "painel de seguros"
  - "gestão de sinistros"
  - "保险管理后台"
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
  example_prompt: "Build me an insurance carrier admin dashboard — line-of-business sidebar, KPI cards for active policies, open claims, renewals due and loss ratio, a claims pipeline board, policies table, renewals panel, and a claims trend chart."
---

# Aegis Insurance Admin Skill

Produce the canonical institutional insurance carrier operations layout —
fit for an underwriter, TPA, or claims management platform back-office.

## Design language

- **Palette** (all chromatic values via CSS custom properties):
  - Navy primary: `--clr-navy-900` #1e3a8a, `--clr-navy-600` #2563eb
  - Teal accent: `--clr-teal-500` #14b8a6, `--clr-teal-300` #5eead4
  - Status green: `--clr-green-500` #22c55e
  - Status amber: `--clr-amber-500` #f59e0b
  - Status red: `--clr-red-500` #ef4444
  - Surface: white / `--clr-surface` #f6f8fb
  - Border: `--clr-border` #e3e8f0
  - Text primary: slate-800 `#1e293b` (neutral, hardcoded OK)
  - Text muted: slate-500 `#64748b` (neutral, hardcoded OK)
- **Font**: inline system stack — "Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif. No external load.
- **No chromatic hex literals** in CSS rules or inline SVG; use `var(--token)` or `currentColor`.

## Workflow

1. Read the active DESIGN.md if present; otherwise use the palette above.
2. Extract from the brief: carrier name, lines of business, KPI figures,
   claim counts per stage, policy records, renewal dates.
3. Layout:

   ### Left sidebar (240px)
   - Brand mark: shield SVG icon + "Aegis" wordmark in navy, "Insurance" muted.
   - Line-of-business switcher (pill dropdown): Auto / Property / Liability / Life.
   - Nav groups:
     - OVERVIEW: Dashboard, Analytics
     - OPERATIONS: Policies, Claims, Renewals, Reinsurance
     - ADMIN: Agents, Reports, Settings
   - Active item: `--clr-navy-600` left border (3px) + tinted `--clr-navy-900`/5% background.
   - Each nav item: SVG icon (16px) + label + optional count badge.

   ### Topbar (60px)
   - Left: page title "Operations Overview" with breadcrumb (Aegis / Dashboard).
   - Center: search input placeholder "Search policy, claim, holder…".
   - Right: period selector (MTD / QTD / YTD), bell icon with amber dot, avatar + "Sarah K." + caret.

   ### KPI cards (4-up grid)
   - **Active Policies**: 48,312 · delta +3.2% green · tiny inline SVG sparkline.
   - **Open Claims**: 1,847 · delta +12 this week amber · tiny bar sparkline.
   - **Renewals Due (30d)**: 3,204 · delta −8% yellow-amber · tiny line sparkline.
   - **Loss Ratio**: 61.4% · delta −2.1pp green · tiny area sparkline.
   - Card style: white, 10px radius, 0 2px 8px rgba(0,0,0,0.05) shadow, teal top-accent bar (3px).

   ### Claims pipeline board (horizontal, 4 stages)
   - Stages: **Filed** / **In Review** / **Approved** / **Paid**
   - Each column: stage header with count badge, 2–3 claim mini-cards.
   - Claim card: claim # + holder name + type (Auto / Property / Liability) +
     amount + days open. Filed cards are red-left-border; Review amber; Approved teal; Paid green.

   ### Policies table (wide card, below pipeline)
   - Columns: Policy # | Holder | Line | Premium | Effective | Status pill
   - 7 rows with invented data (auto, property, liability mix).
   - Status pills: Active (green), Lapsed (red), Pending (amber), Cancelled (slate).
   - Header: "Active Policies" title + "View all policies →" link.

   ### Right panel: Renewals Due (sidebar to policies table)
   - Header: "Renewals Due — Next 30 Days" + count badge.
   - 5 renewal items: policy # + holder + type + renewal date + premium.
   - CTA per item: "Send Notice" ghost button.

   ### Claims Trend chart (full-width, below table)
   - Inline SVG area chart (approx 600×140 viewport).
   - Two series: Filed (navy area) + Paid (teal area), 12 weekly data points.
   - Y-axis labels (0, 200, 400, 600), X-axis month labels (Jan–Dec).
   - Legend: filed dot + "Filed" · paid dot + "Paid".
   - Period tabs: 6M / 12M / 24M.

4. One inline `<style>`, semantic HTML, no external assets, no CDNs.
5. All chromatic colors from CSS custom properties on `:root`; SVG uses
   `currentColor` or `var(--token)`. Neutrals (slate text, shadows) may be hardcoded.

## Output contract

```
<artifact identifier="admin-aegis-insurance" type="text/html" title="Aegis Insurance Admin">
<!doctype html>...</artifact>
```
