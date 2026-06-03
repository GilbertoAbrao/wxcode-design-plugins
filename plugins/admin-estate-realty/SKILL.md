---
name: admin-estate-realty
description: |
  Refined light-mode admin aesthetic: near-white canvas (#f7f9f9), deep teal
  sidebar (#0f2623), teal accent (#0d9488 / #14b8a6), 12px-radius white cards
  with teal shadow, Inter type with tabular figures, medium-density rows, and
  crisp status pills. Archetype = deep-teal 240px left sidebar (brand mark +
  entity switcher + grouped nav with section headers) + sticky 60px topbar
  (search pill + filter select + notification bell + avatar) + 4 KPI cards with
  inline sparklines + 2-column grid (60/40: records table + ranked leaderboard
  panel) + full-width horizontal pipeline (5 stage-columns with deal chips).
  Built for light, breathable back-office dashboards where clarity and refinement
  read at a glance.
triggers:
  - "light teal admin"
  - "refined light-mode dashboard"
  - "teal sidebar admin"
  - "white card back-office"
  - "sparkline KPI admin"
  - "ranked leaderboard panel"
  - "horizontal pipeline admin"
  - "sidebar switcher admin"
example_prompt: "Apply this refined light teal admin aesthetic to my domain"
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

# Estate Realty Admin — Visual Archetype

This plugin contributes a **look** (refined light-mode, deep-teal sidebar,
teal accent, white card surfaces) and a **structure** (teal sidebar + topbar +
KPI cards + records table + leaderboard + horizontal pipeline, plus list / form /
detail screens). It does **not** contribute a domain — the subject matter comes
from the Knowledge Base and the user's prompt. Treat the example below as
illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property; keep the teal/white ramp intact.

- **Canvas / surfaces:** page `#f7f9f9`; card/panel `#ffffff`; sidebar `#0f2623`;
  topbar `#ffffff`; subtle bg `#fafcfc`; hairline border `#e3e9e9`.
- **Text ramp:** primary `#1e2d2b`, muted `#64748b`, sidebar-text `#a8c5c2`,
  sidebar-active `#e2f0ef`, sidebar-head `rgba(255,255,255,0.30)`.
- **Accent:** `--color-accent: #0d9488`, `--color-accent-mid: #14b8a6`,
  `--color-accent-active: #5eead4`, `--color-accent-hover: #0b7a70`,
  `--color-accent-light: #ccfbf1`, `--color-accent-faint: #f0fdfa`. Primary
  CTAs, active nav, key figures, sparkline strokes, progress fills.
- **Status ramp (as tokens):** `--color-success #16a34a` (bg `#dcfce7`),
  `--color-warning #d97706` (bg `#fef3c7`), `--color-danger #dc2626`
  (bg `#fee2e2`). Type-distinction pills: `--color-pill-blue #1d4ed8`
  (bg `#dbeafe`), `--color-pill-violet #6d28d9` (bg `#ede9fe`),
  `--color-pill-amber #854d0e` (bg `#fef9c3`).
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
  sans-serif`. Base 14px. `font-variant-numeric: tabular-nums` on every numeric
  cell. KPI figures 28px / weight 800 / `letter-spacing: -0.03em`. Section-header
  labels 10px, uppercase, `letter-spacing: 0.07em`, muted.
- **Density & radius:** 11px vertical row padding, 18–20px card padding, 16px
  grid gap; card radius `--radius-card: 12px`, control radius 8px, pill radius
  20px (rounded-full), avatar 50%.
- **Borders & shadows:** 1px `#e3e9e9` borders on cards; `--shadow-card:
  0 2px 10px rgba(13,148,136,0.07)` on white cards; no drop shadow on sidebar.
- **Motion:** `.12s–.15s` background/border/color hover transitions; sidebar
  active item has a 3px left bar; no bounce.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Left sidebar** (240px, dark bg, sticky, full viewport height): brand mark
  + wordmark at the top → **entity switcher** (pill/block dropdown with label
  + name + chevron) → grouped nav with uppercase **section headers** (9.5px,
  tracking 0.09em) and nav items (icon + label + optional count badge); active
  item has a teal left-bar and teal-tinted background; footer row: avatar
  initials circle + name/role + settings cog.
- **Top bar** (60px, white bg, 1px bottom border, sticky): page title on the
  left → centered **search pill** (magnifier icon + input, max 380px) → right:
  **dimension filter select** + notification bell with dot badge + avatar circle
  + short name.
- **Main content** (page bg, 24px padding, vertical flow): a **page header**
  (title + sub-line left, ghost + primary buttons right), then the region stack.
- **KPI card row** (4 cards, equal-width grid): each card = white panel, 12px
  radius, teal shadow; **uppercase micro-label** → **big tabular figure** →
  footer row: **delta chip** (up/down/flat with arrow icon + colored bg) + inline
  **SVG sparkline** (5-point polyline, teal/danger/warning stroke, dot at tail).
- **2-column grid (60fr / 40fr):**
  - **Left — records table:** a titled panel with a sub-line count + `View all`
    link; sticky uppercase thead; dense rows with zebra-light tint and teal hover;
    a **thumbnail cell** (small icon-placeholder + two-line text), **type pills**,
    **status pills**, and an **agent/member cell** (initials circle + name);
    table footer with result count + pager buttons.
  - **Right — ranked leaderboard:** a titled panel; rows of `[rank/medal]
    [avatar initials] [name / stats line] [value figure + horizontal bar]`;
    bar width scaled to max; teal accent on the bar fill; gold/silver/bronze
    rank tokens for the top three.
- **Full-width horizontal pipeline:** a titled panel; body is a 5-column grid of
  **stage columns** — each has a stage name (11px uppercase) + count badge, then
  2–3 **deal/record chips** (two-line: title + sub-tag/price); active/highlight
  chips get a teal border + faint teal bg; final-stage chips use success border +
  faint green bg; vertical dividers between columns.
- **Records list screen:** search + filter-chip toolbar (count badge per chip) +
  the records-table archetype as its own page with pager.
- **Record form screen:** sectioned white cards of labelled fields; **rules
  appear as inline validation** — required marks (`*`), helper text under the
  field, inline error messages on invalid fields, disabled-until-valid submit.
  No rules/checklist/validation-status panel.
- **Record detail screen:** breadcrumb → header band (ID + status pill + key
  actions) → meta grid (3-col label/value cards) → related-data panels below
  (sub-table or status rows + activity feed).

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key metrics,
status states, record columns and thumbnail type, form fields and their rules,
leaderboard dimension, pipeline stage names, and detail fields — and map them
onto the archetype above. If no KB/domain is supplied (standalone), use the
Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules
become inline field validation. Do NOT render build/implementation notes or
designer controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent
> (entities, metrics, states, columns, fields) drawn from the KB + prompt.

```
Domain (illustrative): a real-estate brokerage back-office.

Entity switcher  → office: "Downtown SF".
Page context     → "June 2026 · Downtown SF Office".
Sidebar sections → OVERVIEW, LISTINGS, DEALS, TEAM.

KPI tiles (4):
  • Active Listings 47 (▲+6 vs last mo., teal sparkline).
  • Deals in Progress 23 (▲+3 this week, teal sparkline).
  • Avg Days on Market 18 (▼−4 days, red sparkline).
  • Commission MTD $412k (±0.8%, amber sparkline).

Records table (left, 60%) → "Active Listings": property thumbnail + address +
  MLS#, price, type pill (Residential / Commercial / Land), status pill
  (Active / Pending / Under Contract / Sold), agent initials + name.
  8 rows shown, pager.

Leaderboard (right, 40%) → "Top Agents · by Gross Commission Income": rank
  medal (🥇🥈🥉 / 4–6), avatar initials, agent name, listing/closed stats,
  GCI figure, scaled horizontal bar.

Pipeline (full-width) → 5 stages: Prospect → Offer Made → Under Contract →
  Inspection → Closed; 2–3 chips per stage showing abbreviated address + price
  tag; highlighted chips at active stage; closed chips in success green.

List screen     → all listings, search + filter chips (type, status), paginated.

Form screen     → "New Listing": address (required), asking price (required, > 0),
  type (required select), listing agent (required select), go-live date (required,
  not in the past), notes. Required marks + helper text + inline errors;
  "Create Listing" disabled until valid.

Detail screen   → one listing: breadcrumb → header (address + status pill +
  Edit / Archive buttons) → meta grid (price, type, agent, MLS#, listed date,
  days on market) → related panels: deal history sub-table + activity feed.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, status states, record columns, thumbnail/icon type, form fields
   + rules, leaderboard dimension, pipeline stages, and detail fields — from the
   KB + prompt. Standalone: use the Example instantiation above.
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
<artifact identifier="admin-estate-realty" type="text/html" title="Estate Realty Admin">
<!doctype html>...</artifact>
```
