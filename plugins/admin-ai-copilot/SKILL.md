---
name: admin-ai-copilot
description: |
  Split-pane admin aesthetic: deep-navy canvas (#0f1419), indigo accent
  (#6366f1) for actives and agent chrome, pink (#ec4899) for avatar and
  notification dots, subtle card surfaces (#1a2332), hairline borders
  (rgba(255,255,255,0.06)), and 13px compact type on system-ui.
  Archetype = top bar with centered Cmd+K pill + 64px icon-only nav rail
  + scrollable widget canvas (KPI tiles × 4 + area-chart card + records
  table) + 380px right copilot rail (header · thread · composer) + 32px
  bottom status bar (agent state · cost · latency · model chip).
triggers:
  - "split-pane copilot admin"
  - "permanent agent rail"
  - "cmd-k admin dashboard"
  - "indigo navy admin"
  - "agentic split layout"
  - "tool-call card ui"
  - "dark navy conversational admin"
example_prompt: "Apply this split-pane indigo-navy admin aesthetic to my domain"
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
    requires: [state-coverage, laws-of-ux]
---

# AI Copilot Admin — Visual Archetype

This plugin contributes a **look** (deep navy, indigo + pink accent, compact
system-ui type) and a **structure** (Cmd+K top bar + icon rail + widget canvas +
permanent right copilot rail + bottom status bar, plus list / form / detail
screens). It does **not** contribute a domain — the subject matter comes from the
Knowledge Base and the user's prompt. Treat the example below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Every chromatic value as a `:root` CSS custom property.

- **Canvas / surfaces:** page `#0f1419`; rail / header `#111922`; card `#1a2332`;
  card hover `#1f2b3e`; hairline border `rgba(255,255,255,0.06)`;
  stronger border `rgba(255,255,255,0.1)`.
- **Text ramp:** primary `#f1f5f9`, secondary `#94a3b8`, muted `#64748b`.
- **Accent:** `--indigo: #6366f1`; `--indigo-dim: rgba(99,102,241,0.15)`;
  `--indigo-mid: rgba(99,102,241,0.25)`. Active nav items, agent chrome,
  user-message bubbles, interactive focus rings, tool-call card left bar.
- **Secondary accent:** `--pink: #ec4899`; `--pink-dim: rgba(236,72,153,0.15)`.
  Copilot avatar gradient, notification dots, brand-icon gradient.
- **State tokens:** `--green: #22c55e`, `--yellow: #f59e0b`, `--red: #ef4444`.
  Status LEDs, status pills (12–14% alpha tint backgrounds), delta chips.
- **Typography:** `-apple-system, BlinkMacSystemFont, "Segoe UI", system-ui,
  sans-serif`. Base 13px / line-height 1.5. Uppercase micro-labels 10px /
  `letter-spacing 0.07–0.08em` / weight 600, muted. Big KPI figures 26px /
  weight 700 / `letter-spacing -0.03em`. IDs and function names in monospace.
- **Density & radius:** 13px base, 10px micro; cards 12px radius, controls 8px,
  pills 20px (fully rounded). 12–16px panel padding. 12px grid gaps.
- **Borders & shadows:** 1px hairlines do all separation; no drop shadows on cards
  (flat terminal feel). Status bar 1px hairline only.
- **Motion:** `.10s–.15s` hover transitions on background / border-color; no bounce.
  Copilot status dot pulses at 2s. Progress / width transitions at `.4s ease`.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns described by shape and behavior — not meaning.

- **Top bar** (56px, rail-bg, 1px bottom border, sticky, z-index 10):
  brand icon + wordmark → breadcrumb → **centered Cmd+K pill** (flex-1,
  max-width 480px, placeholder text + `⌘K` keyboard chip, hover lifts to
  indigo-dim) → notification icon button (with pink dot) → avatar circle.
- **Left icon rail** (64px, rail-bg, 1px right border): 6–7 icon-only nav items
  (active = indigo-dim bg + indigo color + inset 1px indigo/30 ring; hover =
  white/5 bg; each carries a `title` tooltip), flex spacer, settings item pinned
  to bottom.
- **Center canvas** (flex-1, page-bg, 24px padding, vertical scroll, 20px gap):
  page greeting (h1 + subtitle), then region stack below.
  - **KPI tile row** (4-column grid, 12px gap): each tile = card with 2px top
    accent stripe (indigo / red / green / yellow by state), uppercase 10px label,
    26px tabular figure, delta chip (green up / red down), sub-line in muted.
  - **Chart card** (full-width): card-header with title + meta + period chips, an
    optional legend row, then an inline SVG area-chart (gridlines + axis labels +
    area-fill gradient + polyline stroke + highlight dot/annotation). Self-contained.
  - **Records table** (full-width): card-header with title + meta + filter chip,
    sticky uppercase 10px header, dense rows (10px vertical padding) with status
    pills, mono ID column, right-aligned numerics, footer with count + pager.
- **Right copilot rail** (380px, flex-shrink 0, rail-bg, 1px left border, flex column):
  - **Header** (sticky, 1px bottom border): agent avatar circle (gradient,
    status dot at bottom-right), label chip (uppercase, indigo color), agent name,
    model chip (indigo-dim pill).
  - **Thread** (flex-1, overflow-y auto, 16px padding, 14px gap): alternating
    user messages (right-aligned, indigo-dim bubble) and agent messages (left,
    card bubble). Agent turns may include:
    - **Tool-call card**: indigo left-bar card showing function name (mono, indigo),
      status badge (green, rounded), collapsed args (mono, muted), result line.
    - **Inline artifact**: card with uppercase 9px label + inline SVG chart.
    - **Suggestion chip row**: pill chips that hover to indigo-dim.
  - **Composer** (sticky bottom, 1px top border, 12px padding): tool-chip row
    above the input row; textarea (36px, indigo focus ring) + send button (indigo
    fill, white arrow icon).
- **Bottom status bar** (32px, rail-bg, 1px top border, flex row, 20px gap):
  LED dot + agent state label | separator | cost figure | separator | latency |
  spacer | context count | separator | model chip (indigo-dim pill).
- **Records list screen:** search-pill toolbar + filter chips + count, then the
  records-table archetype as its own page, paged.
- **Record form screen:** sectioned cards of labeled fields; **rules appear as
  inline validation** — required marks (`*`), helper text beneath the field, and
  inline error messages on invalid fields; primary submit disabled-until-valid.
  No rules/checklist/validation-status panel.
- **Record detail screen:** breadcrumb → header band (entity ID + status pill +
  key actions), meta-grid of label/value pairs, then related-data sub-panels
  (thread excerpt or mini-table + activity feed) below.

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key metrics,
status states, record list columns, form fields and their rules, detail fields,
copilot thread topics, tool names, and suggestion chip labels — and map them onto
the archetype above. If no KB/domain is supplied (standalone), use the Example
instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules
become inline field validation. Do NOT render build/implementation notes or
designer controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent
> (entities, metrics, states, columns, fields, tool names) drawn from the KB + prompt.

```
Domain (illustrative): a cloud-operations cockpit.

Brand / wordmark     → "NORTHWIND".
Breadcrumb           → Cloud Ops / Overview.
Cmd+K placeholder    → "Ask Pilot or jump to a deploy, host, or incident".
Rail items           → Overview, Deploys, Hosts, Incidents, Costs, Audit, (Settings).

KPI tiles (4):
  • Healthy Hosts 1,284  (98.6% of 1,302 total · green stripe).
  • Open Incidents 3     (−2 vs yesterday · red stripe, red figure).
  • Today Deploys 18     (+4 vs yesterday · indigo stripe).
  • Avg MTTR 12m         (−3m 7-day avg · green stripe).

Chart card           → "24-Hour p99 Latency" — area-chart (last 24h, 10-min buckets),
  indigo polyline + gradient fill, pink spike annotation ("842ms peak").

Records table        → "Host Fleet — Live": Host ID / Region / Fleet /
  CPU / Mem / Last Deploy / Status pill (Healthy · Degraded · Down).

Copilot thread:
  User: "Which fleet is driving the p99 spike right now?"
  Agent: narrative + tool-call card (query_latency_by_fleet, 218ms, 6 rows)
         + inline bar-chart artifact (p99 by Fleet — last 15m)
         + chips: "Roll back checkout-api-eu" / "Open incident" / "Page on-call".

Status bar           → Pilot · idle | $0.043 today | p50 1.2s | 3 incidents open | sonnet-4-6.

List screen          → all hosts, search pill, filter chips (status, region), paginated.

Form screen          → "Add Host": host ID (required), region (required select),
  fleet (required), instance type, tags. Rules as required marks + helper text +
  inline errors; "Add Host" disabled until valid.

Detail screen        → one host: breadcrumb → header (host ID + status pill + actions),
  meta grid (region, fleet, CPU, mem, last deploy, created), sub-panels
  (deploy history rows + alert log).
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual
   language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities,
   key metrics, status states, record columns, form fields + rules, detail fields,
   copilot tool names, thread topics, and suggestion chip labels — from the KB +
   prompt. Standalone: use the Example instantiation above.
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
<artifact identifier="admin-ai-copilot" type="text/html" title="AI Copilot Admin">
<!doctype html>...</artifact>
```
