---
name: admin-slate-commerce
description: |
  Generates a production-ready light-mode e-commerce back-office dashboard with a sidebar store switcher, topbar date range, KPI cards with sparklines, a revenue bar chart, a recent orders table with status badges, and a top products list. Use this skill whenever a merchant or store operator needs a clean, data-dense admin interface with emerald and amber accents on warm neutral surfaces.
triggers:
  - "ecommerce dashboard"
  - "orders admin panel"
  - "store back office"
  - "painel de e-commerce"
  - "loja back office"
  - "admin de pedidos"
  - "revenue dashboard light mode"
  - "merchant analytics dashboard"
  - "KPI cards orders table"
  - "back office loja virtual"
od:
  mode: prototype
  surface: web
  scenario: e-commerce
  preview:
    type: html
    entry: index.html
  design_system:
    requires: true
    sections: [color, typography, layout, components]
  craft:
    requires: [pixel-discipline, typographic-rhythm]
  example_prompt: "Build me a light-mode e-commerce back-office dashboard — sidebar with store switcher, topbar with date range, 4 KPI cards with sparklines, a revenue bar chart, a recent orders table with status badges, and a top products list."
---

# Slate Commerce Admin Skill

This skill produces a complete light-mode e-commerce back-office dashboard tailored for store operators and e-commerce managers who need a single-screen view of revenue health, order volume, average order value, and refund exposure. The layout uses warm neutral surfaces (#ffffff / #f9fafb), emerald (#10b981) as the primary accent for positive metrics and actions, and amber (#f59e0b) for caution states and highlights — all rendered as a single self-contained HTML file with no external dependencies.

## Workflow

1. Read the active DESIGN.md to pull brand colors, font stack, and border-radius tokens; fall back to the Slate Commerce defaults if no DESIGN.md is present.
2. Extract domain inputs from the brief: store name, reporting date range, currency, any custom KPI labels or product categories the user specifies.
3. Layout — build section by section:
   - **Sidebar (240px fixed):** Logo mark + store name at top; store switcher dropdown; nav links (Dashboard, Orders, Products, Customers, Analytics, Settings) with icons rendered as inline SVG paths; bottom user avatar + logout.
   - **Topbar:** Full-width bar with a search input, a date-range selector showing "May 1 – May 31, 2025", a notification bell with badge count, and a circular avatar.
   - **KPI row (4 cards):** Revenue ($84,320), Orders (1,247), AOV ($67.62), Refunds ($3,180). Each card shows label, large figure, delta pill (↑/↓ % vs prior period), and a tiny 32×24 px inline SVG sparkline.
   - **Revenue bar chart:** 12-bar inline SVG chart (Jan–Dec), Y-axis labels, current month highlighted in emerald, others in a muted slate. Gridlines via SVG <line>.
   - **Recent orders table:** Columns — Order #, Customer, Date, Items, Amount, Status. Six rows with realistic data. Status badges: Delivered (emerald), Processing (amber), Pending (slate), Refunded (rose). Row hover state via CSS.
   - **Top products list:** Five rows, each with a small color-block product thumbnail (inline SVG rect), product name, SKU, units sold bar (inline SVG rect scaled to value), and revenue.
4. One inline `<style>` block using CSS custom properties for the palette. Semantic HTML5 landmarks. No external assets.

## Output contract

```
<artifact identifier="admin-slate-commerce" type="text/html" title="Slate Commerce Admin">
<!doctype html>
...
</html>
</artifact>
```
