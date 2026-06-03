# forge — runtime-neutral plugin generation spec

Forge Open Design plugins from a context brief. This is the **runtime-neutral**
port of the personal Claude skill `~/.claude/skills/od-plugin-forge/SKILL.md`: it
preserves that pipeline's phases, flags, git-safety guarantees, and catalog
regeneration, but (a) describes orchestration in neutral verbs any capable coding
agent can map to its own mechanism, (b) makes the build phase emit the two-layer
authoring standard from `forge/AUTHORING.md`, and (c) shells out to the
deterministic tools in `forge/tools/` instead of inlining Python/bash.

Pipeline:

```
brief
  -> parse  (resolve mode_target: marketplace | bundled | both)
  -> [research agents (3 parallel)]
  -> curate
  -> [build agents (N parallel)]      # each emits the 2-layer SKILL.md + example set
  -> verify  (lint gate: node forge/tools/lint-plugin.mjs <dir>)
  -> regenerate marketplace catalog   (python3 forge/tools/regen-catalog.py; marketplace / both only)
  -> [trigger-enrichment agents (N parallel)]
  -> git commit + push (per-repo; single confirm gate before push)
  -> daemon reload / marketplace refresh
  -> report
```

**Default mode is `marketplace`.** Plugins land in the `wxcode-design-plugins`
repo, the catalog regenerates, and tenants pick them up on the next source
refresh — zero rebuild of any tenant VM or packaged app.

Use `--mode=bundled` only when contributing first-party plugins upstream to
`nexu-io/open-design`. Use `--mode=both` to ship the same plugin to both targets
in one run.

Output: one or more plugin folders, each ready to be picked up by the daemon's
plugin scanner:
- marketplace mode: `<marketplace_repo>/plugins/<slug>/`
- bundled mode: `<output_repo>/plugins/_official/examples/<slug>/`

---

## Runtime mapping

This spec is written for **any capable coding agent**, not just Claude Code. It
uses neutral verbs; each runtime maps them to its own mechanism:

| Neutral verb in this spec | Claude Code | Other coder runtimes (OpenCode, Codex, Cursor, Gemini, etc.) |
|---------------------------|-------------|---------------------------------------------------------------|
| **dispatch N agents** (research / build / enrichment) | one batched call to the `Agent` tool with N `Agent` invocations (`subagent_type: general-purpose`, `model: <id>`) | spawn N sub-tasks / parallel jobs through the runtime's task/subagent/parallel-tool API; if the runtime has no subagent primitive, run the N prompts sequentially in-process |
| **ask the user** (batched) | `AskUserQuestion` (one batched call) | the runtime's interactive prompt / question API; if none, print the question and read one structured reply |
| **web-search** / **web-fetch** | `WebSearch` / `WebFetch` | the runtime's web/search/browse tool, or an MCP browse tool |
| **run a shell command** | `Bash` | the runtime's shell/exec tool |
| **read a file** / **write a file** / **edit a file** | `Read` / `Write` / `Edit` | the runtime's file read/write/patch tools |

Rules that hold across all runtimes:

- "Dispatch N agents in a single batch" means *request them together so they run
  in parallel*; if your runtime cannot parallelize, run them one after another —
  do not change the prompts or the merge logic.
- Each dispatched agent gets a **self-contained prompt** (it does not share this
  conversation's context). Inline everything it needs: the curated reference, the
  target dir(s), the audience, and the full anatomy template below.
- Deterministic steps (lint, catalog regen, JSON/HTML verification) are **shell
  commands**, identical on every runtime: `node forge/tools/lint-plugin.mjs <dir>`
  and `python3 forge/tools/regen-catalog.py`. Do not re-implement them in the
  agent layer.

---

## 1. Parse the brief

The caller invokes the pipeline with a free-form brief (a `/od-plugin-forge`
slash command on Claude, a task prompt on any other runtime, or context from a
prior message). Extract the following fields. For anything missing, **ask the
user once, batched** (do not ping multiple times).

| Field | How to extract | Default if absent |
|-------|----------------|-------------------|
| `brief` | the free-form context text | required (ask if empty) |
| `N` | look for `N=<num>`, `count=<num>`, `<num> plugins`, `<num> variantes` | `1` |
| `model_research` | look for `research:<model>` or `--research <model>` | `claude-haiku-4-5` |
| `model_build` | look for `build:<model>` or `--build <model>` | `claude-sonnet-4-6` |
| `output_repo` | path containing `plugins/_official/examples/` | auto-detect; if none, ask |
| `slug_hint` | look for `slug:<name>` | derive from brief |
| `scenario` | `marketing`, `operations`, `editorial`, `dashboard`, `social`, `e-commerce`... | infer from brief |
| `mode` | `prototype`, `live-artifact`, `deck`... | `prototype` |
| `surface` | `web`, `mobile`, `desktop` | `web` |
| `push_mode` | `--push=auto` (no confirm), `--push=confirm` (default), `--push=skip` (commit only, no push), `--push=none` (no commit no push) | `confirm` |
| `target_branch` | `--branch=<name>` | current branch; if not `main`, ask user |
| `mode_target` | `--mode=bundled`, `--mode=marketplace`, `--mode=both` (see below) | `marketplace` |
| `marketplace_repo` | `--marketplace-repo=<path>` | `$HOME/projetos/wxk/wxcode-design-plugins` |
| `marketplace_catalog` | `--catalog=<filename>` | `registry/wxcode-marketplace.json` |

`mode_target` semantics:
- `--mode=marketplace` — write to `<marketplace_repo>/plugins/<slug>/` and
  regenerate `registry/wxcode-marketplace.json`; tenants pull via the marketplace
  source URL; trust = community.
- `--mode=bundled` — write to `<output_repo>/plugins/_official/examples/<slug>/`;
  daemon scans on restart; trust = bundled.
- `--mode=both` — do both (useful when contributing upstream AND publishing to the
  wxcode catalog simultaneously).

### Auto-detect `output_repo`

Resolution depends on `mode_target`. Run a shell command to probe the candidate
paths:

```bash
case "$MODE_TARGET" in
  marketplace)
    # Marketplace mode (default): writes to wxcode-design-plugins
    if [ -d "$MARKETPLACE_REPO/plugins" ] && [ -f "$MARKETPLACE_REPO/$MARKETPLACE_CATALOG" ]; then
      OUTPUT_REPO="$MARKETPLACE_REPO"
    fi ;;
  bundled|both)
    # Bundled (legacy): writes to open-design/plugins/_official/examples/
    for p in "$PWD" "$PWD/open-design" "$HOME/projetos/wxk/open-design"; do
      if [ -d "$p/plugins/_official/examples" ]; then
        OUTPUT_REPO_BUNDLED="$p"; break
      fi
    done
    ;;
esac
```

If the marketplace repo is missing: **ask the user** for the path (one text
input). If the bundled root is missing under `--mode=bundled|both`: stop — this is
not an open-design repo.

For `--mode=both`, both targets resolve and the build phase writes the same plugin
folder into each (manifest `name` adapts: `example-<slug>` for bundled,
`wxcode-<slug>` for marketplace).

### Model identification rules

- Research agents default to a cheap+fast model (`claude-haiku-4-5`) because they
  spend most of their time on web-search and summarisation.
- Build agents default to a strong code model (`claude-sonnet-4-6`) because they
  emit HTML/CSS that must look production-grade.
- Both overridable per invocation: `--research opus`, `--build opus`,
  `research:haiku-4-5`, `build:sonnet-4-6`.
- Accept short aliases: `haiku` -> `claude-haiku-4-5`, `sonnet` ->
  `claude-sonnet-4-6`, `opus` -> `claude-opus-4-7`.
- Pass the resolved model id to each dispatched agent through whatever model
  parameter your runtime exposes. Do not invent unsupported model ids. If your
  runtime cannot pick a model per agent, ignore these and use its default model.

---

## 2. Research phase (parallel agents)

**Dispatch 3 research agents in a single batch.** Each owns one marketplace bucket
so result sets do not collide. Each agent's prompt is self-contained and instructs
it to **web-search** the listed sites.

### Bucket A — Web design galleries

Model: `<model_research>`. Prompt template:

```
You are a visual-reference scout for the brief below.

BRIEF: <brief>
SCENARIO: <scenario>
TARGET COUNT: <N>

Web-search these galleries (use site: filters when helpful):
- land-book.com
- godly.website
- awwwards.com
- lapa.ninja
- httpster.net
- refero.design

For each gallery, surface 2-4 references that best match the brief.
Return STRICTLY this JSON shape, no prose around it:

{
  "bucket": "web-galleries",
  "references": [
    {
      "name": "<short title>",
      "source_url": "<page url>",
      "screenshot_url": "<image url if visible, else empty>",
      "style_tags": ["editorial", "warm-paper", ...],
      "why_it_fits": "<1-2 sentences>",
      "dominant_palette_guess": ["#aabbcc", ...],
      "layout_motif": "<hero+grid|magazine collage|split panel|...>"
    }
  ]
}

Cap at 8 references total across all galleries. Skip galleries returning
no relevant results. Do NOT fabricate URLs.
```

### Bucket B — Template marketplaces

Same shape, target sites:
- themeforest.net
- creativemarket.com
- ui8.net
- templatemonster.com

`"bucket": "template-marketplaces"`. Cap 6 references.

### Bucket C — Design platforms

Same shape, target sites:
- dribbble.com
- behance.net
- pinterest.com

`"bucket": "design-platforms"`. Cap 6 references.

### After research returns

Collect the three JSON payloads. Merge into a single curated list. Score each
reference on:
- match-to-brief (0-3)
- visual distinctiveness (0-2)
- feasibility as single-file HTML (0-2)

Sort desc by total score. Take top `N` (the requested plugin count). If fewer than
`N` viable references surfaced, **ask the user** whether to (a) proceed with fewer,
(b) re-run research with a relaxed brief, or (c) cancel.

Write the curated list to
`<output_repo>/.od-plugin-forge/<timestamp>-curated.json` so the build phase has a
stable artifact and runs are reproducible.

---

## 3. Build phase (N parallel agents)

**Dispatch `N` build agents in a single batch — one per curated reference.** Model:
`<model_build>`.

Each agent receives, inlined in its prompt:
- one curated reference (the full JSON entry from the curated list)
- the final slug (kebab-case)
- one or two absolute target dirs depending on `mode_target`:
  - `marketplace` mode: `<marketplace_repo>/plugins/<slug>/`
  - `bundled` mode: `<output_repo>/plugins/_official/examples/<slug>/`
  - `both` mode: ONE agent writes to BOTH dirs with the appropriate manifest `name`
    per target (`wxcode-<slug>` vs `example-<slug>`)
- the target audience for the manifest (controls `name`, `homepage`, `author`,
  `tags` prefix — see anatomy below)
- the full anatomy spec (inline in the prompt — the template below)

### Slug derivation

```
slug = lowercase(reference.name)
     | trim
     | non-alphanum -> "-"
     | collapse "-"
     | trim "-"
     | append "-<n>" if collision in target dir
```

### What the plugin folder contains

Unlike the legacy single-`example.html` shape, every forged plugin ships a
**meta-free, theme-discovered example set** so the agent imitating it has a clean
pattern for every screen type (AUTHORING.md rules 5 & 6). The set is a
**representative selection of the theme's page archetypes — intelligently chosen,
capped at 10 example HTML files** — not a fixed CRUD-4. From a harvest run the set
is the `example_pages` list the distill scout selected (Phase 2b of harvest.md);
from a pure-brief forge run with no discovered inventory, the set is the
CRUD-admin floor below. Relevance over count: a focused theme ships exactly its
relevant screens, never padded to 10.

```
<target>/
  open-design.json          # manifest (anatomy below)
  SKILL.md                  # two-layer authoring standard (anatomy below)
  example.html              # marketplace thumbnail = the dashboard/overview screen
  assets/                   # one meta-free screen per SELECTED discovered page (≤10):
    dashboard.html          #   CRUD-admin floor (dashboard + list + form [+ detail])
    list.html               #   when the archetype is CRUD-admin, PLUS the theme's
    form.html               #   domain rules shown as INLINE validation, not panels
    detail.html             #   discovered archetypes the scout selected, e.g.:
    login.html              #   auth (login + register/forgot/lock the theme ships)
    error-404.html          #   error/empty states (404/500/maintenance/empty)
    settings.html           #   settings / profile
    <signature>.html        #   the theme's signature/showcase pages
    <screen>-rtl.html       #   an RTL variant of a key screen IF the theme ships RTL
    template.html           # a seed skeleton: tokens + shell, no domain content
  references/
    layouts.md              # paste-ready section/screen skeletons (domain-neutral)
```

The `assets/` filenames above are illustrative — the actual files are one per
`example_pages` entry (or per CRUD-floor screen when there is no discovered
inventory), HARD-CAPPED at 10 example HTML files (`template.html` is a seed, not
counted toward the 10). `example.html` is the same screen as
`assets/dashboard.html` (or a copy) so the marketplace thumbnail stays a single
screen (`od.preview.entry`), while `od.useCase.exampleOutputs[]` and
`od.context.assets[]` list the full discovered set.

### Build agent prompt template

```
You are forging an Open Design plugin that follows the WXCode aesthetic/semantic
authoring standard (a plugin is a SKIN + SKELETON; its example domain is
illustration and standalone fallback, NEVER the product authority). Output ONLY
the files specified — do not echo explanation text.

CURATED REFERENCE:
<inline JSON entry>

TARGET DIR (must create if missing):
<absolute path>

MANIFEST AUDIENCE: <bundled | marketplace>

------------------------------------------------------------------
FILE 1 — <target>/open-design.json
------------------------------------------------------------------
# NAME / HOMEPAGE / AUTHOR / TAGS vary by manifest audience:
#   - "bundled":     name="example-<slug>", author=Open Design, homepage=github.com/nexu-io/open-design/...
#   - "marketplace": name="wxcode-<slug>",  author=WXCode,      homepage=github.com/GilbertoAbrao/wxcode-design-plugins/tree/main/plugins/<slug>
#     (manifest `name` must be slash-free — daemon regex /^[a-z0-9][a-z0-9._-]*$/; a `/` => install "name: Invalid")
# Tags prefix (REQUIRED, in this order):
#   - "bundled":     ["example", "first-party", "<mode>", "<scenario>", "<surface>", ...style_tags]
#   - "marketplace": ["wxcode-plugin", "wxcode", "first-party", "<mode>", "<scenario>", "<surface>", ...style_tags]
# The "wxcode-plugin" tag is the canonical filter handle — tenants and the UI
# search box use it to isolate WXCode-published plugins from the 400+ bundled
# open-design plugins. Always first in marketplace mode.
# IMPORTANT: `description` here is AESTHETIC-ONLY — describe the look + layout
# archetype, NEVER the example industry/domain (no "MES", "OEE", "production
# lines", "crypto treasury", etc.). Domain words live only inside the fenced
# Example instantiation in SKILL.md.
{
  "$schema": "https://open-design.ai/schemas/plugin.v1.json",
  "specVersion": "1.0.0",
  "name": "<audience-specific>",
  "title": "<Title Case>",
  "version": "0.1.0",
  "description": "<2-3 sentence AESTHETIC pitch: palette + typography + density + layout archetype>",
  "license": "MIT",
  "author": <audience-specific>,
  "homepage": <audience-specific>,
  "tags": [<audience-specific-prefix>, "<mode>", "<scenario>", "<surface>", ...style_tags],
  "compat": { "agentSkills": [{ "path": "./SKILL.md" }] },
  "od": {
    "kind": "scenario",
    "taskKind": "new-generation",
    "mode": "<mode>",
    "scenario": "<scenario>",
    "surface": "<surface>",
    "preview": { "type": "html", "entry": "./example.html" },
    "useCase": {
      "query": {
        "en": "Apply this <visual-style> <archetype> aesthetic to my domain",
        "zh-CN": "将这个 <visual-style> 风格应用到我的领域：<same prompt>"
      },
      # exampleOutputs lists the FULL theme-discovered example set — one entry per
      # SELECTED discovered page (from the curated entry's `example_pages`), capped
      # at 10. The first entry is always the dashboard/overview (= example.html).
      # When there is no discovered inventory, fall back to the CRUD-admin floor
      # (dashboard + list + form [+ detail]). Add auth/error/settings/signature/RTL
      # entries that the theme actually ships. Do NOT pad to 10.
      "exampleOutputs": [
        { "path": "./example.html", "title": "<Title> — Dashboard" },
        { "path": "./assets/list.html", "title": "<Title> — List" },
        { "path": "./assets/form.html", "title": "<Title> — Form" },
        { "path": "./assets/detail.html", "title": "<Title> — Detail" }
        # ...one more per remaining selected discovered page, e.g.:
        # { "path": "./assets/login.html",     "title": "<Title> — Login" },
        # { "path": "./assets/error-404.html", "title": "<Title> — 404" },
        # { "path": "./assets/settings.html",  "title": "<Title> — Settings" },
        # { "path": "./assets/<signature>.html","title": "<Title> — <Signature>" }
        # (≤10 example HTML files total — relevance over count)
      ]
    },
    "context": {
      "skills": [{ "path": "./SKILL.md" }],
      "designSystem": { "primary": true },
      "craft": [<pick 1-2 from: pixel-discipline, typographic-rhythm, state-coverage, laws-of-ux>],
      # assets[] = example.html + EVERY selected discovered screen in assets/ (the
      # same ≤10 set as exampleOutputs) + template.html + references/layouts.md.
      "assets": [
        "./example.html",
        "./assets/dashboard.html",
        "./assets/list.html",
        "./assets/form.html",
        "./assets/detail.html",
        # ...one ./assets/<page>.html per remaining selected discovered page (≤10 screens total)
        "./assets/template.html",
        "./references/layouts.md"
      ]
    },
    "pipeline": {
      "stages": [{ "id": "generate", "atoms": ["file-write", "live-artifact"] }]
    },
    "capabilities": ["prompt:inject", "fs:write"]
  }
}
# (Omit the detail.html entries if the archetype has no record-detail screen.
#  Add an entry for each additional SELECTED discovered page; never exceed 10
#  example HTML files; never pad to 10 if the theme ships fewer relevant pages.)

------------------------------------------------------------------
FILE 2 — <target>/SKILL.md   (TWO-LAYER AUTHORING STANDARD)
------------------------------------------------------------------
The frontmatter carries NO domain semantics. The body has the FOUR labeled
headings below, in this order, with the AUTHORITATIVE markers verbatim. The
Workflow extracts THIS domain's equivalent of the archetype slots — it must NOT
say "extract <domain fields> from the brief".

---
name: <slug>
description: |
  <AESTHETIC ONLY — describe the look (palette, typography, density, radius,
   shadow, motion) AND the layout archetype (navbar + rail + KPI tiles + status
   board + records table, etc.). NO domain claims, NO "use when the brief
   mentions <industry>".>
triggers:
  - "<style / visual phrasing>"      # e.g. "dark industrial admin", "dense data terminal"
  - "<style / visual phrasing>"      # NOT domain phrasings ("mes dashboard", "oee dashboard")
  # 5-8 entries; style phrasings only; mix en/pt where natural; NO industry/domain nouns
example_prompt: "Apply this <visual-style> <archetype> aesthetic to my domain"
od:
  mode: <mode>
  surface: <surface>
  scenario: <scenario>
  preview:
    type: html
    entry: example.html
  design_system:
    requires: true
    sections: [color, typography, layout, components]
  craft:
    requires: [<same craft as manifest>]
---

# <Name> — Visual Archetype

<1-paragraph intent: this plugin contributes a LOOK + STRUCTURE, the domain
comes from elsewhere.>

## Visual language (AUTHORITATIVE)
Colors as `:root` CSS custom properties (use reference.dominant_palette_guess),
typography scale, density, radius, shadows, motion. The non-negotiable look.

## Layout archetype (AUTHORITATIVE, domain-neutral)
Regions + component patterns described generically, with NO domain nouns. Faithful
to reference.layout_motif. Describe shapes, counts, and behaviors — not meaning.
e.g. "top navbar (entity switcher + search + status badge), left icon rail, KPI
tile row (N tiles), 2-column grid: a status board (rows of [label][state pill]
[metric][progress][count]) + a side/alerts panel, a full-width records table with
status pills, a record form (sectioned fields with inline validation), a record
detail (header + meta grid + related list)."

## Applying to a domain (the contract)
The domain comes from the Knowledge Base + the user's prompt. Extract THIS
domain's equivalent of the archetype slots — its primary entities, key metrics,
status states, record list/columns, form fields and their rules, and detail
fields — and map them onto the archetype above. (Standalone, with no KB/domain:
use the Example instantiation below.) Do NOT invent a "rules"/"checklist"/
validation-status panel; domain rules become inline field validation.

## Example instantiation (illustrative only — NOT the domain)
> One concrete example so standalone Open Design has a complete brief. In WXCode
> this is IGNORED — replace every label with the real domain's equivalent.

<the concrete domain-specific instantiation, in the reference's tone, fenced as
illustrative. Map each archetype slot to a real example entity/metric/screen.>

## Workflow
1. Read the active DESIGN.md.
2. Extract THIS domain's equivalent of the archetype slots (primary entities, key
   metrics, status states, record columns, form fields + rules, detail fields)
   from the KB + prompt. Standalone: use the Example instantiation above.
3. Build each screen in the Visual language + Layout archetype above, imitating
   the example set in assets/ (the theme-discovered screens — dashboard/list/form/
   detail plus any auth/error/settings/signature/RTL screens this plugin ships) —
   fresh content for the real domain, NOT the example labels.
4. Express domain rules as INLINE field validation (required marks, helper text,
   inline errors). Never render rules/checklist/validation-status/build-note
   panels or designer/demo controls.
5. One inline `<style>`, semantic HTML, no external assets.

## Output contract

```
<artifact identifier="<slug>" type="text/html" title="<Title>">
<!doctype html>...</artifact>
```

------------------------------------------------------------------
FILE 3 — <target>/example.html
------------------------------------------------------------------
- <!doctype html> single file; this is the marketplace thumbnail. It is the
  DASHBOARD screen of the example set (same content as assets/dashboard.html).
- All CSS inline in <head><style>; all scripts inline (keep minimal; motion via
  CSS where possible).
- No external image URLs; use <svg> placeholders, CSS gradients, or data URIs.
- Use reference.dominant_palette_guess as CSS custom properties.
- Replicate reference.layout_motif faithfully.
- Target 5KB - 30KB unless the design genuinely needs more.

------------------------------------------------------------------
FILE 4 — <target>/assets/*.html   (the THEME-DISCOVERED EXAMPLE SET, ≤10)
------------------------------------------------------------------
Emit a META-FREE example set, all in the SAME visual language + layout archetype.
The set is the theme's REPRESENTATIVE page archetypes — one original screen per
SELECTED discovered page — HARD-CAPPED at 10 example HTML files. Relevance over
count: build exactly the relevant screens the theme ships; do NOT pad to 10.

WHICH SCREENS TO BUILD:
- If the curated entry has an `example_pages` list (from a harvest run): build one
  original screen per entry, mapping each `slot`/`archetype` to a screen in this
  skin. Cap at 10; never add a page not in `example_pages`.
- If there is NO `example_pages` (a pure-brief forge run with no discovered
  inventory): build the CRUD-admin FLOOR — dashboard + list + form (+ detail when
  the archetype implies one).

CRUD-admin FLOOR (always present when the archetype is CRUD-admin):
- dashboard.html — KPI tiles + status board + side panel (same as example.html)
- list.html      — the records table archetype with status pills + filters
- form.html      — a record form. Domain rules appear as INLINE VALIDATION:
                   required marks (*), helper text under fields, and inline error
                   messages on invalid fields. NO "rules"/"checklist"/
                   validation-status summary panel anywhere.
- detail.html    — a record detail (header + meta grid + related list). Omit only
                   if the archetype genuinely has no detail screen.
ADDITIONAL discovered archetypes (build the ones in `example_pages`, in this skin):
- auth      — login (+ register / forgot / lock the theme ships). A meta-free auth
              form: branded panel + inline-validated fields, no demo controls.
- error/empty — 404 / 500 / maintenance / empty-state: a finished error screen in
              the skin (illustration/code + message + primary action), no caveats.
- settings/profile — sectioned settings or a profile screen (inline-validated).
- signature — the theme's distinctive page (analytics board, kanban, calendar,
              pricing, etc.) re-skinned as a finished screen.
- rtl variant — an RTL version of a key screen ONLY if `example_pages` includes one
              (the theme ships RTL): set `dir="rtl"` and mirror the layout.
HARD RULES for every screen (AUTHORING.md rule 6):
- These are FINISHED product screens. No build/implementation notes, no
  "depends on backend" caveats, no todo/checklist panels, no validation-status
  summaries, no designer/demo controls.
- Same single-file inline-CSS discipline as example.html.
- NEVER exceed 10 example HTML files (template.html is a seed, not counted).

------------------------------------------------------------------
FILE 5 — <target>/assets/template.html
------------------------------------------------------------------
A seed skeleton: the :root token block + the app shell (navbar + rail + main
region placeholders) and NO domain content — the smallest reusable starting point
in this skin.

------------------------------------------------------------------
FILE 6 — <target>/references/layouts.md
------------------------------------------------------------------
Paste-ready, DOMAIN-NEUTRAL section/screen skeletons (HTML fragments) for each
archetype region: navbar, icon rail, KPI tile, status-board row, records table
row, form section with an inline-validated field, detail meta grid. Label each
skeleton by archetype slot, not by a domain noun. No prose meta, no checklists.

RULES (apply to every file):
- AUTHOR IS FIXED. Copy the `author`, `name`, and `homepage` values the
  orchestrator gives you VERBATIM. In marketplace mode that is exactly
  `"author": {"name": "WXCode", "url": "https://github.com/GilbertoAbrao/wxcode-design-plugins"}`.
  NEVER write your own agent/model identity (e.g. "OpenCode", "Claude", "Codex")
  as the author — that is always a bug.
- Frontmatter (`description`, `triggers`, `example_prompt`) and the manifest
  `description` are AESTHETIC-ONLY. Domain/industry nouns there are a lint failure.
- Do not include placeholder lorem ipsum — write specific copy in the reference's
  tone (domain copy only inside the Example instantiation and the example set).
- Do not link to external CDNs (no Google Fonts, no Tailwind CDN).
- Do not invent fields outside the anatomy schema above.
- Verify each file parses (json must be valid JSON; every html must have matching
  doctype + closing </html>).

When done, print exactly: `FORGED <slug>`
```

---

## 4. Verify (lint gate — acceptance)

After all build agents return, run the deterministic checks. **Every built plugin
MUST pass the linter** — a plugin that fails lint is re-dispatched, not shipped.

For each new plugin dir, run a shell command:

```bash
for plugin_dir in <new dirs>; do
  echo "=== $(basename "$plugin_dir") ==="

  # 1. Structural sanity (cheap, runtime-neutral)
  python3 -m json.tool "$plugin_dir/open-design.json" > /dev/null \
    && echo "  manifest: OK" || echo "  manifest: BROKEN"
  for html in "$plugin_dir/example.html" "$plugin_dir"/assets/*.html; do
    [ -f "$html" ] || continue
    grep -q '<!doctype html>' "$html" && grep -q '</html>' "$html" \
      && echo "  $(basename "$html"): OK" || echo "  $(basename "$html"): malformed"
  done

  # 2. Authoring-standard gate (the acceptance check). Exit 0 = pass.
  #    Enforces: aesthetic-only frontmatter/manifest description, the four
  #    required AUTHORITATIVE headings, domain-neutral Workflow, the fenced
  #    illustrative-only Example instantiation, no build-meta in any example
  #    HTML, and the theme-discovered example set (warn only if single-screen —
  #    the lint does NOT require all 10 and does NOT penalize a focused set below
  #    the cap; relevance over count, 10 is a hard cap not a floor).
  node forge/tools/lint-plugin.mjs "$plugin_dir"
done
```

Re-dispatch policy:
- If structural sanity fails (broken JSON, malformed HTML) **or**
  `lint-plugin.mjs` exits non-zero (any violation), re-dispatch a single build
  agent for that slug with the failure log (the JSON error / the malformed-file
  name / the verbatim `VIOLATION:` lines) embedded in the prompt.
- A `WARNING:` from the linter (e.g. single-screen) does not block on its own, but
  the build template above always ships the theme-discovered example set (at least
  the CRUD-admin floor), so a faithful instantiation should not warn. The lint does
  not require all 10 screens — relevance over count — so a focused set below the cap
  is not a warning.
- **Cap at 2 retries per plugin.** A plugin still failing after 2 retries is
  dropped from this run and listed in the report as needs-human — never shipped.

---

## 4.5. Marketplace catalog regeneration (marketplace / both mode only)

Skip if `mode_target=bundled`.

After verify passes, regenerate the catalog from scratch by walking every plugin
dir — this avoids drift when entries are added, renamed, or removed across runs.
**Use the deterministic tool; do not inline Python:**

```bash
python3 forge/tools/regen-catalog.py \
  --marketplace-repo "<marketplace_repo>" \
  --catalog "<marketplace_catalog>"
```

`regen-catalog.py` walks `<marketplace_repo>/plugins/*/open-design.json`, rebuilds
`<marketplace_catalog>` (default `registry/wxcode-marketplace.json`), preserves the
existing top-level metadata when present (seeds it otherwise), and stamps
`metadata.updatedAt`. It is the single source of truth for catalog shape; consult
that file (and its `--check` mode) for flags.

### Bump catalog version

If the set of plugin `name`s changed (any added or removed), bump `catalog.version`
patch (`0.1.0` -> `0.1.1`). If only descriptions / tags / versions of existing
entries changed, leave the catalog version and rely on the refreshed
`metadata.updatedAt`. (If `regen-catalog.py` handles the bump itself, do not bump
again by hand.)

---

## 5. Trigger enrichment (parallel agents)

The build agents already write a `triggers:` list, but they bias toward EN
phrasings and miss synonym coverage. **Dispatch one enrichment agent per forged
plugin in a single batch** to widen coverage so the matcher fires reliably. Model:
`<model_research>` (a cheap model is plenty — this is text rewriting, not codegen).

> Because frontmatter is AESTHETIC-ONLY under this standard, enrichment widens
> **style** phrasings, never domain phrasings. A domain noun added here is a lint
> failure — re-run the lint gate after enrichment.

### Enrichment agent prompt template

```
You are tuning the `triggers:` block of an Open Design plugin's SKILL.md so the
daemon's plugin matcher fires reliably across natural-language phrasings — while
keeping every trigger AESTHETIC (style/visual), never domain/industry.

TARGET FILE: <absolute path to SKILL.md>
PLUGIN TITLE: <title from manifest>
PLUGIN ONE-LINE AESTHETIC: <aesthetic description from manifest>

Read the file. Locate the YAML frontmatter `triggers:` list. Rewrite it in-place
(edit the file) so it satisfies ALL of:

- 8-12 entries total
- STYLE / VISUAL phrasings only (palette, density, archetype): e.g.
  "dark industrial admin", "dense data terminal", "near-black admin",
  "status-board dashboard". NEVER industry/domain nouns ("mes dashboard",
  "oee dashboard", "production lines", "crypto treasury") — those fail lint.
- At least 4 English variants (verb-led + noun-led mixed)
- At least 3 Portuguese (pt-BR) STYLE variants natural for visual phrasing
  (e.g. "admin escuro industrial", "terminal de dados denso", "painel status-board")
- 1-2 Chinese variants only when the original SKILL.md already had CJK (keep; do
  not invent new CJK if the plugin had none)
- Mix of broad ("admin dashboard") and specific ("near-black status-board admin")
- No duplicates or near-duplicates
- Lowercase, quoted strings, one per line, preserving YAML list syntax

Avoid colliding with sibling plugins. Sibling triggers (do NOT duplicate any of
these as a sole or near-sole match for this plugin):

<list of trigger strings collected from OTHER forged plugins this run>

When done, print exactly: ENRICHED <slug>

Do not edit any field outside `triggers:`. Do not touch `description:`,
`example_prompt:`, the body, or the `od:` block.
```

### Mechanics

1. After Verify passes for all N plugins, collect every existing trigger string
   across the freshly forged plugins into a single "sibling set". Each enrichment
   agent gets the sibling set MINUS its own current triggers, so it can dedupe
   across the batch.
2. Dispatch N enrichment agents in one batch.
3. After they return, **re-run the lint gate** (`node forge/tools/lint-plugin.mjs
   <dir>`) on every touched plugin. A failure here means an enrichment agent slipped
   in a domain phrasing or broke the frontmatter — restore `triggers:` from a seed
   built from the reference's `style_tags` + 2-3 pt-BR style translations, log a
   warning in the report, and re-lint.

---

## 6. Git commit + push

Commits the freshly forged plugins and (optionally) pushes to the target branch.
Defaults are safe-first: commit runs automatically, push gates behind a single
confirmation unless `--push=auto` was set.

Runs once per target repo. In `marketplace` mode: one commit in
`<marketplace_repo>` covering plugin dirs + `registry/wxcode-marketplace.json`. In
`bundled` mode: one commit in `<output_repo>` covering
`plugins/_official/examples/<slug>/` dirs. In `both` mode: TWO independent commits
in TWO repos (same message shape, different paths).

### Pre-flight checks (per repo)

```bash
cd "<repo>"

# Capture state
CURRENT_BRANCH=$(git branch --show-current)
REMOTE_URL=$(git config --get "remote.origin.url" || echo "<no-remote>")
DEFAULT_REMOTE="origin"

# Verify we are inside the right repo
git rev-parse --is-inside-work-tree > /dev/null 2>&1 \
  || { echo "ERROR: not a git repo"; exit 1; }

# Refuse to operate on a dirty tree we do not own. Allowed paths depend on mode:
#   marketplace: plugins/<slug>/  +  registry/<catalog-file>
#   bundled:     plugins/_official/examples/<slug>/
#   (both):      run the check per-repo with the matching allowed set
DIRTY_OUTSIDE=$(git status --porcelain \
  | grep -v -E "^\?\? <allowed-paths-for-mode>" \
  | grep -v -E "^\?\? \.od-plugin-forge/" \
  | wc -l | tr -d ' ')
```

Decision matrix (each "ask the user" is one batched question):

| Condition | Action |
|----------|--------|
| `CURRENT_BRANCH != target_branch` and `target_branch` came from brief | `git checkout <target_branch>` (fail loudly if branch missing — don't auto-create) |
| `CURRENT_BRANCH != main` and brief did NOT specify branch | Ask the user: "Branch atual = `<x>`. Commit nessa branch ou trocar pra `main`?" Options: stay / switch-to-main / cancel |
| `DIRTY_OUTSIDE > 0` (pre-existing unrelated changes) | Ask the user: "Working tree tem N arquivos não relacionados. Stash antes? Continue + stage only plugin dirs? Cancel?" Default: stage-only |
| No remote configured | Skip push, log warning in report |

### Commit message

Compose from forged plugin titles. Path label varies by mode:

```
od-plugin-forge: add <N> <scenario> plugins (<title-1>, <title-2>, ...)

Generated via forge pipeline from brief:
  "<first 120 chars of brief>..."

Plugins (<path-prefix-for-mode>):
  - <slug-1> — <title-1>
  - <slug-2> — <title-2>
  ...

References curated from:
  <bucket counts>

Models: research=<model_research>, build=<model_build>, enrichment=<model_research>
Curated list: .od-plugin-forge/<timestamp>-curated.json
<if marketplace>
Catalog: registry/wxcode-marketplace.json (version=<x.y.z>, <N> entries)
</if>
```

`<path-prefix-for-mode>` is `plugins/` for marketplace, or
`plugins/_official/examples/` for bundled. Single header line under 72 chars; body
wraps at 72. **No `Co-authored-by:` trailer** (repo rule).

### Stage + commit

Path set varies by mode. **NEVER `git add .` / `git add -A` / `git add *`** — only
the enumerated plugin dirs and the curated-list artifact:

```bash
# marketplace mode:
for slug in <slug-1> <slug-2> ...; do
  git add "plugins/$slug/"
done
git add "registry/wxcode-marketplace.json"
git add ".od-plugin-forge/<timestamp>-curated.json"   # optional, may be .gitignored

# bundled mode:
for slug in <slug-1> <slug-2> ...; do
  git add "plugins/_official/examples/$slug/"
done
git add ".od-plugin-forge/<timestamp>-curated.json"

# Commit with HEREDOC (preserves multi-line formatting)
git commit -m "$(cat <<'EOF'
<commit message from template above>
EOF
)"
```

**Hooks:** never `--no-verify`. If a pre-commit hook fails (e.g. `pnpm guard`,
`pnpm typecheck`), capture stderr, surface it in the report, and exit. Do NOT retry
by stripping flags — fix or surface and stop. The user reviews and re-runs.

### Push gate

Show a summary BEFORE pushing:

```bash
echo "About to push:"
echo "  Remote: $REMOTE_URL"
echo "  Branch: $CURRENT_BRANCH"
echo "  Commit: $(git log -1 --oneline)"
echo "  Files:  $(git diff-tree --no-commit-id --name-only -r HEAD | wc -l) changed"
```

Branch on `push_mode`:

| `push_mode` | Behavior |
|-------------|----------|
| `auto` | Push immediately, no confirmation |
| `confirm` (default) | Ask the user (show the summary above) "Push?" Options: yes / no (commit stays local) |
| `skip` | Commit only, no push |
| `none` | Skip both commit and push |

Push command:

```bash
git push "$DEFAULT_REMOTE" "$CURRENT_BRANCH"
```

**Never** pass `--force` or `--force-with-lease`. **Never** target a remote other
than `origin` without an explicit brief flag `--remote=<name>`. **Never** push to
`main` of a remote whose URL matches `nexu-io/open-design` (the canonical
upstream) — surface a warning and abort push, leaving the commit local.

Upstream-protection check:

```bash
case "$REMOTE_URL" in
  *nexu-io/open-design* )
    if [ "$CURRENT_BRANCH" = "main" ]; then
      echo "WARN: refusing to push to nexu-io/open-design:main directly."
      echo "      Push aborted — commit kept local. Open a PR instead."
      PUSH_RESULT="aborted-upstream-main"
    fi ;;
esac
```

If branch protection rejects the push (HTTP 403 or `protected branch` in stderr),
capture the stderr verbatim, mark `PUSH_RESULT="rejected-branch-protection"`, do
NOT retry, do NOT suggest force.

### Safety guarantees (do not relax these)

- Never `git add .` / `git add -A` / `git add *` — only the enumerated plugin dirs
  and the curated-list artifact
- Never `--amend` — always create a new commit
- Never `--no-verify` / `--no-gpg-sign`
- Never `git reset --hard`, `git checkout .`, `git clean -f`
- Never force-push
- Never push to a remote URL the user did not approve in the brief

---

## 7. Daemon reload / marketplace refresh

Action depends on `mode_target`:

| Mode | Action |
|------|--------|
| `bundled` | `pnpm tools-dev restart` (daemon + web) in `<output_repo>` so the daemon re-scans `plugins/_official/examples/`. See decision tree below. |
| `marketplace` | No local daemon restart needed. After push, surface in the report: "Tenants pull on next marketplace refresh (manual via Plugins -> Sources -> Refresh, or automatic per daemon polling interval)." If a local Open Design dev daemon is running AND has the wxcode catalog registered as a source, OPTIONALLY run a shell command `curl -X POST http://<daemon>/api/plugins/marketplaces/<id>/refresh` to force-pull. |
| `both` | Do both: restart the dev daemon for the bundled scan AND surface the marketplace tenant note. |

### Bundled-mode reload (existing logic)

The web UI's "Example prompts" cards and plugin marketplace surface are populated by
the daemon scanning `plugins/_official/examples/` at boot. Newly forged plugins stay
invisible until the daemon re-scans, so this step ships them to the running UI.

### Decision tree

```bash
cd "<output_repo>"

# Is the daemon already running for this repo?
STATUS=$(pnpm tools-dev status --json 2>/dev/null || echo '{}')

if echo "$STATUS" | grep -q '"daemon"\s*:\s*"running"'; then
  STATE=running
elif echo "$STATUS" | grep -q '"daemon"\s*:\s*"stopped"'; then
  STATE=stopped
else
  STATE=unknown
fi
```

Branch:

| `$STATE` | Action |
|---------|--------|
| `running` | `pnpm tools-dev restart` — restart BOTH daemon and web. Daemon-only restart shifts the daemon to a fresh port but leaves the web sidecar pointing at the dead old port (`ECONNREFUSED` → 502 on `/api/*`), so the UI shows zero plugins until web also restarts. |
| `stopped` | Ask the user: "Daemon parado. Start agora?" Yes -> `pnpm tools-dev start`; No -> skip and tell the user to run `pnpm tools-dev` later |
| `unknown` (status command missing or repo not bootstrapped) | Skip silently, surface a one-line hint in the report: "Could not detect daemon state — run `pnpm tools-dev` manually to see the new plugins in the UI" |

### Safety constraints

- Run `pnpm tools-dev` commands in the **background** (the runtime's
  run-in-background mechanism). The daemon is long-lived; do not block the
  conversation waiting on it.
- Cap startup wait at 8 seconds via `until curl -sf http://127.0.0.1:<port>/api/health > /dev/null; do sleep 1; done`
  inside a `timeout 8` wrapper.
- Never run `pnpm tools-dev` outside `<output_repo>`. Confirm `pwd` first.
- Never pass `--daemon-port`/`--web-port` unless the user specified ports in the
  brief.
- If the daemon was already running with a Web UI open, the restart drops in-flight
  chat streams. Surface this so the user knows to refresh the tab.

---

## 8. Report

Single terse message to the user:

```
Forged <N> plugin(s) in <output_repo>/<path-prefix-for-mode>

  <slug-1>  — <title>  (<dashboard size>KB, <screen count> screens)
  <slug-2>  — <title>  (<dashboard size>KB, <screen count> screens)
  ...

References curated from: <bucket-A count> galleries,
  <bucket-B count> marketplaces, <bucket-C count> platforms.
Models used: research=<model_research>, build=<model_build>,
  enrichment=<model_research>.

Lint: all shipped plugins passed `node forge/tools/lint-plugin.mjs <dir>`.
  <list any slug dropped after 2 retries as needs-human, with the last violations>

Git:
  commit:  <sha-7> on <branch>
  push:    <pushed to origin/<branch> | local-only (push_mode=skip) |
           aborted-upstream-main | rejected-branch-protection |
           hook-failed: <one-line stderr>>
  remote:  <remote url>

Daemon: <running (restarted) | started | stopped (user declined) |
  unknown — run `pnpm tools-dev` manually | n/a (marketplace mode)>.

Next:
  - open each example screen (example.html + every assets/*.html in the
    theme-discovered set) in a browser to spot-check
  - if the daemon was restarted while a browser tab was open, refresh the tab to
    see the new "Example prompts" cards
  - if push was aborted/rejected: review `git log` and decide whether to open a PR
    via `gh pr create` or amend the local commit
  - (optional) further hand-tune `triggers:` only if a specific STYLE phrasing you
    care about does not surface (keep them aesthetic — domain phrasings fail lint)
```

---

## Failure modes & recovery

| Symptom | Recovery |
|---------|----------|
| Research agent returns empty refs for all buckets | Loosen brief or ask the user for explicit reference URLs |
| Research returns refs but all score < 3 | Show top-3 to the user, let them pick or veto |
| Build agent emits invalid JSON | Re-dispatch with the exact json parse error pasted in the prompt |
| Build agent emits HTML with external CDN links | Re-dispatch reminding "no external CDNs" |
| `lint-plugin.mjs` reports a domain term in `triggers`/`description` | Re-dispatch reminding "frontmatter + manifest description are AESTHETIC-ONLY; domain words only inside the fenced Example instantiation" |
| `lint-plugin.mjs` reports a missing/unmarked AUTHORITATIVE heading | Re-dispatch with the verbatim violation and the four-heading template |
| `lint-plugin.mjs` reports "extract … from the brief" | Re-dispatch reminding the Workflow must extract "THIS domain's equivalent of the archetype slots", not domain fields |
| `lint-plugin.mjs` reports build-meta in example HTML | Re-dispatch reminding rule 6: no rules/checklist/validation-status/build-note panels; rules become inline field validation |
| `lint-plugin.mjs` WARNS single-screen | The build template ships the theme-discovered set; if it warned, the agent shipped a lone screen — re-dispatch to emit the selected `example_pages` set (or the CRUD-admin floor: dashboard + list + form [+ detail] when there is no discovered inventory). Do not pad to 10 — relevance over count |
| Plugin still failing lint after 2 retries | Drop from this run, list as needs-human in the report — never ship a failing plugin |
| `output_repo/plugins/_official/examples` doesn't exist (bundled) | This is not an open-design repo — stop and tell the user |
| Slug collision with existing plugin | Append `-2`, `-3`, ... do not overwrite |
| Enrichment agent breaks YAML or adds a domain phrasing | Re-lint; restore `triggers:` from a seed built from `style_tags` + plugin title + 2-3 pt-BR STYLE translations; log warning in report |
| `pnpm tools-dev status` missing or repo not bootstrapped | Skip daemon reload, surface a one-line manual hint in the report |
| Daemon restart hangs past 8s timeout | Background process continues; report says "daemon restart in progress — check `pnpm tools-dev logs`" |
| Port conflict on daemon restart | Surface the stderr from `tools-dev`; do NOT auto-pick a new port |
| After `restart daemon` UI shows 502 / "Catalog is empty" | Web sidecar cached the old daemon port. Run `pnpm tools-dev restart` (no arg) to restart both. §7 defaults to the both-restart form. |
| Pre-commit hook fails (`pnpm guard`, `pnpm typecheck`) | Capture stderr, surface in report, exit. Do NOT retry with `--no-verify`. |
| Working tree dirty with unrelated changes | Ask the user: stash / stage-plugins-only / cancel. Default stage-plugins-only. |
| Current branch != target branch | If the brief specified it, checkout (fail loudly if missing). Else ask the user stay/switch/cancel. |
| Push rejected by branch protection (HTTP 403, "protected branch") | Capture stderr verbatim, mark `rejected-branch-protection`, do NOT retry, do NOT suggest force |
| Remote URL is `nexu-io/open-design` and branch is `main` | Abort push (canonical upstream), keep commit local, surface PR suggestion |
| No `origin` remote configured | Skip push, log warning, keep commit local |

---

## Notes on the canonical anatomy

The `open-design.json` **schema** is owned by Open Design
(`packages/contracts/src/plugins/manifest.ts` is source of truth; the published
JSON schema is `https://open-design.ai/schemas/plugin.v1.json`). If that schema
evolves, update the manifest anatomy in §3 — the daemon is the source of truth,
this spec is a generator that must stay in sync.

The **authoring convention** (the aesthetic/semantic two-layer `SKILL.md` split,
the meta-free, theme-discovered example set — up to 10 relevance-selected screens,
the AUTHORITATIVE headings) is owned by `forge/AUTHORING.md`, and is enforced by
`forge/tools/lint-plugin.mjs`. The §3 build template above is the encoding of that
standard; if `AUTHORING.md` or the linter change, re-sync the template and re-run
the §4 lint gate against a faithful instantiation.

The build template in §3 is **shared**: `forge/pipeline/harvest.md` reuses it for
its build/verify/catalog/commit half. Do not re-solve the aesthetic/semantic split
elsewhere — fix it here and both generators inherit it.

## Marketplace deployment model (default)

Default `--mode=marketplace` ships plugins to the public WXCode plugin catalog at
https://github.com/GilbertoAbrao/wxcode-design-plugins.

- Tenants register the catalog raw URL once:
  `https://raw.githubusercontent.com/GilbertoAbrao/wxcode-design-plugins/main/registry/wxcode-marketplace.json`
- The daemon polls the URL on a fixed interval (or on user-triggered Refresh) and
  lists entries under Plugins → Available
- 1-click install on the tenant UI; pulls the plugin folder from
  `github:GilbertoAbrao/wxcode-design-plugins@main/plugins/<slug>`
- New runs regenerate the catalog (§4.5); tenants pick up the diff on next refresh —
  no VM rebuild

This decouples plugin distribution from tenant VM lifecycle. Adding a plugin = 1
commit to the marketplace repo, propagated to every tenant within one refresh
interval. Catalog spec: `marketplace.v1`
(https://open-design.ai/schemas/marketplace.v1.json).
