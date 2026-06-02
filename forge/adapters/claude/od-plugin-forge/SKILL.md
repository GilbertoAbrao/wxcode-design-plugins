---
name: od-plugin-forge
version: 0.1.0
description: |
  Forge Open Design plugins from a context brief. Research-and-build pipeline:
  parses a textual brief, dispatches research subagents across web design
  galleries, template marketplaces and design platforms to harvest visual
  references, then dispatches build subagents (one per plugin) that emit a
  ready-to-install `open-design.json` + `SKILL.md` + single-file
  `example.html` (+ optional `assets/`) following the canonical anatomy of
  `plugins/_official/examples/<slug>/`.
  Use when asked to: "create open-design plugin", "forge plugin from theme",
  "generate N plugins inspired by X", "scan marketplaces and build plugins",
  "od plugin from brief", "/od-plugin-forge".
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - WebSearch
  - WebFetch
  - Agent
  - AskUserQuestion
---

# /od-plugin-forge — thin adapter shim

This skill is now **versioned in the `wxcode-design-plugins` repo**. It used to be a
personal copy under `~/.claude/skills/`; the authoritative pipeline now lives in the
repo so it can be reviewed and driven from any runtime.

**Do not improvise from this file.** Read and follow the full pipeline spec:

- **Authoritative spec:** `forge/pipeline/forge.md` (repo-relative).
- **When installed via symlink** (this `SKILL.md` lives at
  `~/.claude/skills/od-plugin-forge/SKILL.md` symlinked to
  `<repo>/forge/adapters/claude/od-plugin-forge/`), the spec is at
  `../../pipeline/forge.md` relative to this file — i.e. resolve the symlink to the
  repo and open `forge/pipeline/forge.md`.

Read that spec end to end, then execute it.

## Supporting toolkit

- **Standard:** `forge/AUTHORING.md` — the aesthetic/semantic plugin contract every
  emitted plugin must satisfy.
- **Deterministic tools** (shell out; do not reimplement):
  - `forge/tools/lint-plugin.mjs` — enforces `AUTHORING.md` on a plugin dir.
  - `forge/tools/regen-catalog.py` — rebuilds the marketplace catalog from `plugins/`.
