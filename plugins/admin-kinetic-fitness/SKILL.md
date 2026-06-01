---
name: admin-kinetic-fitness
description: |
  Dark-mode gym and fitness studio operations admin — energetic dark-green
  canvas with lime accent, slim topbar (brand + search + location picker +
  avatar), compact left icon rail, 4 KPI tiles (active members, check-ins
  today, classes today, 30-day retention), class schedule list with inline
  capacity bars, weekly attendance area chart (inline SVG), members table
  with plan tier and status pill, and coach/trainer panel. Original archetype
  for gym chains, boutique studios, and personal-training businesses.
triggers:
  - "gym admin"
  - "fitness dashboard"
  - "studio management"
  - "fitness admin"
  - "gym management"
  - "personal training admin"
  - "class schedule dashboard"
  - "dark fitness dashboard"
  - "painel academia"
  - "健身房管理后台"
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
  example_prompt: "Build me a dark-mode fitness studio admin dashboard — slim topbar with location switch, icon rail sidebar, 4 KPI tiles (active members, check-ins, classes, retention), class schedule with capacity bars, weekly attendance chart, members table, and coach panel."
---

# Kinetic Fitness Admin Skill

Produce the canonical dark-mode gym and fitness studio operations dashboard.
Energetic feel anchored in a deep forest-green canvas with lime accent — built
for gym operators who live in the back-office between member check-ins.

## Workflow

1. Read the active DESIGN.md (if present); otherwise use lime (#84cc16) on a
   deep dark-green canvas (#0f1410 / #19211a / #232e25).
2. Extract from the brief: gym/studio name, location(s), primary KPIs (active
   members, today's check-ins, today's classes, 30-day retention), class types
   and coaches, membership plan tiers.
3. Layout:

   ### Top navbar (48px, full-width, bg #19211a, border-bottom #2c3a2f)
   - Left: compact brand mark (barbell SVG icon) + studio name in lime.
   - Centre-left: search input (dark bg #232e25, 32px tall, placeholder
     "Search members, classes…").
   - Centre-right: location picker dropdown ("Downtown Studio ▾").
   - Right: notification bell icon + avatar circle (initials) + chevron.

   ### Left icon rail (52px wide, full-height, bg #19211a, border-right #2c3a2f)
   Six icon-only items vertically stacked (grid/dashboard, members, calendar,
   dumbbell/classes, chart/analytics, settings). Active item: lime icon,
   lime left-bar, #232e25 background. Tooltip on hover (not required for
   prototype). No text labels — icon rail only.

   ### Main content area (calc(100% - 52px), scrollable)
   padding 20px 24px.

   #### KPI tiles row (4 equal columns, gap 16px)
   Each tile: bg #19211a, border #2c3a2f, border-radius 10px, padding 18px 20px.
   - Tile 1 — Active Members: count 1 847, delta +34 this month (lime up arrow).
     Icon: person silhouette SVG, lime.
   - Tile 2 — Check-ins Today: count 312, delta vs yesterday (lime / muted-red
     down arrow). Icon: scan/barcode SVG.
   - Tile 3 — Classes Today: count 18, "8 completed · 10 upcoming". Icon:
     calendar-clock SVG.
   - Tile 4 — 30-day Retention: 91.4%, delta +1.2 pp. Icon: shield-check SVG.
   Each tile has: small uppercase muted label (10px, letter-spacing 0.08em),
   large number (28px, #e6efe6), delta chip, icon top-right (20×20, currentColor
   via var()).

   #### Two-column row (7fr / 5fr, gap 16px, margin-top 16px)

   **LEFT — Class Schedule (today)**
   Card bg #19211a, border #2c3a2f, border-radius 10px. Header: "Today's Classes"
   + "View all →" lime link. List of 6 classes (time / class name / coach /
   capacity bar + fraction):
   - 06:00  |  HIIT Ignite      |  Coach Priya Mehra   |  ██████░░ 24/30
   - 07:30  |  Power Lift       |  Coach Dom Vasquez   |  ████░░░░ 16/30
   - 09:00  |  Yoga Flow        |  Coach Anika Torres  |  ██████████ 20/20 (full, lime pill)
   - 10:30  |  Spin Burn        |  Coach Dev Okafor    |  █████░░░░ 18/28
   - 12:00  |  Core & Stretch   |  Coach Priya Mehra   |  ██░░░░░░  8/25
   - 17:00  |  Boxing Basics    |  Coach Marcus Reid   |  ███░░░░░ 12/20
   Capacity bar: full-width bg #232e25, filled lime (#84cc16), height 6px,
   border-radius 3px. "Full" pill: bg lime/20, color lime, 10px text.

   **RIGHT — Weekly Attendance Chart**
   Card bg #19211a, border #2c3a2f, border-radius 10px. Header: "Weekly
   Attendance" + "This week vs last week" muted sub-label.
   Inline SVG area chart (100% wide, 140px tall). Two series: this week (lime
   fill, 30% opacity; lime stroke 1.5px) and last week (muted stroke #93a392,
   dashed, no fill). X-axis: Mon Tue Wed Thu Fri Sat Sun. Grid lines: #2c3a2f.
   Invented data points this week: [210, 280, 265, 310, 290, 420, 380].
   Last week: [195, 255, 240, 285, 270, 395, 360].

   #### Members Table (full-width, margin-top 16px)
   Card bg #19211a, border #2c3a2f, border-radius 10px. Header: "Members" +
   search icon + "Export CSV" ghost button (border lime, color lime).
   Table columns: Name / Plan / Status / Last Visit / Actions.
   8 rows of invented members:
   | Jess Kamara     | Elite Annual   | Active   🟢 | 2 hrs ago    | ⋯ |
   | Tobias Wren     | Monthly Flex   | Active   🟢 | Yesterday    | ⋯ |
   | Chloe Nakamura  | Elite Annual   | Active   🟢 | 3 days ago   | ⋯ |
   | Rafael Osei     | Day Pass       | Active   🟢 | Today        | ⋯ |
   | Nina Castillo   | Monthly Flex   | Frozen   🔵 | 12 days ago  | ⋯ |
   | Kwame Diallo    | Elite Annual   | Active   🟢 | 4 hrs ago    | ⋯ |
   | Sasha Petrova   | Monthly Flex   | Overdue  🔴 | 18 days ago  | ⋯ |
   | Leo Andrade     | Student Plan   | Active   🟢 | 1 day ago    | ⋯ |
   Status pills: Active = bg lime/15, color lime; Frozen = bg #3b82f6/15,
   color #60a5fa; Overdue = bg red/15, color #f87171. Hover row: bg #232e25.

   #### Coach Panel row (3 equal columns, gap 16px, margin-top 16px)
   3 coach cards, bg #232e25, border #2c3a2f, border-radius 10px, padding 16px.
   Each: avatar circle (2-letter initials, lime bg, #0f1410 text, 40px) + name
   + specialty tag + this-week class count + rating (★ out of 5, lime stars).
   - Priya Mehra   | HIIT & Yoga    | 8 classes this week | ★★★★★ 4.9
   - Dom Vasquez   | Strength       | 6 classes this week | ★★★★☆ 4.7
   - Marcus Reid   | Boxing & HIIT  | 5 classes this week | ★★★★★ 4.8

4. Typography: system font stack only ("Inter", system-ui, -apple-system,
   "Segoe UI", Roboto, sans-serif). Never load external fonts.
5. All chromatic colors via :root CSS custom properties (--color-accent,
   --color-accent-dim, --color-accent-muted, --color-text-primary,
   --color-text-muted, --color-status-active, --color-status-frozen,
   --color-status-overdue). Neutral dark backgrounds and borders may be
   hardcoded. SVG fill/stroke must reference currentColor or var() — never
   chromatic hex literals.
6. Single inline <style> block, semantic HTML, no external assets, no CDNs.
   Target file size 10–30 KB.

## Output contract

```
<artifact identifier="admin-kinetic-fitness" type="text/html" title="Kinetic Fitness Admin">
<!doctype html>...</artifact>
```
