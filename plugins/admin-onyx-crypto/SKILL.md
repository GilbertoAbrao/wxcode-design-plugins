---
name: admin-onyx-crypto
description: |
  Dark-mode crypto portfolio console with a sleek neon aesthetic:
  emerald (#10b981) and violet (#8b5cf6) accents on deep obsidian
  backgrounds. Left rail navigation, topbar with network/wallet
  switcher, 4 KPI cards (portfolio value, 24h change, staked,
  available), area price/value chart with timeframe tabs, a holdings
  table with gain/loss-colored deltas, and a market movers side list.
  Use when the brief calls for a crypto, web3, DeFi, or digital-asset
  operations console with a dark neon visual direction.
triggers:
  - "crypto admin"
  - "crypto dashboard"
  - "web3 admin"
  - "defi dashboard"
  - "digital asset portfolio"
  - "crypto portfolio console"
  - "dark crypto ui"
  - "blockchain admin"
  - "painel crypto"
  - "加密资产管理后台"
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
  example_prompt: "Build me a dark-mode crypto portfolio admin console — left rail nav, topbar with network and wallet switcher, 4 KPI cards, area price chart with timeframe tabs, holdings table with colored deltas, and a market movers side panel."
---

# Onyx Crypto Admin Skill

Produce a sleek dark-mode digital-asset portfolio console — a layout
crypto operations teams recognize as the standard monitoring surface.

## Workflow

1. Read the active DESIGN.md (if present); otherwise use the Onyx
   palette: emerald (#10b981) primary, violet (#8b5cf6) secondary,
   obsidian backgrounds (#0a0a0f base / #14141c surface / #1c1c28
   elevated), border #262633, text #e8e8f0 / muted #8a8aa0.
2. Extract from the brief: product/protocol name, base asset for the
   chart, portfolio composition, wallet address label, network name.
   Invent fictional token tickers if none provided (e.g. NOVA, KRYO,
   ZEPH, ARXA, PLIX).
3. Layout:
   - **Left rail (220px)**: brand mark + product name at top, grouped
     nav with section labels (PORTFOLIO, MARKETS, MANAGE), each item
     icon (inline SVG) + label + optional badge. Active item has
     emerald left bar and tinted background. Bottom: settings + avatar
     row.
   - **Top bar (60px)**: network badge pill (chain icon + name) and
     wallet switcher dropdown on the left, search bar in center, icon
     row (bell, grid, avatar) on the right.
   - **Page header strip**: title "Portfolio Overview", subtitle date
     range, "Export CSV" ghost button, "+ Deposit" emerald primary CTA.
   - **4 KPI cards** (dark elevated surface, 10px radius, subtle neon
     glow border): each card has an uppercase label, a large tabular
     number, an inline SVG mini sparkline, and a delta chip (emerald
     up / red down). Cards: Portfolio Value (USD), 24h Change (%),
     Staked Assets (USD), Available Balance (USD).
   - **Main grid (8/4 columns)**:
     - LEFT (8 cols): "Asset Value" chart card — title, 5 timeframe
       tabs (1H, 24H, 7D, 30D, ALL), a smooth area chart as inline SVG
       with faint grid lines, emerald stroke and translucent emerald
       fill gradient, current value callout.
     - RIGHT (4 cols): "Market Movers" side list — 8 fictional tokens,
       each row: ticker badge, name, price, 24h delta chip. Alternating
       gains (emerald) and losses (red) for visual variety.
   - **Holdings table card**: header "Holdings" + "View All" link,
     columns (asset icon + ticker + name / current price / 24h% colored
     / amount held / total value / action). 6–8 rows, tinted hover, no
     external images — use inline SVG letter-mark circles as asset icons.
4. Typography: inline system font stack only — "Inter", system-ui,
   -apple-system, "Segoe UI", Roboto, sans-serif. `font-variant-numeric:
   tabular-nums` on all figures. Small caps + letter-spacing for section
   labels. Emerald for active states; violet for secondary accents
   (badges, secondary CTAs).
5. Colors: every chromatic color as :root CSS custom property; SVG
   fill/stroke chromatic colors use var(--token) or currentColor; only
   neutral dark bg/border/gray text hardcoded.
6. One inline `<style>`, semantic HTML, no external assets, no CDNs,
   no lorem ipsum, no real brand names or logos.

## Output contract

```
<artifact identifier="admin-onyx-crypto" type="text/html" title="Onyx Crypto Admin">
<!doctype html>...</artifact>
```
