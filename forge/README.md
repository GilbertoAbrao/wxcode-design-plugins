# forge/ — WXCode plugin authoring toolkit

Versioned, runtime-neutral toolkit that produces and validates the plugins in this
repo's `plugins/` acervo. It replaces the personal Claude-only skills
(`~/.claude/skills/od-plugin-forge`, `~/.claude/skills/wxcode-template-harvest`)
with source that lives in the repo, can be reviewed, and can be driven from any
agent runtime — not just Claude Code.

## Why it lives here

The acervo (`plugins/`), the catalog (`registry/`), the authoring standard, and the
generator that emits them are one cohesive thing. Keeping them together means the
standard, the tool that produces it, and the validator that enforces it travel in
one versioned repo.

## Layout

```
forge/
  AUTHORING.md          # THE STANDARD — the aesthetic/semantic plugin contract
  pipeline/
    forge.md            # runtime-neutral generation spec (brief -> research -> build -> verify -> catalog)
    harvest.md          # runtime-neutral harvest spec (template list -> distill -> build)
  tools/
    lint-plugin.mjs     # deterministic: enforces AUTHORING.md on a plugin dir
    regen-catalog.py    # deterministic: rebuild registry/wxcode-marketplace.json from plugins/
  adapters/
    claude/             # thin shim: a Claude SKILL.md that points at ../pipeline/*.md
  docs/
    2026-06-02-plugin-aesthetic-semantic-split-design.md   # approved design (Phase 1 + Phase 2)
    IMPLEMENTATION-PLAN.md                                  # Phase 2 task plan
```

## Runtime-neutral split

- **Deterministic code** (`tools/`) — any runtime shells out: lint, catalog
  regeneration, token extraction, slug derivation, JSON/HTML verification.
- **LLM orchestration** (`pipeline/*.md`) — runtime-neutral prompt specs for the
  phases that need an agent (research, curate, build, enrichment, distill). Each
  runtime maps "dispatch N subagents" to its own mechanism.
- **Adapters** (`adapters/<runtime>/`) — thin per-runtime entrypoints. `claude/` is
  a `SKILL.md` shim symlinked into `~/.claude/skills/` so `/od-plugin-forge` keeps
  working against the repo-versioned spec.

## Ownership boundary

The `open-design.json` **schema** is owned by Open Design
(`packages/contracts/src/plugins/manifest.ts` is source of truth). The **authoring
convention** (the aesthetic/semantic `SKILL.md` split) is owned here in
`AUTHORING.md`.

## Status

Scaffolded. The standard (`AUTHORING.md`) and design are in place. Generator-spec
ports, the linter, the Claude adapter, and the pilot migration of `admin-forge-mes`
are tracked in `docs/IMPLEMENTATION-PLAN.md`. The 40-plugin retrofit is staged after
the pilot is validated.
