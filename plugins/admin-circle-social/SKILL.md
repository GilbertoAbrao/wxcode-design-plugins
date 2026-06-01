---
name: admin-circle-social
description: |
  Friendly light-mode admin dashboard for online community and social platform
  operators — community switcher sidebar, topbar with search + date-range +
  avatar, 4 KPI cards (active members, posts today, open reports, engagement
  rate), moderation queue with approve/remove actions and reason pills,
  engagement area chart (inline SVG), members table with role + status pills,
  and a trending/flagged side panel. Blue (#3b82f6) and violet (#8b5cf6)
  accent on white/#f8f9fc surfaces. Use when the brief calls for community
  moderation, forum ops, social platform management, or member administration.
triggers:
  - "community admin"
  - "circle admin"
  - "social platform dashboard"
  - "moderation dashboard"
  - "forum admin"
  - "community ops"
  - "member management"
  - "content moderation"
  - "painel de moderação"
  - "社区管理后台"
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
  example_prompt: "Build me an admin dashboard for a community / social platform — sidebar with community switcher, moderation queue, member management, engagement metrics, and flagged content panel."
---

# Circle Community Admin Skill

Produce the Circle Community Admin layout — a friendly, light-mode operations
dashboard purpose-built for community managers, trust & safety teams, and
social platform moderators.

## Design tokens (palette-ready)

Every chromatic color must be a `:root` CSS custom property. Use `var(--token)`
or `currentColor` in all rules and inline SVG; never write a chromatic hex
literal directly in a CSS rule or SVG attribute.

| Token | Value | Role |
|---|---|---|
| `--accent-blue` | `#3b82f6` | Primary CTA, active nav, links |
| `--accent-violet` | `#8b5cf6` | Secondary accent, badges, chart fill |
| `--accent-blue-soft` | `#eff6ff` | Tinted backgrounds, active nav bg |
| `--accent-violet-soft` | `#f5f3ff` | Violet tinted backgrounds |
| `--status-green` | `#22c55e` | Online / approved / positive delta |
| `--status-amber` | `#f59e0b` | Pending / warning |
| `--status-red` | `#ef4444` | Reports / removed / negative delta |
| `--status-green-soft` | `#dcfce7` | Green pill background |
| `--status-amber-soft` | `#fef3c7` | Amber pill background |
| `--status-red-soft` | `#fee2e2` | Red pill background |
| `--chart-line` | `#3b82f6` | Chart stroke |
| `--chart-area` | `rgba(59,130,246,0.12)` | Chart area fill |

Neutrals (hardcoded, not tokenized): `#0f172a` headings, `#334155` body text,
`#64748b` muted, `#94a3b8` placeholder, `#e8eaf2` borders, `#f1f5f9` row hover,
`#f8f9fc` sidebar/canvas bg, `#ffffff` card surfaces.

## Workflow

1. Read the active DESIGN.md (if present); otherwise use the token palette above.
2. Extract from the brief: community/platform name, primary KPIs (4: active
   members, posts today, open reports, engagement rate or domain equivalents),
   types of moderated content (posts, comments, profiles).
3. Layout:

   **Left sidebar (220px fixed)**
   - Top: brand mark (ring-of-dots SVG icon + wordmark "CircleSpace"), then a
     community switcher dropdown (current community name + chevron).
   - Nav groups: OVERVIEW (Dashboard, Analytics), COMMUNITY (Members, Posts,
     Events), MODERATION (Reports, Queue, Flagged), SETTINGS (Roles, Integrations).
     Active item has `var(--accent-blue)` left border (3px) + `var(--accent-blue-soft)`
     background. Icons via tight inline SVG (16×16, `currentColor`).
   - Bottom: operator avatar + name + "Sign out" link, muted.

   **Topbar (56px)**
   - Left: breadcrumb — "CircleSpace / Dashboard".
   - Center: search input with magnifier SVG icon placeholder.
   - Right: date-range chip (e.g. "May 1 – May 31"), notification bell with
     badge counter, operator avatar (initials circle).

   **4 KPI cards (grid, 4 cols)**
   Each: small uppercase label, bold big number, tiny sparkline (inline SVG
   path, 5 points), delta chip below (green up-arrow / red down-arrow + %).
   Cards: Active Members · Posts Today · Reports Open · Engagement Rate.
   One tiny thematic inline SVG icon per card (people / chat bubble / flag / lightning bolt).

   **Moderation Queue (left, ~60% width)**
   Title "Moderation Queue" + "4 pending" badge. 3–4 reported content cards,
   each showing: reporter handle + timestamp, reported content excerpt (italic),
   reason pill (Hate Speech / Spam / Misinformation / NSFW in amber/red), and
   two action buttons — "Approve" (ghost green) and "Remove" (solid red).

   **Engagement Chart (below queue)**
   Card title "Engagement Over Time" with a 7-day period. Inline SVG area chart
   (~480×140) with 5 horizontal grid lines, labeled x-axis (Mon–Sun), two
   paths: posts (blue) + reactions (violet), and a small legend.

   **Members Table (full width)**
   Header: "Community Members" + "Export CSV" ghost button + "+ Invite" primary
   button. Columns: Member (avatar initials + display name + @handle), Role pill
   (Admin / Moderator / Member), Joined date, Status pill (Active / Suspended /
   Pending). 6 rows with invented handles. Tinted row hover.

   **Trending / Flagged panel (right of Queue, ~40% width)**
   Two sections:
   - "Trending Topics" — top 4 hashtags with post-count bar (inline CSS width).
   - "Flagged Accounts" — 3 user rows with avatar initials, handle, flag count,
     and "Review" link in `var(--accent-blue)`.

4. Typography: system font stack inline — `"Inter", system-ui, -apple-system,
   "Segoe UI", Roboto, sans-serif`. Tiny uppercase section labels with
   `letter-spacing: 0.06em`. Blue/violet for active states. Status colors only
   for deltas and pills.
5. One inline `<style>`, semantic HTML, no external assets, no CDNs, no
   `@import`, no `<link>` to external stylesheets or fonts.
6. Target 10–30 KB total. No lorem ipsum — invent community-flavored copy,
   handles, hashtags, and figures.

## Output contract

```
<artifact identifier="admin-circle-social" type="text/html" title="Circle Community Admin">
<!doctype html>...</artifact>
```
