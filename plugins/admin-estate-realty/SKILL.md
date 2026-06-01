---
name: admin-estate-realty
description: |
  Real-estate brokerage back-office admin archetype: light mode,
  refined teal accent (#0d9488 / #14b8a6), left sidebar with
  brokerage-office switcher and grouped nav, topbar with property
  search + region filter + avatar, 4 KPI cards (active listings,
  deals in progress, avg days on market, commission MTD each with
  inline SVG trend), a listings table with status pills, a horizontal
  deals pipeline with stage counts, and an agent leaderboard panel.
  Use when the brief mentions real-estate, property, brokerage,
  MLS listings, or realty back-office.
triggers:
  - "real estate admin"
  - "realty dashboard"
  - "brokerage back-office"
  - "property management admin"
  - "MLS admin"
  - "listings dashboard"
  - "real estate CRM"
  - "estate admin"
  - "painel imobiliário"
  - "房产经纪后台"
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
  example_prompt: "Build me a real-estate brokerage back-office admin dashboard — left sidebar with office switcher, topbar with region filter, 4 KPI cards (active listings, deals in progress, avg days on market, commission MTD), a listings table, a deals pipeline, and an agent leaderboard."
---

# Estate Realty Admin Skill

Produce the canonical real-estate brokerage back-office admin layout —
refined, light-mode, teal-accented, purpose-built for brokers and
operations managers tracking listings, deals, and agent performance.

## Workflow

1. Read the active DESIGN.md (if present); otherwise use teal
   (#0d9488) as the primary accent on a near-white canvas (#f7f9f9).
2. Extract from the brief: brokerage name, office regions, KPI labels
   (default: Active Listings, Deals in Progress, Avg Days on Market,
   Commission MTD), listing record type (residential / commercial /
   mixed), and agent team size.
3. Layout:

   - **Left sidebar (240px)**: brokerage logo mark + name at top,
     office/region switcher dropdown below logo, grouped nav with
     section headers (OVERVIEW, LISTINGS, DEALS, TEAM), each item
     icon (inline SVG) + label + optional count badge. Active item
     has teal left-bar (#0d9488) and teal-tinted background. Footer
     row: avatar + agent name + settings cog.

   - **Top bar (60px)**: page title on left, property search input
     center (placeholder "Search address, MLS#, or agent…"), region
     filter pill-select on right, notification bell with badge,
     avatar + broker name.

   - **4 KPI cards** (full-width row, equal columns): white cards,
     12px radius, subtle shadow (0 2px 10px rgba(13,148,136,0.07)).
     Each card: small uppercase label, large bold number, tiny
     inline SVG sparkline (5 points, teal stroke, no fill), delta
     chip (green arrow-up / red arrow-down / amber dash). Cards:
     Active Listings · Deals in Progress · Avg Days on Market ·
     Commission MTD.

   - **Main content (two-column 60/40)**:
     - LEFT (60%): **Listings table** — title "Active Listings"
       with "+ Add Listing" teal CTA. Columns: Property (address +
       thumbnail placeholder), Price, Type (pill: Residential /
       Commercial / Land), Status (pill: Active / Pending /
       Under Contract / Sold), Agent. 8 rows, zebra-light tint,
       teal hover row highlight, pagination hint.
     - RIGHT (40%): **Agent Leaderboard** panel — title "Top
       Agents · June 2026", 6 rows each: rank medal/number, avatar
       initials circle (teal-shaded), agent name, listings count,
       closed deals, GCI bar (inline SVG horizontal bar scaled
       to max), commission figure.

   - **Deals Pipeline** (full-width below main): horizontal stage
     funnel — 5 stages (Prospect → Offer Made → Under Contract →
     Inspection → Closed), each stage a card with stage name,
     deal count badge, and 2–3 deal chips (address abbreviation +
     price tag). Connector arrows between stages. Teal accent on
     the active/Closed stage.

4. Typography: system font stack only — "Inter", system-ui,
   -apple-system, "Segoe UI", Roboto, sans-serif. Uppercase labels
   with letter-spacing 0.06em for card titles. Teal for active states,
   links, and primary CTAs. Green (#16a34a) / amber (#d97706) /
   red (#dc2626) for status pills and delta chips only.

5. Palette rules: every chromatic color is a :root CSS custom property
   (--color-accent, --color-accent-light, --color-success,
   --color-warning, --color-danger, --color-text, --color-muted,
   --color-border, --color-surface, --color-bg). SVG fill/stroke uses
   var(--token) or currentColor. Only neutral grays may be hardcoded.

6. One inline `<style>`, semantic HTML, no external assets, no CDNs,
   no @import, no Google Fonts. All inline SVG icons. Target 10–30 KB.

## Output contract

```
<artifact identifier="admin-estate-realty" type="text/html" title="Estate Realty Admin">
<!doctype html>...</artifact>
```
