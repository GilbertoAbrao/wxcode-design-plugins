# harvest — runtime-neutral template-harvest spec

Harvest a template-list URL (e.g. ThemeForest popular admin templates) into an
own library of WXCode Open Design plugins. This is the **runtime-neutral** port of
the personal Claude skill `~/.claude/skills/wxcode-template-harvest/SKILL.md`.

Harvest is a **sibling of `forge/pipeline/forge.md`**, not a fork of it. Forge starts
from a textual brief and *researches* visual references; harvest starts from a
**template-list URL** and *captures + distills* concrete live demos into the same
curated shape. Everything downstream of the curated list — build, verify, catalog
regen, git commit/push, daemon/marketplace reload, report — is **identical** and is
owned by `forge.md`. This spec describes only the novel **front half** and then
**hands the curated list to forge.md's build phase (§3 onward)**.

```
list-url
  -> [1] list index   (drive a browser to render the grid; cheap-model distill the cards)
  -> select top-N      (list order; --count)
  -> [2] capture       (bounded browser pool 2-3: render each demo once -> dom.html, tokens.json, shot.png)
  -> [3] distill       (MANY cheap-model scouts, 1/bundle, parallel -> curated.json)
  -> HANDOFF to forge.md §3 build  (N build agents, ORIGINAL single-file plugins)
  -> forge.md §4 verify  (node forge/tools/lint-plugin.mjs <dir>)
  -> forge.md §4.5 catalog regen   (python3 forge/tools/regen-catalog.py)
  -> forge.md §5 trigger enrichment
  -> forge.md §6 git commit + push (single confirm gate)
  -> forge.md §7 daemon reload / marketplace refresh
  -> forge.md §8 report
```

**Default mode is `marketplace`** (same as forge.md): plugins land in the
`wxcode-design-plugins` repo, the catalog regenerates, and tenants pick them up on
the next source refresh. Harvest always tags its plugins `wxcode-plugin`.

---

## ⚠ IP guardrail — read before running

Harvested templates are licensed/paid third-party works. **Never reproduce their
HTML/CSS verbatim.**

- **Capture** is transient internal reference. `.harvest/` is gitignored and is
  NEVER copied into a plugin.
- **Distill** extracts design *characteristics* — palette, font stacks, type
  scale, spacing/radius/shadow, layout archetype, component inventory, features —
  not source markup.
- **Build** emits an **original** `example.html` in that design language. No
  copied markup, no copied class systems, no vendored third-party CSS/JS/fonts/
  images. No external CDNs (no Google Fonts, no Tailwind CDN). Fonts approximated
  with the closest system/open stack; images as original SVG/CSS/dataURI.
- **Provenance** recorded per plugin in `od.provenance = { template, url }`.

If a step seems to need the source to "look right", the fidelity target is wrong —
stay at characteristics + original re-implementation.

---

## Runtime mapping

This spec is written for **any capable coding agent**, not just Claude Code. It uses
the same neutral verbs as forge.md — see **the "Runtime mapping" table in
`forge/pipeline/forge.md`** for the full mapping (dispatch N agents / ask the user /
web-fetch / run a shell command / read-write-edit a file) and the rules that hold
across runtimes. Harvest adds one verb the forge mapping does not need:

| Neutral verb in this spec | Claude Code | Other coder runtimes |
|---------------------------|-------------|----------------------|
| **drive a browser** (navigate / wait / evaluate / snapshot / screenshot) | the Playwright MCP browser tools (`mcp__playwright__browser_navigate`, `_wait_for`, `_evaluate`, `_snapshot`, `_take_screenshot`) | the runtime's browser-automation tool, an MCP browser, or an already-authenticated connected browser; if none, fall back to `--source-urls` + plain web-fetch (lossy — see Failure modes) |

The same cross-runtime rules from forge.md apply: dispatch-in-a-single-batch means
*run them in parallel if you can, sequentially if you cannot, without changing the
prompts*; each dispatched agent gets a self-contained prompt; deterministic steps are
shell commands identical on every runtime.

---

## Flags

| Flag | Default | Meaning |
|------|---------|---------|
| `<list-url>` | ThemeForest popular admin URL | the list to harvest |
| `--count=N` | `12` | top-N templates to build this run |
| `--pages=K` | `1` | list pages to index |
| `--distill=<model>` | `claude-haiku-4-5` | distill scout model (cheap+fast) |
| `--build=<model>` | `claude-sonnet-4-6` | build subagent model (strong codegen) |
| `--marketplace-repo=<path>` | `$HOME/projetos/wxk/wxcode-design-plugins` | output repo |
| `--catalog=<file>` | `registry/wxcode-marketplace.json` | catalog to regenerate |
| `--push=<mode>` | `confirm` | `auto` / `confirm` / `skip` / `none` (forge.md §6 semantics) |
| `--source-urls=<file>` | — | anti-bot fallback: skip list scrape, read demo URLs (one per line) |

Model aliases match forge.md: `haiku` → `claude-haiku-4-5`, `sonnet` →
`claude-sonnet-4-6`, `opus` → `claude-opus-4-7`. The `--distill` model is the
list-index distiller AND the per-bundle distill scout model (forge.md's
`model_research` role); `--build` is forge.md's `model_build`. Pass each resolved id
to the dispatched agents through whatever model parameter your runtime exposes.

`HARVEST=<marketplace-repo>/.harvest/<timestamp>` is the transient capture root for
this run (gitignored, never shipped). Deterministic helpers used below:

- **`forge/tools/extract-tokens.mjs`** — the design-token extractor injected into the
  page during capture; returns design *characteristics* only (palette, fonts, scale,
  radii, shadows, component inventory), never source markup. *Ported in Task 4.*
- **`forge/tools/regen-catalog.py`** — the catalog regenerator forge.md §4.5 already
  shells out to. *Ported in Task 4.*

---

## Phase 1 — list index (drive a browser + cheap-model distill)

Build `templates[]` of `{ name, item_url, demo_url, category, thumb }`.

1. **`--source-urls` shortcut.** If `--source-urls` was given, read it into
   `templates[]` (each line is a `demo_url`; derive `name`/`slug` from the URL) and
   skip to Phase 2.
2. **Feasibility probe (first).** Drive a browser: navigate to `<list-url>`, wait for
   the card grid, then evaluate page JS to pull card anchors + titles + preview links
   into a raw array. If the page returns a Cloudflare/anti-bot challenge or zero
   cards, STOP and **ask the user** (one batched question) to choose:
   - (a) paste demo URLs / pass `--source-urls=<file>`,
   - (b) drive an already-authenticated connected browser instead,
   - (c) cancel.
3. **Distill the card grid.** Dispatch **one cheap-model distill agent**
   (`model: <distill>`) to turn the raw array into clean `templates[]`:
   `{ name, item_url, demo_url, category, thumb }`. `demo_url` is the "Live Preview"
   link (the public author/preview demo). Dedupe: ThemeForest emits a duplicate "Live
   Preview" anchor per card — keep the titled card, drop entries whose title is
   literally "Live Preview".

   **ThemeForest demo resolution (verified):** the `/full_screen_preview/` URL is a
   `preview.themeforest.net` wrapper that embeds the real demo in
   `iframe.full-screen-preview__frame` on the **author domain** (e.g. Metronic →
   `https://keenthemes.com/metronic/`). Before Phase 2, drive the browser to the
   wrapper and resolve `demo_url` to that iframe `src` — the extractor must run on the
   author demo (same-origin) because it cannot read a cross-origin iframe. If the
   resolved root is a marketing page, prefer the actual dashboard demo path when the
   author exposes one (e.g. `/<demo>/demo1`).
4. Repeat for `--pages=K` (advance pagination in the browser between pages).
5. Take the first `--count=N` in list order. Write `templates[]` to
   `$HARVEST/templates.json`.

## Phase 2 — capture (bounded browser pool 2-3)

For each of the top-N templates (process ≤3 at a time; rate-limit between hits):

1. Drive the browser: navigate to `demo_url`, wait for load / network-idle.
2. Evaluate the extractor in the page. Read `forge/tools/extract-tokens.mjs`, then run
   its `extractDesignTokens(document, window)` inside the page context and save the
   returned object to `$HARVEST/<slug>/tokens.json`. (The extractor returns
   characteristics only — see the IP guardrail.)
3. Save the rendered `document.documentElement.outerHTML` to `$HARVEST/<slug>/dom.html`
   (reference only — never shipped, never copied into a plugin).
4. Take a full-page screenshot → `$HARVEST/<slug>/shot.png`.
5. On block / timeout / login wall: log the slug + reason, skip it, continue. Never
   fail the whole run for one demo.

## Phase 3 — distill (MANY cheap-model scouts, parallel) ← the "many scouts"

**Dispatch one cheap-model distill agent per captured bundle, in a single batch**
(cap ~16 concurrent; chunk if N is larger). `model: <distill>`. This produces the
curated list the build half consumes.

Scout prompt template (self-contained — inline the file contents shown in `<...>`):

```
You distill a captured web template into DESIGN CHARACTERISTICS for an original
re-implementation. Do NOT return source HTML/CSS — only characteristics.

INPUT FILES:
  tokens.json: <inline contents of $HARVEST/<slug>/tokens.json>
  dom.html:    <path $HARVEST/<slug>/dom.html — read for structure cues only>
SOURCE: <name> · <demo_url>

Return STRICTLY this JSON (no prose):
{
  "name": "<short title>",
  "source_url": "<demo_url>",
  "style_tags": ["light-mode","clean-cards", ...],
  "dominant_palette": ["#...", ...],
  "layout_motif": "<sidebar+topbar+grid | ...>",
  "why_it_fits": "<1-2 sentences>",
  "design_tokens": {
    "palette": {"bg":"#...","surface":"#...","text":"#...","muted":"#...","accent":"#...","border":"#..."},
    "font_stacks": ["..."], "type_scale": ["12px","14px",...],
    "weights": ["400","600","700"], "radii": ["8px"], "shadows": ["..."],
    "components": ["sidebar","topbar","kpi-tiles","chart","data-table","activity-feed"],
    "features": ["collapsible sidebar","breadcrumb","..."],
    "motion": "<short note>"
  },
  "provenance": {"template":"<name>","url":"<demo_url>"}
}
```

Merge all scout entries into a single curated list and write it to
`$HARVEST/curated.json`.

### Curated shape ↔ forge.md compatibility

`curated.json` is the **forge.md curated shape plus two extras**:
`name`, `source_url`, `style_tags`, `why_it_fits`, `layout_motif`, and
`dominant_palette` are exactly the fields forge.md's build phase reads (note
`dominant_palette` is the harvested-real analogue of forge.md's
`dominant_palette_guess` — build agents use it identically as the `:root` palette
seed). The two harvest-only extras are:

- `design_tokens` — the distilled palette/fonts/scale/radii/shadows/components/
  features the build agent turns into CSS custom properties for an ORIGINAL re-skin.
- `provenance` — `{ template, url }`, recorded per plugin as `od.provenance` so each
  shipped plugin records the template it was inspired by (IP guardrail).

Because the shape is a superset of forge.md's curated entry, the build half consumes
it without modification: forge.md's build agent prompt simply has richer palette/
token input and one extra field (`provenance`) to copy into the manifest.

---

## Handoff to forge.md — build / verify / catalog / commit / report

From here harvest **does not re-describe the build machinery** — it reuses
`forge/pipeline/forge.md` verbatim. Hand `$HARVEST/curated.json` (one entry per
top-N template) to **forge.md's build phase (§3 onward)** and run forge.md's pipeline
through to its report, with these harvest-specific bindings:

1. **Mode is `marketplace`.** Target dir per plugin is
   `<marketplace_repo>/plugins/<slug>/`; manifest `name` = `wxcode-<slug>` (slash-free
   — the daemon validates against `/^[a-z0-9][a-z0-9._-]*$/`); manifest audience =
   `marketplace`, so the `wxcode-plugin` tag leads and the author/homepage are the
   fixed WXCode values forge.md §3 already specifies. **Build agents write only their
   plugin files and must NOT run git, regen the catalog, or touch other plugins** —
   exactly forge.md §3's contract; the orchestrator runs verify/catalog/commit once.

2. **Two harvest deltas on the forge.md §3 build prompt.** Inline them into each build
   agent's prompt on top of the unchanged §3 anatomy template:
   - Build the look from the entry's `design_tokens` (exact palette/fonts/scale as
     `:root` CSS custom properties) — ORIGINAL markup, no copying (IP guardrail).
   - Add `od.provenance = { template, url }` from the entry's `provenance`.

   Everything else in forge.md §3 is inherited unchanged, **including the AUTHORING.md
   two-layer standard and the meta-free multi-screen example set.** The two specs
   share **one** build template (forge.md §3); that template is what emits the
   aesthetic/semantic `SKILL.md` split and the dashboard+list+form(+detail) example
   set. **Do not re-solve the domain split here** — harvest inherits it for free by
   handing the curated list to that template. (forge.md §"Notes on the canonical
   anatomy" states the build template is shared exactly so harvest does not duplicate
   it.)

3. **Verify** — forge.md §4: structural sanity + `node forge/tools/lint-plugin.mjs
   <dir>` as the acceptance gate, with the same 2-retry / drop-as-needs-human policy.
   A harvested plugin is held to the identical lint bar as a forged one.

4. **Catalog regen** — forge.md §4.5: `python3 forge/tools/regen-catalog.py
   --marketplace-repo <marketplace_repo> --catalog <marketplace_catalog>`. Bump
   handled per §4.5.

5. **Trigger enrichment** — forge.md §5 (style-only phrasings; re-lint after).

6. **Git commit + push** — forge.md §6 verbatim: pre-flight branch + dirty-tree
   checks; stage ONLY the enumerated `plugins/<slug>/` dirs + the catalog; **never**
   `git add .`/`-A`, `--amend`, `--no-verify`, force-push, or a push to a
   `nexu-io/open-design` remote; commit with a HEREDOC, **no `Co-authored-by`
   trailer**; push behind `--push` (default `confirm`). `.harvest/` is gitignored and
   never staged.

7. **Daemon reload / report** — forge.md §7 + §8. In `marketplace` mode there is no
   local daemon restart; the report ends with the tenant note: "Tenants pick up on
   next Plugins → Sources → Refresh (or the daemon polling interval)." The report
   should additionally surface harvest-specific counts: captured vs skipped templates
   (with reasons), the distill/build models used, and the `$HARVEST` path.

> **Reuse contract.** `forge/pipeline/forge.md` owns the build template (§3), verify
> gate (§4), catalog regen (§4.5), enrichment (§5), git safety (§6), reload (§7), and
> report (§8). `forge/AUTHORING.md` owns the two-layer authoring standard, enforced by
> `forge/tools/lint-plugin.mjs`. Harvest owns ONLY Phases 1–3 (list-index, capture,
> distill) plus the two build-prompt deltas above. If the daemon plugin schema changes
> (`packages/contracts/src/plugins/manifest.ts`) or AUTHORING.md changes, fix it in
> forge.md / AUTHORING.md and both generators inherit it.

---

## Failure modes & recovery

These cover the harvest front half; the build/verify/catalog/commit failure modes are
inherited from **forge.md's "Failure modes & recovery" table** (lint retries, invalid
JSON, external-CDN re-dispatch, branch/dirty-tree gates, upstream-push protection,
daemon reload edge cases).

| Symptom | Recovery |
|---------|----------|
| List page anti-bot / 0 cards | Ask the user: `--source-urls` / connected browser / cancel |
| One demo blocked or login-walled | Skip that slug, log the reason, continue — never fail the whole run |
| Browser-automation tool unavailable | Fall back to a connected browser, or `--source-urls` + plain web-fetch (lossy: no live tokens, distill works from the fetched HTML only) |
| Distill scout returns source markup | Re-dispatch reminding "characteristics only, no markup" |
| Build emits external CDN / lorem ipsum | forge.md §4 re-dispatch with the rule pasted |
| Slug collision | Append `-2`, `-3`; never overwrite (forge.md slug rule) |
| Catalog JSON invalid after regen | forge.md §4.5 — inspect the offending manifest; fix; re-run regen |
| Push rejected / branch protected | forge.md §6 — capture stderr, keep commit local, do NOT retry/force |
