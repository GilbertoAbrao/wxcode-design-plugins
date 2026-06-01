---
name: admin-pixel-liveops
description: |
  Dark-mode game studio live-operations admin dashboard archetype.
  Deep-space backgrounds (#0c0a14 / #15101f / #1e1730) with neon purple
  (#a855f7 / #c084fc) and cyan (#22d3ee) accents. Left sidebar with
  game/title switcher and nav sections, topbar with search + period
  selector + avatar, 4 KPI tiles (DAU, D1 retention, ARPDAU, live
  events count), DAU-over-time SVG line chart, live events board with
  Live/Scheduled/Ended status pills, top in-game items list with
  revenue bars, and a player segments side panel. Use when the brief
  involves a game studio, live service, mobile game ops, or any
  real-time game analytics dashboard.
triggers:
  - "game dashboard"
  - "liveops"
  - "live ops"
  - "game studio admin"
  - "game analytics"
  - "mobile game ops"
  - "DAU dashboard"
  - "live events board"
  - "in-game items"
  - "player segments"
  - "game operations"
  - "painel de operações de jogo"
  - "游戏运营后台"
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
  example_prompt: "Build me a dark-mode live-ops admin dashboard for a game studio — sidebar with game switcher, KPI tiles for DAU/retention/ARPDAU/live events, a DAU trend chart, a live events board with status pills, a top in-game items list, and a player segments panel."
---

# Pixel LiveOps Admin Skill

Produce the canonical dark-mode game studio live-operations admin layout —
the control center an ops team keeps open all day to monitor player health,
tune live events, and track in-game economy.

## Design language

- **Palette** (CSS custom properties on `:root`): neon purple `--accent`
  (#a855f7), soft purple `--accent-soft` (#c084fc), cyan `--cyan` (#22d3ee).
  Text: `--text` (#ece8f5), `--text-muted` (#968fb0). Backgrounds: `--bg`
  (#0c0a14), `--surface` (#15101f), `--card` (#1e1730). Border: `--border`
  (#2c2440). Hardcode neutral dark values; never put chromatic hex in rules.
- **Typography**: `"Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`.
  All figures use `font-variant-numeric: tabular-nums`. No external font loads.
- **Status pills**: Live → cyan bg (#22d3ee at 15% opacity, cyan text);
  Scheduled → purple bg (#a855f7 at 15% opacity, soft-purple text);
  Ended → neutral (#2c2440, muted text).
- **Accents on interactive states**: neon purple border or glow on hover/active.

## Layout

1. **Left sidebar (220px fixed)**
   - Logo mark (inline SVG pixel-controller icon, neon purple) + studio name
     "NOVA PIXEL STUDIO" in small caps.
   - Game/title switcher dropdown: shows active game name + chevron. Options:
     "Void Hunters", "Chromarush", "Starfall Siege".
   - Nav sections: LIVE OPS (Dashboard, Live Events, Rewards), ECONOMY
     (In-Game Items, Currencies, Offers), PLAYERS (Segments, Bans, Support),
     SETTINGS (Config, Releases). Each item: tiny inline SVG icon + label.
     Active item has neon purple left-border strip and `--accent` text.

2. **Top bar (56px)**
   - Left: current section title "Live Operations · Dashboard" in semibold.
   - Center: search input with magnifier SVG, placeholder "Search players,
     events, items…", `--surface` background, `--border` border.
   - Right: period selector pills (7D / 14D / 30D / 90D), notification bell
     SVG with red badge showing "3", avatar circle ("KL" initials, purple bg),
     studio display name "Kaede L.".

3. **KPI tiles strip (4 cards, equal width)**
   - **DAU**: "1,284,671" — delta "+4.2% vs last week" in green, tiny inline
     SVG sparkline, icon: person group SVG.
   - **D1 Retention**: "38.7%" — delta "−1.3pp" in red.
   - **ARPDAU**: "$0.94" — delta "+$0.07" in green.
   - **Live Events**: "12 active" — delta "3 ending today" in amber.
   Tile shape: `--card` bg, `--border` border, 10px radius, subtle neon glow
   on hover.

4. **Main 2-column grid**
   - **LEFT (grows, ~65%)**: DAU trend chart card — title "Daily Active Users
     (30 days)", subtitle "Void Hunters · all platforms". Inline SVG area chart
     with neon purple fill gradient (top to transparent) over a dark grid.
     X-axis: abbreviated dates; Y-axis: 200K–1.4M labels. Add a "Peak" callout
     dot in cyan at the highest point.
   - **RIGHT (~35%)**: Player Segments panel — title "Segments · live". List of
     5 segments (Whales, Engaged F2P, At-Risk, New Players, Dormant) each with
     a mini horizontal bar (neon purple fill, `--border` track), count, and %
     share. Bottom: "View all segments →" link in `--accent`.

5. **Live Events board (full width)**
   - Section header "Live Events" + "New Event" button (neon purple bg).
   - Table: columns — Event, Type, Window, Status, Actions.
   - 6 rows with invented game events: "Void Surge Weekend" (Limited Drop,
     Sat 00:00→Sun 23:59, Live), "Crystal Cache Bundle" (Bundle, Mon 09:00→
     Mon 23:59, Scheduled), "Chromarush Season 3" (Season Pass, ongoing, Live),
     "Shard Storm Challenges" (Challenge, ends in 2h, Live), "Starfall Siege
     Collab" (Crossover, Thu→Sun, Scheduled), "Galaxy Grind Boost" (XP Boost,
     archived, Ended). Actions: Edit pencil SVG + Pause/Play toggle SVG, muted.

6. **Top In-Game Items (full width)**
   - Section header "Top Items by Revenue · 30D".
   - List of 8 items: item name + rarity chip + sales count + revenue amount +
     inline horizontal bar (proportional, `--accent` fill). Invented items:
     "Stellar Shard Pack" (Legendary), "Void Blade Skin" (Epic), "Crystal
     Keystone" (Rare), "XP Catalyst ×5" (Common), "Nova Pilot Frame" (Epic),
     "Phase Drift Emote" (Rare), "Chromaflux Bundle" (Legendary),
     "Energy Core ×10" (Common).

## Output contract

```
<artifact identifier="admin-pixel-liveops" type="text/html" title="Pixel LiveOps Admin">
<!doctype html>...</artifact>
```

One `<style>` block inside `<head>`. No `<link>` to external sheets. No
`<script src=...>`. No CDN URLs. All SVG inline. All colors via CSS custom
properties (chromatic) or hardcoded neutrals. Single self-contained file,
10–30 KB target.
