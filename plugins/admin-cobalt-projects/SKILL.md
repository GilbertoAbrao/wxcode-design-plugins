---
name: admin-cobalt-projects
description: |
  Focused project and work-management admin dashboard: light mode,
  cobalt-blue accent (#2563eb / #3b82f6), left sidebar listing projects
  with category color chips, topbar with search input + list/board view
  switcher + avatar group, 4 KPI cards (active projects, tasks due this
  week, overall completion rate, overdue tasks), a compact gantt-style
  timeline strip showing 3–4 tasks against week-day columns, a "My Tasks"
  table (task / project / assignee avatar / due date / priority pill /
  status pill), and a right-side Team or Milestones panel. Use when the
  brief mentions project tracking, task management, roadmaps, sprints,
  gantt, or work-management and no other style direction is given.
triggers:
  - "project management dashboard"
  - "tasks dashboard"
  - "gantt admin"
  - "project tracker"
  - "work management"
  - "sprint board admin"
  - "roadmap dashboard"
  - "cobalt admin"
  - "project admin"
  - "painel de projetos"
  - "项目管理后台"
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
  example_prompt: "Build me a focused project management admin dashboard — left sidebar with project list, topbar with search and view switcher, 4 KPI cards (active projects, tasks due, completion rate, overdue), a compact gantt timeline, a My Tasks table with priority and status pills, and a team milestones side panel."
---

# Cobalt Projects Admin Skill

Produce a focused, light-mode project and work-management admin dashboard
with cobalt-blue as the single dominant accent color and small chromatic
chips per project category.

## Workflow

1. Read the active DESIGN.md (if present); otherwise apply cobalt blue
   (#2563eb primary, #3b82f6 lighter variant) on a near-white canvas
   (#f8fafc), slate text (#0f172a / #475569), #e6e9ef borders, white cards.
2. Extract from the brief: team or product name, projects list (4–6 names),
   key metrics (active projects, tasks due this week, completion %, overdue
   count), task records for the table (5–7 rows), and milestone names.
3. Layout:

   **Left sidebar (240px)**
   - Brand mark (square cobalt pill icon + product wordmark) at top.
   - "Projects" section header; list each project with a small chromatic
     category dot, project name, and a task-count badge. Active row has
     cobalt left indicator and tinted background.
   - "Navigation" section below: Overview, My Tasks, Timeline, Reports,
     Settings — each with a compact inline SVG icon.
   - Bottom: user avatar + name + "Workspace" label.

   **Top bar (56px)**
   - Left: current view title + breadcrumb (Home / Projects).
   - Centre: search input (magnifier SVG icon, placeholder "Search tasks,
     projects…").
   - Right: list/board view toggle (two icon buttons), notification bell
     with optional dot, then a tight avatar group (3 overlapping circles +
     "+N" chip) representing active teammates.

   **KPI cards row (4 equal cards)**
   - White cards, 10px radius, subtle shadow (0 1px 4px rgba(0,0,0,0.06)).
   - Card 1: Active Projects — cobalt icon, big number, "+ N this month" delta chip.
   - Card 2: Tasks Due This Week — amber icon, count, "N overdue" sub-label.
   - Card 3: Completion Rate — green icon, percentage with a thin arc or
     progress bar, "+3 pts vs last week" delta.
   - Card 4: Overdue Tasks — rose icon, count, "oldest N days ago" sub-label.

   **Timeline / Gantt strip (card)**
   - Header: "Week Timeline" + current date range + "View full →" link.
   - Column headers: Mon–Sun (or Mon–Fri) date labels.
   - 3–4 task rows: task name + project chip on the left, horizontal duration
     bar spanning the correct columns using inline divs or inline SVG rects,
     colored by project category. Bars have rounded ends (border-radius 4px).
   - Today marker: thin vertical cobalt line.

   **Main lower row — two-column (8/4)**
   - LEFT (8 cols): "My Tasks" table card.
     - Columns: checkbox, task name + project sub-label, assignee avatar,
       due date, priority pill (Critical/High/Medium/Low — rose/amber/cobalt/slate),
       status pill (In Progress/Review/Done/Blocked — cobalt/violet/emerald/rose).
     - 5–7 realistic rows, tinted hover, "View all tasks →" footer link.
   - RIGHT (4 cols): "Milestones" panel card.
     - 4–5 milestone entries: milestone name, due date, completion progress
       bar (thin, colored by nearness), project chip.
     - Bottom: "Team" section with 4 avatars + name + role + tiny active dot.

4. Typography: system font stack only
   ("Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif).
   Tiny uppercase tracking labels for card headings. Cobalt for active
   states, links, and primary CTA. Semantic color for priority/status pills.
5. Color tokens: ALL chromatic colors as CSS custom properties on :root.
   Inline SVG uses var(--token) or currentColor only. Neutrals (grays,
   near-black text, near-white surface, borders) may be hardcoded.
6. One inline `<style>`, semantic HTML, single-file, no external assets,
   no CDNs, no lorem ipsum, target 10–30 KB.

## Output contract

```
<artifact identifier="admin-cobalt-projects" type="text/html" title="Cobalt Projects Admin">
<!doctype html>...</artifact>
```
