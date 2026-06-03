---
name: admin-relay-helpdesk
description: |
  Friendly light-mode operations admin aesthetic: near-white slate canvas
  (#f8fafc), violet accent (#7c3aed / #8b5cf6), status-semantic palette
  (green / amber / red), Inter type at 13–14px, soft-shadow white cards
  with 10px radius, and fine hairline borders. Archetype = left categorised
  sidebar (sections with nav items + badges) + 56px white topbar (search +
  assignee-filter dropdown + notification) + 4 KPI cards with sparklines +
  a compact priority-tier bar strip + a full-width records table with dual
  status pills + a right-side load panel showing item counts with presence
  indicators. Built for clear-glass ops views that must scan at a glance.
triggers:
  - "violet accent light admin"
  - "friendly light-mode ops admin"
  - "status-semantic sidebar admin"
  - "soft-shadow card admin"
  - "dual-pill table admin"
  - "presence indicator panel"
  - "painel admin claro violeta"
example_prompt: "Apply this friendly violet-accent light-mode admin aesthetic to my domain"
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

# Relay Admin — Visual Archetype

This plugin contributes a **look** (friendly light-mode, violet accent, status-semantic
color, soft-shadow cards) and a **structure** (categorised sidebar + topbar + KPI row +
priority-tier bars + records table + right load panel, plus list / form / detail screens).
It does **not** contribute a domain — the subject matter comes from the Knowledge Base
and the user's prompt. Treat the example below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom property.

- **Canvas / surfaces:** page `#f1f5f9`; card / panel `#ffffff`; sidebar `#ffffff`; topbar
  `#ffffff`; hover tint `#fafbfe`; navbar separator `#e2e8f0`.
- **Text ramp:** primary `#1e293b`; body `#334155`; secondary `#475569`; muted `#94a3b8`.
- **Accent:** `--accent: #7c3aed`, `--accent-light: #8b5cf6`, `--accent-tint: #ede9fe`,
  `--accent-bar: #6d28d9`. Active nav, key IDs, primary CTAs, active pager buttons.
- **Status tokens (as :root vars):**
  - `--status-green: #16a34a` / `--status-green-bg: #dcfce7` — resolved / healthy / good
  - `--status-amber: #d97706` / `--status-amber-bg: #fef3c7` — pending / at-risk / warning
  - `--status-red: #dc2626` / `--status-red-bg: #fee2e2` — breached / urgent / error
  - `--status-slate: #475569` / `--status-slate-bg: #f1f5f9` — neutral / open
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`.
  Base 13px. KPI labels 10px / uppercase / `letter-spacing: 0.07em` / muted. KPI values
  28px / weight 700. Table headers 11px / uppercase / `letter-spacing: 0.05em` / muted.
  Sidebar section labels 10px / uppercase / `letter-spacing: 0.07em`. Mono IDs: `"SF Mono",
  "Fira Code", monospace`.
- **Density & radius:** 7px/8px control/pill radius, 10px card radius, 24px page padding,
  16px / 20px card padding; 1px borders throughout.
- **Borders & shadows:** cards `1px solid #e9ecf3` + `box-shadow: 0 1px 4px rgba(0,0,0,.04)`;
  sidebar `border-right: 1px solid #e2e8f0`; topbar `border-bottom: 1px solid #e2e8f0`.
- **Motion:** `.1s` background hover on nav items and table rows; `.3s` width transitions
  on progress bars. Gentle ease; never bouncy.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns described by shape and behavior — not by meaning.

- **Left sidebar (240px, white, 1px right border):** logo mark + product name at top → 2–3
  labeled sections, each with nav items (icon + label + optional badge count); active item =
  left 3px violet bar + tinted background + violet text. Bottom-pinned user row: avatar
  initial circle + name + role + presence dot.
- **Top bar (56px, white, 1px bottom border):** left — page title + breadcrumb block; center
  — full-width search input with magnifier icon; right — contextual filter dropdown (avatar
  chip + label + chevron), notification icon button with badge dot, user avatar.
- **Main area (flex-1, slate page bg, 24px padding):** vertical flow of components below.
- **4 KPI cards** (equal-width row, white, 10px radius, soft shadow): each = uppercase
  micro-label + big figure (28px/700) + delta chip (up/down/neutral colored) + sparkline
  (bar chart, area line, or arc SVG). Chips and sparklines recolor by direction using the
  status token set.
- **Priority-tier bar strip** (white card, compact): a header with title + subtitle + link;
  N tier rows, each = [tier label] [descriptor meta above thin bar] [bar track (green/amber/red
  fill based on compliance)] [percentage label]. Bars colored by the status token set.
- **Full-width records table** (white card): header with title + count + link; sticky
  uppercase header; rows with mono ID column, subject + sub-text cell, requester avatar-
  initial + name, dual status pills (tier + state), assignee avatar-initial + name, elapsed
  time; hover tint; footer with result count + pager (active page = accent fill).
- **Right load panel (260px, white card):** title + subtitle; list of N items showing
  presence dot (green online / amber away / slate offline) + avatar initial circle + name +
  role + count badge. Footer link.
- **Records list screen:** the records-table archetype as its own page — toolbar with search
  + filter chips, count, the same dense table, and a pager.
- **Record form screen:** sectioned white cards of labelled fields; **rules appear as inline
  validation** — required marks (`*`), helper text below the field, and inline error messages
  on invalid fields; submit disabled until valid. No rules/checklist/validation-status panel.
- **Record detail screen:** breadcrumb + header band (title + status pill + key action
  buttons) + a meta grid of label/value pairs + one or more related-data sub-panels or
  activity feeds.

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS domain's
equivalent of the archetype slots — its primary entities, key metrics, status states,
tier/priority labels, record columns, form fields and their rules, and detail fields —
and map them onto the archetype above. If no KB/domain is supplied (standalone), use the
Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules become
inline field validation. Do NOT render build/implementation notes or designer controls —
every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode this is
> IGNORED — replace every label with the real domain's equivalent (entities, metrics,
> states, columns, fields) drawn from the KB + prompt.

```
Domain (illustrative): a SaaS customer support operations platform.

Logo + product name → "Relay Support".
Sidebar sections:
  INBOX  — All Open (badge 47), Unassigned (amber badge 12), My Tickets (badge 8), Mentions.
  VIEWS  — By Priority, By SLA Breach (red badge 3), Awaiting Reply, Resolved Today.
  SETTINGS — Queues, Automations, SLA Policies.
Page title / breadcrumb → "Ticket Queue" / "Support / Ticket Queue".
Filter dropdown → "All Agents".

KPI tiles (4):
  • Open Tickets — 47, ↑ 6 vs ytd (down chip), bar sparkline.
  • Avg First Response — 1h 24m, ↓ 18m (up chip), area line sparkline.
  • SLA Compliance — 91%, ↑ 3% (up chip), arc progress SVG.
  • CSAT Score — 4.6/5, → 0.0 (neutral chip), star motif SVG.

Priority-tier bars → "SLA by Priority" — rows:
  P1 Critical (4h breach, 14 items) — 78% amber bar.
  P2 High     (8h breach, 21 items) — 94% green bar.
  P3 Normal   (24h breach, 9 items) — 97% green bar.

Records table → "Ticket Queue" (47 records):
  Columns: # (violet mono ID) / Subject + category sub / Requester avatar+name /
  Priority pill (P1 red / P2 amber / P3 violet) / Status pill (Open / Pending /
  Resolved / Breached) / Assigned to / Age.
  8 representative rows.

Right panel → "Team Load · Active agents":
  6 agent rows (presence dot + avatar initial + name + role + ticket count badge).

List screen     → all records, search + filter chips (status, priority), paginated.

Form screen     → "New Ticket": subject (required), requester email (required, valid
  email format), category (required select), priority (required radio), description
  (optional textarea), assignee (optional select). Rules as required marks + helper
  text + inline errors; "Create Ticket" disabled until valid.

Detail screen   → one record: breadcrumb + header (#ID + status pill + Edit/Assign
  actions) + meta grid (requester, category, priority, assignee, created, SLA due) +
  "Activity" timeline + "Related" sub-panel.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual language
   tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities, key
   metrics, status states, tier/priority labels, record columns, form fields + rules,
   detail fields — from the KB + prompt. Standalone: use the Example instantiation above.
3. Build each screen in the Visual language + Layout archetype above, imitating the
   example set in `assets/` (dashboard, list, form, detail) and the `assets/template.html`
   seed — with fresh content for the real domain, NOT the example labels.
4. Express domain rules as INLINE field validation (required marks, helper text, inline
   errors, disabled-until-valid submit). Never render rules/checklist/validation-status/
   build-note panels or designer/demo controls.
5. One inline `<style>`, semantic HTML5, no external assets, no CDNs — self-contained.

## Output contract

```
<artifact identifier="admin-relay-helpdesk" type="text/html" title="Relay Admin">
<!doctype html>...</artifact>
```
