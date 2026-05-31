---
name: admin-aurora-analytics
description: |
  Aurora Analytics Admin generates a self-contained light-mode analytics dashboard with a fixed left sidebar, topbar with search, four KPI tiles with sparklines, a sessions area chart, a recent-sessions table, and a right-rail insights panel. Use this skill when a product or growth team needs a polished single-page admin overview rendered without external dependencies. Best suited for SaaS metrics, user-behaviour analytics, and operational monitoring interfaces.
triggers:
  - "analytics admin dashboard"
  - "light mode admin dashboard"
  - "painel de analytics"
  - "dashboard administrativo light"
  - "sessions analytics dashboard"
  - "KPI cards with sparklines"
  - "admin dashboard with sidebar"
  - "painel de operações com gráficos"
  - "light admin dashboard"
  - "analytics overview page"
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
    requires: [pixel-discipline, typographic-rhythm]
  example_prompt: "Build me a polished light-mode analytics admin dashboard — left sidebar, topbar with search, 4 KPI cards with sparklines, a sessions area chart, a recent sessions table, and an insights side panel."
---

# Aurora Analytics Admin Skill

Aurora Analytics Admin produces a single-file, dependency-free HTML dashboard tuned for product and growth analytics contexts. The layout anchors a fixed 240px sidebar with logo and grouped navigation on the left, a sticky topbar with a search field, breadcrumb trail, and user avatar on top, and a three-column main grid that stacks four KPI cards, a primary sessions area chart, a scrollable recent-sessions table, and a right-rail insights and activity panel. Colour, spacing, and type are defined as CSS custom properties so the output inherits any active DESIGN.md palette without touching the structural rules.

## Workflow

1. Read the active DESIGN.md to capture the primary brand palette, typeface stack, border-radius scale, and shadow tokens.
2. Extract domain inputs from the brief: product name, key metrics to surface (sessions, conversions, retention, revenue, or custom), date range context, and any named user segments.
3. Layout build order:
   - **Sidebar**: SVG logo mark + wordmark, nav groups (Overview, Acquisition, Behaviour, Retention, Settings), active-link highlight in indigo, collapsed icon labels.
   - **Topbar**: icon-button search toggle + inline input, breadcrumb (Dashboard › Overview), notification bell badge, avatar with initials chip.
   - **KPI row**: four cards — each has a metric label, a large numeral, a delta badge (green up / red down), and a 7-point inline SVG sparkline path.
   - **Area chart**: 12-week sessions area chart drawn as a single inline SVG with gradient fill, axis labels, a hover crosshair rule, and a legend strip.
   - **Recent sessions table**: columns for User, Source, Country, Duration, Pages, Converted; alternating-row tints, sortable-header chevrons (visual only).
   - **Right rail**: Top channels donut (inline SVG), Quick insights card (3 bullet observations), and an Activity feed (icon + text + timestamp, 5 items).
4. Compose one `<style>` block in `<head>` using CSS custom properties for the full palette. All layout via CSS Grid and Flexbox. No external fonts — use the Inter/system-ui stack. No external images — use inline SVG for charts, icons, and the logo.

## Output contract

```
<artifact identifier="admin-aurora-analytics" type="text/html" title="Aurora Analytics Admin">
<!doctype html>
...
</html>
</artifact>
```
