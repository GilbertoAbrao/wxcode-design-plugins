---
name: admin-midnight-ops
description: |
  Dark observability-console aesthetic: midnight-navy canvas (#0b1120), teal-to-cyan
  accent gradient (#14b8a6 / #22d3ee), high-contrast status pills on a cool-grey
  neutral ramp, Inter type with tabular-nums on every figure, compact 13px rows,
  6–10px radii, hairline #1f2937 borders, and glowing status dots. Archetype =
  slim top navbar (logo + search + context switcher + icon actions + avatar) +
  compact left icon rail + 4 metric tiles with inline sparklines + full-width
  time-series area chart + status-list side panel + full-width records table with
  severity and state pills. Built for high-density real-time consoles that must
  read at a glance under any ambient light.
triggers:
  - "dark navy admin"
  - "teal-on-midnight dashboard"
  - "observability console aesthetic"
  - "navy-teal data console"
  - "dark-mode status-board console"
  - "midnight-navy high-density admin"
  - "glowing-teal dark terminal"
  - "painel escuro azul-marinho"
example_prompt: "Apply this dark navy teal-accent admin aesthetic to my domain"
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

# Midnight Ops — Visual Archetype

This plugin contributes a **look** (midnight navy, teal-to-cyan accent, glowing
status dots, dense tabular data) and a **structure** (slim navbar + compact icon
rail + metric tiles with sparklines + time-series chart + status panel + records
table, plus list / form / detail screens). It does **not** contribute a domain —
the subject matter comes from the Knowledge Base and the user's prompt. Treat the
example below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property.

- **Canvas / surfaces:** page `#0b1120`; raised panel `#111827`; inset / hover
  `#1e293b`; stronger inset `#263347`; hairline border `#1f2937`; stronger hover
  border `#2d3f56`.
- **Text ramp:** primary `#e2e8f0`, muted `#94a3b8`, faint `#64748b`.
- **Accent:** `--accent-teal: #14b8a6`, `--accent-cyan: #22d3ee`,
  `--accent-glow: rgba(20,184,166,.18)`. Primary CTAs, active rail, key figures,
  sparkline fills, chart strokes.
- **Status ramp (as tokens):** `--green #22c55e` / `--green-light #4ade80` /
  `--green-bg rgba(34,197,94,.12)` / `--green-glow rgba(34,197,94,.5)`;
  `--amber #f59e0b` / `--amber-light #fbbf24` / `--amber-bg rgba(245,158,11,.12)` /
  `--amber-glow rgba(245,158,11,.5)`;
  `--red #f43f5e` / `--red-light #fb7185` / `--red-bg rgba(244,63,94,.12)` /
  `--red-glow rgba(244,63,94,.5)`;
  `--blue #3b82f6` / `--blue-light #93c5fd` / `--blue-bg rgba(59,130,246,.12)`.
  Severity pills carry both a background tint and a 1px colour-matched border.
- **Status dots glow:** `box-shadow: 0 0 5px var(--<colour>-glow)` on every
  coloured dot — this is part of the visual identity.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
  sans-serif`. Base 13px. `font-variant-numeric: tabular-nums` on **every** numeric
  cell. Micro-labels 10–11px, `text-transform: uppercase`, `letter-spacing: .05em`,
  muted. Big tile figures 26px / weight 700 / `letter-spacing: -.02em`. IDs in a
  mono face (`"SF Mono", "Fira Code", monospace`).
- **Density & radius:** compact 13px base, 7–10px row padding, 14–16px panel
  padding, 12–16px grid gaps; panel radius 10px, control radius 6px, pill radius
  20px (fully rounded), progress bars 4px / 2px radius.
- **Borders & shadows:** 1px hairlines + `box-shadow: 0 1px 3px rgba(0,0,0,.45),
  0 0 0 1px var(--border)` on cards. Active rail item: accent-glow background +
  1px accent-tinted ring + 3px teal left edge bar.
- **Motion:** `.12s–.15s` background/border hover transitions, 2s pulse on live
  dots, scrollbar hidden (`scrollbar-width: none`). Never bouncy.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns described by shape and behavior — not meaning.

- **Top navbar** (56px, panel bg, 1px bottom border, sticky): brand glyph (inline
  SVG, 24×24) aligned with the rail → **search pill** (flex-1, max 320px, leading
  magnifier icon) → flex spacer → **context switcher** (3-button pill group: active
  button teal-filled, others transparent) → notification icon button with a red
  badge dot → settings icon button → avatar button (teal gradient, initials, 30px
  circle).
- **Left icon rail** (48px, panel bg, 1px right border): 5–6 icon-only nav items
  with `title` tooltips (active item = accent-glow bg + teal left edge bar; hover
  lifts to inset bg), optional separator lines between groups, settings at the
  bottom.
- **Main content** (page bg, 20px padding, `display:flex; flex-direction:column;
  gap:16px; overflow-y:auto`): a **page header** (title + sub-line left; live-dot
  + ghost + primary buttons right), then the region stack below.
- **Metric tile row** (4 tiles, equal grid, 12px gap): each tile = panel card with
  `tile-header` (uppercase micro-label + small icon chip) → big tabular figure
  (26px/700) with a unit suffix → `tile-footer` (delta badge with arrow + % +
  period label on the left; mini 72×24 inline SVG sparkline on the right). Tiles
  recolor figure/icon by state (teal / cyan / red / green).
- **Content row** (2-column: `1fr 280px`, 16px gap):
  - **Left — time-series chart panel:** titled panel, `panel-header` with legend
    chips, inline SVG area chart (full-width, ~160px tall, gradient fill, grid
    lines, Y-axis labels, X-axis tick labels, peak marker circle + callout label).
  - **Right — status-list side panel:** titled panel, rows of
    `[coloured glow dot] [entity name] [state badge]`. Dot colours: green/amber/red
    matching the state token palette; badge is fully rounded, small font.
- **Full-width records table:** titled panel with ghost + count sub-line, a sticky
  `th` row (10px uppercase, 1px bottom border), dense `td` rows (10px padding,
  12px font, 1px bottom divider, hover `inset` bg). Columns include a mono ID, an
  ellipsis-capped title, a dimension column, a duration/numeric column, an assignee
  cell (20px avatar + name), and a fully-rounded state pill.
- **Records list screen:** the table archetype as its own page — search pill +
  filter chip row + count, the same dense table, pager footer.
- **Record form screen:** sectioned panel cards of labelled fields; **rules appear
  as inline validation** — required marks (`*`), helper text under the field,
  inline error messages on invalid fields, primary submit disabled-until-valid. No
  rules/checklist/validation-status panel.
- **Record detail screen:** breadcrumb → header band (mono ID + state pill + key
  actions) → meta grid (3-col label / value pairs) → related sub-panels (a
  mini status-list or table + an activity feed).

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key metrics,
status states, context switcher values, record columns, form fields and their
rules, detail meta fields — and map them onto the archetype above. If no
KB/domain is supplied (standalone), use the Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules
become inline field validation. Do NOT render build/implementation notes or
designer controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent
> (entities, metrics, states, columns, fields) drawn from the KB + prompt.

```
Domain (illustrative): a cloud services operations and incident-management console.

Context switcher    → environment: "prod" / "staging" / "canary".
Rail items          → Overview, Services, Incidents, Metrics, Traces, Settings.

Metric tiles (4):
  • P99 Latency 184 ms (teal down-arrow −6.3%, sparkline trending down, vs 1 h ago).
  • Throughput 42.7 k/s (teal up-arrow +11.2%, sparkline trending up, vs 1 h ago).
  • Error Rate 0.82% (red figure, up-arrow +0.14%, vs 1 h ago).
  • Uptime SLO 99.94% (cyan figure, down-arrow −0.02%, rolling 30 d).

Time-series chart (left) → "Request Throughput — Last 24 h": teal area fill +
  dashed cyan baseline, 24 hourly buckets, peak marker + callout label, Y-axis
  labels (0/25k/35k/45k/55k), X-axis hour ticks (00:00…22:00).

Status-list panel (right) → "Service Health": 8 service rows, each with a
  glow-dot (green/amber/red) + name + badge (OK / Degraded / Down).
  Example: api-gateway OK, payments-svc Degraded, media-transcoder Down.

Records table       → "Active Incidents": Severity pill (P1/P2/P3), mono ID,
  Title (ellipsis), Affected Service, Duration, Assignee (avatar + name),
  Status pill (Investigating / Mitigating / Resolved). At least 5 rows.

List screen         → all incidents, search pill + filter chips (severity, status),
  count sub-line, the same dense table, pager footer.

Form screen         → "New Incident": title (required), affected service (required
  select), severity (required select; default P3), description (textarea, helper:
  "include symptoms, environment, and impact"), assignee (select), runbook URL
  (optional, must start https://). Rules shown as required marks + helper text +
  inline errors; "Create Incident" disabled until valid.

Detail screen       → one incident: breadcrumb → header (mono ID + state pill +
  actions), meta grid (severity, service, duration, assignee, opened, last-updated),
  "Affected Regions" mini status-list sub-panel + "Activity" timeline sub-panel.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, status states, context switcher values, record columns, form fields
   + rules, detail fields — from the KB + prompt. Standalone: use the Example
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
<artifact identifier="admin-midnight-ops" type="text/html" title="Midnight Ops">
<!doctype html>...</artifact>
```
