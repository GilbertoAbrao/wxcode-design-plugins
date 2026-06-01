---
name: admin-vault-treasury
description: |
  Premium dark-mode corporate treasury operations dashboard: deep navy
  backgrounds (#0a0f1e / #121a2e / #1b2640) with amber-gold accent
  (#f59e0b / #fbbf24), calm green for positive flows (#34d399) and
  red for negative (#f87171). Left rail nav with icons and labels,
  topbar entity/period switcher and avatar, 4 KPI cards (total balance,
  inflows, outflows, runway) with inline SVG sparklines, cashflow area
  chart (inline SVG), allocation donut by account/currency, recent
  transactions table with status pills. All figures use tabular-nums.
  Use when the brief asks for treasury, cash management, FX operations,
  liquidity dashboard, or any finance-ops dark admin.
triggers:
  - "treasury dashboard"
  - "cash management"
  - "corporate finance admin"
  - "liquidity dashboard"
  - "fx operations"
  - "vault admin"
  - "treasury operations"
  - "cashflow dashboard"
  - "painel de tesouraria"
  - "资金管理后台"
od:
  mode: prototype
  surface: web
  scenario: operations
  preview:
    type: html
    entry: index.html
  design_system:
    requires: true
    sections: [color, typography, layout, components]
  craft:
    requires: [pixel-discipline, laws-of-ux]
  example_prompt: "Build me a premium dark-mode corporate treasury admin dashboard — left rail nav, entity/period switcher, 4 KPI cards for cash position, inflows, outflows, runway, cashflow area chart, allocation donut, recent transactions table."
---

# Vault Treasury Admin Skill

Produce a premium dark-mode corporate treasury operations dashboard.
Deep navy shell, amber-gold accent, tabular numeric figures throughout.

## Workflow

1. Read the active DESIGN.md (if present); otherwise use amber (#f59e0b)
   on a deep-navy canvas (#0a0f1e / #121a2e panels).
2. Extract from the brief: entity name, reporting currency, 4 KPI values
   (total cash balance, period inflows, period outflows, projected runway
   in days), time range for the cashflow chart, account/currency split
   for the donut, last N transactions for the table.
3. Layout:
   - **Left rail nav (220px fixed)**: vault mark + product name at top,
     grouped nav items (icon + label). Active item has amber left-bar and
     #1b2640 tinted background. Bottom: settings + user menu.
   - **Top bar (60px)**: entity/account switcher on the left (chevron),
     period selector tabs (MTD / QTD / YTD / Custom) in the center,
     notification bell + avatar + name on the right.
   - **4 KPI cards**: dark #121a2e background, 10px radius, 1px border
     #243049. Each card: small uppercase label (#8b97ad), large tabular
     number (#e5e9f0), tiny inline SVG trend sparkline (5-point polyline),
     delta chip (green #34d399 ▲ or red #f87171 ▼ + percent). Card accent
     strip top-left corner in amber.
   - **Main grid (7/5)**:
     - LEFT (7 cols): cashflow area chart card — title, period tabs,
       inline SVG (area fill with amber gradient, baseline axis, 6 grid
       lines, month labels), dual series (inflows green, outflows red).
     - RIGHT (5 cols): allocation donut — inline SVG donut segments
       (4–6 accounts/currencies), centered total label, legend rows
       below with color dot + label + amount + percent.
   - **Wide transactions table card**: "Recent Transactions" header +
     "View all" link, 8 rows, columns (date · counterparty · type ·
     amount colored +/- · status pill). Status pills: Settled (#34d399
     tint), Pending (#f59e0b tint), Rejected (#f87171 tint). Tinted
     hover row (#1b2640). Tabular-nums on all amount cells.
4. Typography: inline system font stack only — "Inter", system-ui,
   -apple-system, "Segoe UI", Roboto, sans-serif. NO external loads.
   font-variant-numeric: tabular-nums on all figure elements.
   Amber for active states, links, and accent marks. #8b97ad for muted
   labels. #e5e9f0 for primary text.
5. Every chromatic color is a CSS custom property on :root. SVG fill/
   stroke chromatic colors use var(--token) or currentColor. Only
   low-saturation neutrals (backgrounds, borders, muted text) may be
   hardcoded.
6. One inline <style>, semantic HTML, no external assets, no CDNs,
   no lorem ipsum. Realistic original copy and currency figures.

## Output contract

```
<artifact identifier="admin-vault-treasury" type="text/html" title="Vault Treasury Admin">
<!doctype html>...</artifact>
```
