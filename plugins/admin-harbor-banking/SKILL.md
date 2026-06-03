---
name: admin-harbor-banking
description: |
  Light-mode trustworthy admin aesthetic: white-card surfaces on a
  slate-tinted canvas (#f6f8fb), navy-to-blue primary gradient
  (#1e3a8a → #2563eb) with teal secondary (#0d9488), tabular-nums on
  all figures, 10px card radius, soft hairline borders and subtle
  box-shadows. Archetype = narrow dark-navy entity-list sidebar (260px)
  + sticky topbar with search pill + hero row (stylized card SVG + 3
  KPI tiles) + 2-column content area (left: inline SVG donut chart +
  dense records table; right: quick-action payee panel + scheduled
  items list). Optimised for high-trust, card-centric financial
  operations consoles.
triggers:
  - "light-mode card admin"
  - "navy-teal operations console"
  - "trustworthy light admin"
  - "card-centric dashboard"
  - "white-surface admin"
  - "navy sidebar admin"
  - "teal CTA admin"
  - "painel claro confiável"
example_prompt: "Apply this light navy-teal card admin aesthetic to my domain"
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

# Harbor Admin — Visual Archetype

This plugin contributes a **look** (trustworthy light mode, navy-blue
primary, teal accent, white-card surfaces, dense tabular data) and a
**structure** (entity-list sidebar + topbar + hero card/KPI strip +
donut chart + records table + quick-action panel, plus list / form /
detail screens). It does **not** contribute a domain — the subject
matter comes from the Knowledge Base and the user's prompt. Treat the
example below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Every chromatic value is a `:root` CSS custom
property; only neutral grays may be hardcoded.

- **Canvas / surfaces:** page `#f6f8fb`; card / panel `#ffffff`; input
  canvas `#f6f8fb`; sidebar bg `#0f2460` (deep navy).
- **Primary ramp:** `--c-navy: #1e3a8a`; `--c-blue: #2563eb`;
  `--c-blue-light: #dbeafe`. Primary gradients run navy → blue.
- **Secondary accent:** `--c-teal: #0d9488`; `--c-teal-light: #ccfbf1`.
  Used for CTAs, active states, positive deltas, and action buttons.
- **Semantic colors:** `--c-green: #16a34a` / `--c-green-light: #dcfce7`;
  `--c-red: #ef4444` / `--c-red-light: #fee2e2`;
  `--c-amber: #d97706` / `--c-amber-light: #fef3c7`;
  `--c-violet: #7c3aed` / `--c-violet-light: #ede9fe`;
  `--c-rose: #e11d48` / `--c-rose-light: #ffe4e6`.
- **Text ramp:** `--c-text-primary: #1e293b`; `--c-text-muted: #64748b`;
  `--c-text-faint: #94a3b8`.
- **Borders & shadows:** `--c-border: #e4e8ef`;
  `--c-shadow-sm: 0 1px 3px rgba(30,58,138,.07), 0 1px 2px rgba(30,58,138,.04)`;
  `--c-shadow-md: 0 4px 12px rgba(30,58,138,.09), 0 2px 4px rgba(30,58,138,.05)`.
  1px hairlines do the separation work; panels stay flat (no heavy drop
  shadows).
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
  sans-serif`. Base 14px. `font-variant-numeric: tabular-nums` on
  **every** numeric cell. Micro-labels: `.65rem`, `text-transform:
  uppercase`, `letter-spacing: .08–.1em`, muted color. Big KPI figures:
  `1.45rem / weight 700`. Card titles: `.9rem / weight 700`. Sidebar
  section labels: `.62rem / uppercase / letter-spacing .1em / faint`.
- **Density & radius:** compact 12px vertical row padding in tables,
  18–20px panel padding; `--r-card: 10px`; control radius 8px; chip /
  pill radius 99px; progress bars 4px tall.
- **Motion:** `.12s–.15s` background/border hover transitions; never
  bouncy. Default easing gentle.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns described by shape and behavior — not
meaning.

- **Narrow left sidebar** (260px, deep-navy bg, 1px right border):
  brand mark + wordmark at top → **entity list** section (color-dot +
  masked label + value per row, active row tinted) → grouped **nav**
  (section label / icon + text items; active item has a left-bar accent
  stripe + tinted bg) → user avatar block pinned at bottom.
- **Sticky topbar** (60px, white bg, 1px bottom border): page title on
  the left → **search pill** (canvas bg, magnifier, focus border) →
  spacer → icon-button cluster (notification bell with badge) → avatar
  circle + name/role + caret.
- **Main content** (page bg, 24px padding, vertical flow): page header
  (title + sub-line left, ghost + primary actions right), then the
  region stack.
- **Hero strip** (4-column grid: 1.45fr + 3×1fr): a **stylized card
  SVG** (gradient panel, abstract bg geometry, chip SVG, masked number,
  holder/expiry/network mark) + **3 KPI tiles** (white card, small
  uppercase label + icon chip on top, large tabular figure, delta chip +
  period text at foot).
- **2-column content grid** (2fr / 1fr):
  - **Left column:** a **donut chart card** (title + period-selector
    tabs, inline SVG donut with 5–6 segments + colored legend with label
    / amount / mini bar / pct) followed by a **records table card**
    (title + View-all link, sticky uppercase header, dense rows with
    category chip + signed amount cell + status pill).
  - **Right column:** a **quick-action panel** (title + link; payee
    avatar row horizontally scrollable with active ring; amount input
    with currency prefix; note field; teal primary CTA button) followed
    by a **scheduled-items list** (icon chip + name/date + amount per
    row, dividers, bottom link).
- **List screen:** the records-table archetype as its own page —
  search pill + filter chips + count, same dense table, pager footer.
- **Form screen:** sectioned white cards of labelled fields; **rules
  appear as inline validation** — required marks (`*`), helper text
  under the field, inline error messages on invalid fields, submit
  disabled-until-valid. No rules/checklist/validation-status panel.
- **Detail screen:** breadcrumb → header band (ID + status pill + key
  actions) → meta grid (label/value cells, 3 columns) → related
  sub-panels (status-board row pattern or a mini-table) below.

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract
THIS domain's equivalent of the archetype slots — its primary entities,
entity-list rows, key metrics, status states, record columns, form
fields and their rules, and detail fields — and map them onto the
archetype above. If no KB/domain is supplied (standalone), use the
Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel;
domain rules become inline field validation. Do NOT render
build/implementation notes or designer controls — every screen is a
finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief.
> In WXCode this is IGNORED — replace every label with the real
> domain's equivalent (entities, metrics, states, columns, fields)
> drawn from the KB + prompt.

```
Domain (illustrative): a personal-finance account management console.

Sidebar entity list → accounts: Primary Checking ····4821 $12,480;
  Savings Vault ····7093 $34,210; Investment Port. ····2255 $58,740.
Sidebar nav groups → Overview (Dashboard, Analytics, Accounts),
  Payments (Cards, Transfers, Transactions), Settings.

Hero card SVG → navy-to-teal gradient, abstract circuit-trace bg,
  chip SVG, masked number ····4821, cardholder Maya A. Reyes,
  expiry 09/29, fictional dual-circle network mark.

KPI tiles (3):
  • Total Balance $105,430.85 (▲2.4%, "vs last month").
  • Monthly Income $7,250.00 (▲5.1%, "vs May 2026").
  • Monthly Spending $3,148.62 (▲8.3%, "vs May 2026").

Donut chart → "Spending by Category" — 6 segments:
  Housing 32%, Food & Dining 22%, Transport 16%, Entertainment 13%,
  Health 10%, Other 7%. Center label shows total figure.

Records table → "Recent Transactions": Date / Merchant (icon+name+sub) /
  Category chip / Amount (green credit / red debit) / Status pill
  (Completed / Pending / Failed).

Quick-action panel → "Quick Transfer": payee avatar row (Theo, Sylvia,
  Ravi, Nadia, +Add), amount input with $ prefix, note field, "Send
  Money" teal CTA.

Scheduled items → "Upcoming Payments": icon + name + due date + amount
  (electric, internet, fitness).

List screen → all transactions, search + filter chips (status,
  category), paginated.

Form screen → "New Transfer": recipient (required select), amount
  (required, > 0), account (required select), date (required, not past),
  note (optional). Rules as required marks + helper text + inline
  errors; "Send Transfer" disabled until valid.

Detail screen → one transaction: breadcrumb, header (TXN ID + status
  pill + actions), meta grid (merchant, category, amount, date, account,
  reference), related sub-panel (similar transactions mini-table +
  activity timeline).
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's
   Visual language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary
   entities, entity-list rows, key metrics, status states, record
   columns, form fields + rules, detail fields — from the KB + prompt.
   Standalone: use the Example instantiation above.
3. Build each screen in the Visual language + Layout archetype above,
   imitating the example set in `assets/` (dashboard, list, form,
   detail) and the `assets/template.html` seed — with fresh content for
   the real domain, NOT the example labels.
4. Express domain rules as INLINE field validation (required marks,
   helper text, inline errors, disabled-until-valid submit). Never
   render rules/checklist/validation-status/build-note panels or
   designer/demo controls.
5. One inline `<style>`, semantic HTML5, `tabular-nums` on figures, no
   external assets, no CDNs — self-contained.

## Output contract

```
<artifact identifier="admin-harbor-banking" type="text/html" title="Harbor Admin">
<!doctype html>...</artifact>
```
