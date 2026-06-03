---
name: admin-glassmorphism
description: |
  Dark-mode admin built on frosted glass panels — translucent surfaces
  (rgba white 4%) with backdrop-filter blur over a soft aurora gradient
  background, cyan accent (#4dd0e1), hairline white-alpha borders, soft
  inner glow on actives. Archetype = glass sidebar (240px) + glass topbar
  + 4 KPI tiles with sparklines + 2-column main grid (area chart 8col /
  top-N list 4col) + full-width glass records table with tinted status
  capsules. Modern frosted alternative to flat-card admins.
triggers:
  - "glassmorphism admin"
  - "frosted glass admin"
  - "aurora background admin"
  - "modern dark admin"
  - "translucent panels admin"
  - "backdrop blur dashboard"
  - "frosted glass dark UI"
  - "painel glassmorphism"
  - "毛玻璃后台"
example_prompt: "Apply this frosted-glass admin aesthetic to my domain"
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
    requires: [pixel-discipline, typographic-rhythm]
---

# Glassmorphism Admin — Visual Archetype

This plugin contributes a **look** (aurora gradient canvas, frosted glass surfaces,
cyan accent, soft inner glow) and a **structure** (glass sidebar + glass topbar +
KPI tile row + area-chart / top-N grid + glass records table, plus list / form /
detail screens). It does **not** contribute a domain — the subject matter comes
from the Knowledge Base and the user's prompt. Treat the example below as
illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property; the aurora gradient and glass recipe are fixed.

- **Canvas:** `--bg-base: #0d1117`; `--bg-mid: #1c1f2a`. Full-viewport fixed
  aurora: radial blobs of cyan (~18% opacity), violet (~14%), pink (~12%), and
  blue (~10%) fading into the base navy. Layer a `feTurbulence` noise SVG at
  `opacity: 0.035` above for grain.
- **Glass recipe (THE surface):**
  `background: rgba(255,255,255,0.04); backdrop-filter: blur(18px) saturate(120%);
  -webkit-backdrop-filter: blur(18px) saturate(120%);
  border: 1px solid rgba(255,255,255,0.10); border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.06);`
  Apply to sidebar, topbar, every card, KPI tile, and table wrapper.
- **Text ramp:** `--white-95: rgba(255,255,255,0.95)` (primary); `--white-60:
  rgba(255,255,255,0.60)` (secondary / labels); `--white-30: rgba(255,255,255,0.30)` (faint).
- **Accent:** `--cyan: #4dd0e1`; `--cyan-dim: rgba(77,208,225,0.15)`;
  `--cyan-glow: rgba(77,208,225,0.08)`. Use ONLY on active nav, active chips,
  links, chart strokes, and key metric figures.
- **State / delta tokens:**
  `--green-glass: rgba(52,211,153,0.18)`, `--green-text: #34d399` (positive delta,
  active status); `--pink-glass: rgba(244,114,182,0.18)`, `--pink-text: #f472b6`
  (negative delta, hold status); amber `rgba(251,191,36,0.15)` / `#fbbf24`
  (warning / verifying); violet `rgba(99,102,241,0.20)` / `#818cf8` (info tier);
  gradient `rgba(167,139,250,0.18)→rgba(244,114,182,0.18)` / `#c084fc`
  (elevated tier).
- **Typography:** `-apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui,
  sans-serif`. Base 13–14px. Uppercase micro-labels 10px, `letter-spacing: 0.12em`,
  `color: var(--white-60)`. KPI figures 28px / weight 800 / `letter-spacing: -.02em`.
- **Density & radius:** glass panels `border-radius: 16px`; controls `border-radius:
  10px`; pills `border-radius: 20px`. Content padding 24–28px; gap 16–20px. Row
  dividers `1px solid rgba(255,255,255,0.06)`.
- **Active-state inner glow (nav):** active nav item uses `background: var(--cyan-dim)`,
  `border: 1px solid rgba(77,208,225,0.20)`, `box-shadow: inset 0 1px 0
  rgba(77,208,225,0.12), 0 0 16px rgba(77,208,225,0.06)`.
- **Motion:** `.15s` background/color transitions on hover, subtle only. No bounce.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Left glass sidebar** (240px, full-height, glass recipe): brand mark at top
  (icon + wordmark + sub-label), 7 nav items with inline SVG icons (active item
  gets cyan inner glow), flex spacer, avatar + name/role footer.
- **Top glass bar** (72px, glass recipe, border-bottom): page title (left) → glass
  search pill (200px) → icon button row → avatar circle with cyan border.
- **KPI tile row** (4 equal tiles, glass recipe, `padding: 20px`): each tile =
  uppercase 10px label → big 28px figure → bottom row with delta chip (green-glass /
  pink-glass) + 64×24px sparkline inline SVG (cyan gradient fill).
- **2-column main grid** (`1fr 340px` gap 20px):
  - **Left — chart panel** (glass, `padding: 24px`): panel header (title + 3 period
    chips) → legend row → full-width area chart as inline SVG (`viewBox="0 0 560 180"`,
    dotted y-axis gridlines at white 6%, axis labels white 35%, one or two area
    polylines with gradient fills + stroke lines).
  - **Right — top-N list panel** (glass, `padding: 24px`): panel header (title +
    "See all" link) → N rows of `[avatar circle][name + sub] [trailing metric in
    cyan]`, `border-bottom: 1px solid rgba(255,255,255,0.06)`.
- **Full-width glass records table** (glass, `overflow: hidden`): table header band
  (frosted `rgba(255,255,255,0.03)` bg, border-bottom) with title + secondary action →
  `<table>` with uppercase 10px `<th>`, dense `<td>` rows (13px), zebra
  `rgba(255,255,255,0.02)` on even rows, status capsules as tinted glass pills.
- **List screen:** glass toolbar (search pill + filter chips with counts) → same
  glass records table → result count + pager row.
- **Form screen:** glass card sections of labelled fields; **rules appear as inline
  validation** — required marks (`*`), helper text under the field, inline error
  messages on invalid fields, primary submit `disabled` until valid. No separate
  rules/checklist panel.
- **Detail screen:** breadcrumb → header band (entity name + status capsule +
  action buttons, inside a glass card) → 3-column meta grid of label/value pairs
  (glass card) → related-data sub-panels below (top-N list pattern or mini-table,
  glass card).

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key metrics,
status states, record list/columns, form fields and their rules, and detail
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
Domain (illustrative): a subscription content-platform admin.

Sidebar nav items  → Overview (active), Members, Subscriptions, Content,
                     Campaigns, Analytics, Settings.
Topbar             → title "Overview", search pill "Search members, plans…",
                     notification icon, avatar.

KPI tiles (4):
  • Monthly Revenue  $1.24M  ▲18%  cyan sparkline
  • Active Members   8,420   ▲6%   cyan sparkline
  • Avg Revenue/User 12.4%   ▼0.3% pink sparkline
  • Churn Rate       0.7%    ▼0.1% cyan sparkline

Chart panel (left) → "Revenue Breakdown" · chips 7d / 30d (active) / 90d ·
  legend: Subscriptions (cyan), Tips (violet), Merch (pink), Live Events (amber) ·
  stacked area SVG.

Top-N list (right) → "Top Members" — 6 rows: avatar initials circle, member
  handle + category, trailing monthly value in cyan.

Records table      → "Member Roster": Member (avatar + name + handle) / Tier
  (tinted capsule: Rising/Pro/Elite/Partner) / Audience / Monthly Value /
  Last Active / Status (Active/Hold/Verifying).

List screen        → all members, glass toolbar with search + tier filter chips
  (All/Rising/Pro/Elite), paginated table.

Form screen        → "New Member": handle (required), display name (required),
  email (required, valid format), plan (required select), audience size (≥0),
  content category (required). Rules as required marks + helper text + inline
  errors; "Add Member" disabled until valid.

Detail screen      → one member: breadcrumb "Members › @handle"; header card
  (display name + status capsule + Edit/Suspend buttons); meta grid (plan, email,
  joined, audience, monthly value, tier); "Top Content" related sub-panel (mini-
  table of content items + engagement metric) + "Recent Activity" feed.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, status states, record columns, form fields + rules, detail fields
   — from the KB + prompt. Standalone: use the Example instantiation above.
3. Build each screen in the Visual language + Layout archetype above, imitating
   the example set in `assets/` (dashboard, list, form, detail) and the
   `assets/template.html` seed — with fresh content for the real domain, NOT the
   example labels.
4. Express domain rules as INLINE field validation (required marks, helper text,
   inline errors, disabled-until-valid submit). Never render
   rules/checklist/validation-status/build-note panels or designer/demo controls.
5. One inline `<style>`, semantic HTML5, no external assets, no CDNs —
   self-contained. Aurora gradient + grain noise via inline SVG data URI.

## Output contract

```
<artifact identifier="admin-glassmorphism" type="text/html" title="Glassmorphism Admin">
<!doctype html>...</artifact>
```
