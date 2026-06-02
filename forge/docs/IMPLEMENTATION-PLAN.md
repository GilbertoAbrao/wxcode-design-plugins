# Phase 2 — Plugin authoring toolkit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Stand up `forge/` as a versioned, runtime-neutral authoring toolkit that emits and enforces the aesthetic/semantic plugin standard, then pilot-migrate `admin-forge-mes` to it.

**Architecture:** Deterministic code in `forge/tools/` (any runtime shells out), runtime-neutral LLM specs in `forge/pipeline/`, a thin Claude adapter in `forge/adapters/claude/`. The standard is `forge/AUTHORING.md`; the linter enforces it. Source for the spec ports is the existing Claude skills `~/.claude/skills/od-plugin-forge/SKILL.md` and `~/.claude/skills/wxcode-template-harvest/SKILL.md`.

**Tech Stack:** Node ≥18 (`.mjs`, `node --test`) for the linter; Python 3 (stdlib only) for catalog regen; Markdown for the standard + pipeline specs. Repo: `~/projetos/wxk/wxcode-design-plugins`, branch `feat/forge-toolkit`.

**Already landed in this scaffold:** `forge/AUTHORING.md` (the standard), `forge/README.md`, `forge/docs/<design>.md`, and the empty `pipeline/ tools/ adapters/claude/` skeleton.

---

## Task 1: `lint-plugin` — enforce the standard (TDD, deterministic)

**Files:**
- Create: `forge/tools/lint-plugin.mjs`
- Test: `forge/tools/lint-plugin.test.mjs`

The linter reads a plugin dir (`<dir>/SKILL.md` + `<dir>/open-design.json`) and
returns `{ ok: boolean, violations: string[] }`. Rules come from `AUTHORING.md`
("Lint" section). It must be a pure function (`lintPlugin(skillMd, manifestJson)`)
plus a thin CLI wrapper (`node lint-plugin.mjs <plugin-dir>` → exit 1 on violations).

- [ ] **Step 1: Write the failing tests**

```js
// forge/tools/lint-plugin.test.mjs
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { lintPlugin } from './lint-plugin.mjs';

const COMPLIANT = `---
name: admin-x
description: |
  Dark industrial-grade admin aesthetic; archetype = navbar + icon rail + KPI tiles + status board + records table.
triggers:
  - "dark industrial admin"
  - "dense data terminal"
example_prompt: "Apply this dark industrial admin aesthetic to my domain"
---
# X — Visual Archetype
## Visual language        (AUTHORITATIVE)
tokens...
## Layout archetype       (AUTHORITATIVE, domain-neutral)
navbar, rail, KPI tiles...
## Applying to a domain   (the contract)
Extract THIS domain's primary entities and key metrics from the KB + prompt.
## Example instantiation (illustrative only — NOT the domain)
> Illustrative only; replace every label with the real domain.
MES example...
## Output contract
<artifact...>
`;

test('compliant plugin passes', () => {
  const r = lintPlugin(COMPLIANT, { description: 'Dark industrial admin aesthetic.' });
  assert.equal(r.ok, true, r.violations.join('; '));
});

test('domain triggers fail', () => {
  const bad = COMPLIANT.replace('"dark industrial admin"', '"mes dashboard"')
                       .replace('"dense data terminal"', '"oee dashboard"');
  const r = lintPlugin(bad, { description: 'Dark industrial admin aesthetic.' });
  assert.equal(r.ok, false);
  assert.ok(r.violations.some(v => /trigger/i.test(v) && /mes|oee/i.test(v)));
});

test('missing required heading fails', () => {
  const bad = COMPLIANT.replace('## Applying to a domain   (the contract)', '## Notes');
  const r = lintPlugin(bad, { description: 'Dark industrial admin aesthetic.' });
  assert.equal(r.ok, false);
  assert.ok(r.violations.some(v => /Applying to a domain/.test(v)));
});

test('authoritative markers required', () => {
  const bad = COMPLIANT.replace('## Visual language        (AUTHORITATIVE)', '## Visual language');
  const r = lintPlugin(bad, { description: 'Dark industrial admin aesthetic.' });
  assert.equal(r.ok, false);
  assert.ok(r.violations.some(v => /AUTHORITATIVE/i.test(v)));
});

test('domain extraction in workflow fails', () => {
  const bad = COMPLIANT.replace(
    "Extract THIS domain's primary entities and key metrics from the KB + prompt.",
    'Extract from the brief: plant name, production lines, OEE targets, work-order list.'
  );
  const r = lintPlugin(bad, { description: 'Dark industrial admin aesthetic.' });
  assert.equal(r.ok, false);
  assert.ok(r.violations.some(v => /extract.*brief/i.test(v)));
});

test('domain words in manifest description fail', () => {
  const r = lintPlugin(COMPLIANT, { description: 'Manufacturing Execution System for OEE and production lines.' });
  assert.equal(r.ok, false);
  assert.ok(r.violations.some(v => /description/i.test(v)));
});

test('build-meta in example HTML fails', () => {
  const html = '<section class="panel"><h2>Regras ativas</h2><p>Persistência real depende do backend</p></section>';
  const r = lintPlugin(COMPLIANT, { description: 'Dark industrial admin aesthetic.' }, { exampleHtml: [html] });
  assert.equal(r.ok, false);
  assert.ok(r.violations.some(v => /meta|build|rules panel|on-screen/i.test(v)));
});

test('single-screen plugin warns, does not fail', () => {
  const r = lintPlugin(COMPLIANT, { description: 'Dark industrial admin aesthetic.' },
                       { assetHtmlNames: ['dashboard.html'], hasLayoutsMd: false });
  assert.equal(r.ok, true);                       // warn-level, not a violation yet
  assert.ok((r.warnings || []).some(w => /example set|single.screen|crud/i.test(w)));
});
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `node --test forge/tools/lint-plugin.test.mjs`
Expected: FAIL — `Cannot find module './lint-plugin.mjs'` / `lintPlugin is not a function`.

- [ ] **Step 3: Implement `lint-plugin.mjs`**

Implement `export function lintPlugin(skillMd, manifest, files = {})` where
`files = { exampleHtml: string[], assetHtmlNames: string[], hasLayoutsMd: boolean }`
(all optional — the pure-string callers pass `{}`):
1. Splits frontmatter (between the first two `---`) from the body.
2. Parses `triggers:` list and `description:` from frontmatter (simple line scan;
   no YAML dep).
3. Defines `BANNED_DOMAIN = [/\bmes\b/i, /\boee\b/i, /production line/i, /work[- ]order/i, /shop[- ]floor/i, /\bcrypto\b/i, /\btreasury\b/i, /\bhelpdesk\b/i, /\bairline\b/i, /\bbanking\b/i, /\binsurance\b/i, ...]` (seed from the 40 plugin domains; keep the list in one exported const) and `BUILD_META = /checklist|depends on (the )?backend|regras ativas|valida(ç|c)(ã|a)o ativa|build report|status de valida/i`.
4. Pushes a **violation** when: any `triggers` entry or the frontmatter `description` or
   `manifest.description` matches `BANNED_DOMAIN`; any of the four required headings
   (`## Visual language`, `## Layout archetype`, `## Applying to a domain`,
   `## Example instantiation`) is absent; `## Visual language`/`## Layout archetype`
   lines lack `AUTHORITATIVE`; the body contains `/extract[^.\n]*from the brief/i`;
   the `## Example instantiation` heading line lacks `illustrative`; **any string in
   `files.exampleHtml` matches `BUILD_META`** (build/design metadata rendered as UI —
   AUTHORING.md rule 6).
5. Pushes a **warning** (not a violation) when the plugin is single-screen:
   `(files.assetHtmlNames?.length ?? 0) < 2 && !files.hasLayoutsMd` (AUTHORING.md
   rule 5 — promote to violation once the 40 are retrofitted).
6. Returns `{ ok: violations.length === 0, violations, warnings }`.
Add a CLI tail: if run directly, read `process.argv[2]` dir, load `SKILL.md` +
`open-design.json`, read every `*.html` under the dir + `assets/` into
`files.exampleHtml`, set `assetHtmlNames`/`hasLayoutsMd` from the dir listing,
print violations + warnings, `process.exit(violations ? 1 : 0)`.

- [ ] **Step 4: Run tests to verify they pass**

Run: `node --test forge/tools/lint-plugin.test.mjs`
Expected: PASS (8 tests).

- [ ] **Step 5: Commit**

```bash
cd ~/projetos/wxk/wxcode-design-plugins
git add forge/tools/lint-plugin.mjs forge/tools/lint-plugin.test.mjs
git commit -m "feat(forge): add lint-plugin enforcing the aesthetic/semantic standard"
```

---

## Task 2: Port the forge generation spec → `forge/pipeline/forge.md`

**Files:**
- Create: `forge/pipeline/forge.md`
- Source: `~/.claude/skills/od-plugin-forge/SKILL.md`

Port the pipeline (parse → research → curate → build → verify → catalog → commit →
report) into a runtime-neutral spec. Changes from the source:

- Replace Claude-only tool names with neutral verbs + a "Runtime mapping" note
  (e.g. "dispatch N build agents" → each runtime maps to its subagent mechanism;
  Claude = Agent tool, others = their equivalent).
- **Rewrite the build subagent's `SKILL.md` template (source §3) to emit the
  `AUTHORING.md` two-layer format**: the four labeled headings, AUTHORITATIVE
  markers, domain-neutral archetype description, and the fenced `## Example
  instantiation`. Remove `## Workflow → 2. <extract domain inputs from brief>`;
  replace with the domain-neutral archetype-slot extraction.
- Point deterministic steps at `forge/tools/` (`regen-catalog.py`, `lint-plugin.mjs`)
  instead of inlining Python/bash.
- **Emit a meta-free multi-screen example set** per plugin (dashboard + list + form
  [+ detail]) into `assets/` + a `references/layouts.md` of paste-ready skeletons +
  an `assets/template.html` seed, and list them in `od.context.assets[]` /
  `od.useCase.exampleOutputs[]`. The build prompt bakes AUTHORING.md rules 5 & 6: the
  example *form* shows domain rules as inline validation (required marks, helper text,
  inline errors), and NO screen renders rules/checklist/validation-status/build-note
  panels or designer controls.
- Add an acceptance gate: every built plugin must pass `node forge/tools/lint-plugin.mjs <dir>` (now also covers the example-set + build-meta checks).

> **Linchpin:** this build template is SHARED — `harvest.md` (Task 3) reuses it for
> its build/verify/catalog/commit half. Rewriting it here to the two-layer standard
> fixes BOTH generators' output at once. Do not re-solve the domain split in Task 3.

- [ ] **Step 1:** Write `forge/pipeline/forge.md` per the above.
- [ ] **Step 2:** Sanity-check: the build template section, copied into a SKILL.md,
  passes `lint-plugin` (manually paste + lint).
- [ ] **Step 3:** Commit `forge(pipeline): port forge generation spec (emits 2-layer standard)`.

---

## Task 3: Port the harvest spec → `forge/pipeline/harvest.md`

**Files:**
- Create: `forge/pipeline/harvest.md`
- Source: `~/.claude/skills/wxcode-template-harvest/SKILL.md` (+ its `scripts/`)

> Harvest's distill step is already aesthetic-only (palette / fonts / layout /
> components, no domain). The domain split is inherited from Task 2's shared build
> template — no separate domain work here. This task only ports harvest's novel
> front-half; its deterministic helper `extract-tokens` is ported in Task 4.

- [ ] **Step 1:** Port the harvest front-half (list index → capture → distill) as a
  runtime-neutral spec; keep the IP guardrail verbatim; reference `forge.md` for the
  shared build/verify/catalog/commit half.
- [ ] **Step 2:** Move `extract-tokens.js` + `regen-catalog.py` references to
  `forge/tools/` (see Task 4).
- [ ] **Step 3:** Commit `forge(pipeline): port harvest spec`.

---

## Task 4: Deterministic tools — `regen-catalog.py` + `extract-tokens.mjs`

**Files:**
- Create: `forge/tools/regen-catalog.py`
- Test: `forge/tools/regen-catalog.test.py` (or a `node --test`-style smoke via pytest if available)
- Create: `forge/tools/extract-tokens.mjs` (port of `~/.claude/skills/wxcode-template-harvest/scripts/extract-tokens.js`)
- Test: `forge/tools/extract-tokens.test.mjs` (port of the sibling `extract-tokens.test.mjs`)

Port the inline Python from the forge skill §4.5 (walk `plugins/*/open-design.json`
→ rebuild `registry/wxcode-marketplace.json`, preserve top-level metadata, stamp
`updatedAt`). Add a `--check` mode that exits non-zero if the catalog is stale.

- [ ] **Step 1:** Write a smoke test: build a temp `plugins/` with 2 fake manifests,
  run regen, assert the catalog has 2 entries with the right `source`/`name`.
- [ ] **Step 2:** Run → fail.
- [ ] **Step 3:** Implement `regen-catalog.py`.
- [ ] **Step 4:** Run → pass.
- [ ] **Step 5:** Commit `feat(forge): add regen-catalog tool`.
- [ ] **Step 6:** Port `extract-tokens.js` → `forge/tools/extract-tokens.mjs` and its
  test from the harvest skill's `scripts/` (verbatim distill logic — palette / font /
  spacing extraction; update import paths only). Run `node --test forge/tools/extract-tokens.test.mjs` → pass.
- [ ] **Step 7:** Commit `feat(forge): port extract-tokens distill helper`.

---

## Task 5: Claude adapter shim

**Files:**
- Create: `forge/adapters/claude/od-plugin-forge.SKILL.md` (thin: front-matter + "follow ../../pipeline/forge.md")
- Create: `forge/adapters/claude/wxcode-template-harvest.SKILL.md`
- Create: `forge/adapters/claude/install.sh` (symlink into `~/.claude/skills/`)

- [ ] **Step 1:** Write the two shim SKILL.md files (keep their `name`/`description`
  frontmatter so discovery still works; body = "This skill is versioned in
  wxcode-design-plugins. Follow `forge/pipeline/forge.md`." + the resolved repo path).
- [ ] **Step 2:** Write `install.sh` that symlinks `~/.claude/skills/od-plugin-forge`
  and `~/.claude/skills/wxcode-template-harvest` to the repo, backing up any existing dir.
- [ ] **Step 3:** Commit `feat(forge): add Claude adapter shims + install script`.

---

## Task 6: Pilot — migrate `admin-forge-mes` to the standard

**Files:**
- Modify: `plugins/admin-forge-mes/SKILL.md`
- Modify (if needed): `plugins/admin-forge-mes/open-design.json` (de-domain description/tags; list the example set in `od.context.assets[]` + `od.useCase.exampleOutputs[]`)
- Create: `plugins/admin-forge-mes/assets/{dashboard,list,form,detail}.html` (the meta-free CRUD set in the Forge skin), `plugins/admin-forge-mes/assets/template.html` (seed), `plugins/admin-forge-mes/references/layouts.md`

- [ ] **Step 1:** Rewrite `plugins/admin-forge-mes/SKILL.md` to the four-layer format:
  Visual language + Layout archetype (AUTHORITATIVE, domain-neutral) + Applying to a
  domain + the fenced MES Example instantiation. De-domain the frontmatter
  `description`/`triggers`/`example_prompt`.
- [ ] **Step 2:** Build the **meta-free multi-screen example set** in the Forge
  dark/orange skin: `dashboard.html` + `list.html` + `form.html` (+ `detail.html`),
  an `assets/template.html` seed, and `references/layouts.md` (paste-ready skeletons).
  The `form.html` must show domain rules as **inline validation** (required marks,
  helper text, inline errors) — NO "rules"/"checklist"/validation-status/"depends on
  backend" panels, no designer controls (AUTHORING.md rules 5 & 6). List the files in
  `open-design.json` `od.context.assets[]` + `od.useCase.exampleOutputs[]`.
- [ ] **Step 3:** `node forge/tools/lint-plugin.mjs plugins/admin-forge-mes` → exit 0
  (no violations, no single-screen warning, no build-meta in any example HTML).
- [ ] **Step 4:** Standalone-fallback check: confirm the Example instantiation + the
  example set are a complete brief (open the screens; the SKILL still fully describes the build).
- [ ] **Step 5:** `python3 forge/tools/regen-catalog.py` (description may have changed); bump catalog if needed.
- [ ] **Step 6:** Commit `refactor(plugins): migrate admin-forge-mes to standard + meta-free CRUD example set`.

---

## Task 7 (STAGED — after pilot validated): retrofit the remaining 39 plugins

Not started until Task 6 is validated live (Forge MES pilot proves the format works
in both standalone and WXCode). Then: fan-out one agent per plugin (each separates
aesthetic from domain, re-emits the standard), each gated by `lint-plugin`, then one
catalog regen + version bump. Track dropped/needs-human cases explicitly — no silent
truncation.

---

## Self-review checklist (run after Tasks 1–6)

- Every plugin built/migrated passes `lint-plugin`.
- `pipeline/forge.md` build template, pasted into a SKILL.md, passes `lint-plugin`.
- `regen-catalog` is idempotent (run twice → no diff beyond `updatedAt`).
- Claude adapter: `/od-plugin-forge` still resolves after `install.sh`.
- Pilot `admin-forge-mes`: lints clean (incl. example-set + build-meta checks);
  ships the meta-free CRUD set (dashboard + list + form); standalone example intact;
  WXCode run uses the school domain in the Forge skin with NO rules/checklist/status panels.
