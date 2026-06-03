---
name: admin-mazer
description: |
  Light friendly admin aesthetic: soft cloud-blue page background (#f2f7ff),
  white card surfaces with 11px radius, deep navy body text (#25396f),
  indigo-blue primary accent (#435ebe), and Nunito-family type at weight 700
  headings. Layout archetype = fixed left sidebar (collapsible nav groups with
  icon + label + disclosure) + sticky top header bar (breadcrumb + search +
  icon actions + avatar) + 4-tile KPI row (icon chip + metric + delta + label)
  + mixed content grid (SVG chart card + recent-activity feed + badge-status
  rows) + full-width data table with rounded badge pills, pagination, and
  filters. Friendly density: 14–16px content, 11px radius on all cards,
  generous 18–20px panel padding, clear typographic hierarchy.
triggers:
  - "light blue admin dashboard"
  - "rounded card admin"
  - "friendly sidebar admin"
  - "indigo accent light admin"
  - "soft cloud admin panel"
  - "painel admin claro arredondado"
  - "admin azul claro com sidebar"
  - "light mode sidebar dashboard"
  - "rounded friendly operations panel"
  - "painel claro com acento índigo"
example_prompt: "Apply this light friendly rounded admin aesthetic to my domain"
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
    requires: [typographic-rhythm, laws-of-ux]
---

# Soft Blue Admin — Visual Archetype

This plugin contributes a **look** (soft cloud-blue, white rounded cards, indigo
accent, Nunito type) and a **structure** (sidebar with grouped nav + top header +
KPI tiles + chart/activity/status grid + dense data table, plus list, form,
settings, auth, error, email, and chat screens). The domain — entities, metrics,
status states, terminology — comes from the Knowledge Base and the user's prompt.
The example below is illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Every chromatic value is a `:root` CSS custom property.

- **Page & surfaces:** page `--bg: #f2f7ff`; card/sidebar `--card: #ffffff`;
  sidebar hover/active `--sidebar-hover: #f0f4ff`; input bg `--input-bg: #f8faff`;
  border `--border: #e0e6ed`; divider `--divider: #eef1f6`.
- **Text ramp:** body `--text-body: #25396f`; secondary `--text-secondary: #6b7ea8`;
  muted `--text-muted: #9daec8`; on-dark `--text-inv: #ffffff`.
- **Accent / primary:** `--primary: #435ebe`; hover `--primary-hover: #3a52aa`;
  light bg `--primary-soft: #eef1fb`; active ring `--primary-ring: rgba(67,94,190,.25)`.
- **Status tokens:** `--state-success: #28c76f`; `--state-success-soft: #e6f9ef`;
  `--state-warn: #ff9f43`; `--state-warn-soft: #fff4e5`;
  `--state-danger: #ea5455`; `--state-danger-soft: #fce8e8`;
  `--state-info: #00cfe8`; `--state-info-soft: #e0f9fc`;
  `--state-neutral: #82868b`; `--state-neutral-soft: #f0f0f0`.
- **Typography:** `"Nunito", "Segoe UI", system-ui, -apple-system, sans-serif`.
  Base 14px / line-height 1.5. Headings weight 700, body weight 400–500.
  Micro-labels 11px uppercase letter-spacing 0.6px muted. Big KPI figures 28px
  weight 700. Nav labels 13px weight 600.
- **Radius:** card/panel `11px`; button `8px`; input `8px`; badge/pill `20px`;
  avatar `50%`; small chip `6px`.
- **Spacing & density:** sidebar width 260px; top bar height 60px;
  card padding 20px; grid gap 18px; row padding 10px 16px.
- **Shadows:** cards `0 4px 24px rgba(67,94,190,.08)`;
  sidebar `2px 0 8px rgba(67,94,190,.06)`; dropdown `0 8px 24px rgba(0,0,0,.12)`.
- **Motion:** hover transitions `0.18s ease`; sidebar collapse `0.25s ease`;
  badge pulse 2s. Ease-out for entrances (~200ms), ease-in for exits (~140ms).

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns described by shape, count, and behavior — not meaning.

- **Fixed left sidebar** (260px, card bg, shadow): brand logo area at top →
  collapsible **nav group sections** (group label in muted uppercase, then items
  with icon + label; active item gets primary-soft bg + primary text + left accent
  bar 3px; hover gets sidebar-hover bg; items with children show a disclosure
  chevron and an indented sub-list). Sidebar footer: avatar + name + role + icon
  button strip.
- **Sticky top header bar** (60px, card bg, 1px bottom border): hamburger toggle
  → breadcrumb trail → flex spacer → search pill → notification icon with dot →
  avatar with dropdown. On collapsed sidebar, the bar extends to full width.
- **Page body** (bg, padding 24px, vertical flow): **page title row** (h1 + sub-
  label on left, primary CTA button on right) → region stack below.
- **KPI tile row** (4 equal tiles, grid): each tile = white rounded card with a
  colored icon chip (48×48px, soft bg), a big figure, a delta badge (▲/▼ + %)
  with success/danger color, and an uppercase micro-label. Border-left accent bar
  3px primary on the active tile.
- **Mixed content grid** (3-column fluid or 2+1 split):
  - **Chart card** (spans 2 cols): titled card with time-range tab buttons, an
    inline SVG area/line chart (gridlines, axis labels, dual series, legend chips),
    and a summary row below.
  - **Activity feed card** (1 col): titled card with a scrollable list of items —
    each item = avatar/icon chip + two-line text (title + sub) + elapsed time badge.
  - A secondary row: **Status rows card** (rows of [icon chip][label + sub][badge
    pill][metric right-aligned]) side by side with a **mini donut/bar chart card**.
- **Full-width data table card**: titled with ghost + primary header actions +
  search input; sticky uppercase column headers; dense rows with rounded **badge
  pills** in status columns, avatar + name + sub two-line cells, right-aligned
  numerics; checkbox column; footer with result count + previous/next pager.
- **List screen**: the data-table archetype as a standalone page — filter chips row
  + search + count, same dense table, floating action button.
- **Form screen**: multi-section card form — each section has a heading, then
  label/input pairs (two-column grid for peers, full-width for textareas/selects).
  Rules expressed as **inline validation**: required mark (`*`), helper text beneath
  the field, inline error message with danger color and icon on invalid fields,
  primary submit disabled until the required fields are valid. No rules panel.
- **Settings / profile screen**: avatar upload block + sectioned preference groups
  (notification toggles, display options, security sub-form) all as inline-validated
  form sections inside cards.
- **Auth screens** (login + register): centered narrow card on the page bg — brand
  mark at top, heading, inline-validated fields, primary button, secondary link.
- **Error screen**: centered illustrative SVG + large code heading + message +
  primary return-home button. No caveats.
- **Email screen**: three-column layout — folder list rail (left narrow) + message
  list (middle) + reading pane (right wide, with toolbar + header + body).
- **Chat screen**: two-column — contact list (left, with search + avatar rows +
  last-message preview + time badge) + conversation pane (right, header + scrollable
  bubble thread + composer bar with attach + send).

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
Domain (illustrative): a project management and resource tracking platform.

Sidebar nav groups:
  Overview: Dashboard, Analytics
  Work: Projects, Tasks, Milestones
  People: Team, Clients
  Tools: Documents, Email, Chat
  System: Settings

KPI tiles (4):
  • Active Projects  24  (▲3 this month, "across 6 departments")
  • Open Tasks       148 (▼12 from last week, "47 overdue")
  • Team Members     63  (▲2 new this week, "across 8 teams")
  • Budget Used      72% (▲5% vs plan, "Q2 total: $128K")

Chart card: "Task Completion — Last 30 Days" — dual-series area chart
  (Completed vs Created per week), with legend chips and a summary row
  (Avg per day · Completion rate · Longest streak).

Activity feed: "Recent Activity" — items like
  "[avatar] Alex Chen closed milestone Sprint 14 · 2h ago",
  "[avatar] Design team uploaded 5 files · 4h ago".

Status rows card: "Projects by Status" — rows of
  [green chip] Active [24] / [amber chip] At Risk [5] / [red chip] Delayed [3].

Data table (dashboard): "Recent Projects" — columns: Project / Lead / Team /
  Due Date / Progress bar / Status pill (Active/At Risk/Delayed/Completed).

List screen: all projects — filter chips (Status, Team, Priority), search,
  paginated table with same columns + checkbox selection.

Form screen: "New Project" — Name (required), Description, Lead (required select),
  Team (multi-select), Start Date (required), Due Date (required, after start),
  Priority (select), Budget (number, > 0). Required marks + helper text +
  inline errors; "Create Project" disabled until valid.

Settings screen: profile photo + Display Name + Email (read-only) + Timezone
  select; Notifications section (email toggles); Security section (change password
  form with current + new + confirm, inline mismatch error).

Login: Email (required, valid format) + Password (required); "Sign in" button;
  "Forgot password?" link.

Register: Full Name (required) + Email (required, valid format) + Password
  (required, min 8 chars) + Confirm Password (required, must match); "Create
  account" button; "Already have an account?" link.

Error: illustration + "404" heading + "This page doesn't exist." + "Back to
  dashboard" primary button.

Email: folders (Inbox 12, Sent, Drafts, Archive, Trash); message list; reading
  pane showing a project update notification email.

Chat: contact list with team channels (General, Design, Engineering, Marketing);
  conversation thread between team members; composer with emoji + attach + send.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, status states, record columns, form fields + rules, detail fields
   — from the KB + prompt. Standalone: use the Example instantiation above.
3. Build each screen in the Visual language + Layout archetype above, imitating
   the example set in `assets/` (dashboard, list, form, charts, settings, login,
   register, error, email, chat) and the `assets/template.html` seed — with fresh
   content for the real domain, NOT the example labels.
4. Express domain rules as INLINE field validation (required marks `*`, helper
   text, inline errors, disabled-until-valid submit). Never render rules/checklist/
   validation-status/build-note panels or designer/demo controls.
5. One inline `<style>`, semantic HTML5, no external assets, no CDNs — self-contained.

## Output contract

```
<artifact identifier="admin-mazer" type="text/html" title="Admin Console">
<!doctype html>...</artifact>
```
