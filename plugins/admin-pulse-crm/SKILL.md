---
name: admin-pulse-crm
description: |
  Airy light-mode admin aesthetic: white/slate canvas (#f8fafc), sky-blue accent
  (#0ea5e9 / #2563eb), subtle 1px #e2e8f0 borders, 10px-radius white cards with a
  faint drop shadow, Inter type with tabular figures. Archetype = workspace-switcher
  sidebar (240px) + topbar (56px) with search and filter chips + 4 KPI tiles with
  inline SVG sparklines and delta chips + a full-width stage-progress strip (N
  columns, proportional fill bars) + a 2-column split (7/5): a dense records table
  with status pills on the left, an activity / tasks side panel on the right.
  Built for clean, scannable SaaS dashboards where metrics and record lists must
  coexist at a glance.
triggers:
  - "airy light-mode admin"
  - "sky-blue accent dashboard"
  - "white card SaaS admin"
  - "sidebar workspace switcher"
  - "sparkline KPI tiles"
  - "stage-progress strip"
  - "light admin dashboard"
  - "slate-on-white admin"
example_prompt: "Apply this airy light-mode admin aesthetic to my domain"
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

# Pulse Admin — Visual Archetype

This plugin contributes a **look** (airy light-mode, sky-blue accent, white-card
surfaces, clean slate typography) and a **structure** (workspace-switcher sidebar +
topbar + KPI tiles with sparklines + stage-progress strip + records table + activity
side panel, plus list / form / detail screens). It does **not** contribute a domain
— the subject matter comes from the Knowledge Base and the user's prompt. Treat the
example below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property.

- **Canvas / surfaces:** page `#f8fafc`; card/panel `#ffffff`; sidebar `#ffffff`;
  topbar `#ffffff`; hover row `#f8fafc`; inset/stripe `#f1f5f9`.
- **Borders:** `#e2e8f0` (1px hairline); inner row dividers `#f1f5f9`.
- **Text ramp:** primary `#0f172a`, body `#334155`, secondary `#475569`, muted
  `#64748b`, faint `#94a3b8`.
- **Accent:** `--accent: #0ea5e9`; `--accent-dark: #2563eb`; `--accent-bg: #e0f2fe`.
  Active nav bars, primary CTAs, search-focus borders, sparkline strokes and fills.
- **Status / stage ramp (as tokens):** `--state-stage1 #0ea5e9` (bg `#e0f2fe`),
  `--state-stage2 #f59e0b` (bg `#fef3c7`), `--state-stage3 #7c3aed` (bg `#ede9fe`),
  `--state-won #10b981` (bg `#d1fae5`), `--state-lost #ef4444` (bg `#fee2e2`).
  Deltas: `--delta-up #059669` (bg `#d1fae5`), `--delta-down #dc2626` (bg `#fee2e2`).
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
  sans-serif`. Base 14px / line-height 1.5 / color `#334155`. `font-variant-numeric:
  tabular-nums` on **every** numeric cell. Nav/micro-labels: 10–11px, uppercase,
  `letter-spacing .06–.08em`, muted. Big KPI figures: 26–28px / weight 800 /
  `color #0f172a`. Column headers: 10px / uppercase / weight 700 / `#94a3b8`.
- **Density & radius:** 14px side padding in cards, 11px vertical row padding, 14px
  grid gaps; card radius 10px, control radius 7–8px, pill radius 20px, nav item
  radius 7px, progress bars 6px tall / 4px radius.
- **Shadows:** `0 1px 4px rgba(0,0,0,.04)` on cards. No heavy elevation. The
  cleanness is the brand.
- **Motion:** `.12s–.15s` background/border/color hover transitions; `.3s` width
  transitions on progress fills. Gentle only — no bounce.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns described by shape and behavior — not meaning.

- **Left sidebar** (240px, white, 1px right border, flex-column): a
  **workspace switcher** at the top (mark/logo + name + chevron, 1px bottom
  border); nav group sections (10px uppercase label + icon-row items, active item
  gets a 3px left accent bar + accent-bg tint + accent-dark text); a spacer; at the
  bottom: an **avatar stack** of 4 overlapping 26px circles + an invite ghost link +
  a member count.
- **Topbar** (56px, white, 1px bottom border, flex row): page title + breadcrumb on
  the left; centered **search pill** (icon + input, max-width 340px, border goes
  accent on focus); **filter chip group** (All / Active / state variants); a **date
  range button**; a **notification icon button** (dot badge); avatar + name.
- **Main content** (flex:1, scroll, 20px padding): vertical flow of regions.
- **KPI tile row** (4 tiles, equal grid, 14px gap): each tile = white card with a
  10px uppercase label, a big tabular figure, and on the right: a small inline SVG
  sparkline (line or bar, stroke `var(--accent)`) + a delta chip (green ▲ or red ▼).
- **Stage-progress strip** (full-width white card): a titled panel with N equal
  columns (one per stage); each column has an uppercase stage name, a deal/item count
  badge, a summary value, and a proportional fill bar in `var(--accent)` at stepped
  opacity. 1px column dividers.
- **Two-column split (1fr / 340px):**
  - **Left — records table card:** header with title + "View all" ghost link; a
    `<table>` with uppercase 10px column headers, 11px vertical row padding, 1px row
    dividers, hover row tint; cells include a **two-line name+sub cell**, an **owner
    cell** (24px avatar + name), a right-aligned value cell, a **status pill**, and a
    muted date cell. Footer: result count + pager.
  - **Right — activity / tasks side panel:** titled card with two sections separated
    by an uppercase 10px divider: a **tasks section** (checkbox rows — 16px square
    with 4px radius, checkmark SVG on done, strikethrough text, muted time stamp) and
    a **feed section** (28px avatar dot + verb + target + relative time).
- **List screen:** records-table archetype as its own page — toolbar with search
  pill + filter chip group + count, the same dense table, pager.
- **Form screen:** sectioned white cards of labelled fields; **rules appear as
  inline validation** — required marks (`*`), helper text under the field, inline
  error messages on invalid fields, primary submit disabled-until-valid. No
  rules/checklist/validation-status panel.
- **Detail screen:** breadcrumb + header band (title + status pill + key actions) +
  a meta grid of label/value pairs (3-col) + one or more related-data sub-panels (a
  mini-table or activity feed) below.

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS domain's
equivalent of the archetype slots — its primary entities, key metrics, status
states, stage or funnel names, record list/columns, form fields and their rules, and
detail fields — and map them onto the archetype above. If no KB/domain is supplied
(standalone), use the Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules
become inline field validation. Do NOT render build/implementation notes or designer
controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent
> (entities, metrics, states, columns, fields) drawn from the KB + prompt.

```
Domain (illustrative): a B2B software sales team managing opportunities.

Workspace switcher  → "Perimeter Sales" with initials mark "P".
Sidebar nav groups  → PIPELINE (Overview, Deals, Leads, Contacts),
                      REPORTING (Analytics, Forecasts, Goals), SETTINGS.
Topbar              → "Pipeline Overview" title, breadcrumb (Home › Sales ›
                      Pipeline), search placeholder "Search deals, contacts,
                      companies…", filter chips: All / Active / Won / Lost.

KPI tiles (4):
  • Pipeline Value $2.4M (sparkline line, ▲ 12%).
  • Win Rate 38.4% (sparkline bar, ▲ 3.1%).
  • New Leads 147 (sparkline line, ▼ 4%).
  • Avg Deal Size $18.6K (sparkline line, ▲ 7%).

Stage-progress strip → "Pipeline by Stage" — 4 columns:
  Lead (63 items / $480K / 35% bar opacity .4),
  Qualified (38 / $720K / 55% bar opacity .6),
  Proposal (21 / $840K / 72% bar opacity .8),
  Won (14 / $360K / 100% bar, won-green).

Records table (left) → "Recent Deals": Deal (name + company), Company, Owner
  (avatar + name), Value, Stage pill (Lead/Qualified/Proposal/Won/Lost), Close Date.
  7 rows. Pager.

Activity panel (right) → "Activity & Tasks":
  Today's Tasks: 3 checkbox rows (1 completed with strikethrough + checkmark,
    2 open), each with a time.
  Recent Activity: 5 feed rows (avatar dot, verb, target, relative time).

List screen   → all records, search + filter chips (All/Active/Won/Lost),
  same dense table, pager.

Form screen   → "New Record": title (required), company (required), value
  (required, > 0), stage (required select), close date (required, not in the
  past), owner (required select). Rules as required marks + helper text +
  inline errors; "Create" disabled until valid.

Detail screen → one record: breadcrumb, header (title + stage pill + Edit
  button), meta grid (company / value / stage / close date / owner / created),
  a "Related Items" sub-table + recent activity feed.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities, key
   metrics, status states, stage/funnel names, record columns, form fields + rules,
   detail fields — from the KB + prompt. Standalone: use the Example instantiation
   above.
3. Build each screen in the Visual language + Layout archetype above, imitating the
   example set in `assets/` (dashboard, list, form, detail) and the
   `assets/template.html` seed — with fresh content for the real domain, NOT the
   example labels.
4. Express domain rules as INLINE field validation (required marks, helper text,
   inline errors, disabled-until-valid submit). Never render
   rules/checklist/validation-status/build-note panels or designer/demo controls.
5. One inline `<style>`, semantic HTML5, `tabular-nums` on figures, no external
   assets, no CDNs — self-contained.

## Output contract

```
<artifact identifier="admin-pulse-crm" type="text/html" title="Pulse Admin">
<!doctype html>...</artifact>
```
