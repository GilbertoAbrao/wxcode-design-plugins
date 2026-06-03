---
name: admin-cobalt-projects
description: |
  Light-mode admin aesthetic: near-white canvas (#f1f5f9), cobalt-blue accent
  (#2563eb / #3b82f6), white card surfaces with soft 1px borders and subtle
  shadow, inter type at 14px, chromatic category chips (violet / emerald /
  amber / rose / sky), compact priority pills and status pills, and sparkline
  KPI cards. Archetype = left sidebar (brand mark + entity list with colored
  dots + nav items) + topbar (breadcrumb + search + view toggle + avatar group)
  + 4 KPI cards + a horizontal timeline strip (Gantt-style bars with a today
  marker) + 2-column lower row (records table + side panels for summary lists).
  Built for focused, card-forward operational consoles where clarity and color
  coding matter more than density.
triggers:
  - "cobalt blue light-mode admin"
  - "light card-forward admin"
  - "sidebar project-list admin"
  - "clean card admin dashboard"
  - "cobalt accent admin"
  - "gantt timeline admin"
  - "multi-category admin"
  - "painel claro cobalt"
example_prompt: "Apply this cobalt light-mode admin aesthetic to my domain"
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
---

# Cobalt Admin — Visual Archetype

This plugin contributes a **look** (light-mode, cobalt-blue accent, white-card
surfaces, chromatic category chips, compact pills) and a **structure** (left
sidebar with entity list + nav, topbar, KPI tiles, Gantt strip, records table,
side panels). It does **not** contribute a domain — the subject matter comes
from the Knowledge Base and the user's prompt. Treat the example below as
illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property; neutrals may be hardcoded.

- **Canvas / surfaces:** page `#f1f5f9`; sidebar/topbar `#ffffff`; card `#ffffff`; sidebar border `#e2e8f0`; card border `#e9ecf0`; card shadow `0 1px 4px rgba(0,0,0,0.05)`.
- **Text ramp:** primary `#0f172a`, heading `#1e293b`, secondary `#475569`, muted `#64748b`, faint `#94a3b8`.
- **Accent:** `--cobalt-700: #1d4ed8`, `--cobalt-600: #2563eb` (primary CTA, active nav indicator, links, primary buttons), `--cobalt-500: #3b82f6` (chart strokes, lighter fills), `--cobalt-100: #dbeafe`, `--cobalt-50: #eff6ff`.
- **Category / semantic chips (as tokens):** `--cat-violet #7c3aed` / `--cat-violet-bg #ede9fe`; `--cat-emerald #059669` / `--cat-emerald-bg #d1fae5`; `--cat-amber #d97706` / `--cat-amber-bg #fef3c7`; `--cat-rose #e11d48` / `--cat-rose-bg #ffe4e6`; `--cat-sky #0284c7` / `--cat-sky-bg #e0f2fe`. Assign categories consistently; recolor by state (cobalt / amber / rose / emerald / sky).
- **Status ramp:** `--status-progress` cobalt `#2563eb` / `--status-progress-bg #eff6ff`; `--status-review` violet `#7c3aed` / `--status-review-bg #ede9fe`; `--status-done` emerald `#059669` / `--status-done-bg #d1fae5`; `--status-blocked` rose `#e11d48` / `--status-blocked-bg #ffe4e6`.
- **Priority ramp:** critical rose, high amber, medium cobalt, low slate — each with a `*-bg` tint.
- **Delta chips:** `delta-up` `background:#d1fae5; color:#065f46`; `delta-down` `background:#ffe4e6; color:#9f1239`.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`. Base 14px. Figures use `font-variant-numeric: tabular-nums`. Big KPI figures 26px / weight 800 / `letter-spacing: -.03em`. Micro-labels 10–11px uppercase, `letter-spacing: .07em`, muted. Section labels 10px uppercase weight 700 tracking wide.
- **Density & radius:** compact 7px vertical item padding in sidebar, 11–18px card padding; card/panel radius 10px, control/button radius 7–8px, pill/chip radius 10–12px, sidebar active indicator `inset 3px 0 0 var(--cobalt-600)`.
- **Borders & shadows:** 1px `#e2e8f0`/`#e9ecf0` borders on all cards; `0 1px 4px rgba(0,0,0,0.05)` card shadow. No dark panels.
- **Motion:** `.12s–.15s` background/border hover transitions. Sparkline gradients are decorative, not animated.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns described by shape and behavior — not meaning.

- **Left sidebar (240px, white, 1px right border):** top brand mark (icon + wordmark + sub-label) → **entity list section** (section label + list rows of `[category dot] [entity name] [count badge]`; active row has cobalt left indicator + tinted bg) → **navigation section** (section label + nav items with leading icon) → bottom user footer (avatar initials + name + workspace label).
- **Topbar (56px, white, 1px bottom border):** breadcrumb (parent / current) → flexible **search input** (magnifier icon, placeholder) → spacer → **view-toggle** pair (icon buttons for alternate layouts, active = cobalt fill) → notification bell with optional dot → **avatar group** (3 overlapping circles + "+N" chip).
- **Page header (within main content):** title + sub-line on the left, ghost + primary action buttons on the right.
- **KPI tile row (4 equal cards):** each tile = white card with `[UPPERCASE MICRO-LABEL] [icon chip (color by state)]` header, a big tabular figure, and a footer of `[delta chip] [context line]`, optionally followed by a tiny sparkline SVG area.
- **Timeline / Gantt strip (card):** header (`[title] [date range + context]` on left, `View full →` link on right) → column headers (label column + 7 day columns, today column accented) → task rows (`[task name + sub-label] | [bars area]`) where bars are absolutely positioned `div`s spanning the correct column offsets, each colored by category. A thin cobalt vertical line with a dot cap marks today.
- **2-column lower row (fluid left / 300px right):**
  - **Left — records table card:** card header (title + summary line) → `<table>` with uppercase sticky header, rows of `[text name cell with sub-label] [assignee avatar + name] [due date (overdue = rose)] [priority pill] [status pill]`, tinted hover, footer link.
  - **Right — side panels stack:** one or more panel cards, each with a title and a scrollable list. Primary side panel: summary list rows of `[name] [date]` over a thin progress bar, a footer line of `[percent] [category chip]`. Secondary side panel: member rows of `[avatar with status dot] [name + role]`.
- **List screen:** records table as its own page — toolbar (search input + filter chips with counts) → full table → pager footer.
- **Form screen:** sectioned field cards (`<section>` groups with a section title); **rules appear as inline field validation** — required marks (`*`), helper text below the field, inline error messages on invalid fields, submit disabled until valid. No rules/checklist/validation-status panel.
- **Detail screen:** breadcrumb → detail header band (entity ID + status pill + key actions) → meta grid (label/value cells, 3-col) → related data panels (summary-list rows or a mini-table + an activity feed).

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key metrics,
status states, record list/columns, form fields and their rules, and detail
fields — and map them onto the archetype above. If no KB/domain is supplied
(standalone), use the Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules
become inline field validation. Do NOT render build/implementation notes or
designer controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent
> (entities, metrics, states, columns, fields) drawn from the KB + prompt.

```
Domain (illustrative): a cross-functional software delivery workspace — teams
tracking projects, tasks, weekly timelines, and milestones.

Sidebar entity list    → "Projects" section with 5 entries: Platform Relaunch
  (cobalt dot, 14 tasks), Mobile App v3 (violet, 9), Data Pipeline (emerald, 6),
  Brand Refresh (amber, 5), Auth Module (rose, 3). Active = Platform Relaunch.

Navigation items       → Overview, My Tasks (active), Timeline, Reports, Settings.

Topbar                 → breadcrumb: Home / Projects; search "Search tasks,
  projects…"; view toggle (list active); bell with dot; avatar group (SC / MT / PL + +4).

Page header            → "Platform Relaunch" title; "Q3 delivery · Sprint 7 of
  10 · Updated 2 hours ago" sub-line; Export (ghost) + New Task (primary) actions.

KPI tiles (4):
  • Active Projects — cobalt icon, figure "5", delta "↑ 1 vs last quarter", sparkline.
  • Tasks Due This Week — amber icon, figure "23", delta "↓ 4 vs last week", sparkline.
  • Completion Rate — emerald icon, figure "72%", delta "↑ 3 pts vs last sprint", sparkline.
  • Overdue Tasks — rose icon, figure "7", delta "↑ 2 · oldest 9 days ago", sparkline.

Timeline strip         → "Week Timeline" · Jun 2–8 · Sprint 7; 4 task bars:
  API Gateway Refactor (cobalt, Mon–Thu), Design System Tokens (amber, Tue–Thu),
  OAuth2 Integration (rose, Wed–Sat), Spark Job Profiling (emerald, Thu–Sat).
  Today line at Tue (Jun 3).

Records table          → "My Tasks" — columns: Task (+ project sub-label) /
  Assignee (avatar + name) / Due / Priority pill / Status pill.
  7 rows with realistic names, priorities Critical→Low, statuses
  Blocked / In Progress / Review / Done. Footer "View all tasks →".

Side panel 1 (Milestones) → 4 milestones: Beta Launch 68% (cobalt, Jun 14),
  Brand Handoff 45% (amber, Jun 20), Auth v2 Stable 82% (emerald, Jun 12),
  Mobile App Soft Launch 30% (violet, Jul 1). Each with progress bar + project chip.

Side panel 2 (Team)       → 5 members with initials avatar + name + role +
  status dot (online / away / offline).

List screen            → all tasks, search + filter chips (status, priority,
  assignee), paginated dense table.

Form screen            → "New Task": title (required), description, project
  (required select), assignee (select), due date (required), priority (required
  select), status (select). Rules as required marks + helper text + inline errors;
  "Create Task" disabled until valid.

Detail screen          → one task: header (task title + status pill + actions),
  meta grid (project, assignee, due date, priority, created), related subtasks
  mini-table + activity feed.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, status states, record columns, form fields + rules, detail fields
   — from the KB + prompt. Standalone: use the Example instantiation above.
3. Build each screen in the Visual language + Layout archetype above, imitating
   the example set in `assets/` (dashboard, list, form, detail) and the
   `assets/template.html` seed — with fresh content for the real domain, NOT the
   example labels.
4. Express domain rules as INLINE field validation (required marks, helper text,
   inline errors, disabled-until-valid submit). Never render
   rules/checklist/validation-status/build-note panels or designer/demo controls.
5. One inline `<style>`, semantic HTML5, `tabular-nums` on figures, no external
   assets, no CDNs — self-contained.

## Output contract

```
<artifact identifier="admin-cobalt-projects" type="text/html" title="Cobalt Admin">
<!doctype html>...</artifact>
```
