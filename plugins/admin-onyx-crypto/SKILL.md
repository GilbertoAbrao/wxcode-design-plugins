---
name: admin-onyx-crypto
description: |
  Deep-obsidian admin aesthetic: near-black canvas (#0a0a0f), elevated dark
  panels (#14141c / #1c1c28), emerald primary accent (#10b981) with a neon glow
  border hover, violet secondary accent (#8b5cf6), Inter type with tabular-nums
  on every figure, neon-tinted delta chips (emerald up / rose down), 10px radii,
  hairline #262633 borders. Archetype = wide left rail (220px, section labels +
  grouped nav items + avatar footer) + sticky topbar (context-switcher pill +
  entity address pill + search + icon actions) + 4 KPI cards with sparklines +
  main grid (area chart with timeframe tabs left / ranked-rows side panel right)
  + full-width records table with delta-colored value column. Built for
  high-density monitoring consoles that need a sleek neon-dark aesthetic at a
  glance.
triggers:
  - "deep obsidian admin"
  - "neon dark dashboard"
  - "emerald violet dark admin"
  - "sleek dark monitoring console"
  - "dark neon admin aesthetic"
  - "obsidian panel dashboard"
  - "teal-accent dark admin"
  - "painel escuro neon"
example_prompt: "Apply this deep-obsidian neon admin aesthetic to my domain"
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

# Onyx Admin — Visual Archetype

This plugin contributes a **look** (deep obsidian, emerald neon accent, violet
secondary, dense tabular data) and a **structure** (wide labeled left rail +
sticky topbar + 4 KPI sparkline cards + area chart + ranked-rows side panel +
records table, plus list / form / detail screens). It does **not** contribute a
domain — the subject matter comes from the Knowledge Base and the user's prompt.
Treat the example below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property; hardcode the neutral dark ramp.

- **Canvas / surfaces:** page `#0a0a0f`; surface panel `#14141c`; elevated
  panel `#1c1c28`; hover `#222232`; hairline border `#262633`; lighter border
  `#2e2e40`.
- **Text ramp:** primary `#e8e8f0`, muted `#8a8aa0`, dim `#55556a`.
- **Accent (primary — emerald):** `--accent: #10b981`, `--accent-dim:
  #0d9166`, `--accent-bg: rgba(16,185,129,.10)`, `--accent-glow:
  rgba(16,185,129,.18)`. Active nav bars, primary CTAs, gain states, chart
  strokes, progress fills.
- **Accent (secondary — violet):** `--accent2: #8b5cf6`, `--accent2-bg:
  rgba(139,92,246,.12)`. Secondary badges, secondary CTAs, alternative series.
- **Gain / Loss tokens:** `--gain: #10b981`, `--gain-bg: rgba(16,185,129,.12)`;
  `--loss: #f43f5e`, `--loss-bg: rgba(244,63,94,.12)`. Delta chips recolor by
  direction.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
  sans-serif`. Base 14px. `font-variant-numeric: tabular-nums` on **every**
  numeric cell. Micro-labels 10–11px, `text-transform: uppercase`,
  `letter-spacing: .07em`, muted. Big KPI figures 24px / weight 700 /
  `letter-spacing: -.5px`. Entity addresses and codes in monospace.
- **Density & radius:** compact 9–10px vertical padding on nav items, 18–20px
  panel padding, 16px grid gaps; card radius 10px, control radius 7–8px, pill
  radius 20px (full-round), progress bars 4px tall.
- **Borders & shadows:** 1px hairlines; no drop shadows by default — flat
  terminal feel. Neon glow hover on KPI cards: `0 0 16px var(--accent-glow)` +
  border-color switches to `--accent`.
- **Motion:** `.12s–.15s` background/border hover transitions; neon-dot pulse
  2s ease-in-out on the topbar context status dot. Never bouncy.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Wide left rail** (220px, surface bg, 1px right border, fixed): brand mark +
  product wordmark at top (border-bottom) → **grouped nav** with uppercase
  10px section labels before each group, nav items = icon + label + optional
  count badge (active item: emerald left bar + tinted emerald bg; hover: subtle
  bg lift) → flex spacer → **footer row** (avatar gradient + name + role label).
- **Sticky topbar** (60px, surface bg, 1px bottom border): left cluster =
  **context-switcher pill** (status dot + label + chevron) + **entity address
  pill** (icon + truncated mono address + chevron) → **center search bar** (max
  320px, elevated bg) → right cluster = icon action buttons with notification
  dot + avatar.
- **Main content** (page bg, 24px padding, flex column, gap 20px): **page
  header** (title + subtitle left; ghost + primary CTAs right), then region
  stack below.
- **KPI card row** (4 equal-grid cards): each card = elevated panel (10px
  radius, neon glow on hover) with an uppercase micro-label top, then a row of
  [big tabular figure] + [inline SVG sparkline] side by side, then a footer row
  with a [delta chip (emerald/rose)] + [sub-label]. Figure color can recolor by
  state (emerald / rose / default).
- **Main grid (1fr + fixed 340px side):**
  - **Left — area chart card:** card-header = [title + sub] / [timeframe tab
    row (5 tabs, active = emerald bg)]; then a callout line [big value +
    delta + period]; then an inline SVG area chart (emerald stroke +
    translucent emerald area-fill gradient, faint grid lines, axis labels, live
    endpoint dot).
  - **Right — ranked-rows side panel:** card-header = [title + sub]; body =
    vertical list of rows, each row = [badge chip (letter-mark, alternating
    accent colors)] + [name block (primary label + sub)] + [right-aligned value
    + delta label (gain/loss colored)]. No external images; badge chips use
    inline SVG or CSS letter-marks.
- **Full-width records table card:** card-header = [title + sub] / [view-all
  link]; sticky uppercase header row; dense tbody rows with tinted hover;
  columns include an asset-cell (badge icon + two-line label), numeric columns
  (tabular-nums), a **delta-colored percent column**, a quantity column, a
  total-value column, and an action button. Footer: result count + pager.
- **Records list screen:** toolbar (search pill + filter chips with counts) +
  same dense table + pager.
- **Record form screen:** sectioned cards of labelled fields; **rules appear as
  inline validation** — required marks (`*`), helper text under the field,
  inline error messages on invalid fields, submit disabled-until-valid. No
  rules/checklist/validation-status panel.
- **Record detail screen:** breadcrumb → header band (ID + status pill + action
  buttons) → meta grid (3-column label/value cells) → one or more related-data
  sub-panels (ranked-rows pattern or a mini-table) below.

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key metrics,
status states, record columns, form fields and their rules, and detail fields
— and map them onto the archetype above. If no KB/domain is supplied
(standalone), use the Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules
become inline field validation. Do NOT render build/implementation notes or
designer controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent
> (entities, metrics, states, columns, fields) drawn from the KB + prompt.

```
Domain (illustrative): a multi-account digital-asset portfolio tracker.

Context-switcher pill  → network: "NovaSphere Mainnet" (emerald dot).
Entity address pill    → active account: "0x4f8a…c3d2".
Rail section groups    → PORTFOLIO (Overview, Performance, History), MARKETS
                         (Spot Market, Derivatives, Screener), MANAGE (Wallets,
                         API Keys, Settings).
Active item            → Overview.

KPI cards (4):
  • Portfolio Value $284,912 (sparkline, +8.34% vs last week).
  • 24h Change +$6,241 (sparkline, +2.24% since yesterday).
  • Staked Assets $98,450 (violet sparkline, +0.71%, APY 12.4%).
  • Available Balance $41,307 (loss sparkline, -3.10% from withdrawals).

Area chart (left)      → "Asset Value" — 5 timeframe tabs (1H/24H/7D/30D/ALL,
                          active 24H); callout $284,912 +$6,241; emerald area
                          chart over 24-hour time axis.

Ranked-rows (right)    → "Market Movers · 24h" — 8 rows of ticker badge /
                          name / price / delta; alternating gains and losses.

Records table          → "Holdings" — columns: Asset (badge + ticker + name) /
                          Price / 24h % (delta colored) / Holdings / Value (USD)
                          / Action. 6 rows. "View All →" link.

List screen            → all holdings, search + filter chips (status, type),
                          paginated dense table.

Form screen            → "New Position": asset (required select), account
                          (required), quantity (required, > 0), entry price
                          (required), notes. Rules as required marks + helper
                          text + inline errors; "Add Position" disabled until
                          valid.

Detail screen          → one holding: header (ticker + status pill + actions),
                          meta grid (asset, account, quantity, entry price,
                          current value, added date), and a "Price History"
                          sub-panel + recent activity list.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, gain/loss states, record columns, form fields + rules, detail
   fields — from the KB + prompt. Standalone: use the Example instantiation
   above.
3. Build each screen in the Visual language + Layout archetype above, imitating
   the example set in `assets/` (dashboard, list, form, detail) and the
   `assets/template.html` seed — with fresh content for the real domain, NOT
   the example labels.
4. Express domain rules as INLINE field validation (required marks, helper text,
   inline errors, disabled-until-valid submit). Never render
   rules/checklist/validation-status/build-note panels or designer/demo
   controls.
5. One inline `<style>`, semantic HTML5, `tabular-nums` on figures, no external
   assets, no CDNs — self-contained.

## Output contract

```
<artifact identifier="admin-onyx-crypto" type="text/html" title="Onyx Admin">
<!doctype html>...</artifact>
```
