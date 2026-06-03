---
name: admin-aegis-insurance
description: |
  Institutional light-mode admin aesthetic: white card surfaces on a cool
  #f6f8fb page, deep-navy sidebar (#0f2057) with teal accent (#14b8a6 /
  #5eead4), navy-600 (#2563eb) as the primary interactive color, and clean
  Inter type at 14px. Archetype = 240px grouped sidebar (entity switcher +
  labeled nav groups) + sticky topbar (breadcrumb + search + period tabs +
  avatar) + 4 KPI cards with inline sparklines + a horizontal 4-stage
  pipeline board + 2-column lower grid (wide records table · side detail
  panel) + full-width inline SVG trend chart.
triggers:
  - "light institutional admin"
  - "navy-teal sidebar admin"
  - "cool light-mode dashboard"
  - "card-surface operations admin"
  - "pipeline board admin"
  - "teal accent light admin"
  - "grouped sidebar dashboard"
  - "painel institucional claro"
example_prompt: "Apply this light institutional admin aesthetic to my domain"
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

# Aegis Admin — Visual Archetype

This plugin contributes a **look** (institutional light mode, deep-navy sidebar,
teal accent, card-surface layout) and a **structure** (entity-switcher sidebar +
topbar + KPI cards + pipeline board + records table + trend chart, plus list /
form / detail screens). It does **not** contribute a domain — the subject matter
comes from the Knowledge Base and the user's prompt. Treat the example below as
illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Every chromatic value declared as a `:root` CSS custom
property; neutral slate text may be hardcoded.

- **Page & surfaces:** page `#f6f8fb`; card/topbar `#ffffff`; card border
  `--clr-border: #e3e8f0`; card shadow `0 2px 8px rgba(0,0,0,0.05)`; card
  radius `10px`. Teal top-accent bar on KPI cards: 3px solid `--clr-teal-500`.
- **Sidebar:** deep navy `--clr-sidebar-bg: #0f2057`; active bg
  `--clr-sidebar-active: rgba(37,99,235,0.18)`; hover `rgba(255,255,255,0.06)`.
  Active item: 3px left border `--clr-navy-600` + tinted bg.
- **Primary/accent ramp:**
  `--clr-navy-900: #1e3a8a`, `--clr-navy-700: #1d4ed8`,
  `--clr-navy-600: #2563eb` (links, active states, CTAs, primary buttons),
  `--clr-navy-100: #dbeafe`, `--clr-navy-050: #eff6ff`.
  `--clr-teal-500: #14b8a6` (card top-bar, pipeline stages, chart series),
  `--clr-teal-300: #5eead4`, `--clr-teal-100: #ccfbf1`,
  `--clr-teal-700: #0f766e`.
- **Status ramp:** `--clr-green-500: #22c55e` / `--clr-green-100: #dcfce7` /
  `--clr-green-700: #15803d`; `--clr-amber-500: #f59e0b` /
  `--clr-amber-100: #fef3c7` / `--clr-amber-700: #b45309`;
  `--clr-red-500: #ef4444` / `--clr-red-100: #fee2e2`.
- **Text ramp (neutral, may hardcode):** primary `#1e293b`; secondary `#334155`;
  muted `#64748b`; faint `#94a3b8`.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
  sans-serif`. Base 14px / 1.5 line-height. Big KPI figures: 28px / weight 800 /
  letter-spacing −1px. Section micro-labels: 10–11px uppercase, letter-spacing
  0.6–1px, muted. Policy/record IDs: `"Menlo", "Consolas", monospace` at 12px.
  `font-variant-numeric: tabular-nums` on every numeric cell.
- **Controls:** inputs/selects: 1px `--clr-border` border, 8px radius, 36px
  height, background `#f6f8fb`. Primary button: `--clr-navy-600` fill, white
  text, 8px radius. Ghost button: transparent fill, `--clr-border` border,
  `--clr-navy-600` text.
- **Motion:** `0.12s–0.15s` background/border hover transitions, gentle ease.
  No bounce. Period-tabs and filter-chips swap with a background color shift.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns described by shape and behavior — not meaning.

- **Left sidebar** (240px, deep-navy, sticky full-height): brand mark (icon +
  wordmark + sub-label) → **entity switcher** (ghost pill with label + chevron)
  → labeled nav groups with section headings: each item = SVG icon + label +
  optional count badge. Active item: navy-600 left border (3px) + tinted bg.
  Footer: avatar initials chip + user name/role stack.
- **Sticky topbar** (60px, white, 1px border-bottom): breadcrumb title stack →
  **search pill** (icon + input, stretches center) → **period tabs** (MTD / QTD
  / YTD or equivalent short-period selectors) → bell icon with amber notification
  dot → avatar + name + chevron.
- **Main content** (#f6f8fb page bg, 24px padding, flex-column gap 24px):
  - **KPI card row** (4 equal cards): each card = white surface + teal 3px top
    bar + micro-label + big tabular figure + inline SVG sparkline + delta chip
    (green / amber / red pill with directional arrow).
  - **Horizontal pipeline board** (white card, 4 equal columns): each column =
    stage header pill (color-coded by stage) with count badge + 2–3 item mini-
    cards. Mini-card = colored left border (stage color) + ID + primary name +
    meta row (type + amount) + elapsed sub-line.
  - **Two-column lower grid** (`1fr 300px`): left = wide records table card
    (sticky uppercase header, dense rows, monospace ID column, status pills,
    "View all" link); right = side detail panel (header + count badge + list of
    items each with meta + CTA ghost button).
  - **Full-width trend chart card** (white, inline SVG, two-series area chart):
    header with legend dots + period tab row; Y-axis labels; X-axis period
    labels; two filled area series in nav-color and teal.
- **Records list screen:** full-width records-table archetype as its own page —
  toolbar (search input + filter chips with counts) + the same dense table + pager.
- **Record form screen:** sectioned white cards of labeled fields; **rules appear
  as inline validation** — required marks (`*`), helper text under the field,
  inline error messages on invalid fields, submit disabled-until-valid. No
  rules/checklist/validation-status panel.
- **Record detail screen:** breadcrumb + detail header band (title + status pill
  + actions) + meta grid (label/value pairs, 3-column) + related sub-panels
  (mini-table or status rows) below.

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key metrics,
status states, pipeline stages, record list columns, form fields and their rules,
and detail fields — and map them onto the archetype above. If no KB/domain is
supplied (standalone), use the Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules
become inline field validation. Do NOT render build/implementation notes or
designer controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent
> (entities, metrics, stages, columns, fields) drawn from the KB + prompt.

```
Domain (illustrative): an institutional insurance carrier back-office.

Entity switcher     → "All Lines of Business" (Auto / Property / Liability / Life).
Nav groups          → Overview (Dashboard, Analytics) / Operations (Policies, Claims,
                      Renewals, Reinsurance) / Admin (Agents, Reports, Settings).
User footer         → "Sarah Keller · Operations Lead".

KPI cards (4):
  • Active Policies  48,312  · sparkline navy-line  · ▲ +3.2% green
  • Open Claims      1,847   · sparkline red-bar    · ▲ +12 this week amber
  • Renewals Due     3,204   · sparkline amber-line  · ▼ −8% amber
  • Loss Ratio       61.4%   · sparkline teal-line   · ▼ −2.1pp green

Pipeline board (4 stages):
  Filed → In Review → Approved → Paid
  Each stage has 2–3 claim mini-cards: claim # + holder + type + amount + days.
  Left borders: red (Filed) / amber (Review) / teal (Approved) / green (Paid).

Lower grid:
  Table  → "Active Policies": Policy # | Holder | Line | Premium | Effective | Status pill
            Status pills: Active (green), Lapsed (red), Pending (amber), Cancelled (slate).
  Panel  → "Renewals Due — Next 30 Days": 5 items each with policy # + holder +
            type + renewal date + premium + "Send Notice" ghost button.

Trend chart → two-series area: Filed (navy) + Paid (teal), 12 monthly data points.
              Period tabs: 6M / 12M / 24M.

List screen  → all policy records, search + filter chips (status, line of business),
               paginated dense table.

Form screen  → "New Record": primary entity ID (required), description, quantity /
               coverage amount (required, > 0), category select (required), effective
               date (required, not in the past), priority. Rules as required marks +
               helper text + inline errors; submit disabled until valid.

Detail screen → one record: breadcrumb + header (ID + status pill + actions),
                meta grid (holder, line, premium, effective, agent, created),
                related sub-panels (timeline entries + linked records mini-table).
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, pipeline stages, status states, record columns, form fields +
   rules, detail fields — from the KB + prompt. Standalone: use the Example
   instantiation above.
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
<artifact identifier="admin-aegis-insurance" type="text/html" title="Aegis Admin">
<!doctype html>...</artifact>
```
