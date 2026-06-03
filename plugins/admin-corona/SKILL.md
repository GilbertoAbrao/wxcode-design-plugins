---
name: admin-corona
description: |
  Dark admin aesthetic: deep-charcoal canvas (#191c24), raised card surfaces
  (#1e2130), subdued body text (#6c7293), hairline borders (#2c2e33), and a
  violet accent (#8862e0) with a violet-to-blue gradient on primary CTAs.
  Rubik type at weight 500 for headings; 4px card radius; generous 20–24px
  padding; crisp status pills with muted tint backgrounds. Archetype = sticky
  top navbar (search + notification + avatar) + collapsible left icon sidebar +
  KPI card row (4 tiles with icon + delta + big figure) + 2-column grid (chart
  panel left, status-list panel right) + full-width data table with status pills
  + auth screens (login / register) + error screens (404 / 500) + a dedicated
  charts page.
triggers:
  - "dark charcoal admin"
  - "violet accent admin dashboard"
  - "deep charcoal admin panel"
  - "violet gradient buttons admin"
  - "rubik dark admin"
  - "admin escuro violeta"
  - "painel admin carvão escuro"
  - "admin com acento roxo"
  - "dark admin with gradient CTAs"
  - "charcoal sidebar admin"
example_prompt: "Apply this dark charcoal admin aesthetic with violet accent to my domain"
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

# Violet Night Admin — Visual Archetype

This plugin contributes a **look** (dark charcoal canvas, violet gradient accent,
Rubik type, generous breathing room) and a **structure** (sticky navbar + icon
sidebar + KPI tiles + chart/status grid + data table, plus auth and error screens).
It does **not** contribute a domain — the subject matter comes from the Knowledge
Base and the user's prompt. Treat the example below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property; only true neutrals are hardcoded.

- **Canvas / surfaces:** page `#191c24`; raised card `#1e2130`; inset / hover `#252836`; border `#2c2e33`; stronger border on hover `#3d3f4a`.
- **Text ramp:** primary `#e4e6ef`; secondary `#b5b5c3`; muted `#6c7293`; faint `#4a4b68`.
- **Accent:** `--accent: #8862e0` (violet); `--accent-end: #5b8ef0` (blue); gradient `linear-gradient(135deg, #8862e0 0%, #5b8ef0 100%)` for primary CTAs, active sidebar items, and focus rings. `--accent-dim: rgba(136,98,224,.14)` for pill tints and hover chips.
- **Status ramp (tokens):** `--state-active #22c55e`; `--state-pending #f59e0b`; `--state-error #ef4444`; `--state-inactive #6c7293`; `--state-info #38bdf8`; each with a `…-dim` tint at ~12% alpha for pill backgrounds. Delta up `#4ade80`, delta down `#f87171`.
- **Typography:** `"Rubik", "Nunito Sans", system-ui, -apple-system, "Segoe UI", sans-serif`. Base 14px / line-height 1.5. Headings weight 500; body 400; figures `font-variant-numeric: tabular-nums`. Micro-labels 11px uppercase letter-spacing ~0.6px, muted color. Big KPI figures 28–32px, weight 700. IDs in `"Courier New", monospace`.
- **Density & radius:** card padding 20–24px; table row padding 12px vertical / 16px horizontal; 16px grid gap; card radius 4px; control radius 4px; pill radius 12px; button radius 4px; progress bar 6px height / 3px radius.
- **Borders & shadows:** 1px `#2c2e33` card borders; subtle `box-shadow: 0 2px 8px rgba(0,0,0,.25)` on raised cards; no drop shadows on nested elements. Sidebar and navbar do not shadow — clean flat separation via border.
- **Gradient CTA:** `background: linear-gradient(135deg, var(--accent) 0%, var(--accent-end) 100%)` on primary buttons; white text; no border; hover: `opacity .9`.
- **Motion:** `.15s ease` on hover color/border transitions; `.2s ease` on sidebar expand/collapse; no bounce or spring. Status dot pulses with a 2s `opacity` keyframe.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns described by shape and behavior — not meaning.

- **Top navbar** (60px, card bg, 1px bottom border, sticky z-50): brand logo + wordmark left → flexible **search bar** (pill, 280px, muted placeholder) → right cluster (notification bell with badge, settings gear, avatar circle with dropdown). All hover states use `--accent-dim` chip.
- **Left icon sidebar** (240px expanded / 64px collapsed, card bg, 1px right border, full-height): a section heading "MAIN MENU" (muted micro-label) → 5–7 nav items each with a leading icon + label + optional badge; active item gets the violet gradient background-chip + white text; hover item gets `--accent-dim` bg; a fold toggle at the foot collapses to icon-only mode. Bottom section: profile tile (avatar + name + role).
- **Main content** (page bg, 24px padding, vertical flex flow): **page header** (breadcrumb + title left, ghost + primary gradient button right) → region stack below.
- **KPI card row** (4 equal cards, 4-column grid): each card = raised surface, 4px radius, a left-side icon box with `--accent-dim` tint + SVG icon in `--accent`, a right side with a big tabular figure + micro-label title + a delta chip (colored up/down arrow + percentage/count). Cards recolor icon by state token.
- **2-column grid (7fr / 5fr):**
  - **Left — chart panel:** titled raised card with a period-picker tab strip, an inline SVG area/line chart (polyline + area-fill + dotted gridlines + x/y axis labels + hover tooltip placeholder), and a legend row of colored dot + label + value below.
  - **Right — status list panel:** titled raised card listing rows of `[icon chip] [entity label + sub-label] [state pill] [metric / timestamp]`; a "View all" ghost link at the foot.
- **Full-width data table panel:** titled raised card with a search input + filter chips + "Add" gradient CTA in the header; sticky uppercase 11px column headers (muted); dense rows (12px vert padding) with a mono ID cell, a two-line name/sub cell, right-aligned numerics with `tabular-nums`, status pills, and an actions kebab; footer with result count + prev/next pager controls.
- **Charts page:** a full-width panel with multiple chart sections — bar chart, doughnut/pie chart, and a sparkline row; each section is a titled raised card with the same period-picker pattern.
- **Auth screens (login / register):** centered card on a full-page charcoal background; brand wordmark at top; a compact form with inline-validated fields; gradient primary CTA; footer link to the alternate auth screen. No sidebars, no navbar.
- **Error screens (404 / 500):** full-page centered layout; large SVG illustration (geometric / abstract); a short title + description; a single gradient primary CTA ("Go Home" / "Retry"). No sidebars.
- **Form screen:** sectioned raised cards of labelled fields; **rules appear as inline validation** — required marks (`*`), helper text, and inline error messages on invalid fields; gradient primary CTA disabled-until-valid; cancel ghost button alongside. No rules / checklist / validation-status panel.
- **List screen:** the data-table archetype as its own full page — search + filter chips + count badge, the dense table, and a pager.

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key metrics,
status states, record list/columns, form fields and their rules, and detail fields
— and map them onto the archetype above. If no KB/domain is supplied (standalone),
use the Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules
become inline field validation. Do NOT render build/implementation notes or
designer controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent
> (entities, metrics, states, columns, fields) drawn from the KB + prompt.

```
Domain (illustrative): a cloud infrastructure monitoring service.

Navbar: brand "Cloudwatch" + search "Search metrics, hosts, alerts…" +
  notification bell (3 alerts) + avatar "AJ".

Sidebar nav items: Dashboard, Hosts, Alerts, Metrics, Reports, (Settings).

KPI tiles (4):
  • Active Hosts 142 (▲12 online, "Total registered: 158").
  • Avg CPU Load 38% (▲4%, "Threshold 80% · healthy").
  • Open Alerts 7 (▼3, amber, "Critical: 2 · Warning: 5").
  • Uptime 99.8% (▲0.1%, green, "Last 30 days").

Chart panel (left) → "Traffic Overview" area chart, periods: 24h / 7d / 30d;
  series: Inbound MB/s (violet), Outbound MB/s (blue); legend row below.

Status list (right) → "Recent Alerts" rows:
  [red chip ■] [HOST-042 · us-east-1] [Critical] [CPU 97% · 4 min ago]
  [amber chip ■] [HOST-091 · eu-west-2] [Warning] [Disk 88% · 12 min ago]

Data table → "Hosts": ID / Hostname / Region / CPU% / Memory% / Status pill
  (Online / Degraded / Offline / Maintenance) / Last Seen / Actions kebab.

Charts page → "Performance Overview": Bar chart (requests/min by region),
  Doughnut (status distribution: Online 90%, Degraded 6%, Offline 4%),
  Sparkline row (latency p50 / p95 / p99 per region).

Login → Email + Password (required, inline error on invalid), "Sign In" gradient
  CTA, "Forgot password?" link, "Don't have an account? Register" footer link.

Register → Full Name + Email + Password (min 8 chars, helper text) + Confirm
  Password (must match, inline error) + Terms checkbox (required), "Create Account"
  gradient CTA.

404 → Large SVG geometric illustration; "Page Not Found"; "The page you requested
  doesn't exist or has been moved."; "Go to Dashboard" gradient CTA.

500 → Large SVG illustration; "Internal Server Error"; "Something went wrong on
  our end. Please try again."; "Retry" gradient CTA.

Form (Add Host) → sections: "Host Details" (Hostname required, IP Address required
  validated as IP, Region required select, OS Type select), "Monitoring" (Alert
  threshold % required 1-100, Check interval select, Tags multi-input); inline
  required marks + helper text + inline errors; "Save Host" gradient CTA disabled
  until valid; "Cancel" ghost.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, status states, record list/columns, form fields + rules, detail
   fields — from the KB + prompt. Standalone: use the Example instantiation above.
3. Build each screen in the Visual language + Layout archetype above, imitating
   the example set in `assets/` (dashboard, list, form, charts, login, register,
   error-404, error-500) and the `assets/template.html` seed — with fresh content
   for the real domain, NOT the example labels.
4. Express domain rules as INLINE field validation (required marks `*`, helper
   text under fields, inline error messages, disabled-until-valid submit). Never
   render rules / checklist / validation-status / build-note panels or designer
   controls.
5. One inline `<style>`, semantic HTML5, `tabular-nums` on all figures, no
   external CDNs, no external image URLs — self-contained.

## Output contract

```
<artifact identifier="admin-corona" type="text/html" title="Admin Console">
<!doctype html>...</artifact>
```
