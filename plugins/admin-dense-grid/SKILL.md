---
name: admin-dense-grid
description: |
  High-density dark-mode operations dashboard in the trading-desk style.
  Distinctive feature is DENSITY: compact rows (24–28px), small type
  (11–13px), monospace tabular figures, color-coded up/down deltas.
  Panels: slim toolbar → watchlist instruments table → positions/orders
  mini-table → sparkline strip → order-book depth panel → stats row.
  Use when the brief asks for a trading terminal, ops console, data-grid
  dashboard, or any layout where maximum information per pixel matters
  more than whitespace and aesthetics.
triggers:
  - "dense admin"
  - "trading dashboard"
  - "trading terminal"
  - "ops console"
  - "data grid admin"
  - "watchlist dashboard"
  - "order book"
  - "dark ops admin"
  - "compact dashboard"
  - "high density dashboard"
  - "painel denso"
  - "terminal de operações"
  - "高密度仪表盘"
  - "交易台"
od:
  mode: prototype
  surface: web
  scenario: operations
  preview:
    type: html
    entry: index.html
  design_system:
    requires: true
    sections: [color, typography, layout, components]
  craft:
    requires: [pixel-discipline, laws-of-ux]
  example_prompt: "Build a high-density dark-mode operations dashboard — trading-desk style with compact watchlist, positions table, order book, sparkline strip, and monospace tabular figures."
---

# Dense Grid Admin Skill

Produce a maximum-information-density admin layout in the style of a
professional trading terminal or operations console. Every pixel earns
its place; whitespace is used only to separate data groups, not for
breathing room.

## Core design tokens

| Token | Value | Usage |
|-------|-------|-------|
| `--bg-base` | `#0c0f12` | Page background |
| `--bg-panel` | `#12161b` | Panel/card background |
| `--bg-row-hover` | `#191e25` | Table row hover |
| `--border` | `#232a31` | All borders and dividers |
| `--text-primary` | `#d7dde4` | Body and label text |
| `--text-muted` | `#7b8694` | Secondary labels, timestamps |
| `--accent-green` | `#22c55e` | Up delta, positive P&L, bid |
| `--accent-red` | `#ef4444` | Down delta, negative P&L, ask |
| `--accent-blue` | `#3b82f6` | Primary action, links, selected row |
| `--mono` | `ui-monospace, Menlo, monospace` | All numeric figures |

Spacing follows a 4-px grid: `4 / 8 / 12 / 16 / 20 / 24 / 32px`.
Font sizes: labels 11px, values 12px, headers 13px, section titles 13px bold.

## Workflow

1. Read the active DESIGN.md (if present); otherwise use the token
   defaults above. Dark palette is non-negotiable for this archetype.

2. Extract from the brief:
   - Domain name and product/workspace label for the toolbar.
   - Instrument type (equities, FX, crypto, commodities, custom ops
     entities) — determines column names and symbol conventions.
   - Main entity set: 8–12 invented symbols/tickers with plausible
     figures (do NOT reproduce real market data; invent original symbols
     such as NOVQ, ELTX, MRFA, etc.).

3. Layout — assemble these panels top-to-bottom then side-by-side:

   ### Slim toolbar (36px height)
   - LEFT: product mark (small inline SVG or 2-letter monogram in a
     4×4 blue square) + workspace name in 13px bold.
   - MIDDLE: compact filter chips (All / Active / Flagged / Alerts) as
     toggle pills + a small search input (icon + placeholder, 240px max).
   - RIGHT: live clock (HH:MM:SS, monospace), connection-status dot
     (green = live), notification bell with count badge, avatar circle
     with initials.

   ### Main content grid — two columns (flex or CSS grid)

   #### LEFT column (~60% width)

   **Watchlist / instruments table**
   - Table header row: SYMBOL | LAST | CHG | CHG% | VOL | OPEN | HIGH | LOW
   - 10–12 compact rows (28px each), alternating subtle background.
   - SYMBOL: bold 12px, blue on hover.
   - LAST: monospace 12px.
   - CHG and CHG%: colored green (positive) or red (negative); include
     a tiny ▲/▼ glyph before the number.
   - VOL: monospace muted, abbreviated (K / M).
   - OPEN / HIGH / LOW: monospace muted gray.
   - Clicking a row marks it selected (blue left border + tinted row).
   - Compact pagination or "1–12 of 48" label below.

   **Positions / open orders mini-table**
   - Sits below watchlist, separated by a 1px `--border` divider.
   - Header: "POSITIONS" label (uppercase 11px muted) + "8 open" count.
   - Columns: SYM | SIDE (BUY tag green / SELL tag red) | QTY | AVG PRICE | MARK | UNRL P&L
   - 5–6 rows, same compact style.

   #### RIGHT column (~40% width, stacked panels)

   **Sparkline strip**
   - 2×2 or 2×3 grid of mini sparkline cards (each ~100px wide, 56px tall).
   - Each card: symbol label top-left (11px muted) + last price top-right
     (monospace 12px) + inline SVG polyline sparkline with a subtle fill,
     green or red based on direction + delta % bottom-right (colored).
   - Thin border, dark background.

   **Order book / depth panel**
   - Title "ORDER BOOK" + selected symbol name.
   - TWO columns side by side: BID (left, green text) | ASK (right, red text).
   - 8 price levels each, with SIZE column. Depth bars shown as background
     width percentage fills (green on bid side, red on ask side, opacity 0.12).
   - Spread row in the center (muted, small).

   **Stats row / ticker strip**
   - A bottom strip inside the right column with 4–5 compact stat tiles:
     TOTAL VOL / DAY TRADES / WIN RATE / DRAWDOWN / NET P&L
   - Each tile: label (11px muted uppercase) + value (monospace 14px bold,
     colored when directional) + tiny delta chip below.

4. Typography rules:
   - Body/labels: system font stack (`-apple-system, BlinkMacSystemFont,
     'Segoe UI', sans-serif`), no external load.
   - All numeric figures: `font-family: ui-monospace, Menlo, monospace;
     font-variant-numeric: tabular-nums;`
   - Use letter-spacing 0.06em on ALL-CAPS section labels.

5. Interactivity hints (CSS-only):
   - Row hover: `--bg-row-hover` background.
   - Selected row: blue left 2px border + tinted background.
   - Filter chips: toggle via `:focus-within` or a checked state; show
     pressed chip with `--accent-blue` border and subtle tint.
   - Toolbar search: expand on focus (120px → 240px, transition 200ms).

6. Palette-ready contract:
   - Every chromatic color (greens, reds, blue, text-primary, text-muted)
     must be a `:root` CSS custom property.
   - SVG fill/stroke must use `var(--token)` or `currentColor`.
   - Neutral backgrounds and border (#0c0f12, #12161b, #232a31) may be
     hardcoded.

7. One inline `<style>`, semantic HTML, no external assets, no CDNs,
   no lorem ipsum, no real market data. Invent all symbols and figures.

## Output contract

```
<artifact identifier="admin-dense-grid" type="text/html" title="Dense Grid Admin">
<!doctype html>...</artifact>
```
