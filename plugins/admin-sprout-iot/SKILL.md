---
name: admin-sprout-iot
description: |
  Dark technical-fresh admin aesthetic: deep navy canvas (#0c1118), raised
  panels (#131b26 / #1a2533), lime (#84cc16) and cyan (#22d3ee) dual accents,
  amber/red for severity, Inter type with tabular-nums on every figure, dense
  13–14px rows, 6–10px radii, #223040 hairline borders, and crisp status pills.
  Archetype = context-switcher topbar + left label rail + 4 KPI cards (sparkline
  + delta chip) + 2-column grid: a multi-series channel panel (stacked sparklines
  + time axis) and a severity feed (labeled pills + elapsed time) + full-width
  records table with signal/state indicators. Built for high-density live-data
  consoles that must be legible at a glance.
triggers:
  - "dark technical admin"
  - "navy dual-accent admin"
  - "live-data console"
  - "deep navy dashboard"
  - "lime cyan dark admin"
  - "multi-channel telemetry panel"
  - "density-first dark admin"
  - "painel técnico escuro"
example_prompt: "Apply this dark technical admin aesthetic to my domain"
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

# Sprout Admin — Visual Archetype

This plugin contributes a **look** (deep navy, lime/cyan dual accent, dense
tabular data) and a **structure** (context-switcher topbar + left label rail +
KPI cards + multi-channel panel + severity feed + records table, plus list /
form / detail screens). It does **not** contribute a domain — the subject
matter comes from the Knowledge Base and the user's prompt. Treat the example
below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property; hardcode the neutral navy ramp.

- **Canvas / surfaces:** page `#0c1118`; raised panel `#131b26`; inset / hover
  `#1a2533`; hairline border `#223040`.
- **Text ramp:** primary `#dfe7ef`, secondary `#b0bdca`, muted `#8597a8`.
- **Dual accent:** `--c-lime: #84cc16` (healthy/online/positive), `--c-cyan:
  #22d3ee` (data/telemetry/info), each with a dim tint at ~8–12% alpha for
  sparkline fills and tag backgrounds.
- **Severity ramp (as tokens):** `--c-amber: #f59e0b` (warning / medium),
  `--c-red: #ef4444` (critical / offline), each with a `…-dim` tint at ~12–15%
  alpha for pill backgrounds and area fills. Severity borders at ~30% alpha.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
  sans-serif`. Base 13–14px. `font-variant-numeric: tabular-nums` on **every**
  numeric cell. Micro-labels 10px, `text-transform: uppercase`,
  `letter-spacing: 0.07–0.08em`, muted color. Big figures 26–28px / weight 700
  / `line-height: 1.1`. Short codes and UIDs in a mono face
  (`"Courier New", monospace`).
- **Density & radius:** compact 9–10px vertical row padding, 16–20px panel
  padding, 14px grid gaps; panel radius 10px, control radius 6px, pill radius
  4–6px, progress bars 4px tall / 2px radius.
- **Borders & shadows:** 1px hairlines do the separation work; no drop shadows
  on panels (flat, terminal feel). Active left-rail item gets a 3px lime bar.
- **Motion:** subtle only — `.12s–.15s` background/color hover transitions, a
  glowing pulse on live-status dot. Never bouncy.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Left label rail** (220px, surface bg, 1px right border): brand mark +
  wordmark at top; grouped nav items with inline SVG icons (active item gets a
  3px left bar + `--c-lime` tint + raised bg); optional badge count on items
  with pending severity; footer strip: status dot + short status label.
- **Top context bar** (56px, surface bg, 1px bottom border, sticky): a
  **context-switcher pill** (icon + label + chevron, raised bg), a flexible
  **search** input (raised bg, full-width cap), a spacer, then icon buttons
  (refresh + notification + avatar + operator name/role).
- **KPI card row** (4 cards, equal grid): each card = surface panel with an
  uppercase micro-label + icon glyph (muted), a big tabular figure in an accent
  color, a tiny inline-SVG sparkline (8 points, area fill), and a delta chip
  (`up` / `down` / `warn`). Figures recolor by state (lime / red / cyan /
  amber).
- **2-column panel row:**
  - **Left — multi-channel panel:** a titled card with a legend chip row, then
    N stacked channel rows each containing: `[UPPERCASE label] [inline-SVG
    sparkline, full-width] [current value in accent color]`, followed by a time
    axis tick row.
  - **Right — severity feed:** a titled card with a view-all link and 5–6 rows
    of `[severity pill CRIT/WARN/INFO] [entity name + message] [elapsed time]`,
    hover-highlighted on `--c-bg-raised`.
- **Full-width records table:** titled card with filter pills (All / positive /
  negative / warning) and a manage link; sticky uppercase header; dense rows
  with a two-line name cell (icon chip + name + mono UID), type/category cell,
  a version/code badge (accent for current, amber-tinted for outdated), a
  signal / strength indicator (4-bar inline SVG), a last-seen timestamp, and a
  status pill; footer with a result count + pager.
- **Records list screen:** the records-table archetype as its own page — search
  + filter chips + a count, same dense table, pager.
- **Record form screen:** sectioned cards of labelled fields; **rules appear as
  inline validation** — required marks (`*`), helper text under the field, and
  inline error messages on invalid fields, with the primary submit
  disabled-until-valid. No rules/checklist/validation-status panel.
- **Record detail screen:** a breadcrumb + header band (mono ID + status pill +
  key actions), a meta grid of label/value pairs (3-col), and one or more
  related-data sub-panels (channel row pattern or a mini-table) + an activity
  feed below.

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
Domain (illustrative): an IoT device-fleet monitoring console for a facility.

Context switcher → site/gateway: "Meridian Plant — GW-NORTH".
Left rail items  → Overview (active), Devices, Alerts, Telemetry, Gateways,
                   Firmware, Settings.

KPI cards (4):
  • Devices Online  142 (lime figure, ↑ 3 from yesterday).
  • Devices Offline   8 (red figure, ↑ 2 from yesterday).
  • Avg Signal    −67 dBm (cyan figure, ↑ 2 dBm this week).
  • Open Alerts       7 (amber figure, "2 critical · 5 warning").

Multi-channel panel (left) → "Live Telemetry — last 30 min"
  Legend chips: Temperature (cyan), Humidity (lime), Power Draw (amber).
  Three channel rows (TEMPERATURE / HUMIDITY / POWER DRAW), each with an
  inline sparkline + current value callout. Time axis: −30m → now.

Severity feed (right) → "Active Alerts"
  Rows: [CRIT] SENS-COLD-A3 — Temperature exceeded 28°C threshold — 3 min ago
         [CRIT] GW-ROOF-04  — Gateway heartbeat lost for 9 min — 9 min ago
         [WARN] ACT-VALVE-12 — Actuator response latency > 800 ms — 17 min ago
         [WARN] SENS-PWR-07  — Battery level at 12% — replace soon — 31 min ago
         [INFO] GW-DOCK-01   — Firmware v2.4.1 available — 1 hr ago

Records table → "Devices" — All (150) / Online / Offline / Warning filter:
  Columns: Device (icon + name + mono UID) / Type / Firmware / Signal (4-bar) /
           Last Seen / Status pill (Online / Offline / Warning).
  Rows: GW-NORTH-01 Gateway v3.1.0 ████ just now Online
        SENS-COLD-A3 Temp Sensor v2.9.1 ███░ 2 sec Warning
        ACT-VALVE-12 Actuator v2.6.3(outdated) ██░░ 5 sec Warning
        … (8 rows total)

List screen    → all records, search + filter pills, paginated.

Form screen    → "New Record": name (required), category (required select),
  firmware channel (required select), location/grouping (required),
  polling interval in seconds (required, > 0), notes.
  Rules shown as required marks + helper text + inline errors; submit disabled
  until valid.

Detail screen  → one record: breadcrumb + header (mono ID + status pill +
  actions), meta grid (type, location, firmware, last seen, group, added),
  a "Recent Readings" multi-channel sub-panel + an "Event Log" activity feed.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, status states, record columns, form fields + rules, detail
   fields — from the KB + prompt. Standalone: use the Example instantiation above.
3. Build each screen in the Visual language + Layout archetype above, imitating
   the example set in `assets/` (dashboard, list, form, detail) and the
   `assets/template.html` seed — with fresh content for the real domain, NOT
   the example labels.
4. Express domain rules as INLINE field validation (required marks, helper
   text, inline errors, disabled-until-valid submit). Never render
   rules/checklist/validation-status/build-note panels or designer/demo controls.
5. One inline `<style>`, semantic HTML5, `tabular-nums` on figures, no external
   assets, no CDNs — self-contained.

## Output contract

```
<artifact identifier="admin-sprout-iot" type="text/html" title="Sprout Admin">
<!doctype html>...</artifact>
```
