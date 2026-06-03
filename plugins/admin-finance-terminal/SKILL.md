---
name: admin-finance-terminal
description: |
  Pure-black terminal aesthetic: page canvas #0E0E0E, raised panels #1A1A1A,
  amber accent (#FFB800), monospace type throughout (ui-monospace / SF Mono /
  Consolas), 12px dense rows, no-radius sharp edges, grid-line borders #2a2a2a,
  and square-cornered status/tag chips. Archetype = 32px status bar (clock +
  session + env chip + latency + help hint) + 24px ticker strip (scrolling
  symbol/price/delta row) + 200px left module rail (F-key shortcuts + module
  label + status dot) + 3-column body (rail | center 2-row panel | right 2-row
  panel) + 36px command-line prompt footer. Built for high-density real-time
  consoles that must scan 50+ data points without scrolling.
triggers:
  - "black monospace terminal admin"
  - "amber accent dark console"
  - "dense data terminal"
  - "zero-radius dark admin"
  - "ticker-strip dashboard"
  - "F-key module rail"
  - "command-line footer panel"
  - "sharp-edge black admin"
example_prompt: "Apply this black monospace terminal aesthetic to my domain"
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

# Finance Terminal — Visual Archetype

This plugin contributes a **look** (pure-black, amber accent, monospace, dense,
no-radius) and a **structure** (status bar + ticker strip + F-key module rail +
3-column split with stacked panels + command-line footer). It does **not**
contribute a domain — the subject matter comes from the Knowledge Base and the
user's prompt. Treat the example below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property.

- **Canvas / surfaces:** page `#0E0E0E`; raised panel `#1A1A1A`; ticker strip
  `#111111`; hairline border `--grid: #2a2a2a`; row hover `rgba(255,184,0,.06)`.
- **Text ramp:** primary `#ffffff`; muted `--ink-dim: #888888`; amber accent
  figures `--amber: #FFB800`; positive green `--green: #00C851`; negative
  amber (NOT red — terminal convention) `--amber`.
- **Accent:** `--amber: #FFB800`. Active rail items, panel titles, key figures,
  gauge fills (warn state), sparkline zero-line, command-prompt glyph, logo.
- **Status colors:** positive / confirmed `--green: #00C851`; negative /
  cancelled uses `--amber`; neutral / pending uses `--ink-dim`; danger bars use
  `#ff4444`.
- **Typography:** `ui-monospace, "SF Mono", Menlo, Consolas, "Liberation Mono",
  monospace` for **all** numerics, labels, headers, and body text. Sans serif
  (`-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`) is reserved for
  a single help-hint string only. Base 12px. All numbers right-aligned. Big
  summary figures 28px / letter-spacing -0.02em. Uppercase micro-labels at
  10–11px / letter-spacing 0.08–0.12em.
- **Density & radius:** 0 (zero) border-radius on all panels, chips, gauge
  tracks, and buttons — strict square corners. Row padding ~5px vertical / 8px
  horizontal. Panel header 28px tall. Status bar 32px. Ticker strip 24px.
  Command line 36px. Rail width 200px. Right panel 280px.
- **Borders & shadows:** 1px `var(--grid)` hairlines separate every region; no
  drop shadows, no gradients. Zebra rows at `rgba(255,255,255,0.018)`.
- **Motion:** minimal — no transitions except `.blink` animation (1s step-end
  infinite) on the command-line caret.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns described by shape and behavior — not meaning.

- **Status bar** (32px, panel bg, 1px bottom border): brand/logo token → sep →
  session label → sep → env chip (LIVE / STAGING) → session-ID chip → sep →
  latency indicator → sep → user label → spacer → help hint (sans) → sep →
  live clock (amber).
- **Ticker strip** (24px, slightly darker bg, 1px bottom border): label tag
  (amber, 10px, letter-spaced) → flex row of symbol/price/delta items
  (sym=muted, price=white, delta=green for up/amber for down), each separated
  by a `var(--grid)` right border.
- **Left module rail** (200px, panel bg, 1px right border): section header
  (10px uppercase muted) → list of module rows — each row is `F-key (amber,
  22px) | label (11px, center) | status dot (6px circle)`. Active row has
  left amber 2px border + `#1f1a00` background + amber label + amber dot. OK
  rows show green dot. Footer: version/env string (10px muted).
- **Center column** (flex 1, 2-row grid): **top panel** (flex 1) = panel header
  (amber title + meta + badge) + scrollable table with sticky header, zebra
  rows, right-aligned numeric cells, amber symbol column, colored pos/neg cells;
  **bottom panel** (fixed height ~200px) = panel header + scrollable activity
  log table (left-aligned, colored action type cells, muted timestamps).
- **Right column** (280px, 2-row grid): **top panel** (flex 1) = panel header +
  summary block (period label, 28px big figure in green or amber, sub-line
  pairs, SVG sparkline at foot); **bottom panel** (fixed height ~220px) = panel
  header + gauge list (each: name/value meta row + full-width 6px track with
  colored fill — green/amber/danger).
- **Command-line footer** (36px, panel bg, 1px top border): prompt glyph `CMD>`
  in amber + blinking underscore → full-width monospace input → hint chip row
  (10px, `var(--grid)` border) → sep → keyboard hint text (10px muted).

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary monitored entities
(for the ticker), its session/scope identity (status bar), its module list
(rail F-keys), its main data table columns, its activity/event log, its key
summary figure + sparkline, and its limit/gauge metrics — and map them onto
the archetype above. If no KB/domain is supplied (standalone), use the Example
instantiation below.

Do NOT invent a rules / checklist / validation-status panel; domain rules
become inline field validation. Do NOT render build/implementation notes or
designer controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent
> (entities, metrics, states, columns, fields) drawn from the KB + prompt.

```
Domain (illustrative): a logistics fleet-operations dispatch console.

Status bar      → brand: "AXYS DISPATCH" · session: "SHIFT B · NIGHT" ·
                  env chip: LIVE · session-ID: SID-2026-0602-N2 ·
                  latency: LAT 4ms · user: OPS.SILVA · clock: live UTC.

Ticker strip    → FLEET  |  TRK-084 1,247 km ▲+82  |  TRK-091 IDLE ▼  |
                  TRK-112 832 km ▲+14  |  VAN-003 411 km ▲+6  |
                  DRV-22 +3 deliveries  |  FUEL 94.2% ▲+0.4.

Module rail (F-keys):
  F1 HELP  |  F2 OVERVIEW (active)  |  F3 ROUTES (ok)  |  F4 DRIVERS (ok)  |
  F5 ALERTS  |  F6 FUELING  |  F7 SCHEDULE  |  F8 ADMIN.

Center top panel → "ACTIVE FLEET" table: UNIT / TYPE / ROUTE / KM TODAY /
  ETA / STATUS (MOVING / IDLE / BREAKDOWN / STANDBY).

Center bottom panel → "EVENT LOG" table: TIME / EVENT / UNIT / LOCATION /
  DRIVER / NOTES (colored: DEPART=green, BREAKDOWN=amber, CANCEL=amber, MOD=muted).

Right top panel → "DELIVERIES TODAY" — big figure 284 (green) + sub-lines
  (ON TIME 261, DELAYED 23) + sparkline (deliveries/hr, last 8h).

Right bottom panel → "CONSTRAINTS" gauges:
  FLEET UTILIZATION 78% (green) · FUEL RESERVE 12% (warn) ·
  OVERTIME HRS 6.2h (warn) · INCIDENT RATE 0.4% (green).

List screen   → all fleet units, search + filter chips (status, type), paginated.

Form screen   → "New Dispatch Order": unit (required select), route (required),
  departure time (required, not in past), cargo type (required), driver
  (required), notes. Rules as required marks + helper text + inline errors;
  "Dispatch" disabled until valid.

Detail screen → one unit record: header (unit ID + status chip + actions),
  meta grid (type, route, driver, km today, fuel %, last ping), and a
  "Today's Route Stops" sub-table + recent event feed.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens above.
2. Extract THIS domain's equivalent of the archetype slots — its live-ticker
   entities and metrics, session/scope label, module list, primary data table
   columns and rows, event/activity log, key summary figure + sparkline, and
   gauge constraints — from the KB + prompt. Standalone: use the Example
   instantiation above.
3. Build each screen in the Visual language + Layout archetype above, imitating
   the example set in `assets/` (dashboard, list, form, detail) and the
   `assets/template.html` seed — with fresh content for the real domain, NOT
   the example labels.
4. Express domain rules as INLINE field validation (required marks, helper text,
   inline errors, disabled-until-valid submit). Never render
   rules/checklist/validation-status/build-note panels or designer/demo controls.
5. One inline `<style>`, semantic HTML5, monospace everywhere, no external
   assets, no CDNs — self-contained.

## Output contract

```
<artifact identifier="admin-finance-terminal" type="text/html" title="Terminal Admin">
<!doctype html>...</artifact>
```
