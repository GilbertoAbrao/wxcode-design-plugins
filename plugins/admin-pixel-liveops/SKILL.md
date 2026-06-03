---
name: admin-pixel-liveops
description: |
  Deep-space dark admin aesthetic: near-black canvas (#0c0a14), neon purple
  (#a855f7 / #c084fc) and cyan (#22d3ee) dual-accent on a violet-tinted dark
  neutral ramp, Inter type with tabular-nums on every figure, 13px compact rows,
  10px radii, hairline #2c2440 borders, glowing pill hover states. Archetype =
  full-height sidebar (entity switcher + grouped nav sections + footer user chip)
  + topbar (title · search · period-selector pills · notification + avatar) +
  4 KPI tiles with sparklines + 2-column grid (area-chart card + segments side
  panel) + full-width status-event table + full-width ranked items list with
  inline bars.
triggers:
  - "deep-space dark admin"
  - "neon purple admin"
  - "violet dark dashboard"
  - "sidebar nav admin"
  - "dual accent dark console"
  - "status-event board"
  - "ranked items panel"
  - "period-selector dashboard"
  - "painel escuro violeta"
example_prompt: "Apply this deep-space neon-purple admin aesthetic to my domain"
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

# Pixel LiveOps — Visual Archetype

This plugin contributes a **look** (deep-space violet dark, neon-purple + cyan
dual accent, glowing hover states) and a **structure** (full-height sidebar with
entity switcher + grouped nav sections, topbar with period filter, KPI tiles with
sparklines, area-chart card + segments panel, status-event table, ranked items
list). It does **not** contribute a domain — the subject matter comes from the
Knowledge Base and the user's prompt. Treat the example below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property; hardcode the violet-dark neutral ramp.

- **Canvas / surfaces:** page `#0c0a14`; sidebar/topbar `#15101f`; card `#1e1730`;
  deep inset `#110e1c`; hairline border `#2c2440`; hover border `#3a2e5a`.
- **Text ramp:** primary `#ece8f5`, muted `#968fb0`. No additional intermediate
  stops needed — the violet shift in the muted value keeps it on-brand.
- **Accent pair:** `--accent: #a855f7` (neon purple), `--accent-soft: #c084fc`
  (softer purple). Primary CTAs, active nav indicator, KPI hover glow. Use
  `rgba(168,85,247,.12)` for tint backgrounds and `rgba(168,85,247,.18)` for glow
  shadows.
- **Second accent:** `--cyan: #22d3ee`. Status "active/live" pills, peak callout
  dots on charts, secondary icon chips, selected data points.
- **State ramp (as tokens):** `--green: #4ade80`, `--red: #f87171`,
  `--amber: #fbbf24`. Used for up/down/warn deltas on KPI tiles and status
  indicators. Tint backgrounds at ~12–15% opacity.
- **Status pills:** active/live → `rgba(34,211,238,.12)` bg + `--cyan` text;
  scheduled/pending → `rgba(168,85,247,.12)` bg + `--accent-soft` text;
  ended/archived → `--border` bg + muted text. Pills have a 5px leading dot
  (`::before`) in `currentColor`.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
  sans-serif`. Base 13px body. `font-variant-numeric: tabular-nums` on **every**
  numeric cell. Section nav labels are 9px uppercase + `letter-spacing:.14em` +
  muted color. KPI values 22px / weight 700 / `letter-spacing:-.02em`. Mono IDs
  and codes in `"Courier New", monospace`.
- **Density & radius:** compact 11px vertical row padding, 16px card padding,
  14px grid gaps; card radius 10px, control radius 8px, pill radius 10px, progress
  bars 4–5px tall / 3–4px radius.
- **Borders & shadows:** 1px hairlines; no drop shadows on panels (flat, terminal
  feel). Hover glow: `0 0 18px rgba(168,85,247,.18)` on cards; `border-color:
  var(--accent)` on focused controls.
- **Motion:** `.12s–.15s` background/border hover transitions; subtle `0 0 18px`
  glow on card hover. Default easing stays gentle; never bouncy.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Full-height sidebar** (220px fixed, surface bg, 1px right border):
  - **Logo strip** (18px padding, 1px bottom border): inline SVG glyph (accent
    color) + studio/brand name in small-caps, 10px.
  - **Entity switcher** (12px margin, surface inset bg, 8px radius): active entity
    name + sub-line + trailing chevron. Clicking opens a picker.
  - **Nav sections** (multiple, each: 9px uppercase label + nav items below): each
    nav item = 14px icon + label + optional badge chip. Active item: accent-tinted
    bg + `--accent-soft` text + 3px left border strip in `--accent`.
  - **Footer user chip** (auto pushed to bottom, 1px top border): small avatar
    circle (purple gradient, initials) + display name + role label.
- **Top bar** (56px, surface bg, 1px bottom border, sticky):
  - Left: **section title** (semibold, with muted sub-section span).
  - Center: **search input** (inset bg, 8px radius, magnifier icon left).
  - Right: **period-selector pill group** (4 pills: e.g. 7D / 14D / 30D / 90D;
    active pill has accent bg + white text); notification icon button with red
    badge dot; **avatar circle** + display name.
- **Main content** (page bg, 20px padding, vertical flex with 20px gaps):
- **KPI tile row** (4 tiles, equal grid): each tile = card bg + border + 10px
  radius + hover glow; layout = `[label + icon chip top row] → [big figure] →
  [delta chip + sparkline SVG bottom row]`. Delta chips recolor by state
  (green / red / amber). Sparkline is a 52×20 `<polyline>` in the delta color.
- **2-column grid (`1fr 300px`):**
  - **Left — trend chart card:** titled panel with sub-line; SVG area chart with
    gradient fill (accent → transparent), dotted gridlines, y-axis labels, x-axis
    date labels, and a highlighted peak dot in cyan with a callout label.
  - **Right — segments side panel:** titled panel listing rows of
    `[name] [count · % share] [mini horizontal bar (accent gradient fill)]`;
    a "View all →" footer link.
- **Full-width status-event table:** titled panel + primary action button header;
  sticky uppercase `<th>` header; dense rows with **status pills**, a type chip
  per row, a time-window cell, and 2 icon action buttons (edit + toggle).
- **Full-width ranked items list:** titled panel; rows of
  `[rank number] [item name + tier/rarity chip] [proportional inline bar + sales count] [revenue value]`.
- **Records list screen:** full-width table with search input + filter chips + count;
  dense rows with status pills; pager at footer.
- **Record form screen:** sectioned cards of labelled fields; **rules appear as
  inline validation** — required marks (`*`), helper text under the field, and
  inline error messages on invalid fields, with the primary submit
  disabled-until-valid. No rules/checklist/validation-status panel.
- **Record detail screen:** breadcrumb + header band (entity ID + status pill +
  key actions), a meta grid (3-column label/value cells), and one or more related
  sub-panels (a status-board–style row list or a mini-table) below.

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key metrics,
status states, event/record list columns, form fields and their rules, and detail
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
Domain (illustrative): a live-service game studio operations console.

Entity switcher  → active title: "Void Hunters · Mobile · Live Service".
Section title    → "Live Operations · Dashboard".
Period selector  → 7D / 14D / 30D / 90D (30D active).
Nav sections     → LIVE OPS (Dashboard, Live Events, Rewards);
                   ECONOMY (In-Game Items, Currencies, Offers);
                   PLAYERS (Segments, Bans, Support);
                   SETTINGS (Config, Releases).

KPI tiles (4):
  • Daily Active Users 1,284,671 (▲4.2% vs last week, sparkline trending up).
  • D1 Retention 38.7% (▼1.3pp vs prev 30D, sparkline trending down).
  • ARPDAU $0.94 (▲$0.07, sparkline trending up, cyan icon chip).
  • Live Events 12 active (⚠ 3 ending today, sparkline amber).

Trend chart (left) → "Daily Active Users · 30 Days" — area chart (purple fill +
  cyan peak dot + callout "Peak May 18"), y-axis 500K–1.4M, x-axis May dates.

Segments panel (right) → "Player Segments" — rows of
  [Whales · 38,540 · 3.0% + bar], [Engaged F2P · 514,668 · 40.1%],
  [At-Risk · amber bar], [New Players · cyan bar], [Dormant · neutral bar].

Status-event table → "Live Events" with "New Event" button:
  columns: Event / Type / Window / Status pill / Actions.
  States used: Live (cyan) / Scheduled (purple) / Ended (muted).
  6 rows with game event names.

Ranked items list → "Top Items by Revenue · 30D":
  columns: rank / item name + rarity chip / proportional bar + sales count / revenue.
  8 rows; rarity chips: Legendary (amber tint), Epic (purple tint),
  Rare (cyan tint), Common (neutral).

List screen      → all events, search + filter chips (status, type), paginated.

Form screen      → "New Event": title (required), type (required select), window
  start / end (required dates, end must be after start), status (required select),
  description. Rules shown as required marks + helper text + inline errors;
  "Create Event" disabled until valid.

Detail screen    → one event: breadcrumb + header (event title + status pill +
  Edit / Archive buttons), meta grid (type, window, status, created, owner,
  affected titles), "Participation Metrics" sub-table + recent activity feed.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, status states, event/record columns, form fields + rules, detail
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
<artifact identifier="admin-pixel-liveops" type="text/html" title="Pixel LiveOps Admin">
<!doctype html>...</artifact>
```
