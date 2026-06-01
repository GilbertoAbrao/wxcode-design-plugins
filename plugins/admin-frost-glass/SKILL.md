---
name: admin-frost-glass
description: |
  Glassmorphism operations dashboard archetype — frosted, translucent glass
  cards layered over a deep indigo-violet-teal radial gradient canvas.
  Signature style: backdrop-filter blur, 1px translucent white border,
  ambient soft shadows, cyan (#22d3ee) and violet (#a78bfa) accent system,
  near-white text on a dark surface. Use when the brief calls for dark mode,
  futuristic aesthetics, premium SaaS analytics, or any "frosted glass" look.
triggers:
  - "glassmorphism dashboard"
  - "frosted glass admin"
  - "dark gradient dashboard"
  - "glass ui analytics"
  - "frost glass"
  - "dark premium dashboard"
  - "futuristic analytics"
  - "painel escuro translucido"
  - "玻璃拟态仪表盘"
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
  example_prompt: "Build me a dark glassmorphism analytics dashboard — frosted glass cards over a deep gradient, KPI tiles, inline SVG chart, data table, and side panel with cyan and violet accents."
---

# Frost Glass Admin Skill

Produce the signature glassmorphism analytics dashboard — dark gradient canvas
with frosted-glass panels, futuristic data density, and a refined cyan/violet
accent system. The glass effect is non-negotiable; everything else adapts.

## Palette tokens (all as CSS custom properties on :root)

```css
:root {
  /* Canvas gradient stops */
  --grad-a: #0f0c29;
  --grad-b: #1a0533;
  --grad-c: #0d2137;
  --grad-d: #0c2a3a;

  /* Accent system */
  --accent-cyan: #22d3ee;
  --accent-cyan-dim: #0891b2;
  --accent-violet: #a78bfa;
  --accent-violet-dim: #7c3aed;
  --accent-rose: #f472b6;
  --accent-emerald: #34d399;
  --accent-amber: #fbbf24;

  /* Glass surfaces */
  --glass-bg: rgba(255, 255, 255, 0.06);
  --glass-bg-hover: rgba(255, 255, 255, 0.10);
  --glass-border: rgba(255, 255, 255, 0.12);
  --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.36);
  --glass-blur: blur(16px);

  /* Chart series */
  --chart-1: #22d3ee;
  --chart-2: #a78bfa;
  --chart-3: #34d399;
  --chart-4: #fbbf24;

  /* Text */
  --text-primary: rgba(255, 255, 255, 0.95);
  --text-muted: rgba(255, 255, 255, 0.50);
  --text-faint: rgba(255, 255, 255, 0.28);
}
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use the tokens above.
2. Extract from the brief: product/company name, domain (infra, SaaS ops, fintech,
   logistics, etc.), 4 primary KPIs, record entity for the table.
3. Invent coherent metrics and labels — no lorem ipsum, no placeholder text.

## Layout

- **Body**: `background: radial-gradient(ellipse at 60% 20%, var(--grad-b), var(--grad-a) 55%, var(--grad-c) 80%, var(--grad-d))` covering 100vh, fixed.
- **Glass sidebar (72px wide collapsed rail OR 220px full)**: glass surface, brand icon + product wordmark at top, 6–8 nav items each with a small inline SVG icon + label. Active item: left 2px cyan bar + cyan text glow.
- **Glass topbar (60px)**: glass panel full width. Left: hamburger + breadcrumb path. Center: search field with frosted input styling. Right: notification icon, avatar circle, username.
- **Greeting strip**: white heading "Good morning, <name>" + muted date + "Export" ghost button + cyan "+ New Event" primary button.
- **4 glass KPI tiles** (equal columns): each card has — small cyan/violet dot accent top-right, uppercase muted label, large near-white metric, tiny inline SVG sparkline (5–7 points), delta chip (emerald or rose). Cards use `var(--glass-bg)`, `backdrop-filter: var(--glass-blur)`, `border: 1px solid var(--glass-border)`, `box-shadow: var(--glass-shadow)`.
- **Main grid (2:1 ratio)**:
  - LEFT (two-thirds): primary chart card — title, 4 period tabs (1H, 24H, 7D, 30D), legend row, area/line inline SVG chart with subtle grid lines (rgba strokes), gradient area fill using SVG `<linearGradient>` from accent-cyan to transparent.
  - RIGHT (one-third): glass side panel — "Live Alerts" list, 5–6 entries with colored dot, short message, relative time; OR "Top Sources" bar list with mini bar segments in var(--chart-*) colors.
- **Wide glass table card**: header with title + "View All" link, 6–8 rows, columns: entity name + icon, category, value, date, status pill. Status pills: emerald/amber/rose for active/pending/critical. Tinted hover row via `--glass-bg-hover`.
- **Scrollbar**: thin, semi-transparent, matching the dark palette.

## Typography

- System stack only: `"Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`.
- No external font loads.
- KPI metric numbers: 28–32px, weight 700, `color: var(--text-primary)`.
- Section labels: 10–11px, weight 600, `letter-spacing: 0.08em`, `text-transform: uppercase`, `color: var(--text-muted)`.
- Body text: 13–14px, `color: var(--text-primary)`.
- Muted secondary: `color: var(--text-muted)`.

## Rules

- ALL chromatic colors (hex, hsl, rgb with saturation) must be referenced via
  `var(--token)` or `currentColor` in CSS rules and SVG attributes.
  Neutral rgba glass surfaces (rgba whites/blacks with no hue) may stay inline.
- No external CDN, no web font loads, no image embeds, no lorem ipsum.
- All SVG inline: charts, icons, sparklines. Use `var()` for fill/stroke colors.
- Single `<style>` block, all CSS contained within the HTML file.
- Target 10–30 KB final file.

## Output contract

```
<artifact identifier="admin-frost-glass" type="text/html" title="Frost Glass Admin">
<!doctype html>...</artifact>
```
