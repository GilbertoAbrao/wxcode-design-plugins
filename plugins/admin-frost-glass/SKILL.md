---
name: admin-frost-glass
description: |
  Glassmorphism admin aesthetic: deep indigo-violet-teal radial gradient canvas,
  frosted translucent panels (backdrop-filter blur, 1px rgba white borders,
  0 8px 32px rgba-black shadow), cyan (#22d3ee) and violet (#a78bfa) dual-accent
  system, near-white text on dark surfaces. Archetype = full-width glass sidebar
  (brand mark + labeled nav sections) + glass topbar (breadcrumb + frosted search
  + icon actions + avatar) + 4 glass KPI tiles with inline SVG sparklines + delta
  chips + 2-column grid (area/line chart card with period tabs and legend + live
  alerts side panel) + full-width glass records table with status pills, plus
  matching list, form, and detail screens.
triggers:
  - "glassmorphism admin"
  - "frosted glass admin"
  - "dark gradient dashboard"
  - "glass ui analytics"
  - "frost glass"
  - "dark premium dashboard"
  - "futuristic analytics"
  - "painel escuro translucido"
  - "cyan violet dark admin"
  - "blur panel admin"
example_prompt: "Apply this glassmorphism admin aesthetic to my domain"
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

# Frost Glass Admin — Visual Archetype

This plugin contributes a **look** (deep gradient canvas, frosted glass panels,
cyan/violet dual-accent, translucent surfaces with blur) and a **structure**
(glass sidebar + topbar + KPI tiles + chart + alerts panel + records table, plus
list / form / detail screens). It does **not** contribute a domain — the subject
matter comes from the Knowledge Base and the user's prompt. Treat the example
below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Every chromatic value is a `:root` CSS custom property.

- **Canvas:** `background: radial-gradient(ellipse at 65% 15%, var(--grad-b) 0%,
  var(--grad-a) 45%, var(--grad-c) 70%, var(--grad-d) 100%) fixed` covering
  100vh. Gradient stops: `--grad-a: #0f0c29`, `--grad-b: #1a0533`,
  `--grad-c: #0d2137`, `--grad-d: #0c2a3a`.
- **Glass surfaces:** `--glass-bg: rgba(255,255,255,0.06)`;
  `--glass-bg-hover: rgba(255,255,255,0.10)`;
  `--glass-border: rgba(255,255,255,0.12)`;
  `--glass-shadow: 0 8px 32px rgba(0,0,0,0.36)`;
  `--glass-blur: blur(16px)`. Every panel uses
  `background: var(--glass-bg); backdrop-filter: var(--glass-blur);
  border: 1px solid var(--glass-border); box-shadow: var(--glass-shadow)`.
- **Accent system:** `--accent-cyan: #22d3ee`; `--accent-cyan-dim: #0891b2`;
  `--accent-violet: #a78bfa`; `--accent-violet-dim: #7c3aed`;
  `--accent-rose: #f472b6`; `--accent-emerald: #34d399`; `--accent-amber: #fbbf24`.
- **Chart series:** `--chart-1: #22d3ee`; `--chart-2: #a78bfa`;
  `--chart-3: #34d399`; `--chart-4: #fbbf24`.
- **Text ramp:** `--text-primary: rgba(255,255,255,0.95)`;
  `--text-muted: rgba(255,255,255,0.50)`; `--text-faint: rgba(255,255,255,0.28)`.
- **Status pills:** emerald background `rgba(52,211,153,0.14)` + emerald text for
  active/running; amber `rgba(251,191,36,0.14)` + amber for pending/warning;
  rose `rgba(244,114,182,0.14)` + rose for critical/error; violet
  `rgba(167,139,250,0.14)` + violet for info/scheduled.
- **Delta chips:** `rgba(52,211,153,0.14)` / emerald text for up; rose tint / rose
  text for down.
- **Typography:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`.
  Base 14px. KPI figures 28px / weight 700 / `letter-spacing: -0.03em`. Section
  micro-labels 10px / weight 600 / `text-transform: uppercase` /
  `letter-spacing: 0.1em` / muted. Sidebar nav items 13px / weight 500.
- **Radius:** panel `--radius: 14px`; controls / pills `--radius-sm: 8px`;
  round elements (avatar, dot) use `border-radius: 50%`; pill chips `99px`.
- **Active nav:** `border-left: 2px solid var(--accent-cyan)`;
  `color: var(--accent-cyan)`; `background: rgba(34,211,238,0.08)`;
  `text-shadow: 0 0 12px rgba(34,211,238,0.4)`.
- **Motion:** `.12s–.15s` ease for background/border/color hover transitions.
  Primary button glow `0 0 16px rgba(34,211,238,0.3)` lifts to
  `0 0 24px rgba(34,211,238,0.5)` on hover. Period-tab active state uses
  `background: var(--accent-cyan); color: #0f0c29`. No bouncy motion.
- **Scrollbar:** 6px, `rgba(255,255,255,0.14)` thumb, transparent track, 99px radius.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns, described by shape and behavior — not meaning.

- **Glass sidebar** (220px, glass surface, `border-right: 1px solid
  var(--glass-border)`, sticky): brand mark (inline SVG glyph + wordmark +
  sub-label) at top → labeled section groups (`nav-section-label`) → nav items
  each with inline SVG icon + label, active item gets left-2px-cyan bar + cyan
  glow; optional badge chip on item right edge → user pill at bottom
  (avatar gradient + name + role).
- **Glass topbar** (60px, glass surface, `border-bottom: 1px solid
  var(--glass-border)`): breadcrumb path (muted / active) on left → centered
  frosted pill search input (magnifier icon, focus lifts border to cyan-alpha) →
  icon buttons (notification with rose dot, secondary action) + avatar on right.
- **Greeting / page header**: bold name greeting + muted date-and-scope line on
  left; ghost export button + cyan primary action button on right.
- **4 glass KPI tiles** (equal grid): each card has — small accent dot top-right,
  uppercase muted label, large near-white figure, inline SVG sparkline with
  gradient area fill, delta chip (emerald or rose). Cards use glass surface tokens.
- **2-column grid (2fr / 1fr)**:
  - **Left — primary chart card:** title + period-tab strip (1H / 24H / 7D / 30D,
    active tab cyan fill) + legend row (dot + label pairs) + inline SVG area/line
    chart (multiple series, `<linearGradient>` area fills, rgba grid lines).
  - **Right — live alerts / side panel:** panel title + "View all" link + alert rows
    each `[accent-color dot] [message with <strong> entity] [elapsed time]`.
- **Full-width glass records table**: title + "View all" link in header; sticky
  uppercase faint-text `<th>` row; dense rows with entity cell (icon chip + name +
  sub), category/dim cells, numeric cells, status pill; hover row lifts to
  `--glass-bg-hover`. No footer pager in dashboard view.
- **Records list screen:** toolbar (frosted search pill + filter chips with count
  badges + result count) above the full records table with pager footer.
- **Record form screen:** sectioned glass cards of labeled fields; **rules appear
  as inline validation** — required marks (`*`), helper text under the field, and
  inline error messages on invalid fields with warning icon; primary submit
  disabled-until-valid. No rules/checklist/validation-status panel.
- **Record detail screen:** breadcrumb → detail header band (ID chip + status pill
  + key actions) → glass meta-grid card (label/value pairs in 3 columns) → two
  related-data panels below (sub-table or activity feed).

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
Domain (illustrative): a cloud infrastructure operations platform.

Brand / wordmark     → "Aurorix · Ops Center".
Sidebar sections     → Main (Overview, Analytics, Telemetry, Regions),
                        Manage (Clients, Security, Pipelines), Settings (Configuration).
Topbar breadcrumb    → Aurorix / Overview.
Search placeholder   → "Search metrics, events, clients…"

KPI tiles (4):
  • Throughput/s 84.7K (cyan dot, ▲+12.4%, sparkline rising).
  • Active Nodes 1,248 (violet dot, ▲+6.1%, sparkline stable-rising).
  • Error Rate 0.18% (rose dot, ▼+0.04% worsening, sparkline rising = bad).
  • Avg Latency 38 ms (emerald dot, ▲−8.2% improving, sparkline falling).

Chart (left)         → "Event Throughput" area chart — 3 series:
                        Ingested (cyan), Processed (violet), Dropped (rose dashed).
Alerts panel (right) → "Live Alerts" — 6 rows:
  [rose]    eu-2-k8s-14 memory at 91%      — just now
  [amber]   ingest-raw pipeline lagging    — 2 min ago
  [cyan]    autoscale on ap-east-1         — 7 min ago
  [emerald] certificate renewed            — 12 min ago
  [amber]   disk IOPS spike pg-replica-7   — 18 min ago
  [violet]  deployment v4.11.2 rolled out  — 31 min ago

Records table        → "Active Pipelines": Pipeline / Source / Events per min /
                        Lag / Region / Status pill (Active / Lagging / Critical / Warming).

List screen          → all pipelines, search + filter chips (status, region), paginated.

Form screen          → "New Pipeline": name (required), source endpoint (required),
                        destination (required select), region (required select),
                        max throughput (required, > 0), schedule (optional).
                        Rules shown as required marks + helper text + inline errors;
                        "Create Pipeline" disabled until valid.

Detail screen        → one pipeline: header (pipeline ID + status pill + actions),
                        meta grid (source, destination, region, throughput, lag, owner,
                        created), and a "Recent Events" sub-table + activity feed.
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
   All chromatic colors via `var(--token)`; neutral rgba glass surfaces may stay inline.

## Output contract

```
<artifact identifier="admin-frost-glass" type="text/html" title="Frost Glass Admin">
<!doctype html>...</artifact>
```
