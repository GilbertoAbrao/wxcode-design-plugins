---
name: admin-saas-bestseller
description: |
  Polished light-mode SaaS admin aesthetic: near-white canvas (#f5f7fa),
  white card surfaces, indigo accent (#5369f8), soft 1–2px shadows, 12px card
  radius, system font stack. Archetype = collapsible 256px grouped-nav left
  sidebar + breadcrumb topbar (search + notification + avatar) + greeting strip +
  4 stat tiles with sparklines + 8/4 mid-grid (area chart card / activity feed) +
  full-width records table card. Built for clean, buyer-recognizable polished
  admin interfaces.
triggers:
  - "polished light admin"
  - "clean card admin"
  - "indigo accent admin"
  - "soft shadow admin"
  - "sidebar breadcrumb dashboard"
  - "sparkline stat tiles"
  - "activity feed dashboard"
  - "painel claro polido"
example_prompt: "Apply this polished light-mode admin aesthetic to my domain"
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

# SaaS Admin Bestseller — Visual Archetype

This plugin contributes a **look** (clean light-mode, indigo accent, white card
surfaces, soft shadows) and a **structure** (grouped-nav sidebar + breadcrumb
topbar + greeting strip + stat tiles + mid-grid chart/feed + records table, plus
list / form / detail screens). It does **not** contribute a domain — the subject
matter comes from the Knowledge Base and the user's prompt. Treat the example
below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property.

- **Canvas / surfaces:** page `#f5f7fa`; card/panel `#ffffff`; sidebar `#ffffff`;
  topbar `#ffffff`; input background `#f5f7fa`; hover row `#f9fafb`.
- **Borders:** `--border: #e8eaed`; hairline dividers 1px.
- **Text ramp:** primary `#111827`; secondary `#6b7280`; muted `#9ca3af`.
- **Accent:** `--indigo: #5369f8`; `--indigo-dark: #3d52d5`; `--indigo-light:
  #eef0fe`. Primary CTAs, active nav bar, active period tabs, links.
- **Semantic deltas:** `--green: #10b981` / `--green-light: #d1fae5` (positive
  deltas, active status); `--red: #ef4444` / `--red-light: #fee2e2` (negative
  deltas, alert dot, past-due); `--orange: #f59e0b` / `--orange-light: #fef3c7`
  (trial / warning status).
- **Typography:** `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
  "Helvetica Neue", Arial, sans-serif`. Base 14px. Section header labels
  10px / weight 600 / uppercase / `letter-spacing: 0.08em` / muted. Card titles
  15px / weight 700. Big stat figures 26px / weight 800 / `letter-spacing: -0.5px`.
  `font-variant-numeric: tabular-nums` on every numeric cell. IDs and codes in
  `"Courier New", monospace`.
- **Density & radius:** sidebar nav item 8px vertical padding; tile 20px padding;
  card header 20px padding; table row 12px vertical padding. Card radius 12px;
  nav-item radius 8px; button radius 8px; pill radius 20px; control radius 6px.
- **Shadows:** `0 1px 2px rgba(15,23,42,.04), 0 2px 8px rgba(15,23,42,.04)` on
  cards/tiles. No heavy drop shadows.
- **Motion:** `0.12s–0.15s` background / border / color transitions on interactive
  elements. No bouncy easing.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Left sidebar** (256px, white, 1px right border, vertical flex): brand mark
  (32px rounded square + wordmark) pinned at top in a 64px brand row; then
  **grouped nav** with section-header labels (10px uppercase muted) and nav items
  (icon + label + optional count badge); sidebar footer with avatar row (user
  initials chip + name + role + chevron).
- **Topbar** (64px, white, 1px bottom border, sticky): breadcrumb on the left
  (`Home / Screen`); centered **search pill** (max 320px); right cluster: icon
  button with notification dot + help icon button + divider + avatar chip + name
  + chevron.
- **Greeting strip** (below topbar, in scroll container): heading + date line on
  the left; "Export" ghost button + primary "+ New" CTA on the right.
- **4 stat tiles** (equal-width grid row): each tile = white card with small
  uppercase label + icon chip (top-right), large tabular figure, then a footer row
  with a color delta chip (green up / red down) + inline SVG sparkline.
- **8/4 mid-grid:**
  - **Left (8 cols) — chart card:** title + period tabs (24H / 7D / 30D / YTD) at
    top; legend row; inline SVG area chart with dotted gridlines + axis labels.
  - **Right (4 cols) — activity feed:** card with title, rows of `[color dot]
    [action text with bold actor] [relative timestamp]`, subtle bottom-border
    dividers between rows.
- **Full-width records table card:** title + "View all" link header, sticky
  uppercase thead, dense tbody rows with hover tint, columns: entity name +
  sub-label (avatar chip optional), category/plan pill, right-aligned numeric,
  date, status pill. Table footer with result count + pagination buttons.
- **List screen:** the records-table archetype as its own page — search pill +
  filter chips + count, the same dense table with full-width layout, and a pager.
- **Form screen:** sectioned white cards of labelled fields; **rules appear as
  inline validation** — required marks (`*`), helper text under each field, and
  inline error messages with an alert glyph on invalid fields; primary submit
  `disabled` until valid. No rules/checklist/validation-status panel.
- **Detail screen:** breadcrumb → header strip (ID/name + status pill + ghost +
  primary action buttons) → meta grid (3-col label/value pairs in a card) →
  two related-data sub-panels (a category/operations list card + an activity
  timeline card) below.

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key metrics,
status states, record columns, form fields and their rules, and detail fields —
and map them onto the archetype above. If no KB/domain is supplied (standalone),
use the Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules
become inline field validation. Do NOT render build/implementation notes or
designer controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent
> (entities, metrics, states, columns, fields) drawn from the KB + prompt.

```
Domain (illustrative): a B2B workflow-automation SaaS platform.

Sidebar nav groups:
  MAIN     → Dashboard (active), Workflows, Runs, Integrations
  MANAGE   → Customers, Billing, Team
  SETTINGS → Profile, API Keys, Webhooks

Greeting strip → "Good morning, Jamie" + date + "Export" ghost + "New Workflow" primary.

Stat tiles (4):
  • Monthly Revenue $48.2K (▲12%, sparkline, indigo icon chip).
  • Active Workflows 1,284 (▲3%, sparkline, green icon chip).
  • Churn Rate 2.4% (▼0.3%, sparkline, red icon chip).
  • NPS Score 71 (▲4 pts, sparkline, orange icon chip).

Chart card (left) → "Revenue — Monthly Recurring" area chart in indigo,
  period tabs 24H / 7D / 30D / YTD, legend shows "Current" vs "Previous".

Activity feed (right) → rows like:
  [indigo dot] Marcus H. created workflow "Lead nurture" · 2 min ago
  [green dot] Acme Corp upgraded to Scale · 18 min ago
  [red dot] Stripe webhook failed for Orbit Ltd · 1 hr ago

Records table → "Recent Customers": name+email / plan pill (Free / Starter /
  Scale / Enterprise) / MRR / Signup Date / Status pill (Active / Trial /
  Past Due).

List screen → all customers, search + filter chips (status, plan), paginated.

Form screen → "New Customer": company (required), contact email (required,
  valid format), plan (required select), MRR (required, ≥ 0), trial end date
  (required when plan = Trial, not in the past). Rules shown as required marks +
  helper text + inline errors; "Create Customer" disabled until valid.

Detail screen → one customer: breadcrumb (Customers › Acme Corp), header
  (name + status pill + "Export" ghost + "Edit" primary), meta grid (plan, MRR,
  signup date, owner, billing email, trial end), "Active Subscriptions" list card +
  "Recent Activity" feed card.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens (indigo on near-white canvas, white cards, soft shadows).
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
<artifact identifier="admin-saas-bestseller" type="text/html" title="SaaS Admin">
<!doctype html>...</artifact>
```
