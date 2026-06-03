---
name: admin-aurora-analytics
description: |
  Light-mode analytics admin aesthetic: crisp white-and-slate canvas (#f8fafc /
  #ffffff), indigo-violet accent ramp (#6366f1 / #7c3aed), clean Inter type,
  subtle card shadows, and soft 12px radius panels. Archetype = fixed 240px
  sidebar with grouped nav sections + sticky topbar (search + actions + avatar)
  + 4 KPI cards with inline sparklines + primary area chart + records table +
  right-rail side panel (donut chart + insight bullets + activity feed). Built
  for polished product dashboards that read clearly on a desktop screen.
triggers:
  - "light mode admin dashboard"
  - "indigo accent clean admin"
  - "card-based analytics dashboard"
  - "white canvas admin with sidebar"
  - "soft shadow card dashboard"
  - "violet accent light admin"
  - "painel claro com cartões e gráficos"
  - "clean SaaS admin aesthetic"
example_prompt: "Apply this light indigo admin aesthetic to my domain"
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
    requires: [pixel-discipline, typographic-rhythm]
---

# Aurora Admin — Visual Archetype

This plugin contributes a **look** (light-mode, indigo-violet accent, clean card
surfaces, subtle shadows) and a **structure** (fixed sidebar with grouped nav +
sticky topbar + KPI tile row with sparklines + area chart + records table + right
rail, plus list / form / detail screens). It does **not** contribute a domain —
the subject matter comes from the Knowledge Base and the user's prompt. Treat the
example below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property.

- **Canvas / surfaces:** page `#f8fafc`; card / panel `#ffffff`; soft border
  `#e2e8f0`; faint separator `#f1f5f9`; hover tint `#f8fafc`.
- **Text ramp:** primary `#0f172a`, secondary / muted `#475569`, faint `#94a3b8`.
- **Accent — indigo / violet ramp:** `--c-indigo: #6366f1`, `--c-indigo-lt:
  #eef2ff`, `--c-indigo-mid: #818cf8`, `--c-indigo-pale: #a5b4fc`,
  `--c-indigo-pale2: #e0e7ff`; `--c-violet: #7c3aed`, `--c-violet-lt: #f5f3ff`.
  Primary CTAs, active nav highlight, chart strokes, figure emphasis.
- **Status / delta tokens:** `--c-green: #10b981` (up / success, `--c-green-lt:
  #ecfdf5`); `--c-red: #ef4444` (down / error, `--c-red-lt: #fef2f2`); `--c-amber:
  #f59e0b` (warn, `--c-amber-lt: #fffbeb`); `--c-sky: #0ea5e9` (info,
  `--c-sky-lt: #f0f9ff`).
- **Supplemental hues:** `--c-blue: #3b82f6`, `--c-orange: #f97316`, `--c-rose:
  #f43f5e`, `--c-pink: #db2777` — used for avatar gradients, source pills,
  chart series.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
  sans-serif`. Base 14px. `font-variant-numeric: tabular-nums` on every numeric
  cell. Big KPI figures 28px / weight 800 / `letter-spacing: -1px`. Section
  micro-labels 10–12px, uppercase, letter-spacing 0.5–0.8px, faint color.
- **Density & radius:** comfortable 20px card padding, 16px gap in KPI grids,
  20–28px page padding; card radius 12px (`--radius-md`), control/chip radius
  8px (`--radius-sm`), large card 16px (`--radius-lg`). Avatar 50% (circle),
  delta chips 100px (pill).
- **Shadows:** `--shadow-sm: 0 1px 3px rgba(0,0,0,.06), 0 1px 2px
  rgba(0,0,0,.04)`; `--shadow-md: 0 4px 12px rgba(0,0,0,.06), 0 2px 4px
  rgba(0,0,0,.04)`. Panels float on the page canvas with subtle depth.
- **Motion:** `.12s` background/color hover transitions. No bouncy easing.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Fixed sidebar** (240px, white bg, 1px right border, full-height): logo
  mark + wordmark → grouped nav sections (each with an uppercase micro-label +
  nav items with icon + label; active item gets indigo bg tint + indigo text);
  flex spacer; user row at the bottom (avatar + name + role + chevron).
- **Sticky topbar** (60px, white bg, 1px bottom border): breadcrumb trail on
  the left → search pill (bg input) in the center-right → notification icon
  button (with red dot) + help icon button + avatar chip on the far right.
- **Main content** (page bg, 28px pad, CSS grid `1fr 296px`): page header
  spanning full width, then the region stack below.
- **Page header** (full-width): title + subtitle on the left; date-range ghost
  button on the right.
- **KPI tile row** (full-width, 4-column equal grid): each tile = white card
  with shadow; header row = uppercase micro-label + icon chip (tinted bg +
  accent icon); big tabular figure below; footer = delta chip (green/red pill
  with arrow) + inline SVG sparkline (7-point path + gradient fill).
- **Left column (primary):** area chart card (title + meta + legend, then an
  SVG area chart with gridlines, axis labels, data-point dots, and gradient
  fill) followed by a records table card (title + "view all" action, then a
  dense table with user cell / source pill / flag / numerics / conversion badge,
  paged via a footer count + "view all" link).
- **Right rail (296px):** stacked cards — (1) donut chart card (SVG donut with
  center value + legend list + bar-track rows per category); (2) insights card
  (icon chip + prose observation rows with a bottom border divider); (3)
  activity feed card (colored dot + title + timestamp rows).
- **List screen:** full-page version of the records table — toolbar with search
  pill + filter chips + count, dense table, pager footer.
- **Form screen:** sectioned white cards of labeled fields; **rules appear as
  inline validation** — required marks (`*`), helper text under the field,
  inline error messages on invalid fields, disabled-until-valid primary submit.
  No rules/checklist/validation-status panel.
- **Detail screen:** breadcrumb → header band (title + status pill + key
  actions) → meta-grid card (label/value pairs, 2–3 columns) → related panels
  row (a sub-table or stat-row panel + an activity / timeline panel).

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
Domain (illustrative): a SaaS product growth analytics platform.

Sidebar sections → Overview (Dashboard active, Records), Acquisition (Users,
  Traffic Sources, Campaigns), Behaviour (Funnels, Heatmaps), Retention
  (Cohorts, Reports), System (Settings).

User row → "Marta Alves · Growth Lead".

Topbar breadcrumb → "Platform › Overview".

Page header → "Analytics Overview", "Week ending Jun 1, 2025 · All segments",
  date-range button "May 26 – Jun 1, 2025".

KPI tiles (4):
  • Total Sessions 48,312 (▲12.4%, indigo sparkline).
  • Unique Users 19,847 (▲8.7%, violet sparkline).
  • Conversion Rate 3.81% (▲0.4 pp, green sparkline).
  • Avg. Session 4m 22s (▼5.1%, amber sparkline).

Area chart → "Weekly Sessions" — 12-week dual-series (sessions + unique users),
  indigo + violet strokes with gradient fills, dot markers, gridlines, axis
  labels (Mar 17 → Jun 1).

Records table → "Recent Sessions": User (avatar + name + email) / Source pill
  (colored by channel) / Country (flag + name) / Duration / Pages / Converted
  (yes/no badge). Last 50 · footer "View all sessions".

Right rail:
  • Donut card → "Top Channels": Organic 38%, Paid 24%, Referral 19%, Social
    12%, Email 7%; center shows "48k · sessions".
  • Insights card → 3 bullet observations (organic up 22%, session drop 5.1%,
    conversion at 3.81% — highest since Dec 2024).
  • Activity feed → 5 items (goal created, A/B test significance, alert
    triggered, segment exported, campaign connected).

List screen → all records, search pill + filter chips (source, conversion),
  paginated dense table.

Form screen → "New Record": entity name (required), category (required select),
  numeric target (required, > 0), date range (required, not in the past),
  assignee (optional). Rules as required marks + helper text + inline errors;
  primary submit disabled until valid.

Detail screen → one record: breadcrumb, header (ID + status pill + Edit /
  Export buttons), meta-grid (entity, category, target, date, owner, created),
  related sub-table (period breakdown) + activity feed.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, status states, record columns, form fields + rules, detail
   fields — from the KB + prompt. Standalone: use the Example instantiation
   above.
3. Build each screen in the Visual language + Layout archetype above, imitating
   the example set in `assets/` (dashboard, list, form, detail) and the
   `assets/template.html` seed — with fresh content for the real domain, NOT
   the example labels.
4. Express domain rules as INLINE field validation (required marks, helper text,
   inline errors, disabled-until-valid submit). Never render
   rules/checklist/validation-status/build-note panels or designer/demo controls.
5. One inline `<style>`, semantic HTML5, `tabular-nums` on figures, no external
   assets, no CDNs — self-contained.

## Output contract

```
<artifact identifier="admin-aurora-analytics" type="text/html" title="Aurora Admin">
<!doctype html>...</artifact>
```
