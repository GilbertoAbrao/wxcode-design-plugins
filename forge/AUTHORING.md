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

## Example screens — ship a meta-free CRUD set (not just a dashboard)

A dashboard alone is not enough reference. With only one screen, the agent
improvises the rest (forms, lists) and pads them with invented "rules" /
"checklist" / build-status panels. Ship a small, meta-free example set so the
agent has a clean pattern to imitate for every screen type.

- **Minimum set:** dashboard + list + form (+ detail when the archetype implies
  one), all in the plugin's visual language and layout archetype.
- **Where:** bundle them as `od.context.assets[]` (OD stages them into the run as
  reference) plus a `references/layouts.md` with paste-ready section/screen
  skeletons and an `assets/template.html` seed. `od.preview.entry` stays a single
  screen for the marketplace thumbnail; `od.useCase.exampleOutputs[]` lists the
  set. The manifest already allows arrays here (`manifest.ts`: `exampleOutputs`,
  `assets` are both arrays).
- **Rules as validation, not panels:** the example *form* must express domain
  rules as inline field validation — required marks, helper text, inline errors —
  NOT as a "rules"/"checklist" summary panel. This teaches the agent "a rule
  shapes a field, it is not UI content."
- **Meta-free everywhere:** no example screen may contain validation-status
  summaries, build/implementation notes, "depends on backend" caveats,
  todo/checklist panels, or designer/demo controls. The examples are finished
  product screens.

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
5. **Ship a meta-free multi-screen example set** (dashboard + list + form
   [+ detail]), not a single dashboard — see "Example screens" above.
6. **No build/design metadata as UI.** No example screen — and no output the plugin
   guides — may render rules/checklist/validation-status/build-note panels or
   designer/demo controls. Domain rules become inline field validation.

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
  than two screens in `assets/`) — a compliant admin plugin ships the CRUD set
  (dashboard + list + form). (Warn-level for now; promote to fail once the 40 are
  retrofitted.)
- Any example screen contains build/design metadata as UI — heuristic match on
  `/checklist|depends on (the )?backend|valida(ç|c)(ã|a)o ativa|regras ativas|build report|status de valida/i`
  in the example HTML.

The Phase 1 WXCode directive (prepended to the embed KB context) is a runtime
safety net for third-party or not-yet-migrated plugins; a compliant plugin must
not rely on it. The directive's anti-meta clause and rule 6 above are the same
contract enforced at two layers (runtime vs authoring).
