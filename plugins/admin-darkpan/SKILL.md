---
name: admin-darkpan
description: |
  Midnight-black admin aesthetic: pure-black canvas (#000000), deep charcoal
  surface panels (#191c24), teal accent (#009688) on a slate neutral ramp, Open
  Sans type at 14px base, zero-radius sharp corners throughout, hairline #2a2e38
  borders, and crisp teal status pills. Archetype = collapsible icon sidebar +
  fixed top header bar + KPI metric tile row (4–6 tiles) + full-width data table
  with sortable columns and status pills + form screens with inline field
  validation + auth panels (sign-in / sign-up) + error / empty state screens +
  widget gallery. High-contrast, sharp-edged, information-dense dark console
  designed to scan fast on large monitors.
triggers:
  - "midnight black admin"
  - "dark teal accent admin"
  - "sharp corners dark dashboard"
  - "zero-radius dark panel admin"
  - "pitch-black admin console"
  - "high-contrast dark admin"
  - "dark mode sharp-edge dashboard"
  - "teal accent data dashboard"
  - "admin escuro fundo preto"
  - "painel escuro com cantos retos"
  - "console administrativo preto e azul"
example_prompt: "Apply this midnight-black sharp-corner admin aesthetic to my domain"
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
    requires: [pixel-discipline, state-coverage]
---

# Onyx Sharp Admin — Visual Archetype

This plugin contributes a **look** (midnight-black canvas, teal accent, sharp
zero-radius corners, dense tabular data) and a **structure** (collapsible icon
sidebar + top header + KPI tiles + status-pill tables, plus list / form / auth /
error / widget screens). It does **not** contribute a domain — the subject matter
comes from the Knowledge Base and the user's prompt. Treat the example below as
illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Every chromatic value is a `:root` CSS custom property;
neutral dark ramp may be hardcoded.

- **Canvas / surfaces:** page `#000000`; card / panel `#191c24`; inset / hover
  `#212535`; selected / active bg `#2a2e38`; hairline border `#2a2e38`;
  divider `#1e2130`.
- **Text ramp:** primary `#ffffff`; secondary `#b1b7c1`; muted `#6c7293`;
  faint `#454865`.
- **Accent:** `--accent: #009688` (teal), `--accent-hover: #00b09c`,
  `--accent-dim: rgba(0,150,136,.15)`. CTAs, active nav items, progress fills,
  chart strokes, key figures.
- **Status ramp (tokens):** `--state-success #00c897`, `--state-warning #ffab00`,
  `--state-danger #ff4c61`, `--state-info #5b73e8`, `--state-neutral #6c7293`;
  each with a `…-dim` at ~14% alpha for pill backgrounds.
- **Typography:** `"Open Sans", "Helvetica Neue", Arial, sans-serif`. Base 14px /
  400. `font-variant-numeric: tabular-nums` on every numeric cell. Labels 12px /
  uppercase / `letter-spacing: .5px` / muted. Big figures 28–32px / 700 /
  `letter-spacing: -.5px`. Monospace IDs in `"Courier New", monospace`.
- **Density & radius:** compact 10–12px vertical row padding, 16–20px panel
  padding, 12px grid gaps; **corner radius = 0px everywhere** (cards, inputs,
  buttons, pills, badges). Pill text 11px uppercase.
- **Borders & shadows:** 1px hairlines (`#2a2e38`) for separation; no drop
  shadows on panels — flat terminal feel. Active / focus ring: 1px solid
  `--accent`.
- **Motion:** `.12s–.18s ease` for background / border / color hover transitions;
  sidebar collapse `.25s ease`; never bouncy.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Top header bar** (56px, `#191c24`, 1px bottom border `#2a2e38`, sticky):
  hamburger toggle → brand wordmark → flexible spacer → global search input
  (inline, ghost) → notification bell with badge → user avatar chip (name +
  role label + chevron).
- **Left sidebar** (240px expanded / 60px collapsed, `#191c24`, 1px right
  border, collapsible): logo zone at top; nav section groups with uppercase
  micro-labels; each nav item = icon + label + optional count badge; active
  item fills `--accent-dim` with a 3px left `--accent` bar; hover lightens to
  `#212535`; collapsed shows icons only with native tooltips; settings item
  pinned at the bottom.
- **Main content** (`#000000` bg, 24px padding, vertical flow): **page title
  row** (H1 + breadcrumb trail on left, date-range picker + primary action on
  right), then the region stack below.
- **KPI metric tile row** (4–6 tiles, equal CSS grid): each tile = `#191c24`
  panel with an icon box (accent-dim bg + accent icon), a big tabular figure,
  a label, and a delta chip (up/down arrow + percentage). Figures recolor by
  state token.
- **Full-width data table panel** (`#191c24`, 0px radius): panel title row with
  search input + filter chips + export ghost button; a sticky uppercase header
  row; dense rows — mono ID cell, text cells, right-aligned numeric cells,
  **status pill** (teal / amber / red / slate), and an action menu; row hover
  lifts to `#212535`; footer with result count + prev / next pager.
- **Charts panel** (same panel style): section title + optional period tabs;
  SVG/canvas chart area with `--accent` strokes, area fills at 20% alpha, dotted
  gridlines in `#2a2e38`, axis labels in muted text. Secondary series use
  `--state-info`, `--state-warning`, `--state-danger`.
- **Widget gallery** (masonry / responsive grid): each widget = `#191c24` panel
  with a title + subtitle, the content type (mini chart, progress bar, list, or
  stat), and a footer action link.
- **List screen**: page header (title + primary action) + search bar + filter
  pills row + the full-width data table + pager.
- **Form screen**: sectioned `#191c24` panels of labeled fields; **rules as
  inline validation** — required mark (`*`), helper text under the field, inline
  error message on invalid field, submit button disabled until valid. No rules
  / checklist / validation-status summary panel.
- **Auth screens (sign-in / sign-up)**: centered card (`#191c24`, 0px radius)
  on a pure-black page; brand mark at top; labeled inputs with inline validation;
  teal primary button; secondary link below.
- **Error / empty state screen**: centered layout on `#000000`; large SVG or
  CSS numeric code; short heading + sub-line; primary teal action button.

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key metrics,
status states, record list columns, form fields and their rules, and detail
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
Domain (illustrative): a cloud infrastructure monitoring platform.

Header: brand "Nexus Monitor" · search · notifications (3 unread) · user avatar
"A. Rivera · Admin".

Sidebar sections:
  Overview → Dashboard
  Resources → Servers | Containers | Databases | Networks
  Observability → Alerts | Logs | Metrics
  (Settings, pinned bottom).

KPI tiles (4):
  • Total Servers 142 (▲6 this week, teal)
  • Active Incidents 7 (▲2, red)
  • Avg CPU Load 61% (▼4%, amber)
  • Uptime (30d) 99.94% (▲0.02%, teal)

Data table → "Servers — All":
  columns: ID / Hostname / Region / CPU % / Memory % / Status pill
  (Running / Degraded / Offline / Maintenance) / Last Seen / Actions.

List screen → filterable server list with search + status filter chips.

Form screen → "Add Server":
  Hostname (required, no spaces), IP Address (required, valid IPv4), Region
  (required select), CPU Threshold (required, 1–100, helper "alert fires above
  this value"), Tags (optional). Submit "Register Server" disabled until valid;
  inline error on invalid IP format.

Charts screen → CPU & Memory trend SVG line chart (7-day); Incident Frequency
  bar chart; Region distribution donut chart.

Widgets screen → Active Alerts widget (list), Top CPU Consumers mini-table,
  Uptime Progress bars, Recent Activity feed.

Sign-in → email + password (required), "Remember me" checkbox, "Sign In" teal
  button, "Forgot password?" link.

Sign-up → full name + email + password (required, ≥8 chars, helper text) +
  confirm password (must match, inline error if mismatch).

Error screen → "404" large teal digit, "Page not found", "Go to Dashboard" teal
  button.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, status states, record columns, form fields + rules, detail
   fields — from the KB + prompt. Standalone: use the Example instantiation
   above.
3. Build each screen in the Visual language + Layout archetype above, imitating
   the example set in `assets/` (dashboard, list, form, charts, widgets, signin,
   signup, error) and the `assets/template.html` seed — with fresh content for
   the real domain, NOT the example labels.
4. Express domain rules as INLINE field validation (required marks, helper text,
   inline errors, disabled-until-valid submit). Never render
   rules/checklist/validation-status/build-note panels or designer/demo controls.
5. One inline `<style>`, semantic HTML5, `tabular-nums` on figures, no external
   assets, no CDNs — self-contained.

## Output contract

```
<artifact identifier="admin-darkpan" type="text/html" title="Admin Console">
<!doctype html>...</artifact>
```
