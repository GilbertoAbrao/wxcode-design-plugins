---
name: admin-meridian-people
description: |
  Warm-professional HR / people-operations admin dashboard: light mode
  with indigo accent (#4f46e5 / #6366f1), left sidebar with org-and-team
  switcher plus grouped HR navigation, topbar with search and period
  selector, 4 KPI tiles (headcount / attendance / open roles / turnover),
  a headcount-over-time area chart, a department headcount horizontal bar
  chart, a paginated employees table with avatar + role + status pill, and
  a right-side time-off / requests panel. Use when the brief is about HR,
  workforce, people ops, HRIS, or employee management.
triggers:
  - "hr dashboard"
  - "people operations"
  - "headcount dashboard"
  - "workforce admin"
  - "employee management"
  - "hris dashboard"
  - "painel de rh"
  - "人力资源后台"
  - "time off management"
  - "org chart admin"
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
  example_prompt: "Build me an HR people-operations admin dashboard — left sidebar with org/team switcher, topbar with search and period selector, 4 KPI tiles for headcount / attendance / open roles / turnover, a headcount-over-time chart, department headcount bars, an employees table, and a time-off requests side panel."
---

# Meridian People Admin Skill

Produce a complete, single-file HR people-operations admin layout that
operations leads and HR managers will immediately recognize as purpose-built
for workforce management.

## Palette (palette-ready)

All chromatic colors MUST be declared as `:root` CSS custom properties.
SVG fill/stroke chromatic colors MUST use `var(--token)` or `currentColor`.
No chromatic hex literal in CSS rules or inline SVG attributes.

| Token                  | Value       | Role                        |
|------------------------|-------------|-----------------------------|
| `--color-accent`       | #4f46e5     | Primary indigo (active nav, CTA buttons) |
| `--color-accent-mid`   | #6366f1     | Hover / lighter indigo      |
| `--color-accent-bg`    | #eef2ff     | Indigo tint backgrounds     |
| `--color-success`      | #16a34a     | Positive deltas, active status |
| `--color-success-bg`   | #dcfce7     | Success pill background     |
| `--color-warn`         | #d97706     | Warning / leave pending     |
| `--color-warn-bg`      | #fef3c7     | Warning pill background     |
| `--color-danger`       | #dc2626     | Negative deltas, terminated |
| `--color-danger-bg`    | #fee2e2     | Danger pill background      |
| `--color-dept-eng`     | #6366f1     | Engineering bar             |
| `--color-dept-design`  | #ec4899     | Design bar                  |
| `--color-dept-product` | #f59e0b     | Product bar                 |
| `--color-dept-sales`   | #10b981     | Sales bar                   |
| `--color-dept-ops`     | #8b5cf6     | Operations bar              |
| `--color-dept-finance` | #0ea5e9     | Finance bar                 |

Surface + text (hardcoded neutrals permitted):
- Canvas: `#f8f8fb`
- Sidebar: `#ffffff`
- Card: `#ffffff`
- Border: `#e8e8ef`
- Text primary: `#1e1e2d`
- Text secondary: `#6b7280`
- Text muted: `#9ca3af`

## Workflow

1. Read the active DESIGN.md (if present); otherwise fall back to the
   palette table above.
2. Extract from the brief: company name, reporting period, list of
   departments, any custom KPI labels or headcount figures.
3. Layout (all widths reference 1440px viewport):

   ### Left sidebar (240px, fixed)
   - Top area: app logo mark (inline SVG diamond) + "Meridian" wordmark.
   - Org/team switcher card: current org name + arrow, clickable.
   - Nav sections — OVERVIEW (Dashboard, Headcount, Attendance),
     TALENT (Recruitment, Onboarding, Performance), PEOPLE (Directory,
     Time Off, Payroll), SETTINGS (Roles & Permissions, Integrations).
   - Active item: `--color-accent` left bar + `--color-accent-bg` background.
   - Bottom: avatar + "HR Admin" label + cog icon.

   ### Topbar (64px)
   - Left: page title "People Dashboard" + breadcrumb "Meridian / HR".
   - Center: search input ("Search employees, roles…").
   - Right: period selector tabs (MTD / QTD / YTD), notification bell
     (badge count), and user avatar + name.

   ### KPI strip — 4 tiles in a row
   Each tile: white card, 12px radius, soft shadow, uppercase label,
   large number, colored delta chip (+/−), and a tiny 60×32 inline SVG
   sparkline.
   - **Total Headcount** — 847 (+12 this month) — sparkline: steady upward
   - **Attendance Rate** — 94.3% (−0.8 pp) — sparkline: slight dip
   - **Open Roles** — 23 (+5 new) — sparkline: stepped up
   - **Turnover (12 mo)** — 8.2% (−1.1 pp) — sparkline: trending down

   ### Main grid (two-column: 60% / 40%)
   **LEFT — Headcount Over Time chart card**
   - Title "Headcount Growth" + subtitle + period tabs.
   - Inline SVG area chart: 12 monthly data points, dual-layer
     (total headcount area fill in `--color-accent-bg`, line in
     `--color-accent`). Y-axis labels left, X-axis month labels bottom.
     Grid lines in `#e8e8ef`. Original invented monthly figures.

   **RIGHT — Department Breakdown card**
   - Title "By Department".
   - Six horizontal bars, each: dept color swatch square, dept name,
     count, percentage bar (fill = dept color token), percentage text.
   - Departments (original invented counts):
     Engineering 182, Design 64, Product 48, Sales 211, Operations 97, Finance 58.

   ### Employees table (full-width card below grid)
   - Header: "Employees" title + "+ Add Employee" indigo button + filter pill row.
   - Columns: Name (avatar + full name), Role, Department, Status (pill), Start Date.
   - 8 rows with invented realistic names, roles, and dates.
   - Status pills: Active (green), On Leave (amber), Probation (indigo), Terminated (red).
   - Hover: `#f8f8fb` row tint. Pagination hint row.

   ### Right panel — Time Off & Requests (320px, sticky)
   Appears as a card column to the right of the table area on wider
   viewports, or below on narrower.
   - Title "Time Off Today" + date.
   - 4 entries: employee avatar circle (initials), name, type of leave
     (Annual / Sick / Personal), day count, approve/decline buttons.
   - Below: "Pending Approvals" section with 3 request rows and a
     "View all requests" link.

4. Typography: system font stack only — `"Inter", system-ui, -apple-system,
   "Segoe UI", Roboto, sans-serif`. Tile labels in 11px uppercase +
   letter-spacing 0.06em. Section headers in 10px uppercase + letter-spacing
   0.1em + `--text-muted`. Links and active states in `--color-accent`.

5. One inline `<style>` block, semantic HTML5, no external assets, no CDNs,
   no lorem ipsum, all copy and figures invented.

## Output contract

```
<artifact identifier="admin-meridian-people" type="text/html" title="Meridian People Admin">
<!doctype html>...</artifact>
```
