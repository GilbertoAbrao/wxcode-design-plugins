---
name: admin-sterling-bankops
description: |
  Sober light-mode admin aesthetic: white card surfaces on a cool-grey page
  (#f7f8fa), slate-blue (#475569 / #334155) structural chrome with an emerald
  (#10b981) positive accent, Inter type with tabular-nums on every figure,
  comfortable 14px density, 10px card radii, 1px #e4e7ec borders, and crisp
  status pills. Archetype = grouped-nav sidebar (entity switcher + section
  labels) + white topbar (search + period tabs + avatar) + 4 KPI cards + 2-column
  grid: an action-queue panel (inline approve / reject per row) + a severity-feed
  side panel, a full-width records table with status pills, and an inline bar
  chart. Built for clarity and institutional trust.
triggers:
  - "sober light-mode admin"
  - "slate-blue sidebar admin"
  - "institutional trust dashboard"
  - "emerald accent light admin"
  - "approval queue admin panel"
  - "light-mode operations console"
  - "white card dense table admin"
  - "grouped sidebar admin"
example_prompt: "Apply this sober light-mode admin aesthetic to my domain"
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

# Sterling Admin — Visual Archetype

This plugin contributes a **look** (sober light-mode, slate-blue chrome, emerald
positive accent, white cards, dense tabular data) and a **structure** (grouped-nav
sidebar + white topbar + 4 KPI cards + action-queue panel + severity-feed side
panel + records table + bar chart). It does **not** contribute a domain — the
subject matter comes from the Knowledge Base and the user's prompt. Treat the
example below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property; keep the neutral light ramp hardcoded.

- **Canvas / surfaces:** page `#f7f8fa`; card / sidebar top `#ffffff`; sidebar
  chrome `var(--accent-deep)` = `#334155`; sidebar item hover `var(--accent-tint)`
  = `#f1f5f9`; hairline border `#e4e7ec`; row divider `#f7f8fa`.
- **Text ramp:** primary `#1e293b`; secondary `#475569`; muted `#64748b`; faint
  `#94a3b8`.
- **Accent:** `--accent: #475569` (slate-blue), `--accent-deep: #334155` (pressed /
  sidebar bg). Sidebar active bar, primary buttons, focus rings, table row hover.
- **Positive / approve:** `--emerald: #10b981`, `--emerald-tint: #d1fae5`. Settled
  pills, approve button, positive delta chips, peak chart bar.
- **Warning:** `--amber: #f59e0b`, `--amber-tint: #fef3c7`. Warning flags, delta
  chips on increases that are undesirable (e.g. pending count up).
- **Critical / reject:** `--red: #ef4444`, `--red-tint: #fee2e2`. Flagged pills,
  reject button, critical severity dots, negative delta chips.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
  sans-serif`. Base 14px / line-height 1.5. `font-variant-numeric: tabular-nums`
  on **every** numeric cell and KPI figure. Section labels 10px / uppercase /
  `letter-spacing: .08em` / weight 600 / muted. KPI figures 30–32px / weight 700.
  Mono IDs and codes: inherit Inter with `font-variant-numeric: tabular-nums`.
- **Density & radius:** comfortable — 18–20px card padding, 11px vertical row
  padding, 16px gaps; card radius 10px, button radius 6–8px, pill radius 20px,
  badge radius 10px. Subtle `0 1px 4px rgba(0,0,0,.05)` card shadows.
- **Borders & shadows:** 1px `#e4e7ec` lines do the separation work; 1px
  `#f7f8fa` row dividers inside tables. Cards have the single 1px shadow above;
  modals would use a stronger shadow, but no modals in this archetype.
- **Motion:** `.15s` background/border/opacity hover transitions. Period tab active
  state: white bg + box-shadow. No bouncy or entrance animations.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns described by shape and behavior — not meaning.

- **Left sidebar** (240px, fixed, `var(--accent-deep)` bg): brand mark (inline SVG
  + wordmark, white) → **entity / scope switcher** (rounded pill with label + value
  + chevron, white/translucent) → **grouped nav** (2–4 named sections, each with
  icon-label items; active item has a 3px left bar in `--emerald` + translucent bg;
  badge counts float right on affected items) → footer strip (avatar initials
  bubble + name + role + settings icon).
- **Top bar** (56px, `#ffffff`, 1px `#e4e7ec` bottom border): page title +
  breadcrumb → flexible **search** input (icon prefix, `#f7f8fa` bg, focus
  border-color `--accent`) → **period selector** tabs (Today / Week / Month /
  Quarter, pill group, active tab gets white bg + shadow) → notification bell with
  amber badge dot → avatar chip.
- **KPI card row** (4 cards, equal grid): each card = white 10px-radius panel with
  1px shadow. Top: `[uppercase label + large figure]` left, `[icon chip colored by
  state]` right. Bottom: delta chip (`.up` / `.down` / `.warn`) + "vs …" sub-text.
- **2-column grid (2/3 left + 1/3 right):**
  - **Left — action-queue card:** titled panel with "View all →" link; dense table
    rows of `[mono ID] [person] [type] [right-aligned amount] [time] [inline
    Approve + Reject buttons]`. Followed below by a **records table card** with
    filter tabs (All / sub-types) and status pills.
  - **Right — severity-feed card:** titled panel; list rows of `[severity dot] +
    [description + entity ref + timestamp + acknowledge link]`. Below it: an
    **inline bar chart card** with hourly/periodic bars (`--accent` color, peak bar
    `--emerald`), x-axis labels, y-axis range.
- **Full-width records table** (list screen): search + filter chip toolbar; dense
  table with sticky uppercase header, status pills, mono ID column, right-aligned
  numerics, footer with result count + pager.
- **Record form screen:** sectioned cards of labelled fields; **rules appear as
  inline validation** — required marks (`*`), helper text under the field, and
  inline error messages on invalid fields, submit disabled until valid. No
  rules/checklist/validation-status panel.
- **Record detail screen:** breadcrumb → header band (mono ID + status pill + action
  buttons) → meta grid (label/value pairs, 3-col) → one or more related sub-panels
  (a table or list of related records + an activity feed/timeline).

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key metrics,
status states, queue columns, form fields and their rules, and detail fields —
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
Domain (illustrative): a retail banking back-office operations centre.

Entity switcher  → branch scope: "Main Branch · All Units".
Period selector  → Today / Week / Month / Quarter.
Sidebar sections → MAIN (Operations Center), OPERATIONS (Today's Transactions,
                   Clearing Room), COMPLIANCE (Approvals Queue, Wire Transfers,
                   Loan Disbursements, FX & Trade, Risk & AML, Audit Trail),
                   SETTINGS (Preferences).

KPI cards (4):
  • Pending Approvals — amber icon, ~38, warn delta "↑ 14% vs yesterday".
  • Transactions Today — emerald icon, ~1,247, up delta "↑ 8.3%".
  • Flagged Items — red icon, ~12, down delta "↓ 2 vs yesterday".
  • SLA Met — accent icon, ~96.4%, up delta "↑ 0.4 pp vs last week".

Action-queue card → "Pending Approvals" — table columns:
  Request ID (mono) / Requestor / Type / Amount (right-aligned) / Submitted /
  Actions (Approve + Reject inline). Types: Wire Transfer, Loan Disbursement,
  Account Override, Limit Increase, FX Trade.

Records table card → "Today's Transactions" with filter tabs (All / Credit /
  Debit / Pending / Flagged). Columns: Txn ID (mono) / Account / Type /
  Amount / Time / Status pill (Settled, Pending, Flagged, Reversed).

Severity-feed card → "Risk & Exceptions" — rows: severity dot (red/amber/emerald)
  + description + entity ref + timestamp + Acknowledge link.

Bar chart card     → "Transaction Throughput" — 12 hourly bars (08–19),
  --accent bars, peak bar --emerald. Y-axis settlements per hour.

List screen        → all records, search + filter chips (by status, by type),
  paginated.

Form screen        → "New Request": entity reference (required), type (required
  select), amount (required, > 0), counterparty name (required), requested date
  (required, not in the past), notes. Rules as required marks + helper text +
  inline errors; submit disabled until valid.

Detail screen      → one record: breadcrumb → header (mono ID + status pill +
  Edit/Approve/Reject actions) → meta grid (type, amount, counterparty, date,
  requestor, created) → related sub-table (linked transactions) + activity feed.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, status states, queue/table columns, form fields + rules, detail
   fields — from the KB + prompt. Standalone: use the Example instantiation above.
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
<artifact identifier="admin-sterling-bankops" type="text/html" title="Sterling Admin">
<!doctype html>...</artifact>
```
