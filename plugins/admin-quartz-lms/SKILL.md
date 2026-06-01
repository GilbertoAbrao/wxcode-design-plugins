---
name: admin-quartz-lms
description: |
  Friendly-academic LMS administration dashboard: light mode with a
  purple (#9333ea / #a855f7) accent, left sidebar with school/program
  switcher and grouped navigation, topbar with global search, term
  selector and avatar, 4 KPI tiles (active students, courses,
  completion rate, avg score), an enrollment vs completion area chart,
  a courses table with progress bars and status pills, and an upcoming
  assignments/deadlines side panel. Use this archetype when the brief
  involves a learning management system, course platform, university
  portal, or e-learning administration interface.
triggers:
  - "lms admin"
  - "learning management"
  - "course admin"
  - "university dashboard"
  - "e-learning admin"
  - "school admin"
  - "education dashboard"
  - "painel educacional"
  - "学习管理系统"
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
  example_prompt: "Build me a friendly academic LMS admin dashboard — left sidebar with school switcher, topbar with term selector, 4 KPI tiles (active students, courses, completion rate, avg score), enrollment/completion chart, courses table, and upcoming assignments panel."
---

# Quartz LMS Admin Skill

Produce a polished, friendly-academic LMS administration layout with a
purple accent palette and supportive category accents for course
subjects (science, arts, tech, language, etc.).

## Workflow

1. Read the active DESIGN.md (if present); otherwise use purple
   (#9333ea) as primary accent on a near-white canvas (#faf9fc) with
   slate text (#1e293b / #475569).
2. Extract from the brief: institution name, academic term, primary
   KPIs (active students, courses, completion rate, avg score or
   equivalents), course/subject types.
3. Layout:

   - **Left sidebar (260px)**: institution logo mark + name at top,
     school/program dropdown switcher below. Grouped nav with section
     labels (OVERVIEW, ACADEMIC, MANAGE, SETTINGS). Each item: icon +
     label + optional count badge. Active item has a purple left-bar
     and light-purple tinted background. Footer: support link + version.

   - **Top bar (60px)**: page title + breadcrumb on the left, a search
     input in the centre, a term/semester selector pill, notification
     bell with badge, and a user avatar + name on the right.

   - **Greeting + action strip**: "Welcome back, <name>" subheader,
     current date, "Download Report" ghost button, purple "+ Add Course"
     primary CTA.

   - **4 KPI tiles**: white cards, 10px radius, soft shadow
     (0 2px 8px rgba(0,0,0,0.05)). Each tile: small uppercase label,
     large bold number, tiny inline SVG sparkline or donut, and a delta
     chip (green ▲ / red ▼). Tiles: Active Students, Active Courses,
     Completion Rate (%), Avg Score (0–100).

   - **Main grid (8/4 cols)**:
     - LEFT (8 cols): "Enrollment vs Completion" chart card — title,
       period tabs (This Week / Month / Term), legend dots, dual-line or
       stacked area SVG chart with labeled axes and grid lines. Use
       purple for enrollment line, teal/emerald for completion line.
     - RIGHT (4 cols): "Upcoming Deadlines" panel — 5–6 entries listing
       assignment title, course name, due date, and a colored subject
       tag pill.

   - **Courses table card (full width)**: header "Courses This Term"
     + view-all link. 6–8 rows with columns: course name + subject icon,
     instructor name + avatar initial, enrolled count, a mini progress
     bar (% completed), and a status pill (Active / Draft / Archived).
     Tinted hover row.

4. Subject category accents (use as CSS custom properties, not hardcoded
   hex): science → teal, arts → orange/amber, technology → indigo,
   language → rose, mathematics → blue, humanities → green.
5. Typography: system font stack only ("Inter", system-ui, -apple-system,
   "Segoe UI", Roboto, sans-serif). Uppercase labels with letter-spacing
   for tile titles. Purple for links and active states. Status pill colors:
   Active = green, Draft = amber, Archived = slate.
6. All chromatic colors as :root CSS custom properties; SVG uses
   var(--token) / currentColor; only neutrals hardcoded.
7. Single inline `<style>`, semantic HTML, no external assets, no CDNs,
   no lorem ipsum. Target 10–30 KB.

## Output contract

```
<artifact identifier="admin-quartz-lms" type="text/html" title="Quartz LMS Admin">
<!doctype html>...</artifact>
```
