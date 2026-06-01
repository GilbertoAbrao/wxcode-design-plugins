---
name: admin-pulse-crm
description: |
  Airy light-mode sales CRM admin dashboard: workspace-switcher sidebar,
  topbar with global search and stage/owner filters, 4 pipeline KPI tiles
  with inline SVG sparklines, a horizontal pipeline-by-stage progress strip
  (Lead→Qualified→Proposal→Won), a "Recent deals" table with stage pills and
  owner avatars, and a right-side activity + tasks panel. Sky-blue (#0ea5e9 /
  #2563eb) accent on white/#f8fafc surfaces with slate text and #e2e8f0
  borders. Choose this when the brief mentions CRM, deals, pipeline, leads,
  or sales dashboard.
triggers:
  - "crm dashboard"
  - "sales pipeline"
  - "deals admin"
  - "lead tracking"
  - "pipeline dashboard"
  - "sales crm"
  - "pipeline kanban"
  - "painel crm"
  - "销售CRM"
od:
  mode: prototype
  surface: web
  scenario: sales
  preview:
    type: html
    entry: index.html
  design_system:
    requires: true
    sections: [color, typography, layout, components]
  craft:
    requires: [pixel-discipline, laws-of-ux]
  example_prompt: "Build me a CRM admin dashboard for a sales team — left sidebar with workspace switcher, topbar with search and filters, 4 pipeline KPI tiles, pipeline-by-stage strip, recent deals table, and an activity/tasks side panel."
---

# Pulse CRM Admin Skill

Produce an airy, light-mode sales CRM admin layout with sky-blue accent
and a focus on pipeline visibility and deal tracking.

## Workflow

1. Read the active DESIGN.md if present; otherwise use sky-blue (#0ea5e9
   primary, #2563eb hover/active) on a #f8fafc canvas with white card
   surfaces and #e2e8f0 borders.
2. Extract from the brief: team name, pipeline stages (default:
   Lead / Qualified / Proposal / Won), KPI labels (pipeline value, win
   rate, new leads, avg deal size), record type (deals, opportunities).
3. Layout:

   **Left sidebar (240px)**
   - Workspace switcher at the top: company logo mark + name + chevron.
   - Primary nav groups: PIPELINE (Overview, Deals, Leads, Contacts),
     REPORTING (Analytics, Forecasts, Goals), SETTINGS. Each item: 16px
     icon + label. Active item has a sky-blue left bar (3px) and a
     sky-blue/10 tinted background. Inactive icon color slate-400.
   - Bottom: team member avatar stack + "Invite teammate" ghost link.

   **Topbar (56px, white, 1px bottom border #e2e8f0)**
   - Left: page title "Pipeline Overview" + breadcrumb (Home / Sales /
     Pipeline).
   - Center: search input with magnifier icon, placeholder "Search deals,
     contacts, companies…"
   - Right: stage filter chip group (All / Active / Won / Lost), date
     range button, notification bell (dot badge), and avatar + name.

   **4 KPI tiles (white, 10px radius, subtle shadow)**
   - Pipeline Value — total open pipeline in $. Sparkline: line SVG.
     Delta chip green/red.
   - Win Rate — percentage of closed-won vs total closed. Sparkline: bar
     SVG. Delta chip.
   - New Leads — count added this month. Sparkline: line SVG. Delta chip.
   - Avg Deal Size — mean value of closed-won deals. Sparkline: line SVG.
     Delta chip.

   **Pipeline-by-stage strip (full width card)**
   - Horizontal row of 4 stage columns: Lead / Qualified / Proposal / Won.
   - Each column: stage name, deal count badge, total value, and a
     proportional fill bar in sky-blue (opacity stepped: 30/50/70/100%).
   - A thin connecting arrow or chevron divider between stages.

   **Two-column main area (roughly 7/5 split)**
   - LEFT — "Recent Deals" table card:
     - Header: title + "View all" link.
     - Columns: Deal name + company logo mark, Company, Owner (avatar +
       name), Value ($), Stage pill (color-coded: sky for Lead, amber for
       Qualified, violet for Proposal, emerald for Won), close date.
     - 6–7 rows with tinted hover. All figures original, no lorem ipsum.
   - RIGHT — "Activity & Tasks" panel card:
     - Section "Today's tasks" (3 checkbox items with due time).
     - Section "Recent activity" (5 feed items: avatar dot + verb +
       target + relative time).

4. Typography: system font stack only ("Inter", system-ui, -apple-system,
   "Segoe UI", Roboto, sans-serif). Tile labels: 11px uppercase
   letter-spacing 0.06em slate-500. Numbers: 28px bold slate-900.
   Body: 13–14px slate-700.
5. Every chromatic color is a CSS custom property on :root. SVG sparklines
   use var(--color-accent) or currentColor. Neutral grays may be hardcoded.
6. One inline `<style>`, semantic HTML, no external assets, no CDNs,
   no external fonts, target 10–30 KB.

## Output contract

```
<artifact identifier="admin-pulse-crm" type="text/html" title="Pulse CRM Admin">
<!doctype html>...</artifact>
```
