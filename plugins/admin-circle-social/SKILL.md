---
name: admin-circle-social
description: |
  Friendly light-mode admin aesthetic: white card surfaces on a soft grey canvas
  (#f8f9fc), blue (#3b82f6) and violet (#8b5cf6) dual-accent, system font at
  14px, 12px rounded cards, hairline #e8eaf2 borders, subtle 1px shadows, and
  crisp role/status pills. Archetype = left sidebar (brand mark + context
  switcher + grouped nav + footer) + sticky topbar (breadcrumb + search + date
  chip + icon buttons + avatar) + 4 KPI cards + 2-column mid row (action-queue
  panel + side panel) + full-width content chart + full-width records table.
  Built for bright, friendly operations consoles that prioritise legibility and
  low operator fatigue.
triggers:
  - "friendly light-mode admin"
  - "white card admin"
  - "blue violet admin"
  - "dual-accent sidebar dashboard"
  - "soft light operations console"
  - "sidebar nav admin"
  - "bright admin dashboard"
  - "painel claro com sidebar"
example_prompt: "Apply this friendly light-mode admin aesthetic to my domain"
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

# Circle Admin — Visual Archetype

This plugin contributes a **look** (friendly light-mode, blue/violet dual-accent,
white card surfaces) and a **structure** (left sidebar + sticky topbar + KPI cards
+ action-queue panel + side panel + chart + records table, plus list / form /
detail screens). It does **not** contribute a domain — the subject matter comes
from the Knowledge Base and the user's prompt. Treat the example below as
illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property; hardcode the neutral light ramp.

- **Canvas / surfaces:** page `#f8f9fc`; card `#ffffff`; sidebar `#ffffff`;
  row hover `#f1f5f9`; faint alt `#fafbfc`; hairline border `#e8eaf2`.
- **Text ramp:** heading `#0f172a`; body `#334155`; secondary `#475569`; muted
  `#64748b`; placeholder `#94a3b8`.
- **Accent (primary):** `--accent-blue: #3b82f6`; `--accent-blue-soft: #eff6ff`;
  border tint `#bfdbfe`. CTAs, active nav border, links, icon fills.
- **Accent (secondary):** `--accent-violet: #8b5cf6`; `--accent-violet-soft: #f5f3ff`.
  Secondary badges, chart fills, alternate icon tints.
- **Status ramp (tokens):** `--status-green: #22c55e`; `--status-amber: #f59e0b`;
  `--status-red: #ef4444`; each with a `…-soft` tint (`--status-green-soft:
  #dcfce7`; `--status-amber-soft: #fef3c7`; `--status-red-soft: #fee2e2`) for
  pill backgrounds and card tints.
- **Chart:** `--chart-line: #3b82f6` (primary stroke); `--chart-area:
  rgba(59,130,246,0.12)`; `--chart-violet: #8b5cf6` (secondary stroke);
  `--chart-violet-area: rgba(139,92,246,0.10)`.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
  sans-serif`. Base 14px / `#334155`. Section micro-labels 10–11px, uppercase,
  `letter-spacing: 0.06–0.07em`, `#94a3b8`. Big KPI figures 28px / weight 800 /
  `letter-spacing: -0.02em`.
- **Density & radius:** 13–14px row padding, 18–20px card padding, 16px gaps;
  card radius 12px, control radius 8px, pill radius 999px (fully rounded).
- **Borders & shadows:** hairline 1px `#e8eaf2` separators; cards carry a
  `box-shadow: 0 1px 4px rgba(0,0,0,0.04)` — soft lift only, not dramatic.
- **Motion:** `.10s–.15s` background/border transitions on interactive elements.
  Default `ease`. Never bouncy.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Left sidebar** (220px, white bg, 1px right border, sticky full-height):
  - **Brand band** (1px bottom border): 32px icon mark + wordmark, 14–18px padding.
  - **Context switcher** (pill button, accent-blue-soft bg + blue border, chevron):
    a tinted interactive chip for switching the active context scope.
  - **Grouped nav sections** (each group: 10px uppercase micro-label + nav items):
    items are `border-left: 3px solid transparent`; active item gets `--accent-blue`
    left border + `--accent-blue-soft` bg + blue text weight 600. Optional badge
    (red pill) on items with counts.
  - **Footer** (auto-push to bottom, 1px top border): 32px avatar initials circle +
    name / role micro-text + sign-out icon.
- **Sticky topbar** (56px, white bg, 1px bottom border, z-index 10):
  breadcrumb → flexible search pill (icon + input, focus border-color blue) →
  date-range chip → icon-button (notification bell with dot) → avatar circle.
- **Main content** (`#f8f9fc` bg, 24px padding, vertical flex, 20px gap): page
  header (title + sub-line / right ghost + primary CTA buttons), then region stack.
- **KPI card row** (4 cards, equal `1fr` grid, 16px gap): each card = white panel,
  12px radius, 1px border, soft shadow; inside: **header** (10px uppercase label +
  thematic icon in accent color) → **big figure** (28px / 800) → **footer** (delta
  chip in green-soft or red-soft + tiny 5-point inline SVG sparkline).
- **2-column mid row** (`1fr 300px`, 16px gap, `align-items: start`):
  - **Left — action-queue panel:** a titled card (title + count badge) holding a
    list of 3–4 item cards; each item: reporter meta row (avatar + label + source +
    timestamp), content excerpt (italic), action buttons (ghost positive + solid
    negative), reason pill.
  - **Right — side panel:** 2 stacked cards; first = ranked list (label + bar); 
    second = flagged/notable items (avatar + name + meta + link).
- **Full-width content chart:** titled card with legend, inline SVG area chart
  (~520×140): horizontal grid lines, y-axis labels, x-axis day labels, two
  overlapping filled areas (blue primary, violet secondary), data point circles.
- **Full-width records table:** titled card with ghost + primary header buttons; a
  sticky header (11px uppercase, `#94a3b8`); dense rows with avatar initials cell,
  role pill, date cell, status pill; hover row bg `#f8f9fc`; no footer on the
  dashboard instance (use a footer with count + pager on the list screen).
- **List screen:** search + filter chips toolbar, same dense table, footer pager.
- **Form screen:** sectioned white cards of labelled fields; **rules appear as
  inline validation** — required marks (`*`), helper text under the field, and
  inline error messages on invalid fields; primary submit disabled-until-valid. No
  rules/checklist/validation-status panel.
- **Detail screen:** breadcrumb + header band (title + status pill + key actions),
  a 2-col meta grid of label/value pairs, and related sub-panels below.

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
Domain (illustrative): an online community and social platform ops console.

Context switcher → active community: "Design Creators Hub".
Nav groups: OVERVIEW (Dashboard, Analytics), COMMUNITY (Members, Posts, Events),
            MODERATION (Reports, Queue, Flagged), SETTINGS (Roles, Integrations).
Breadcrumb → "CircleSpace / Dashboard".

KPI cards (4):
  • Active Members 2,418 (blue icon, ▲8.3%).
  • Posts Today 347 (violet icon, ▲14.1%).
  • Reports Open 4 (red icon, –2 vs yesterday).
  • Engagement Rate 62.4% (green icon, ▲3.7pp).

Action-queue panel (left) → "Moderation Queue · 4 pending" — item cards of
  [reporter avatar + handle + source + timestamp] [content excerpt (italic)]
  [Approve ghost-green / Remove solid-red] [reason pill: Spam / Hate Speech /
  Misinformation / NSFW].

Side panel (right) — two stacked cards:
  • "Trending Topics" — hashtag rows with post-count bars (violet fill).
  • "Flagged Accounts" — user rows (avatar + handle + flag-count + joined date +
    "Review" blue link).

Engagement chart → "Engagement Over Time · Mon–Sun" — two area paths:
  Posts published (blue) + Reactions received (violet dashed), 7-day x-axis.

Records table → "Community Members": Member (avatar + name + @handle) /
  Role pill (Admin / Moderator / Member) / Joined date /
  Status pill (Active / Suspended / Pending).

List screen → all members, search + filter chips (Role, Status), paginated.

Form screen → "Invite Member": email (required, valid format), display name
  (required), role (required select), optional bio. Rules as required marks +
  helper text + inline errors; "Send Invite" disabled until valid.

Detail screen → one member: breadcrumb + header (display name + status pill +
  Edit / Suspend actions), meta grid (email, role, joined, last active, post
  count, flag count), and a "Recent Activity" sub-panel below.
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
5. One inline `<style>`, semantic HTML5, no external assets, no CDNs — self-contained.

## Output contract

```
<artifact identifier="admin-circle-social" type="text/html" title="Circle Admin">
<!doctype html>...</artifact>
```
