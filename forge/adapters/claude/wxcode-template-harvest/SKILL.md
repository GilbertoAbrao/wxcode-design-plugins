---
name: wxcode-template-harvest
version: 0.1.0
description: |
  Harvest a template-list URL (e.g. ThemeForest popular admin templates) into an
  own library of WXCode Open Design plugins. A browser captures each public live
  demo once; many Haiku scouts distill the captures into structured design tokens
  in parallel; Sonnet build subagents re-implement each as an ORIGINAL single-file
  plugin tagged `wxcode-plugin`. Reuses od-plugin-forge for build/verify/catalog/
  commit. Use when asked to: "harvest dashboard templates", "scan themeforest admin
  and build plugins", "build a plugin acervo from a template list",
  "/wxcode-template-harvest".
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - WebFetch
  - Agent
  - AskUserQuestion
  - mcp__playwright__browser_navigate
  - mcp__playwright__browser_evaluate
  - mcp__playwright__browser_snapshot
  - mcp__playwright__browser_take_screenshot
  - mcp__playwright__browser_wait_for
---

# /wxcode-template-harvest — thin adapter shim

This skill is now **versioned in the `wxcode-design-plugins` repo**. It used to be a
personal copy under `~/.claude/skills/`; the authoritative pipeline now lives in the
repo so it can be reviewed and driven from any runtime.

**Do not improvise from this file.** Read and follow the full harvest spec:

- **Authoritative spec:** `forge/pipeline/harvest.md` (repo-relative).
- **When installed via symlink** (this `SKILL.md` lives at
  `~/.claude/skills/wxcode-template-harvest/SKILL.md` symlinked to
  `<repo>/forge/adapters/claude/wxcode-template-harvest/`), the spec is at
  `../../pipeline/harvest.md` relative to this file — i.e. resolve the symlink to the
  repo and open `forge/pipeline/harvest.md`.

Read that spec end to end, then execute it.

## Supporting toolkit

- **Standard:** `forge/AUTHORING.md` — the aesthetic/semantic plugin contract every
  emitted plugin must satisfy.
- **Deterministic tools** (shell out; do not reimplement):
  - `forge/tools/lint-plugin.mjs` — enforces `AUTHORING.md` on a plugin dir.
  - `forge/tools/regen-catalog.py` — rebuilds the marketplace catalog from `plugins/`.
