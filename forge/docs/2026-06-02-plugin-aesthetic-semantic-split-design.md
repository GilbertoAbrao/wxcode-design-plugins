# Plugin aesthetic/semantic split — design

Date: 2026-06-02
Status: design (approved sections 1–2 + generator home; pending full spec review)
Scope: WXCode-embedded Open Design ("Design" tab). Cross-repo.

## Problem

In WXCode Design the user picks a visual plugin (e.g. "Forge MES Admin") and the
real product domain comes from the tenant Knowledge Base (KB) + the user's prompt
(e.g. a school: Aluno / Turma / professor). Today the plugin's `SKILL.md` carries
its **domain semantics** as well as its visual identity, so the agent briefs and
generates the plugin's *example* domain (manufacturing / MES — plant name, lines,
OEE, work orders) instead of the user's domain.

Root cause is structural, confirmed by reading
`wxcode-design-plugins/plugins/admin-forge-mes/SKILL.md`:

- Frontmatter (`description`, `triggers`, `example_prompt`, tags) is pure MES.
- `## Workflow` step 2 literally says *"Extract from the brief: plant name, active
  shift, production lines, product codes, KPI targets for OEE / output / downtime /
  scrap, work-order list."* — this is what drives the MES briefing questions.
- Layout/components interleave aesthetic and semantics (`OEE % gauge-circle SVG,
  big number in orange` — the gauge+orange is aesthetic, the OEE is semantics).

The KB digest is already injected into the agent's system prompt via
`project.customInstructions` (see `wxcode-od-plugin-and-kb-wiring` memory), but it
is descriptive, not directive, so the plugin's `SKILL.md` wins.

## Principle

In WXCode Design:

- **Plugin = skin + skeleton.** Visual language (color, typography, tokens,
  density) AND structural archetype (navigation, grid, KPI tiles, status boards,
  data tables, component patterns). Authoritative for *how it looks and is laid
  out*.
- **KB + user prompt = semantics.** Domain, entities, screens, metrics, workflows,
  terminology. Authoritative for *what the product is*.

Standalone Open Design is unchanged: with no KB, the plugin's example domain is a
legitimate brief. We must not break that dual use.

## Approach (chosen: C — hybrid)

Two phases. Phase 1 fixes the live leak across all 40 plugins immediately with no
plugin regeneration. Phase 2 makes the plugin prompts themselves clean and durable,
and consolidates the generator into a versioned, runtime-neutral authoring toolkit.

---

## Phase 1 — WXCode directive preamble (immediate fix)

**Where.** Prepend an authoritative directive in the embed-specific endpoint
`GET /api/v1/internal/designs/kb-context`
(`src/wxcode/api/internal_design_kb_context.py`), NOT in the generic renderer
`src/wxcode/services/open_design_kb_context.py` (that service is also used by
other callers such as `write_open_design_kb_context`, so the directive must not
leak into them). The endpoint renders the digest at a reduced budget and prepends
the directive. It rides the existing channel: `?kbContext=` → OD
`resolveEmbedKbContext` → `project.customInstructions` → `composeSystemPrompt`
"## Custom instructions (project-level)". It only fires when the shell injects
(embed), so standalone OD is untouched and **no OD rebuild is needed** — only a
wxcode backend deploy + tenant rollout.

**Directive text (authoritative preamble, ~700 bytes):**

```
PRODUCT DOMAIN — AUTHORITATIVE
The product is defined by the Knowledge Base below + the user's prompt. THIS is
the domain: its entities, screens, metrics, workflows, terminology.

The selected visual plugin is an AESTHETIC + LAYOUT template ONLY. Use it for
visual language (color, type, spacing, density) and structural archetype
(navigation, grid, component patterns). IGNORE the plugin's example domain
(e.g. manufacturing/MES, finance, crypto) entirely — in the briefing AND in
generation. Do NOT ask questions about the plugin's example domain. Map every
plugin structure onto THIS domain: a "production lines status board" becomes a
status board for this domain's primary entities; example KPI tiles become this
domain's key metrics. When briefing, ask only about THIS domain.
```

**Byte budget.** The `kbContext` param is capped at 3000 bytes (nginx request-line
limit + OD's 5000-char `customInstructions` cap). The preamble (~700 B) must fit
inside that ceiling, so reduce the KB digest cap from 3000 → ~2300 (`KB_CONTEXT_MAX_BYTES`
in `internal_design_kb_context.py` / the `max_bytes` passed to the renderer) so
preamble + digest ≤ 3000. The school digest fits comfortably in 2300.

**Behavioral target.** Forge MES + school KB → a school admin dashboard rendered in
the Forge dark/orange visual language; the briefing asks about school entities
(Aluno / Turma / professor), not plant/lines/OEE.

**Surface-area note.** This rides the existing embed launch path; no new UI/CLI
surface. The CLI dual-track rule does not apply (internal embed transport, not a
user-facing OD capability).

---

## Phase 2 — Two-layer plugin standard + portable generator

### 2a. The `SKILL.md` standard (two labeled layers)

Replace the domain-coupled `SKILL.md` shape with a standard format whose authority
is explicit:

```
---
name: admin-forge-mes
description: <AESTHETIC ONLY> "Dark industrial-grade admin aesthetic: near-black
  canvas, orange accent, dense tabular data; status-board + KPI-tile + work-table
  archetype." (no "MES / manufacturing / use when brief mentions OEE")
triggers: [<style/visual phrasings, NOT domain phrasings>]
example_prompt: "Apply this dark industrial admin aesthetic to my domain"
---

# <Name> — Visual Archetype

## Visual language        (AUTHORITATIVE)
colors, typography, density, radius, tokens.

## Layout archetype       (AUTHORITATIVE, domain-neutral)
regions + component patterns described generically:
"status board: N rows, each [label][state pill][metric][progress][count]".

## Applying to a domain   (the contract)
"The domain comes from the KB + user prompt. Extract THIS domain's entities,
metrics, screens, and terminology, and map them onto the archetype above."

## Example instantiation (illustrative only — NOT the domain)
the MES example, clearly fenced as "one example; replace entirely".

## Output contract
<artifact ...>
```

**Dual-use mechanism.** The example domain becomes the **standalone fallback** AND
the illustration — never the authority. Standalone OD (no KB) falls back to the
example; WXCode (KB present) routes to the real domain via the Phase 1 preamble +
the "Applying to a domain" section. This is the elegant part: one format serves
both contexts.

**Frontmatter.** Strip domain `description` / `triggers` / `example_prompt` (they
biased plugin selection and seeded the MES briefing); keep style triggers.

### 2b. Consolidate the generator into a versioned, runtime-neutral toolkit

The generators exist today only as personal Claude Code skills
(`~/.claude/skills/od-plugin-forge`, `~/.claude/skills/wxcode-template-harvest`).
`od-plugin-forge` §3 (build subagent template) is the source of truth for plugin
anatomy and is where the domain coupling is born (`## Workflow → 2. <extract domain
inputs from brief>`).

**Home (one place):** `wxcode-design-plugins` becomes acervo + toolkit. It is
already versioned and already the marketplace output target.

**Runtime-neutral split** (so any coder runtime — Claude Code, opencode, codex,
gemini — can drive it, manually triggered by the user):

- **Deterministic code** (`tools/`, any runtime shells out): brief-flag parsing,
  slug derivation, JSON/HTML verify, catalog regeneration (existing
  `regen-catalog.py`), `extract-tokens` (harvest), git pre-flight/commit/push
  safety, and a NEW `lint-plugin` that enforces the 2a standard (no domain triggers
  in frontmatter; the labeled sections present; the example fenced as illustrative).
- **LLM orchestration spec** (runtime-neutral markdown, e.g. `PIPELINE.md` for
  forge + `HARVEST.md`): the current `SKILL.md` bodies, expressed without
  Claude-only tool names where possible, with a tool-mapping note for runtimes that
  differ. Describes the research / curate / build / enrichment / distill phases that
  genuinely need an agent; each runtime maps "dispatch N subagents" to its own
  mechanism.
- **Authoring standard** (`AUTHORING.md`): the 2a two-layer format, the source the
  build phase must emit.
- **Adapters** (`adapters/claude/`): a thin `SKILL.md` shim that points to
  `../PIPELINE.md`, symlinked into `~/.claude/skills/` so `/od-plugin-forge` keeps
  working. Other runtimes get an adapter when needed.

**Ownership split.** The `open-design.json` *schema* stays owned by open-design
(`packages/contracts/src/plugins/manifest.ts` is source of truth). The *authoring
convention* (the aesthetic/semantic `SKILL.md` split) is owned by
`wxcode-design-plugins`. No conflict.

**Generator change that matters:** update the build template (formerly forge §3,
now in `PIPELINE.md`) to emit the 2a standard — replacing `## Workflow → 2. extract
domain inputs from brief` with the four labeled sections and the illustrative-only
example.

### 2c. Retrofit the 40 existing plugins

Transform every `wxcode-design-plugins/plugins/admin-*/SKILL.md` to the 2a standard
(separate aesthetic from domain; relabel the domain block as illustrative; clean
frontmatter). Implementation will be a fan-out (one agent per plugin) gated by the
new `lint-plugin`. Regenerate the catalog and bump versions afterward. Not part of
this design's first implementation slice — see "Out of scope / staging".

### Relationship to Phase 1

Once Phase 2 lands, the Phase 1 preamble becomes a belt-and-suspenders safety net —
still valuable for third-party or not-yet-migrated plugins — and stays.

---

## Rollout & verification

- **Phase 1:** wxcode backend deploy + tenant rollout (no OD rebuild). Verify on the
  tenant: a fresh Forge MES + school KB run briefs about the school domain (Aluno /
  Turma), and the generated dashboard uses Forge's dark/orange visual language with
  school content. Check the run's first turn (`events.jsonl`) / the project
  `custom_instructions` in `app.sqlite` carries the preamble + digest.
- **Phase 2 (generator + standard):** `lint-plugin` passes on a hand-migrated pilot
  plugin (forge-mes); a forge run with the updated `PIPELINE.md` produces a
  standard-compliant plugin; standalone OD still generates the example domain when no
  KB is present.
- **Phase 2c (retrofit):** all 40 pass `lint-plugin`; catalog regenerated; spot-check
  one migrated plugin standalone (example fallback) and in WXCode (real domain).

## Out of scope / staging

- The 40-plugin retrofit (2c) is staged after the standard + generator + lint land
  and are validated on a pilot. First implementation slice = Phase 1 + Phase 2a/2b
  (standard, toolkit consolidation, lint, generator update) + pilot-migrate forge-mes.
- Turning forge/harvest into an `od` capability (CLI + HTTP) is explicitly NOT this
  work; the chosen target is a portable authoring toolkit the user triggers manually.
- No changes to the OD daemon prompt composition or the embed transport beyond the
  Phase 1 byte-budget cap reduction.

## Open question carried to review

Keep the example domain as standalone fallback (chosen here), versus stripping
domain entirely from plugins (standalone loses quality). This design keeps the
example as fallback; flag on review if you prefer a hard strip.
