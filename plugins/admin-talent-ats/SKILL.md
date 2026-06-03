---
name: admin-talent-ats
description: |
  Light admin aesthetic: white sidebar on a near-white canvas (#f8f8fc),
  indigo accent (#4f46e5 / #6366f1) + pink secondary accent (#ec4899),
  slate neutral text, 1px #e8e8f2 borders, 12px-radius cards with a
  whisper shadow. Archetype = left sidebar (logo mark + entity switcher +
  grouped nav) + topbar (search + period picker + avatar) + 4 KPI cards
  with inline sparklines + a kanban-style stage board + a conversion
  funnel chart (inline SVG) + an upcoming-items side panel + a full-width
  records table. Built for clean, airy operational overviews where the
  pipeline stage counts matter at a glance.
triggers:
  - "light indigo admin"
  - "indigo pink sidebar admin"
  - "kanban pipeline dashboard"
  - "airy admin with sparklines"
  - "left sidebar light admin"
  - "stage-board dashboard"
  - "funnel chart admin panel"
  - "painel admin claro índigo"
example_prompt: "Apply this light indigo admin aesthetic to my domain"
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

# Talent ATS Admin — Visual Archetype

This plugin contributes a **look** (airy light admin, indigo + pink accent,
sparkline KPI cards, kanban stage board) and a **structure** (left sidebar +
topbar + KPI row + stage columns + funnel panel + records table, plus list /
form / detail screens). It does **not** contribute a domain — the subject
matter comes from the Knowledge Base and the user's prompt. Treat the example
below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property.

- **Canvas / surfaces:** page `#f8f8fc`; card / sidebar `#ffffff`; inset hover
  `#f1f0fe`; border `#e8e8f2`; hover border `#c7c4f0`.
- **Text ramp:** primary `#1e1b4b`, secondary `#334155`, muted `#475569`,
  faint `#94a3b8`.
- **Accent (indigo):** `--c-primary: #4f46e5`, `--c-primary-lt: #6366f1`,
  `--c-primary-bg: #eef2ff`. Primary CTAs, active nav marker, accent figures,
  sparkline strokes.
- **Secondary accent (pink):** `--c-accent: #ec4899`, `--c-accent-lt: #f472b6`,
  `--c-accent-bg: #fdf2f8`. Secondary highlights, stage bar color, badge dot.
- **Supporting palette:** `--c-violet: #7c3aed` / `--c-violet-bg: #f5f3ff`;
  `--c-success: #22c55e` / `--c-success-bg: #f0fdf4`;
  `--c-warning: #f59e0b` / `--c-warning-bg: #fffbeb`.
- **Stage / status ramp (tokens):** applied `#94a3b8`, screening `var(--c-violet)`,
  interview `var(--c-accent)`, offer `var(--c-success)`, each available as a
  `-bg` tint. Deltas: up `#dcfce7 / #15803d`, down `#fee2e2 / #b91c1c`.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
  sans-serif`. Base 13px. `font-variant-numeric: tabular-nums` on every numeric
  cell. KPI figures 26px / weight 800 / color `#1e1b4b`. Section labels 10–10.5px
  / weight 700 / `text-transform: uppercase` / `letter-spacing: .06–.08em` /
  color `#94a3b8`. Sidebar nav items 12.5px / weight 500.
- **Density & radius:** cards 16px internal padding, 12px radius, `0 1px 4px
  rgba(79,70,229,.04)` shadow. Sidebar 232px wide. Topbar 56px tall. Stage
  columns 12px padding, 12px radius. Pills 2px 10px padding, 20px radius.
  Tag chips 1px border, 20px radius.
- **Borders:** 1px `#e8e8f2` on all panels; no heavy shadows. Active sidebar
  item gets a 3px left bar at `var(--c-primary)`.
- **Motion:** `.12s` background/border transitions on interactive elements.
  Subtle, never bouncy.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns described by shape and behavior — not meaning.

- **Left sidebar** (232px, white, 1px right border, vertical flex): top **brand
  block** (logo mark + name + sub-label), **entity switcher** (indigo-bg pill
  with dot + truncated label + caret), **grouped nav** (section labels in
  all-caps muted, items with icon + label + optional badge), flex spacer,
  **footer** (overlapping avatar cluster + team label).
- **Topbar** (56px, white, 1px bottom border): page title + breadcrumb on the
  left → **search pill** (centered, max 320px) → flex-push **period picker**
  → notification bell with unread dot → **avatar chip** + name.
- **Main content** (page bg, 20px padding, vertical flow): **page header** (h1
  + date chip on the left, ghost + primary buttons on the right).
- **KPI card row** (4 equal columns): each card = white panel with label +
  big figure on the left and a colored icon chip on the right, then a **inline
  sparkline SVG** (polyline + area-fill gradient), then a delta chip + sub-line
  at the bottom.
- **Stage board** (kanban, 4 equal columns): each column = tinted bg panel with
  header (stage name + count badge), then 3–4 **entity mini-cards** (left-bar
  accent by stage color, avatar initials, name, type, source tag, elapsed days).
- **Lower grid (8fr / 4fr):**
  - **Left — conversion funnel panel:** titled card with a horizontal-bar
    inline SVG funnel (indigo-to-pink gradient bars, narrowing right with
    percentage labels; stages labeled left, counts right).
  - **Right — upcoming-items panel:** date-grouped list rows (time slot in
    accent color + entity name + role + interviewer + format badge).
- **Full-width records table:** titled card with ghost + primary header actions,
  a sticky uppercase header, rows with **avatar initials + name + sub-line** in
  first cell, stage pill, source badge, star rating, action buttons, footer
  with count + pager.
- **Records list screen:** same table archetype with a toolbar (search input +
  filter chip group).
- **Record form screen:** sectioned white cards of labelled fields; **rules as
  inline validation** — required marks (`*`), helper text, inline errors,
  primary submit disabled-until-valid. No rules/checklist/validation-status panel.
- **Record detail screen:** breadcrumb + header band (ID chip + status pill +
  action buttons), meta grid (3-column label/value cells), one or more
  related-data panels (stage progress row or mini-table + activity feed).

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key metrics,
stage states, record columns, form fields and their rules, and detail fields —
and map them onto the archetype above. If no KB/domain is supplied (standalone),
use the Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules
become inline field validation. Do NOT render build/implementation notes or
designer controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent
> (entities, metrics, stages, columns, fields) drawn from the KB + prompt.

```
Domain (illustrative): a recruiting / applicant-tracking system for an HR team.

Brand block          → logo mark + "HireFlow" / "Talent Ops Platform".
Entity switcher      → active requisition: "Sr. Frontend Engineer".
Sidebar nav groups   → PIPELINE (Dashboard, Candidates, Pipeline Board);
                       SOURCING (Job Postings, Campaigns, Referrals);
                       REPORTS (Analytics, Funnel Report, Export).
Topbar               → "Hiring Overview" + breadcrumb; search "candidates, roles…";
                       period picker (This Month / Q2 / YTD); bell; recruiter avatar.

KPI cards (4):
  • Open Roles — 24 (▲4 this qtr vs 20 last month). Indigo icon.
  • Active Candidates — 318 (▲12% vs 284 last month). Violet icon.
  • Interviews This Week — 41 (▲8 vs last wk, 33 completed). Pink icon.
  • Avg. Time-to-Hire — 18 d (▼2 d vs last month). Green icon.

Stage board (4 columns):
  Applied (12) / Screening (9) / Interview (7) / Offer (3).
  Each column has 3 candidate mini-cards: initials + name + role + source tag
  (LinkedIn / Referral / Agency / Job Board) + days-in-stage.
  Left-bar color: applied=slate, screening=violet, interview=pink, offer=green.

Lower grid:
  Left  → "Recruiting Funnel" SVG: Applied 318 → Screened 187 (59%) →
          Interviewed 84 (45%) → Offered 21 (25%) → Hired 14 (67%).
  Right → "Upcoming Interviews" grouped by date (Today / Tomorrow):
          time · candidate name · role · interviewer · video/onsite badge.

Records table → "Active Candidates":
  Candidate (initials + name + email) / Applied Role / Stage pill / Source badge /
  Rating (stars) / Actions (view / schedule). 8 rows, hover tint, pager.

List screen   → all candidates, search + filter chips (stage, source), paginated.

Form screen   → "New Candidate": full name (required), email (required, valid
  format), applied role (required select), source (required select), LinkedIn URL
  (optional, valid URL format), notes. Rules as required marks + helper text +
  inline errors; "Add Candidate" disabled until valid.

Detail screen → one candidate: breadcrumb + header (name + stage pill + actions),
  meta grid (role, source, rating, applied date, recruiter, last activity),
  "Stage History" progress rows + "Interview Notes" activity feed.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, stage states, record columns, form fields + rules, detail fields
   — from the KB + prompt. Standalone: use the Example instantiation above.
3. Build each screen in the Visual language + Layout archetype above, imitating
   the example set in `assets/` (dashboard, list, form, detail) and the
   `assets/template.html` seed — with fresh content for the real domain, NOT the
   example labels.
4. Express domain rules as INLINE field validation (required marks, helper text,
   inline errors, disabled-until-valid submit). Never render
   rules/checklist/validation-status/build-note panels or designer/demo controls.
5. One inline `<style>`, semantic HTML5, `tabular-nums` on figures, no external
   assets, no CDNs — self-contained.

## Output contract

```
<artifact identifier="admin-talent-ats" type="text/html" title="Light Indigo Admin">
<!doctype html>...</artifact>
```
