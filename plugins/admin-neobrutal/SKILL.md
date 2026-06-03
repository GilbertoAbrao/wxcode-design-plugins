---
name: admin-neobrutal
description: |
  Neo-brutalist admin aesthetic: white canvas with thick black borders (2–3px),
  hard 4px offset shadows (no blur), vibrant pastel accent blocks (coral #F5A86E,
  lime #8FD14F, cream #FFF5E6), monospace numerics and uppercase micro-labels,
  zero border-radius everywhere. Archetype = left sidebar (brand block + monospace
  nav glyphs + user footer) + top bar (search slab + CTA block) + 4 stat tiles
  with coloured top-border accents + 2-column grid (records table + activity feed)
  + footer meta strip.
triggers:
  - "brutalist admin"
  - "neobrutalism dashboard"
  - "pastel admin"
  - "bold borders admin"
  - "flat blocks dashboard"
  - "hard shadow admin"
  - "monospace admin panel"
  - "painel brutalista"
  - "zero radius admin"
  - "野兽派后台"
example_prompt: "Apply this neo-brutalist admin aesthetic to my domain"
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
    requires: [pixel-discipline, state-coverage]
---

# Neobrutalist Admin — Visual Archetype

This plugin contributes a **look** (white canvas, thick black borders, hard
offset shadows, pastel accent blocks, monospace type) and a **structure** (left
sidebar + search topbar + stat tiles + two-column content grid, plus list / form
/ detail screens). It does **not** contribute a domain — the subject matter comes
from the Knowledge Base and the user's prompt. Treat the example below as
illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Declare every chromatic value as a `:root` CSS custom
property.

- **Canvas / surfaces:** page `#ffffff`; cream block `#FFF5E6`; coral accent
  `#F5A86E`; lime accent `#8FD14F`; lavender accent `#B8A4FF`; yellow accent
  `#FDE74C`; cyan accent `#90E0EF`; ink `#000000`.
- **Borders:** ALL borders `2–3px solid #000000`. No exceptions. Border-radius:
  `0` everywhere — every element is a hard rectangle.
- **Shadows:** ALL interactive/panel shadows are hard offset only —
  `4px 4px 0 #000000`. Never blurred, never spread-only. On hover/active: shift
  to `5px 5px 0 #000000` or compress to `2px 2px 0 #000000`.
- **Typography:** monospace (`ui-monospace, "SF Mono", Menlo, Consolas,
  monospace`) for all numbers, labels, nav items, buttons, IDs, codes, and
  timestamps. System-UI for body prose only. Micro-labels: 10–11px, uppercase,
  `letter-spacing: 0.12em`, `opacity: 0.6`. Big stat figures: 36px, weight 700,
  `letter-spacing: -0.03em`. Nav items: 12px monospace, weight 700, uppercase,
  `letter-spacing: 0.08em`.
- **Status pills:** flat pastel blocks — `border: 2px solid #000000`,
  `border-radius: 0`, uppercase monospace 10px, weight 700. Palette:
  lime = active/running, coral = review/warning, yellow = on-hold/idle,
  lavender = draft/queued, grey `#D0D0D0` = done/completed.
- **Stat tile accents:** each tile gets a `6px` coloured top border from the
  accent palette (coral, lime, lavender, yellow in rotation).
- **CTAs:** lime block (`background: var(--lime)`) + `border: 2px solid #000000`
  + hard shadow; uppercase monospace. No rounded corners.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns described by shape and behavior, not meaning.

- **Left sidebar** (220px, `border-right: 3px solid #000`): top brand block
  (coral fill, bold ink text, `border-bottom: 3px solid #000`) → monospace nav
  list (6 items, each with a single-char ASCII glyph prefix (`>`, `#`, `*`, `+`,
  `%`, `@`), active item gets lime fill + ink left border) → user footer block
  (avatar in coral square + name + role label, `border-top: 2px solid #000`).
- **Top bar** (`border-bottom: 3px solid #000`, `padding: 12px 24px`): page
  section label → cream search slab (cream fill, `border: 3px solid #000`, no
  radius) → right: CTA button (lime block + hard shadow) + avatar square (coral).
- **4 stat tiles** (`grid-template-columns: repeat(4,1fr); gap: 16px`): each
  tile = cream block + `border: 3px solid #000` + hard shadow; coloured
  `6px` top border accent, uppercase micro-label, monospace big figure, delta
  row (↑ green / ↓ red, inline SVG arrow).
- **2-column content grid** (`grid-template-columns: 1fr 340px; gap: 16px`):
  - LEFT — records panel: black panel header (ink fill, paper text, title +
    meta count), dense table (cream odd rows / paper even, `border-bottom: 1px
    solid #000`, monospace cells, status pills as flat pastel blocks).
  - RIGHT — activity/event feed: black panel header, stacked cards (cream block,
    `border: 2px solid #000`, stacked without top gap except first), each card =
    icon square (24px, pastel fill, `border: 2px solid #000`) + event text +
    sub-line + monospace timestamp.
- **Records list screen:** full-width panel with a toolbar (cream search slab +
  filter chips — `border: 2px solid #000`, lime active chip), the records table,
  and a footer row (result count + hard-shadow pager buttons).
- **Record form screen:** sectioned layout with field cards; **rules appear as
  inline validation** — required marks (`*`), helper text under the field, and
  inline error messages on invalid fields. Submit button stays disabled until
  valid. No rules/checklist/validation-status panel.
- **Record detail screen:** breadcrumb → header band (ID + status pill + action
  buttons with hard shadows) → meta grid (3-column label/value pairs in a cream
  panel) → related data sub-panels (status-board row pattern or mini-table).
- **Footer strip** (`border-top: 3px solid #000`, ink fill, paper text): monospace
  meta row (version, build, env) + coral-block link on the right.

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
Domain (illustrative): a creative studio project management tool.

Sidebar brand block    → studio name "Atelier Mosaic" + product name "Studio OS".
Nav items (6)          → > Dashboard  # Projects  * Clients  + Invoices  % Time Logs  @ Settings.
Active item            → Dashboard (lime fill).
Top bar                → "Dashboard" label + search slab ("Search projects, clients…") + "+ New" CTA + avatar "LC".

Stat tiles (4):
  • Projects Live   14  (▲ +3 this month)          — coral top accent
  • Billable Hours 382  (▲ +47 vs last month)       — lime top accent
  • Open Invoices   07  (▼ €42,500 outstanding)     — lavender top accent
  • Client NPS      72  (▲ +8 pts from Q1)          — yellow top accent

Records table (left)   → "Active Projects": Project / Client / Owner / Status pill / Due date.
  Status pills: Active (lime), In Review (coral), On Hold (yellow), Draft (lavender), Done (grey).
  Row: overdue due date shown in red bold with "!".

Activity feed (right)  → "Activity Feed · last 48h": stacked cards of
  [icon square] [event line] [sub-line (actor · context)] [timestamp].
  Icon fill colours rotate through lime / coral / yellow / lavender / cyan.

Footer                 → ink strip: "Studio OS v1.4.2 · Build #20240527 · ENV: production · © Atelier Mosaic 2024"
                         + "Support" in coral block on the right.

List screen            → all projects, cream search slab + filter chips (Status: All / Active / In Review /
                         On Hold / Draft / Done), paginated records table.

Form screen            → "New Project": client (required select), title (required text), owner (required select),
                         due date (required date, not in the past), priority (select), brief (textarea).
                         Rules as inline marks + helper text + inline errors; "Create Project" disabled until valid.

Detail screen          → one project: breadcrumb (Projects › Brand Identity Relaunch), header band
                         (project title + status pill + "Edit" CTA with hard shadow + "Archive" ghost),
                         meta grid (Client / Owner / Due Date / Priority / Created / Billable Hours),
                         "Linked Invoices" mini-table + "Activity" feed below.
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
5. ALL borders `2–3px solid #000`, ALL shadows `4px 4px 0 #000` (no blur),
   `border-radius: 0` everywhere; monospace type on all figures, labels, nav,
   buttons, and codes; single inline `<style>`, semantic HTML5, no external
   assets, no CDNs.

## Output contract

```
<artifact identifier="admin-neobrutal" type="text/html" title="Neobrutalist Admin">
<!doctype html>...</artifact>
```
