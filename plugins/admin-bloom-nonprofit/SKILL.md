---
name: admin-bloom-nonprofit
description: |
  Warm-optimistic light-mode admin dashboard for nonprofit organizations —
  fundraising, donor management, and campaign operations. Left sidebar with
  org/program switcher and nav, topbar with search + period selector + avatar,
  4 KPI cards, campaigns progress list, inline SVG trend chart, donor-segments
  donut panel, and recent donations table. Emerald (#10b981) + coral (#fb7185)
  accent palette on white/#f7fbf9 surfaces. Use when the brief mentions
  nonprofit, charity, fundraising, donor CRM, donation dashboard, or campaign
  tracking with a warm/optimistic visual tone.
triggers:
  - "nonprofit dashboard"
  - "donor management"
  - "fundraising admin"
  - "charity admin"
  - "campaign tracking dashboard"
  - "donation dashboard"
  - "painel ong"
  - "painel de doações"
  - "公益管理后台"
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
  example_prompt: "Build me a nonprofit fundraising admin dashboard — left sidebar with org and program switcher, KPI cards for total raised and donors, campaigns list with progress bars, donations trend chart, donor segments donut, and recent donations table."
---

# Bloom Nonprofit Admin Skill

Produce a warm-optimistic nonprofit admin dashboard for fundraising and donor
management operations. Every color value must reference a CSS custom property;
no chromatic hex literals in rules or inline SVG.

## Palette tokens (required in :root)

```
--accent:       #10b981   /* emerald primary */
--accent-light: #d1fae5   /* emerald tint */
--accent-dark:  #059669   /* emerald hover */
--coral:        #fb7185   /* coral CTA / alert */
--coral-light:  #ffe4e8   /* coral tint */
--coral-dark:   #e11d48   /* coral hover */
--amber:        #f59e0b   /* status / warning */
--amber-light:  #fef3c7   /* amber tint */
--surface:      #f7fbf9   /* page background */
--card:         #ffffff   /* card background */
--border:       #e4ede9   /* dividers */
--text-primary: #1e293b   /* slate-900 */
--text-secondary: #64748b /* slate-500 */
--text-muted:   #94a3b8   /* slate-400 */
```

Neutrals (#1e293b, #64748b, #94a3b8, #ffffff, #f7fbf9, #e4ede9) may be
hardcoded where they are guaranteed stable. All emerald, coral, and amber
values MUST use var(--token).

## Layout

### Left sidebar (260px)
- **Org/program switcher** at top: org avatar (initial circle, var(--accent)
  fill), org name + caret. Below: program chip row (2–3 pills, active in
  var(--accent-light) + var(--accent) text).
- **Navigation groups**: OVERVIEW (Dashboard, Campaigns), DONORS (Donor List,
  Segments, Import), FINANCE (Revenue, Grants, Reports), SETTINGS (Team,
  Integrations). Each item: 18px inline SVG icon + label. Active item:
  var(--accent) icon, var(--accent-light) background, 3px left bar in
  var(--accent).
- **Bottom**: current user avatar + name + "Sign out" link.

### Topbar (60px)
- Left: page title "Dashboard" with current date subtitle.
- Center: search input with magnifier SVG icon, placeholder "Search donors,
  campaigns…".
- Right: period selector (THIS MONTH / THIS QUARTER / THIS YEAR — tab style,
  active tab underlined var(--accent)); notification bell with amber dot;
  avatar circle with initials.

### 4 KPI cards (equal-width grid)
Each card: small uppercase label (letter-spacing .06em), large number,
delta chip (↑ green or ↓ coral), small label for context, tiny 40×24 inline
SVG sparkline. Cards:
1. **Total Raised** — $1,247,380 · ↑14% vs last period · 7-point sparkline
2. **Active Donors** — 4,821 · ↑9% · 7-point sparkline
3. **Active Campaigns** — 12 · ↑2 · flat sparkline
4. **Recurring Gifts** — $38,950/mo · ↑7% · 7-point sparkline

### Campaigns list card (left, ~60% width)
Table/list with columns: Campaign name + badge (Active/Ending Soon/Paused),
Goal progress bar (var(--accent) fill, var(--border) track), Raised amount,
Goal amount, Days left. 5 campaigns:
- Harvest Hope Food Drive · Active · $84,200/$120,000 · 18 days
- Spring Literacy Fund · Active · $56,780/$80,000 · 31 days
- Clean Water Initiative · Ending Soon · $198,500/$200,000 · 4 days
- Youth Arts Scholarship · Active · $32,100/$60,000 · 47 days
- Emergency Relief 2026 · Paused · $410,000/$500,000 · —

### Donations trend chart (below campaigns, full row)
Title "Donations Trend — Last 12 Months" + legend (One-time: var(--accent),
Recurring: var(--coral)). Inline SVG area chart (100% width, 140px tall),
dual filled areas with 50% opacity, x-axis month labels (Jun 25 → May 26),
subtle grid lines in var(--border). No external chart lib.

### Recent donations table (left, ~65% width)
Columns: Donor name + avatar initial, Campaign, Amount, Type (One-time pill /
Recurring pill), Date. 8 rows of invented plausible names and amounts.
Header row with sort-hint carets. Striped hover.

### Donor segments panel (right, ~35% width)
Title "Donor Segments". Inline SVG donut chart (160px × 160px, 4 arcs with
gap). Legend below: segment name + color dot + count + percentage. Segments:
- Major Donors (≥$5k) — var(--accent) — 148 — 3%
- Mid-Level ($500–$4.9k) — #34d399 — 812 — 17%
- General (<$500) — var(--coral) — 3,204 — 66%
- Lapsed (>12 mo) — var(--amber) — 657 — 14%

## Type

System font stack only — no @import, no Google Fonts:
`"Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`

- Section labels: 10px, uppercase, letter-spacing .06em, var(--text-muted)
- KPI numbers: 28px, font-weight 700, var(--text-primary)
- Body: 14px, var(--text-primary)
- Table cells: 13px
- Nav items: 13px, font-weight 500

## Output contract

```
<artifact identifier="admin-bloom-nonprofit" type="text/html" title="Bloom Nonprofit Admin">
<!doctype html>...</artifact>
```
