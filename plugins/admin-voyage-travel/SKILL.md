---
name: admin-voyage-travel
description: |
  Airy light-mode travel agency operations dashboard: agency/region
  switcher in a left sidebar, topbar with global search + date-range +
  avatar, 4 KPI cards (bookings today, occupancy %, revenue, avg lead
  time), an itinerary/bookings board, a destinations breakdown with
  inline SVG bars, a recent bookings table with status pills, and an
  occupancy side panel. Sky (#0ea5e9) and coral (#fb7185) accent palette
  on a white/#f6fafc canvas. Use when the brief mentions travel, tours,
  booking operations, or itinerary management.
triggers:
  - "travel agency dashboard"
  - "booking operations"
  - "tour operator admin"
  - "itinerary management"
  - "travel admin"
  - "painel de agência de viagens"
  - "旅行社运营仪表板"
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
  example_prompt: "Build me an airy travel agency admin dashboard — agency/region switcher sidebar, topbar with date range, 4 KPI cards (bookings, occupancy, revenue, avg lead time), itinerary board, destinations chart, recent bookings table, occupancy panel."
---

# Voyage Travel Admin Skill

Produce an airy, light-mode operations dashboard purpose-built for
travel agencies and tour operators — think clean air, open horizons,
and the quiet confidence of a booking ops team that knows exactly
where every passenger is headed.

## Palette

All chromatic values are CSS custom properties on `:root`. Never
write a chromatic hex literal in rules or inline SVG attributes;
use `var(--token)` or `currentColor` instead.

```
--sky:      #0ea5e9   /* primary sky accent */
--sky-lt:   #38bdf8   /* hover / highlight variant */
--coral:    #fb7185   /* secondary / alert accent */
--coral-lt: #fda4af   /* coral tint for badges */
--green:    #22c55e   /* confirmed / on-track status */
--amber:    #f59e0b   /* pending / delayed status */
--surface:  #ffffff   /* card / panel background */
--canvas:   #f6fafc   /* page background */
--border:   #e2eaf0   /* dividers and card borders */
```

Neutrals (hardcoded, not tokens): slate text `#1e293b`, muted text
`#64748b`, subtle label `#94a3b8`.

## Workflow

1. Read the active DESIGN.md if present; otherwise apply the palette
   above verbatim.
2. Extract from the brief: agency name, regions (default: EMEA, APAC,
   Americas), KPI labels (bookings today, occupancy, revenue,
   avg lead time).
3. Layout:

   **Left sidebar (240px)**
   - Top: agency logo mark (compass SVG, sky accent) + agency name +
     region dropdown pill (EMEA ▾).
   - Nav groups with uppercase muted labels:
     - OVERVIEW: Dashboard, Analytics
     - OPERATIONS: Bookings, Itineraries, Fleet, Suppliers
     - CLIENTS: Guests, Corporate, Loyalty
     - SETTINGS: Team, Billing, Integrations
   - Active item: left border 3px sky accent, sky-tinted row (#f0f9ff).
   - Bottom: logged-in agent avatar + name + "Logout" icon link.

   **Top bar (60px, white, 1px border-bottom)**
   - Left: page title "Operations Hub" bold slate + breadcrumb "Voyage /
     Dashboard" muted.
   - Center: search input (magnifier SVG + placeholder "Search
     bookings, guests, destinations…", 320px wide, rounded-full).
   - Right: date-range chip (calendar SVG + "May 19 – Jun 1, 2026" +
     caret, sky-border pill), bell icon with coral 8px dot, avatar +
     "Fatima R." + caret.

   **KPI cards row (4 equal columns)**
   Each card: white, 10px radius, 0 2px 12px rgba(14,165,233,.07)
   shadow. Structure: icon circle (sky-tinted) top-right, uppercase
   label, large number, delta chip (green ▲ / red ▼ / amber ●) + mini
   sparkline SVG (8 points, 60×24px, sky stroke).
   - Bookings Today: 84 ▲ +12% vs yesterday
   - Occupancy Rate: 73% ▲ +4 pts vs last week
   - Revenue (MTD): $214,800 ▲ +8% vs last month
   - Avg Lead Time: 18 days ▼ −2 days vs last month

   **Main content grid (left 60% / right 38%, gap 20px)**

   LEFT — Itinerary Board card
   - Header: "Active Itineraries" + "View all →" sky link.
   - List of 6 trip rows: destination flag-SVG + trip name / dates /
     pax count / status pill (Confirmed green, Pending amber,
     Cancelled coral).
   - Trips: "Amalfi & Capri Escape · Jun 4–14 · 12 pax · Confirmed",
     "Kyoto Cherry Blossom Tour · Jun 8–18 · 8 pax · Confirmed",
     "Sahara Dunes Expedition · Jun 11–21 · 6 pax · Pending",
     "Fjords of Norway Voyage · Jun 15–25 · 14 pax · Confirmed",
     "Patagonia Trekking Route · Jun 17–29 · 9 pax · Pending",
     "Zanzibar Island Escape · Jun 20–30 · 11 pax · Confirmed".

   RIGHT — Destinations Breakdown card (inline SVG bar chart)
   - Title: "Top Destinations · May 2026".
   - 6 rows, each: destination name, horizontal bar (sky fill,
     var(--sky)), value label right.
   - Data: Italy 38, Japan 31, Morocco 24, Norway 22, Argentina 17,
     Tanzania 14. Bar width proportional to max value (38).

   **Bottom row — two-panel layout**

   LEFT (65%) — Recent Bookings table card
   - Header: "Recent Bookings" + "Export CSV" ghost button.
   - Columns: Ref #, Customer, Destination, Travel Dates, Pax, Total,
     Status.
   - 7 rows of invented data with realistic booking refs (VGT-XXXXX).
   - Status pills: Confirmed (green bg #dcfce7, green text),
     Pending (amber bg #fef9c3, amber text),
     Cancelled (coral bg #ffe4e6, coral text).
   - Tinted hover row (#f0f9ff).

   RIGHT (33%) — Occupancy Panel card
   - Title: "Room/Seat Occupancy".
   - Inline donut SVG (140px, sky + coral + border segments) +
     center legend: Booked / Available / Held.
   - Below: 3 property rows (resort name + occupancy % bar + value).
   - Properties: Villa Adriatica 88%, Ryokan Higashiyama 74%,
     Riad Al-Andalus 61%.

4. Typography: system font stack only; no external font loads.
   Uppercase labels 10px letter-spacing 0.06em muted slate.
   Page heading 20px/700. Card title 14px/600.
5. All SVGs: fill/stroke chromatic via `var(--token)` or
   `currentColor`; neutrals hardcoded.
6. One inline `<style>`, semantic HTML, no external assets, no CDNs,
   no lorem ipsum. Target 10–30 KB.

## Output contract

```
<artifact identifier="admin-voyage-travel" type="text/html" title="Voyage Travel Admin">
<!doctype html>...</artifact>
```
