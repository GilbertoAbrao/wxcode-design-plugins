---
name: admin-statute-legal
description: |
  Refined professional law firm admin dashboard for case and matter
  management. Light mode with a burgundy (#9f1239 / #be123c) and gold
  (#b45309) accent palette on warm white (#faf8f6) surfaces and slate
  text. Left sidebar with practice-area switcher and grouped nav;
  topbar with global search, period selector, and attorney avatar;
  4 KPI tiles (active cases, billable hours MTD, deadlines this week,
  realization rate); CASES/MATTERS table with matter#, client, practice
  area, lead attorney, and status pill; upcoming deadlines side panel;
  matters-by-practice inline SVG bar chart; recent documents list.
  Use when the brief calls for a legal, law firm, attorney portal,
  matter management, or case-tracking admin interface.
triggers:
  - "law firm dashboard"
  - "legal admin"
  - "matter management"
  - "case management dashboard"
  - "attorney portal"
  - "legal operations"
  - "painel jurídico"
  - "gestão de processos"
  - "法律事务所管理系统"
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
  example_prompt: "Build me a refined law firm admin dashboard for case and matter management — practice-area sidebar, 4 KPI tiles (active cases, billable hours MTD, deadlines this week, realization rate), matters table with status pills, upcoming deadlines panel, matters-by-practice chart, recent documents list. Burgundy and gold accents on warm white."
---

# Statute Legal Admin Skill

Produce a refined professional law firm matter management dashboard —
the shape a legal-ops director or managing partner expects for daily
case oversight.

## Palette

- Accent burgundy: `--clr-accent` #9f1239 / `--clr-accent-hi` #be123c
- Accent gold: `--clr-gold` #b45309 / `--clr-gold-hi` #d97706
- Surface warm white: `--clr-surface` #faf8f6 / `--clr-surface-raised` #ffffff
- Border: `--clr-border` #e8e2dc
- Text: slate — headings #1e293b, body #334155, muted #64748b
- Status: active #16a34a bg #dcfce7; pending #b45309 bg #fef3c7; closed #64748b bg #f1f5f9; urgent #be123c bg #ffe4e6
- All chromatic colors as :root CSS custom properties; neutrals hardcoded.

## Workflow

1. Read the active DESIGN.md if present; otherwise use the Statute Legal
   palette defined above on a warm white (#faf8f6) canvas.
2. Extract from the brief: firm name, practice areas (4–6), KPI values,
   matter list, attorney names, deadline dates, document names.
3. Layout (single-page, no JS framework):
   - **Left sidebar (240px)**: firm monogram + name at top, practice-area
     switcher (All / Corporate / Litigation / Real Estate / Employment /
     IP), grouped nav — OVERVIEW (Dashboard, Matters, Clients, Calendar),
     BILLING (Timesheets, Invoices, Receipts), SETTINGS (Team, Roles,
     Integrations). Active item: burgundy left bar + tinted #fdf2f4
     background. Footer: logged-in attorney chip.
   - **Topbar (60px)**: page title "Matter Overview" on the left,
     global search input, period selector (This Month / Q2 / YTD),
     notification bell (inline SVG), avatar + initials on the right.
   - **Greeting strip**: date + "Realization Rate: 87%" status chip +
     ghost "Export CSV" button + burgundy "+ New Matter" primary CTA.
   - **4 KPI tiles** (white cards, 8px radius, warm shadow
     0 2px 8px rgba(0,0,0,0.05)): Active Cases (number + vs-last-month
     delta chip), Billable Hours MTD (number + progress bar), Deadlines
     This Week (number + urgency indicator), Realization Rate (percentage
     + sparkline SVG). Each tile has a small inline SVG icon in the
     top-right corner using var(--clr-accent) or var(--clr-gold).
   - **Main content grid (flex row, 2/3 + 1/3)**:
     - LEFT (2/3): CASES/MATTERS table card — columns: Matter# | Client |
       Practice Area | Lead Attorney | Status pill | Action link. 8 rows
       of invented data. Hover: #fdf7f5 row tint. Status pills use the
       palette above. Table header: uppercase 11px letterspaced slate-muted.
     - RIGHT (1/3): Upcoming Deadlines panel — 6 deadline entries each
       with colored urgency dot, matter#, description, date in a clean
       compact list. Below it: a Matters by Practice inline SVG bar chart
       (horizontal bars, var(--clr-accent) fill, 5 practice areas with
       count labels).
   - **Recent Documents list** (full width, below grid): 6 document rows
     with an inline SVG document icon, document name, matter link,
     uploaded-by attorney, upload date, and a "View" ghost link.
4. Typography: system font stack — "Inter", system-ui, -apple-system,
   "Segoe UI", Roboto, sans-serif. No external font loads.
   - Tile labels: 11px uppercase, letter-spacing 0.06em, muted slate.
   - Tile numbers: 28px, 600 weight, #1e293b.
   - Table headers: 11px uppercase, 500 weight, #64748b.
   - Body copy: 14px, #334155.
5. SVG icons: inline, currentColor or var(--clr-accent). No raster images.
   No external CDNs. No lorem ipsum.
6. One inline `<style>` block; semantic HTML5; single self-contained file.

## Output contract

```
<artifact identifier="admin-statute-legal" type="text/html" title="Statute Legal Admin">
<!doctype html>...</artifact>
```
