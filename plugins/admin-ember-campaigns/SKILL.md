---
name: admin-ember-campaigns
description: |
  Vibrant-but-clean marketing campaign analytics admin: light mode,
  rose-pink (#e11d48 / #ec4899) accent with secondary indigo for
  contrast, white/#fafafa surfaces, slate text, #ececf0 borders.
  Left sidebar with brand + nav, topbar with search + date-range +
  avatar, 4 KPI cards (reach / CTR / spend / ROAS) with inline SVG
  sparklines, a multi-series campaign performance chart, a conversion
  funnel (stacked horizontal segments), and a campaigns table with
  channel chips and status pills. Use when the brief is campaign
  management, marketing analytics, ad performance, or growth dashboards.
triggers:
  - "campaign dashboard"
  - "marketing admin"
  - "campaign analytics"
  - "ad performance dashboard"
  - "marketing campaigns"
  - "growth dashboard"
  - "ember campaigns"
  - "painel de campanhas"
  - "营销活动管理"
od:
  mode: prototype
  surface: web
  scenario: marketing
  preview:
    type: html
    entry: index.html
  design_system:
    requires: true
    sections: [color, typography, layout, components]
  craft:
    requires: [pixel-discipline, laws-of-ux]
  example_prompt: "Build me a marketing campaign analytics admin — left sidebar, date-range topbar, 4 KPI cards with sparklines, multi-series performance chart, conversion funnel, and campaigns table with channel chips."
---

# Ember Campaigns Admin Skill

Produce the Ember Campaigns marketing command-centre layout — a
vibrant-but-clean rose-accented admin purpose-built for campaign
managers and growth teams.

## Palette (palette-ready: all chromatic values via CSS custom properties)

```
--color-accent:       #e11d48   /* rose-600 — primary CTAs, active states */
--color-accent-soft:  #ec4899   /* pink-500 — hover, gradients */
--color-indigo:       #4f46e5   /* indigo-600 — secondary contrast */
--color-indigo-soft:  #6366f1   /* indigo-500 — chart series 2 */
--color-success:      #16a34a   /* green-600 — positive deltas, "live" pills */
--color-warning:      #d97706   /* amber-600 — "paused" pills */
--color-danger:       #dc2626   /* red-600 — negative deltas, "ended" pills */
--color-sky:          #0ea5e9   /* sky-500 — chart series 3 / Email chip */
```

Neutral and surface tokens (hardcoded, not chromatic):
- Canvas: `#fafafa`; cards: `#ffffff`; sidebar: `#ffffff`; border: `#ececf0`
- Text-primary: `#0f172a`; text-secondary: `#64748b`; text-muted: `#94a3b8`

## Workflow

1. Read the active DESIGN.md if present; otherwise use the palette above.
2. Extract from the brief: brand name, campaign types (paid-search,
   social, email, display…), primary KPIs (4 from reach / CTR / spend /
   ROAS / conversions / revenue), date range.
3. Layout:

   **Left sidebar (240px fixed)**
   - Brand icon (ember flame SVG, rose fill) + product name "Ember" at top.
   - Nav sections: OVERVIEW (Dashboard, Analytics), CAMPAIGNS (All
     Campaigns, Audiences, Creatives), REPORTS (Performance, Attribution,
     Export), SETTINGS (Integrations, Team, Billing). Active item: rose
     left-border + `var(--color-accent)` tinted background + bold label.
   - Bottom: workspace avatar cluster + "Upgrade" CTA button.

   **Topbar (60px)**
   - Left: page title "Campaigns" + breadcrumb (Home › Campaigns).
   - Centre: search input with magnifier icon.
   - Right: date-range selector button (calendar icon + "May 1 – May 31"),
     notification bell, round avatar.

   **KPI row (4 cards, equal-width)**
   Each card: small uppercase label, large number, tiny 40×24 inline SVG
   sparkline, delta chip (arrow + ±%). Cards: Reach / CTR / Spend / ROAS.
   Sparkline stroke uses `currentColor` set to `var(--color-accent)`.

   **Middle row (7/5 split)**
   - LEFT (7): "Campaign Performance" multi-series line chart (inline SVG,
     original path data, 3 series: Impressions / Clicks / Conversions).
     Legend chips use --color-accent, --color-indigo-soft, --color-sky.
     X-axis week labels; Y-axis tick lines; no external lib.
   - RIGHT (5): "Conversion Funnel" — 4 horizontal stacked bars
     (Impressions → Clicks → Leads → Customers) in progressively shorter
     widths. Each bar: fill from accent gradient, label + count + drop %.
     Title, subtitle.

   **Campaigns table (full width)**
   Header: "Active Campaigns" + "+ New Campaign" rose button.
   Columns: Name | Channel chip | Impressions | Clicks | Spend | Status pill.
   Channel chips: Paid Search (indigo), Social (rose), Email (sky), Display
   (amber). Status pills: Live (green), Paused (amber), Ended (red).
   8 rows of realistic invented copy. Tinted hover; light header row.

4. Typography: inline system stack only. Uppercase letter-spaced labels
   for KPI tiles. Rose for active states and primary actions.
5. One inline `<style>`, semantic HTML, no external assets, no CDNs,
   no lorem ipsum. Target 10-30 KB.

## Output contract

```
<artifact identifier="admin-ember-campaigns" type="text/html" title="Ember Campaigns Admin">
<!doctype html>...</artifact>
```
