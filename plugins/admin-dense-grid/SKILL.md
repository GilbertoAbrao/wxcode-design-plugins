---
name: admin-dense-grid
description: |
  Maximum-information-density dark-mode admin aesthetic: near-black canvas
  (#0c0f12), raised panels (#12161b), blue accent (#3b82f6), green/red
  directional signals, all-monospace tabular figures on a 4-px grid, 11–12px
  type with uppercase 10px section labels. Archetype = slim 36px toolbar
  (brand mark + filter chips + search + live clock + status dot + avatar) +
  2-column main grid: left ~60% = primary data table (10–12 compact 28px rows,
  status-colored deltas) + secondary mini-table; right ~40% = sparkline strip
  (2×3 mini cards) + depth/book panel (two-column bid/ask with depth-bar fills)
  + 5-tile stats strip. Built for maximum data density: every pixel earns its
  place, whitespace separates data groups only.
triggers:
  - "dense data terminal"
  - "maximum density admin"
  - "compact data grid admin"
  - "dark compact console"
  - "blue accent dense admin"
  - "monospace tabular admin"
  - "high-density dark admin"
  - "operations console dark"
  - "painel denso escuro"
  - "terminal de dados compacto"
example_prompt: "Apply this high-density dark-mode terminal aesthetic to my domain"
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

# Dense Grid Admin — Visual Archetype

This plugin contributes a **look** (near-black canvas, blue accent, monospace
tabular data, ultra-compact rows) and a **structure** (slim toolbar + 2-column
main grid: primary data table + secondary mini-table on the left, sparkline
strip + depth panel + stats strip on the right, plus list / form / detail
screens). It does **not** contribute a domain — the subject matter comes from
the Knowledge Base and the user's prompt. Treat the example below as
illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property; hardcode the neutral dark ramp.

- **Canvas / surfaces:** page `#0c0f12`; raised panel `#12161b`; row hover
  `#191e25`; hairline border `#232a31`; stronger border `#2e3640`.
- **Text ramp:** primary `#d7dde4`, muted `#7b8694`, faint `#4b5563`.
- **Accent:** `--accent-blue: #3b82f6`. Primary actions, selected-row markers,
  active nav, links. Hover tint `rgba(59,130,246,.08)`.
- **Directional signals:** `--up: #22c55e` (positive / bid side), `--dn: #ef4444`
  (negative / ask side), each with dim tints at ~10–15% alpha for cell
  backgrounds and depth-bar fills.
- **Typography:** body `-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`;
  all numeric figures `ui-monospace, Menlo, "Courier New", monospace` +
  `font-variant-numeric: tabular-nums`. Font sizes: section labels 10px
  (uppercase, letter-spacing 0.08em), body labels 11px, data values 12px, panel
  titles 13px bold. Stat tile values 14px bold.
- **Density & spacing:** 4-px grid throughout — `4 / 8 / 12 / 16 / 20 / 24px`
  spacings. Table rows 28px tall (3px vertical padding per cell). Toolbar 36px.
  Panel headers 26–28px.
- **Borders:** 1px hairlines at `#232a31` do all separation; no drop shadows
  (flat terminal feel). Row dividers `rgba(35,42,49,.6)`.
- **Motion:** `.15s` background/border hover transitions; search input
  width-expand on focus (`200ms cubic-bezier(0.23,1,0.32,1)`). Never bouncy.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Slim toolbar** (36px, panel bg, 1px bottom border, flex-row): brand mark
  (20×20 blue square with 2-letter monogram) + workspace label → separator →
  filter chips (3–4 pill toggles, active = blue border + text) → search input
  (icon + placeholder, expands on focus, 260px max) → right-anchored cluster:
  live clock (monospace 11px), connection status dot (green), notification bell
  with badge, avatar circle.
- **2-column main grid** (flex, left ~62%, right ~38%, 1px divider):
  - **Left column** (flex column, scrollable):
    - **Primary data table:** panel with header (title + count + one action),
      sticky uppercase 10px column headers, 10–12 compact rows (28px), first
      column bold with hover-blue text, numeric columns in monospace with
      `--up`/`--dn` color for directional values, selected row = blue 2px left
      border + blue tint, compact pagination footer (range label + prev/next).
    - **Secondary mini-table:** below the primary table, separated by 1px border;
      panel header (uppercase label + count chip), 5–6 compact rows with a
      two-value tag column (green/red colored tags), numeric monospace columns,
      one directional P&L-style column.
  - **Right column** (flex column, scrollable):
    - **Sparkline strip:** panel with a 2×3 grid of mini-cards (each: symbol
      label top-left + last value top-right, inline SVG polyline + area-fill
      gradient in `--up`/`--dn` color, delta % bottom-right). Thin border, dark
      bg.
    - **Depth / book panel:** panel with title + selected-symbol label; two
      sub-columns side-by-side (left = bid rows in `--up` color; right = ask
      rows in `--dn` color); each row shows 2 values in monospace; background
      depth-bar fills by percentage; spread/mid row between the two sides.
    - **Stats strip:** panel with header; a 5-tile horizontal grid — each tile:
      uppercase label (10px muted) + large monospace value (14px bold, colored
      when directional) + tiny delta chip below.
- **List screen:** same primary-data-table archetype as its own page — toolbar
  (search + filter chips + count badge) + the same dense table + pager.
- **Form screen:** sectioned cards of labelled fields; **rules appear as inline
  validation** — required marks (`*`), helper text under the field, and inline
  error messages on invalid fields; primary submit disabled-until-valid. No
  rules/checklist/validation-status panel.
- **Detail screen:** breadcrumb + header band (title + status tag + key
  actions), a meta grid (label/value pairs, 3 columns, monospace values), and
  one or more related-data sub-panels (the mini-table row pattern or a stats
  strip) below.

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key metrics,
directional states, record columns, form fields and their rules, and detail
fields — and map them onto the archetype above. If no KB/domain is supplied
(standalone), use the Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules
become inline field validation. Do NOT render build/implementation notes or
designer controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent
> (entities, metrics, directional states, columns, fields) drawn from the KB + prompt.

```
Domain (illustrative): a financial instrument monitoring console.

Toolbar workspace label → "NovexOps".
Filter chips → All / Active / Flagged / Alerts (with count badge).
Connection dot → green "Live".

Primary data table     → "Watchlist" — columns: SYMBOL | LAST | CHG | CHG% |
  VOL | OPEN | HIGH | LOW. 12 compact rows with invented symbols (NOVQ, ELTX,
  MRFA, ZYLK, ORBN, FXDT, VELM, KRUX, TAQL, SNVX, BQRF, LXPR); CHG/CHG%
  green (▲) or red (▼); VOL/OPEN/HIGH/LOW muted monospace; selected row tinted
  blue; footer shows "1–12 of 48".

Secondary mini-table   → "Positions" — columns: SYM | SIDE | QTY | AVG PRICE |
  MARK | UNRL P&L | STATUS. 6 rows; SIDE tag green "BUY" or red "SELL"; UNRL
  P&L green (positive) or red (negative); STATUS "OPEN" in matching color.

Sparkline strip        → 6 cards in 2×3 grid: NOVQ (+1.33% green), ELTX
  (-1.21% red), MRFA (+1.74% green), ORBN (+2.94% green), ZYLK (-1.19% red),
  VELM (+1.43% green).

Depth/book panel       → "Order Book · NOVQ": 8 bid levels (green, left) and
  8 ask levels (red, right), spread row: "Spread: 0.02 · Mid: 284.40".

Stats strip            → "Session Stats · Today · UTC": TOTAL VOL 24.8M |
  DAY TRADES 142 | WIN RATE 64.1% (green) | DRAWDOWN -1.8% (red) |
  NET P&L +3,389 (green).

List screen            → all watchlist instruments, search + filter chips
  (direction, status), paginated dense table.

Form screen            → "New Instrument": symbol (required, format: 2–6 caps),
  name (required), category (required select), target price (required, > 0),
  alert threshold % (required, 0–100). Rules: required marks + helper text +
  inline errors; "Add Instrument" disabled until valid.

Detail screen          → one instrument: breadcrumb + header (symbol + status
  tag + actions), meta grid (name, category, exchange, added date, last updated,
  alert), related panels: recent price history mini-table + activity log.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, directional states, record columns, form fields + rules, detail
   fields — from the KB + prompt. Standalone: use the Example instantiation above.
3. Build each screen in the Visual language + Layout archetype above, imitating
   the example set in `assets/` (dashboard, list, form, detail) and the
   `assets/template.html` seed — with fresh content for the real domain, NOT the
   example labels.
4. Express domain rules as INLINE field validation (required marks, helper text,
   inline errors, disabled-until-valid submit). Never render
   rules/checklist/validation-status/build-note panels or designer/demo controls.
5. One inline `<style>`, semantic HTML5, `tabular-nums` on all numeric figures,
   no external assets, no CDNs — self-contained.

## Output contract

```
<artifact identifier="admin-dense-grid" type="text/html" title="Dense Grid Admin">
<!doctype html>...</artifact>
```
