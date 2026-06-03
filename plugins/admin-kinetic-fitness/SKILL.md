---
name: admin-kinetic-fitness
description: |
  Energetic dark-green admin aesthetic: deep forest-green canvas (#0f1410),
  raised panels (#19211a / #232e25), lime accent (#84cc16) on a muted-green
  neutral ramp, Inter type with tabular-nums on every figure, compact 13px
  rows, 10px radii, hairline #2c3a2f borders, and crisp status pills. Archetype
  = slim topbar (brand + search + entity-switcher + avatar) + icon rail + 4 KPI
  tiles + 2-column row (schedule/slot-list with inline capacity bars + area-chart
  card) + full-width records table with plan-tier and status pills + 3-card
  personnel panel. Built for high-density operational consoles with an energetic,
  athletic character.
triggers:
  - "dark green admin"
  - "energetic dark admin"
  - "lime accent dashboard"
  - "forest-green operations console"
  - "athletic dark admin"
  - "capacity-bar schedule panel"
  - "dark green data dense"
  - "painel verde escuro"
example_prompt: "Apply this energetic dark-green admin aesthetic to my domain"
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

# Kinetic Admin — Visual Archetype

This plugin contributes a **look** (energetic dark-green, lime accent, dense
tabular data) and a **structure** (slim topbar + icon rail + KPI tiles +
schedule/capacity panel + chart card + records table + personnel cards, plus
list / form / detail screens). It does **not** contribute a domain — the subject
matter comes from the Knowledge Base and the user's prompt. Treat the example
below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property; hardcode the neutral dark-green ramp.

- **Canvas / surfaces:** page `#0f1410`; raised panel `#19211a`; inset / hover
  `#232e25`; hairline border `#2c3a2f`; stronger hover border `#3a4c3d`.
- **Text ramp:** primary `#e6efe6`, secondary `#c5d5c5`, muted `#93a392`, faint
  `#5a6e5a`.
- **Accent:** `--accent: #84cc16` (lime green), `--accent-bright: #a3e635`,
  `--accent-dim: rgba(132,204,22,.18)`, `--accent-muted: rgba(132,204,22,.08)`.
  Primary CTAs, active nav bar, key figures, progress fills, chart strokes.
- **Status ramp (as tokens):** `--state-active #84cc16`, `--state-frozen
  #60a5fa`, `--state-overdue #f87171`, `--state-pending #f59e0b`, each with a
  `…-bg` tint at ~13% alpha for pill backgrounds. Deltas: `--delta-up #84cc16`,
  `--delta-down #f87171`.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
  sans-serif`. Base 13px. `font-variant-numeric: tabular-nums` on **every**
  numeric cell. Micro-labels are 10–11px, `text-transform: uppercase`,
  `letter-spacing` ~.08em, muted. Big figures 28px / weight 800 /
  `letter-spacing: -.03em`. Codes in a mono face (`"Courier New", monospace`).
- **Density & radius:** compact 11px vertical row padding, 18–20px tile padding,
  16px grid gaps; panel radius 10px, control radius 7–8px, pill radius 20px,
  capacity bars 5–6px tall / 3px radius.
- **Borders & shadows:** 1px hairlines do the separation work; no drop shadows
  on panels (flat, athletic-terminal feel). 1px inner row dividers `#232e25`.
- **Motion:** subtle only — `.12s` background/border hover transitions, `.3s`
  width transitions on capacity bars. Default easing stays gentle; never bouncy.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Top topbar** (48px, `#19211a`, 1px bottom border, sticky): brand icon + name
  in accent → **search** pill (dark bg) → flexible spacer → **entity-switcher**
  (pill button with leading icon + chevron, entity name) → notification icon with
  dot → avatar circle (initials) + name + chevron.
- **Left icon rail** (52px, `#19211a`, 1px right border): 4–6 icon-only nav
  items (active item has accent color + left accent bar + inset bg; hover lifts
  to inset bg), a divider, then additional items. Each carries a native `title`
  tooltip. No text labels.
- **Main content** (page bg, 20–24px padding, vertical flex flow): a **page
  header** (title + sub-line on the left, ghost + primary buttons on the right),
  then the region stack below.
- **KPI tile row** (4 tiles, equal grid, gap 16px): each tile = raised panel
  with an icon chip top-right, an uppercase micro-label, a big tabular figure,
  an optional sub-line, and a delta chip. Figures and icon chips recolor by state
  (lime / amber / red) via token.
- **2-column row (7fr / 5fr, gap 16px):**
  - **Left — slot/schedule board:** a titled panel whose rows are
    `[time] [item name] [facilitator] [capacity bar + fraction]`. Capacity bars:
    thin filled-lime bars with a "Full" pill when capacity is reached. Followed or
    preceded by a view-all link.
  - **Right — area-chart card:** a titled panel with a sub-label, a legend, and
    an inline SVG area chart (two series: current/lime fill + prior/muted dashed
    line). X-axis label row + dotted gridlines.
- **Full-width records table:** titled panel with ghost + primary header actions,
  a sticky uppercase header, dense rows with **status pills**, an avatar-initial
  column, plan/tier text, right-aligned numerics, last-activity timestamp, and a
  footer with a result count + pager.
- **Personnel card row** (3 cards, equal grid): each card = inset-bg panel with
  an avatar circle (initials, lime bg, dark text) + name + specialty tag +
  this-period activity count + star rating (lime stars).
- **Records list screen:** the records-table archetype as its own page —
  search + filter chips + a count, the same dense table, and a pager.
- **Record form screen:** sectioned cards of labelled fields; **rules appear as
  inline validation** — required marks (`*`), helper text under the field, and
  inline error messages on invalid fields, with the primary submit
  disabled-until-valid. No rules/checklist/validation-status panel.
- **Record detail screen:** a header band (title + status pill + key actions), a
  meta grid of label/value pairs, and one or more related-data sub-panels (the
  slot-board row pattern or a mini-table) below.

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
Domain (illustrative): a boutique fitness studio and gym operations back-office.

Entity switcher → location: "Downtown Studio ▾".
Rail items       → Dashboard, Members, Schedule, Classes, Analytics, Settings.

KPI tiles (4):
  • Active Members 1,847 (lime, ▲ +34 this month, person icon).
  • Check-ins Today 312 (▲ +18 vs yesterday, scan icon).
  • Classes Today 18 ("8 completed · 10 upcoming", calendar icon).
  • 30-Day Retention 91.4% (▲ +1.2 pp, shield-check icon).

Schedule board (left) → "Today's Classes" — rows of
  [06:00] [HIIT Ignite] [Coach Priya Mehra] [████░░ 24/30].
  [07:30] [Power Lift] [Coach Dom Vasquez] [████░░░░ 16/30].
  [09:00] [Yoga Flow] [Coach Anika Torres] [██████████ 20/20 · Full pill].
  [10:30] [Spin Burn] [Coach Dev Okafor] [█████░░░░ 18/28].
  [12:00] [Core & Stretch] [Coach Priya Mehra] [██░░░░░░ 8/25].
  [17:00] [Boxing Basics] [Coach Marcus Reid] [███░░░░░ 12/20].

Chart card (right) → "Weekly Attendance" — area chart, two series:
  This week (lime fill/stroke): [210, 280, 265, 310, 290, 420, 380].
  Last week (muted dashed, no fill): [195, 255, 240, 285, 270, 395, 360].
  X-axis: Mon Tue Wed Thu Fri Sat Sun.

Records table → "Members": Name + avatar / Plan / Status pill / Last Visit /
  Actions.  Status: Active (lime) / Frozen (blue) / Overdue (red).

List screen → all members, search + filter chips (status, plan type),
  paginated.

Form screen → "New Member": full name (required), email (required, valid email),
  plan (required select), start date (required, not in the past), emergency
  contact (optional). Rules shown as required marks + helper text + inline
  errors; "Add Member" disabled until valid.

Detail screen → one member: header (name + status pill + actions), meta grid
  (plan, join date, last visit, check-ins this month, retention score), and a
  "Upcoming Classes" slot-board + recent activity feed.

Personnel panel → 3 personnel cards: [avatar] [name] [specialty tag]
  [activity count this week] [★ rating].
  • Priya Mehra | HIIT & Yoga | 8 sessions | ★★★★★ 4.9
  • Dom Vasquez | Strength     | 6 sessions | ★★★★☆ 4.7
  • Marcus Reid  | Boxing & HIIT| 5 sessions | ★★★★★ 4.8
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
<artifact identifier="admin-kinetic-fitness" type="text/html" title="Kinetic Admin">
<!doctype html>...</artifact>
```
