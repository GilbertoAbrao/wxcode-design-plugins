# Plugin Authoring Standard — aesthetic/semantic split

This is the contract every plugin in this repo must follow. It exists so a plugin
behaves correctly in **both** contexts it ships into:

- **Standalone Open Design** — there is no Knowledge Base; the plugin's example
  domain is a legitimate brief.
- **WXCode Design (embedded)** — the real product domain comes from the tenant
  Knowledge Base + the user's prompt; the plugin must contribute only its look
  and structure.

## The principle

- **Plugin = skin + skeleton.** Visual language (color, typography, tokens,
  density) AND structural archetype (navigation, grid, KPI tiles, status boards,
  data tables, component patterns). Authoritative for *how it looks and is laid out*.
- **KB + user prompt = semantics.** Domain, entities, screens, metrics, workflows,
  terminology. Authoritative for *what the product is*.

A plugin must never hard-code its example domain as the product domain. The
example is illustration and standalone fallback — never the authority.

## The `SKILL.md` format (two labeled layers)

```
---
name: <slug>
description: |
  <AESTHETIC ONLY — describe the look + the layout archetype. NO domain claims,
   NO "use when the brief mentions <industry>".>
triggers:
  - "<style / visual phrasings>"        # e.g. "dark industrial admin", "dense data terminal"
  # NOT domain phrasings ("mes dashboard", "oee dashboard", "production lines")
example_prompt: "Apply this <visual> admin aesthetic to my domain"
od:
  mode: <mode>
  surface: <surface>
  scenario: <scenario>
  preview: { type: html, entry: example.html }
  design_system: { requires: true, sections: [color, typography, layout, components] }
  craft: { requires: [<craft ids>] }
---

# <Name> — Visual Archetype

## Visual language        (AUTHORITATIVE)
Colors (as :root CSS custom properties), typography, density, radius, shadows,
motion. The non-negotiable look.

## Layout archetype       (AUTHORITATIVE, domain-neutral)
Regions + component patterns described generically, with NO domain nouns:
"top navbar (entity switcher + search + status badge), left icon rail, KPI tile
row (N tiles), 2-column grid: a status board (rows of [label][state pill][metric]
[progress][count]) + an alerts/side panel, a full-width records table with status
pills." Describe shapes, counts, and behaviors — not what they mean.

## Applying to a domain   (the contract)
"The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's entities, metrics, screens, and terminology and map them onto the
archetype above. If no KB/domain is supplied (standalone), use the Example
instantiation below."

## Example instantiation (illustrative only — NOT the domain)
> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent.

<the original domain-specific instantiation, fenced as illustrative>

## Output contract
<artifact identifier="<slug>" type="text/html" title="<Title>">...
```

## Example screens — ship a meta-free, theme-discovered set (up to 10)

A dashboard alone is not enough reference. With only one screen, the agent
improvises the rest (forms, lists) and pads them with invented "rules" /
"checklist" / build-status panels. Ship a small, meta-free example set so the
agent has a clean pattern to imitate for every screen type.

The example set is **not a fixed CRUD-4**. It is a **representative set of the
theme's page archetypes — intelligently selected, capped at 10 example HTML
files** — so the plugin reflects what the reference theme actually ships, not a
generic admin skeleton. Relevance over count: a focused theme that only ships a
dashboard + a couple of CRUD screens should ship exactly those; do NOT pad to 10.

- **CRUD-admin floor (still expected when the archetype is CRUD-admin):**
  a dashboard/overview + at least one list + one form + one detail, all in the
  plugin's visual language and layout archetype. This floor is the minimum for a
  CRUD-admin theme; the rest of the set is theme-discovered.
- **Add the archetypes the theme actually showcases (selected, not exhaustive):**
  - **Auth screens** — login, plus any register / forgot-password / lock screen
    the theme ships.
  - **Error / empty states** — any of 404 / 500 / maintenance / empty-state the
    theme ships (include at least one when present).
  - **Settings / profile** — account/settings/profile screens when the theme has
    them.
  - **Signature / showcase pages** — the theme's distinctive pages (e.g. an
    analytics board, a kanban, a calendar, a pricing/landing page) — whatever the
    theme leads with.
  - **RTL variant** — an RTL version of a key screen **only when the theme
    demonstrates RTL** (do not invent an RTL variant for an LTR-only theme).
- **Hard cap: 10 example HTML files per theme.** Selection is relevance-based.
  When the discovered inventory exceeds 10, keep the most representative subset
  (the CRUD-admin floor first, then login, an error state, settings, and the
  theme's signature pages) and drop the rest — never silently truncate; the
  harvest pipeline logs which pages were chosen vs skipped (see
  `pipeline/harvest.md`).
- **Where:** bundle them as `od.context.assets[]` (OD stages them into the run as
  reference) plus a `references/layouts.md` with paste-ready section/screen
  skeletons and an `assets/template.html` seed. `od.preview.entry` stays a single
  screen (the dashboard/overview) for the marketplace thumbnail;
  `od.useCase.exampleOutputs[]` lists the full discovered set. The manifest
  already allows arrays here (`manifest.ts`: `exampleOutputs`, `assets` are both
  arrays).
- **Rules as validation, not panels:** the example *form* must express domain
  rules as inline field validation — required marks, helper text, inline errors —
  NOT as a "rules"/"checklist" summary panel. This teaches the agent "a rule
  shapes a field, it is not UI content."
- **Meta-free everywhere:** no example screen may contain validation-status
  summaries, build/implementation notes, "depends on backend" caveats,
  todo/checklist panels, or designer/demo controls. The examples are finished
  product screens.
- **No theme/plugin name as brand:** the source THEME name
  (`od.provenance.template`, e.g. "Sneat"/"DarkPan"/"Kai Admin") and the plugin
  name/slug must NEVER appear on screen — `<title>`, brand/logo text, headers,
  `aria-label`s, or copy. Name the example product GENERICALLY ("Admin",
  "Console", a neutral domain placeholder). The linter enforces this via
  `od.provenance.template` (see rule 7).

These are reference context — the agent imitates the patterns and builds fresh
screens for the real domain; they are not injected verbatim into the output. This
complements the Phase 1 directive's anti-meta clause: the examples *show* the
clean pattern, the directive *forbids* the meta — together they kill the leak.

## Authority rules

1. **Visual language + Layout archetype are authoritative** regardless of context.
2. **Domain is authoritative from the KB + prompt** when present; otherwise from
   the Example instantiation (standalone fallback).
3. The **Workflow must not say "extract <domain fields> from the brief."** It says
   "extract THIS domain's equivalent of [archetype slots]." The archetype slots are
   domain-neutral (e.g. "primary-entity status rows", "key-metric tiles"), not
   "production lines" / "OEE".
4. **Frontmatter carries no domain semantics.** `description`, `triggers`, and
   `example_prompt` describe style, not industry. Domain words belong only inside
   the fenced Example instantiation.
5. **Ship a meta-free, theme-discovered example set** — a representative set of
   the theme's page archetypes (CRUD-admin floor of dashboard + list + form
   [+ detail] when relevant, plus auth / error-state / settings / signature /
   RTL screens the theme actually ships), intelligently selected and capped at
   **10** example HTML files. Relevance over count, never a single dashboard —
   see "Example screens" above.
6. **No build/design metadata as UI.** No example screen — and no output the plugin
   guides — may render rules/checklist/validation-status/build-note panels or
   designer/demo controls. Domain rules become inline field validation.
7. **No plugin/theme name as brand.** The harvested source THEME name
   (`od.provenance.template`) and the plugin name/slug must NEVER appear ON SCREEN —
   not in `<title>`, brand/logo text, page headers, `aria-label`s, or any visible
   copy. Name the example product GENERICALLY ("Admin", "Console", a neutral domain
   placeholder), never after the template/theme. `lint-plugin.mjs` enforces this:
   when `od.provenance.template` is set, the example HTML must not contain that name
   (any case, spaced or despaced).

## Worked example: `admin-forge-mes`

**Before (domain-coupled — the bug):**

- `description`: "Industrial dark-mode Manufacturing Execution System (MES)…
  OEE %, units output, downtime, scrap, production lines, work orders…"
- `triggers`: "mes dashboard", "oee dashboard", "production lines", "factory dashboard"
- Workflow step 2: "Extract from the brief: plant name, active shift, production
  lines, product codes, KPI targets for OEE / output / downtime / scrap, work-order list."

**After (aesthetic/semantic split):**

- `description`: "Dark industrial-grade admin aesthetic: near-black canvas
  (#0c0f14), orange accent (#f97316), dense tabular data; archetype = entity
  switcher navbar + icon rail + 4 KPI tiles + status board + alerts panel +
  full-width records table."
- `triggers`: "dark industrial admin", "dense data terminal", "near-black admin", "status-board dashboard"
- `example_prompt`: "Apply this dark industrial admin aesthetic to my domain"
- Workflow step 2: "Extract THIS domain's primary entities, key metrics, status
  states, and record list from the KB + prompt (standalone: use the Example below)."
- `## Example instantiation` fences the full MES layout (plant switcher, OEE tiles,
  production lines status board, work orders table) as illustrative-only.

Outcome: Forge MES + a school KB → a school admin dashboard in the dark/orange
Forge skin, with Aluno / Turma / professor content — not plant/lines/OEE.

## Lint (enforced by `forge/tools/lint-plugin`)

A plugin FAILS lint if any of these hold:

- `triggers` or `description` contain domain phrasings from the banned list
  (industry/domain nouns: `mes`, `oee`, `production line`, `work order`, `crypto`,
  `treasury`, … — list maintained in the linter), rather than style phrasings.
- The `SKILL.md` body is missing any of the four required headings:
  `## Visual language`, `## Layout archetype`, `## Applying to a domain`,
  `## Example instantiation`.
- `## Visual language` or `## Layout archetype` are not marked AUTHORITATIVE.
- The Workflow contains "extract … from the brief" with domain fields instead of
  the domain-neutral archetype-slot phrasing.
- `## Example instantiation` is not fenced/labeled as illustrative-only.
- The plugin ships only one example screen (no `references/layouts.md` and fewer
  than two screens in `assets/`) — a compliant admin plugin ships at least the
  CRUD-admin floor (dashboard + list + form), and richer themes ship up to 10
  theme-discovered screens. (Warn-level for now; promote to fail once the 40 are
  retrofitted.) The single-screen warning is the only count check: the lint does
  NOT require all 10 screens and does NOT warn on a focused set below 10 —
  relevance over count. The 10 is a hard *cap*, never a floor.
- Any example screen contains build/design metadata as UI — heuristic match on
  `/checklist|depends on (the )?backend|valida(ç|c)(ã|a)o ativa|regras ativas|build report|status de valida/i`
  in the example HTML.

The Phase 1 WXCode directive (prepended to the embed KB context) is a runtime
safety net for third-party or not-yet-migrated plugins; a compliant plugin must
not rely on it. The directive's anti-meta clause and rule 6 above are the same
contract enforced at two layers (runtime vs authoring).
