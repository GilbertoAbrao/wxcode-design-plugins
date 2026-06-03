---
name: admin-statute-legal
description: |
  Refined light-mode professional admin aesthetic: warm-white canvas (#faf8f6),
  deep-burgundy primary accent (#9f1239 / #be123c), gold secondary accent
  (#b45309 / #d97706), Inter type with tabular-nums on figures, 14px body,
  10px uppercase micro-labels, white raised cards with a 3px burgundy top
  stripe, hairline #e8e2dc borders, and crisp status pills. Archetype = dark
  sidebar with an entity-switcher grouped nav + a top bar with global search +
  period selector + 4 KPI tiles + 2-column grid (records table left, deadline
  feed + horizontal bar chart right) + full-width documents list. Built for
  professional service consoles that must feel authoritative and approachable.
triggers:
  - "warm-white professional admin"
  - "burgundy gold light admin"
  - "refined professional dashboard"
  - "dark sidebar light content admin"
  - "law-firm aesthetic admin"
  - "authoritative light-mode console"
  - "gold accent professional admin"
  - "painel profissional claro"
example_prompt: "Apply this refined warm-white professional admin aesthetic to my domain"
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

# Statute Admin — Visual Archetype

This plugin contributes a **look** (refined warm-white, deep-burgundy + gold
accents, dark sidebar, professional density) and a **structure** (dark
sidebar entity-switcher nav + top bar + KPI tiles + records table + deadline
side panel + bar chart + documents list, plus list / form / detail screens).
It does **not** contribute a domain — the subject matter comes from the
Knowledge Base and the user's prompt. Treat the example below as
illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS
custom property; hardcode the neutral warm-white ramp.

- **Canvas / surfaces:** page `#faf8f6`; raised card `#ffffff`; sidebar
  `#1e1714`; sidebar hover `#2d2420`; sidebar active `#3a2820`.
- **Text ramp:** headings `#1e293b`; body `#334155`; muted `#64748b`; sidebar
  primary `#d6cfc8`; sidebar muted `#8b7f78`.
- **Borders:** main `#e8e2dc`; inner rows `#f4f0ec`; sidebar separator `#2d2420`.
- **Primary accent (burgundy):** `--clr-accent: #9f1239`;
  `--clr-accent-hi: #be123c`; `--clr-accent-subtle: #fdf2f4`;
  `--clr-accent-muted: #fce7eb`. CTAs, active nav left-bar, key figures, mono
  IDs, pill borders, focus rings, card top stripes.
- **Secondary accent (gold):** `--clr-gold: #b45309`; `--clr-gold-hi: #d97706`;
  `--clr-gold-subtle: #fffbeb`. Secondary CTAs, progress fills, alternate card
  top stripes, bar-chart fills.
- **Status ramp (as tokens):** `--status-active-bg: #dcfce7` /
  `--status-active-fg: #15803d`; `--status-pending-bg: #fef3c7` /
  `--status-pending-fg: #b45309`; `--status-closed-bg: #f1f5f9` /
  `--status-closed-fg: #64748b`; `--status-urgent-bg: #ffe4e6` /
  `--status-urgent-fg: #be123c`. Deltas: up `#dcfce7 / #15803d`; down
  `#ffe4e6 / #be123c`; warn `#fef3c7 / #b45309`. Urgency dots: urgent
  `var(--clr-accent-hi)`; warn `var(--clr-gold-hi)`; ok `#16a34a`.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
  sans-serif`. Base 14px / 1.5 line-height. `font-variant-numeric: tabular-nums`
  on **every** numeric cell. Micro-labels 10–11px, `text-transform: uppercase`,
  `letter-spacing` ~.05–.08em, muted slate. Big figures 28–30px / weight 700 /
  `line-height: 1`. Mono IDs in `ui-monospace, "Cascadia Code", "Fira Code",
  monospace`.
- **Density & radius:** 11px vertical row padding; 16–20px panel padding;
  14–16px grid gaps; card radius 10px; control radius 6–8px; pill radius 20px;
  progress bars 5px tall / 3px radius; sidebar nav-item radius 6px.
- **Borders & shadows:** `box-shadow: 0 2px 8px rgba(0,0,0,0.05)` on white
  cards; 1px hairlines for separation; no heavy drop shadows. Each white card
  carries a 3px top stripe in the accent color.
- **Motion:** `.12s–.15s` background/border/color transitions on nav items,
  table rows, and buttons. No bounce; subtle ease.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Left sidebar** (240px, dark `#1e1714`, full-height sticky): brand monogram
  chip + org name/tagline at top → **entity-switcher** (dark select with
  category label) → **grouped nav sections** (section micro-label + nav items
  with icon + label + optional badge; active item: burgundy left bar + tinted
  background) → footer with logged-in user chip (avatar dot + name + role sub-line).
- **Top bar** (60px, white, 1px bottom border, sticky): page title on the left
  → flexible **global search** pill → **period selector** (grouped pill buttons,
  one active in accent) → icon buttons (bell with notification dot) → user avatar.
- **Page header strip** (below topbar, above tiles): timestamp/context line +
  summary metric chip + ghost export button + accent primary CTA.
- **KPI tile row** (4 tiles, equal grid): each = white card with 3px accent top
  stripe, a large ghosted SVG icon (top-right, 15% opacity), a micro-label, a
  big tabular figure, a sub-line with optional delta chip or progress bar. Burgundy
  and gold alternate for visual rhythm.
- **2-column grid (2/3 + 1/3):**
  - **Left — records table card:** titled card with a "View all →" link header;
    sticky uppercase 11px table header; dense rows with a `font-variant-numeric`
    numeric column, a monospace ID column, status pills, and a ghost action link;
    row hover tinted.
  - **Right — deadline / events feed + bar chart:**
    - **Deadline feed card:** rows of `[urgency dot] [mono ref] [description]
      [date]` with colored dots (urgent/warn/ok).
    - **Distribution chart card:** horizontal bar rows —
      `[label 80px right-aligned] [bar track: filled + count label inside]`.
      Bars alternate accent and gold.
- **Full-width documents / items list:** card with header action link; rows of
  `[type icon chip] [title + meta sub-line] → [date right-aligned] [ghost view
  link]`; row hover tinted.
- **Records list screen:** standalone page — search input + filter chips (with
  count badges, one active) + result count, the records-table archetype, pager.
- **Record form screen:** sectioned cards of labelled fields; **rules appear as
  inline validation** — required marks (`*`), helper text under the field, and
  inline error messages on invalid fields, with the primary submit
  disabled-until-valid. No rules/checklist/validation-status panel.
- **Record detail screen:** breadcrumb + header band (mono ID + status pill +
  key action buttons) + meta grid (label/value pairs, 3-col) + related-data
  sub-panels (operations/routing rows or a mini-table + activity timeline) below.

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
Domain (illustrative): a professional-services matter management portal
for a multi-practice firm.

Sidebar entity switcher → scope: "All Practices" (options: Corporate & M&A,
  Litigation, Real Estate, Employment Law, Intellectual Property).
Sidebar nav groups     → OVERVIEW (Dashboard, Matters, Clients, Calendar),
  BILLING (Timesheets, Invoices, Receipts), SETTINGS (Team, Roles, Integrations).
Topbar title           → "Matter Overview".
Period selector        → 24H / This Month (active) / Q2 / YTD.

KPI tiles (4):
  • Active Cases 42  (▲+5 vs last month; burgundy stripe).
  • Billable Hours MTD 1,284  (target 1,500 hrs; progress bar 85.6%; gold stripe).
  • Deadlines This Week 7  (⚠ 2 urgent; burgundy stripe).
  • Realization Rate 87%  (▲+3pp vs Q1 avg; gold stripe).

Records table (left)   → "Active Matters" — columns: Matter# / Client /
  Practice Area / Lead Person / Status pill / Action. Status: Active / Urgent /
  Pending / Closed.

Deadline feed (right)  → "Upcoming Deadlines" — rows of urgency dot +
  mono reference + description + date. Urgency: urgent/warn/ok dots.

Bar chart (right)      → "Distribution by Category" — horizontal bars,
  label + burgundy/gold bars with count inside.

Documents list (full)  → "Recent Documents" — icon chip + title + meta
  (reference + uploaded-by) → date + ghost view link.

List screen            → all records, search + filter chips (status, category),
  paginated.

Form screen            → "New Record": code/reference (required, mono format),
  description, quantity/amount (required, > 0), category (required select),
  due date (required, not in the past), assignee. Rules shown as required marks
  + helper text + inline errors; "Create" disabled until valid.

Detail screen          → one record: breadcrumb + header (mono ID + status pill +
  Edit/Archive actions), meta grid (category, assignee, amount, due, owner,
  created), a related sub-table + activity timeline.
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
<artifact identifier="admin-statute-legal" type="text/html" title="Statute Admin">
<!doctype html>...</artifact>
```
