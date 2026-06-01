---
name: admin-savory-pos
description: |
  Restaurant point-of-sale back-office admin dashboard: warm light mode,
  amber (#f59e0b) + tomato (#ef4444) accent on white/#faf8f5 surfaces,
  left sidebar with venue switcher and grouped nav, topbar with shift
  indicator and avatar, 4 KPI tiles (today's sales / orders / avg ticket /
  tables occupied), live orders kanban (New / Cooking / Served), top-selling
  items list with inline bar, sales sparkline SVG, and a recent orders table
  with status pills. Use when the brief mentions restaurant, café, food
  service, POS, kitchen display, or back-office for hospitality.
triggers:
  - "restaurant admin"
  - "restaurant dashboard"
  - "pos admin"
  - "point of sale dashboard"
  - "café back-office"
  - "kitchen display"
  - "food service admin"
  - "painel restaurante"
  - "餐厅管理后台"
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
  example_prompt: "Build me a restaurant POS back-office admin dashboard — venue switcher sidebar, live orders kanban board, daily KPI tiles, top-selling items, sales sparkline, and recent orders table."
---

# Savory POS Admin Skill

Produce the canonical restaurant POS back-office layout — warm, operational,
scannable at a glance during a busy dinner rush.

## Workflow

1. Read the active DESIGN.md (if present); otherwise use amber (#f59e0b) as
   the primary accent and tomato (#ef4444) for alerts/cancel states on a
   warm near-white canvas (#faf8f5).
2. Extract from the brief: venue name(s), service period (breakfast / lunch /
   dinner / all-day), KPIs (4: today's sales, order count, avg ticket, tables
   occupied), menu items for the top-sellers list, and order categories for
   the kanban board.
3. Layout:
   - **Left sidebar (240px)**: venue logo mark at top (amber square with fork
     icon), venue switcher dropdown, grouped nav with section labels
     (OVERVIEW, SERVICE, MENU, REPORTS, SETTINGS), each item with inline SVG
     icon + label + optional count badge. Active item: amber left bar + warm
     tinted background. Footer: staff avatar + name + "End Shift" link.
   - **Top bar (60px)**: page title on the left, global search input
     (placeholder "Search orders, tables, items…"), shift indicator chip
     (e.g. "Dinner shift · 6:00 PM – 11:00 PM"), notification bell with red
     dot, manager avatar + name.
   - **4 KPI tiles**: white cards with 10px radius and warm box-shadow. Each:
     small uppercase label, bold number with currency/unit, tiny inline SVG
     sparkline, delta chip (green ▲ / tomato ▼). Tiles: Today's Sales /
     Orders Served / Avg Ticket / Tables Occupied.
   - **Live Orders kanban (full-width, 3 columns)**:
     - NEW — incoming orders (card: order# + table + items summary + time
       elapsed + amber "Accept" button).
     - COOKING — orders being prepared (card: order# + table + items +
       elapsed time bar + tomato indicator if >15 min).
     - SERVED — completed, awaiting payment (card: order# + table + total +
       green "Mark Paid" button).
   - **Bottom two-column grid**:
     - LEFT (~55%): Top-Selling Items — list of 6 dishes with rank dot,
       name, qty sold today, revenue, and a thin inline amber bar scaled to
       the max.
     - RIGHT (~45%): Sales Sparkline card — inline SVG polyline chart for
       the last 8 hours, hourly labels on X axis, € value on Y axis, amber
       fill gradient.
   - **Wide recent orders table**: "Recent Orders" header + "View all" link;
     columns: Order# / Table / Items / Total / Status pill (Paid green /
     Pending amber / Cancelled tomato). 8 rows, alternating row tint, last
     column right-aligned.
4. Typography: system font stack only — "Inter", system-ui, -apple-system,
   "Segoe UI", Roboto, sans-serif. Slate (#1e293b) for primary text, slate-500
   (#64748b) for secondary. Uppercase 10px letter-spaced labels for tile
   titles and section headers.
5. Color tokens: every chromatic color as :root CSS custom property; SVG
   fill/stroke via var(--token) or currentColor; only neutral grays may be
   hardcoded.
6. Single inline <style>, semantic HTML, no external assets, no CDNs, no
   lorem ipsum, original invented brand + dish names.

## Output contract

```
<artifact identifier="admin-savory-pos" type="text/html" title="Savory POS Admin">
<!doctype html>...</artifact>
```
