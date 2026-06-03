---
name: admin-quartz-lms
description: |
  Friendly-academic light-mode admin aesthetic: near-white canvas (#faf9fc),
  purple accent (#9333ea / #a855f7) on a slate neutral ramp, white card surfaces
  with soft shadow, Inter type at 14px, 12px radii, gentle 1px lilac borders, and
  crisp status pills. Archetype = left sidebar (entity switcher + grouped nav) +
  top bar (search + period selector + avatar) + 4 KPI tiles + 2-column grid (dual-
  line area chart + upcoming-items side panel) + full-width records table with
  subject-category tag pills and progress bars. Built for content-dense, data-rich
  management interfaces that feel approachable rather than technical.
triggers:
  - "light mode friendly admin"
  - "purple accent admin"
  - "academic-style dashboard"
  - "soft card admin"
  - "lilac sidebar admin"
  - "warm light admin"
  - "pastel accent management"
  - "painel claro roxo"
example_prompt: "Apply this friendly light-mode purple admin aesthetic to my domain"
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

# Quartz Admin — Visual Archetype

This plugin contributes a **look** (friendly-academic light mode, purple accent,
soft cards, pastel tag pills, subject-category color ramp) and a **structure**
(left sidebar + top bar + KPI tiles + chart + side panel + records table, plus
list / form / detail screens). It does **not** contribute a domain — the subject
matter comes from the Knowledge Base and the user's prompt. Treat the example
below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property; hardcode the neutral ramp.

- **Canvas / surfaces:** page `#faf9fc`; card/sidebar `#ffffff`; hover tint
  `#faf5ff`; hairline border `#ebe7f1`; stronger focus `#d8b4fe`.
- **Text ramp:** primary `#1e293b`, secondary `#475569`, muted `#94a3b8`.
- **Accent:** `--accent: #9333ea` (purple-600), `--accent-light: #a855f7`,
  `--accent-dim: #f3e8ff`, `--accent-deep: #7e22ce`. CTAs, active nav bar,
  links, selected tabs, progress fills, chart strokes.
- **Category color ramp (as tokens):** `--clr-cat-science #0d9488`,
  `--clr-cat-arts #ea580c`, `--clr-cat-tech #4f46e5`, `--clr-cat-language #e11d48`,
  `--clr-cat-math #2563eb`, `--clr-cat-humanities #16a34a`, each with a `…-bg`
  tint for tag pill backgrounds.
- **Status ramp (as tokens):** `--state-active #22c55e / #dcfce7 / #15803d`,
  `--state-draft #f59e0b / #fef3c7 / #b45309`, `--state-archived #94a3b8 / #f1f5f9`.
  Chart second line: `--clr-teal-600 #0d9488`.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`.
  Base 14px / line-height 1.5. Uppercase tile labels: 10.5px, `letter-spacing: .7px`,
  `font-weight: 700`, muted. Big figures 26px / weight 800 / `letter-spacing: -.5px`.
- **Density & radius:** 9px vertical row padding, 18px panel padding, 16–18px grid
  gaps; card radius 12px, control radius 8px, pill radius 20px, progress bars 5px
  tall / 20px radius.
- **Borders & shadows:** 1px `var(--border)` (#ebe7f1) lines + `0 2px 8px
  rgba(0,0,0,0.04)` card shadow. Sidebar is shadowless (right-border only).
- **Motion:** `.15s` background/color transitions; no bouncy easings. Active nav
  indicator is a 3px left-edge bar (`border-radius: 0 3px 3px 0`).

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Left sidebar** (260px, white bg, 1px right border, sticky 100vh): brand mark +
  name at top, then **entity switcher** (lilac-tinted pill with icon + label + name
  + chevron), then 3–4 **grouped nav sections** (uppercase 10px section label +
  nav items with icon + label + optional count badge; active item has a 3px purple
  left-edge bar + light-purple bg), then a footer (support link + version tag).
- **Top bar** (60px, white bg, 1px bottom border, sticky): page title + breadcrumb
  on the left, a **search pill** centred, a **period-selector pill** (live-dot +
  label + chevron), notification icon + avatar + name/role on the right.
- **Content area** (page bg, 24px padding, vertical flow):
  - **Greeting strip**: h1 welcome + sub-line date/context on left; ghost + primary
    action buttons on right.
  - **KPI tile row** (4 tiles, equal grid): white card, 12px radius, soft shadow;
    each tile = `[icon chip, top-right] [big tabular figure] [delta chip + sparkline]`
    with an uppercase micro-label.
  - **2-column grid (auto + 320px):**
    - **Left — dual-line area chart card**: title + period-tabs (3 options), legend
      dots, dual-line area-fill SVG with labeled axes and dashed gridlines.
    - **Right — upcoming-items panel**: title + subtitle, list rows of
      `[category dot] [title + parent + tag pill] [due date + urgency label]`,
      "View all" link at header.
  - **Full-width records table**: card with header actions (ghost + primary), sticky
    uppercase header, dense rows of `[name cell + tag pill] [secondary cell with
    avatar] [numeric] [mini progress bar + pct] [status pill]`, no footer pager in
    the dashboard view (promoted to list screen).
- **Records list screen:** toolbar with search + filter chips + count; same dense
  table; footer pager.
- **Record form screen:** sectioned field cards; **rules appear as inline
  validation** — required marks (`*`), helper text under the field, inline error
  on invalid fields, submit disabled-until-valid. No rules/checklist panel.
- **Record detail screen:** a breadcrumb + header band (ID + name + status pill +
  actions), a meta grid (label/value pairs), and related sub-panels (a mini-table
  or status-row list + an activity/timeline feed) below.

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key metrics,
status states, category tags, record columns, form fields and their rules, and
detail fields — and map them onto the archetype above. If no KB/domain is supplied
(standalone), use the Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules
become inline field validation. Do NOT render build/implementation notes or
designer controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent
> (entities, metrics, states, category tags, columns, fields) drawn from the KB + prompt.

```
Domain (illustrative): a higher-education Learning Management System.

Entity switcher  → institution: "Meridian University".
Period selector  → active term: "Spring 2026 Term".
Nav sections     → Overview (Dashboard, Analytics), Academic (Courses, Students,
                   Assignments, Schedule), Manage (Instructors, Certificates, Reports),
                   Settings.

KPI tiles (4):
  • Active Students 1,204 (▲+48 this week; purple icon chip; sparkline).
  • Active Courses 38 (▲+3 new term; teal icon chip; sparkline).
  • Completion Rate 72.4% (▲+4.1% vs last; green icon chip; donut sparkline).
  • Avg Score 81.6 (▼−1.3 vs last; blue icon chip; sparkline).

Chart (left)     → "Enrollment vs Completion" — dual-line area, purple = enrolled,
                   teal = completed; period tabs Week / Month / Term.

Side panel (right) → "Upcoming Deadlines" — rows of [category dot] [task title +
                   parent course] [subject tag pill] [due date + urgency: Tomorrow /
                   2 days / later]. Categories: Tech, Math, Science, Language, Arts,
                   Humanities.

Records table    → "Courses This Term": course name + subject tag pill / instructor
                   name + avatar initial / enrolled count / mini progress bar + pct /
                   status pill (Active / Draft / Archived).

List screen      → all records, search + filter chips (status, category),
                   paginated table.

Form screen      → "New Record": primary-entity name (required), secondary field
                   (required), numeric quantity (required, > 0), category select
                   (required), date (required, not in the past), additional fields.
                   Required marks + helper text + inline errors; submit disabled until
                   valid.

Detail screen    → one record: breadcrumb + header (ID + status pill + actions),
                   meta grid (name, category, qty, date, owner, created), related
                   sub-table + activity feed.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, status states, category types, record columns, form fields + rules,
   detail fields — from the KB + prompt. Standalone: use the Example instantiation
   above.
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
<artifact identifier="admin-quartz-lms" type="text/html" title="Quartz Admin">
<!doctype html>...</artifact>
```
