#!/usr/bin/env bash
#
# install.sh — symlink the Claude adapter shims into ~/.claude/skills/
#
# These shims keep /od-plugin-forge and /wxcode-template-harvest discoverable by
# Claude Code while their authoritative pipeline specs live in this repo
# (forge/pipeline/*.md). Re-running is idempotent: a correct symlink is left as-is.
#
set -euo pipefail

# Repo root, resolved from this script's location:
#   <repo>/forge/adapters/claude/install.sh -> <repo>
REPO_ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
ADAPTER_DIR="${REPO_ROOT}/forge/adapters/claude"
SKILLS_DIR="${HOME}/.claude/skills"

SKILLS=(od-plugin-forge wxcode-template-harvest)

mkdir -p "${SKILLS_DIR}"

for name in "${SKILLS[@]}"; do
  src="${ADAPTER_DIR}/${name}"
  dest="${SKILLS_DIR}/${name}"

  if [ ! -d "${src}" ]; then
    echo "error: adapter source missing: ${src}" >&2
    exit 1
  fi

  # Already the correct symlink? No-op.
  if [ -L "${dest}" ] && [ "$(readlink "${dest}")" = "${src}" ]; then
    echo "ok: ${dest} already links to ${src} (no change)"
    continue
  fi

  # Something is there (real dir, file, or a stale/wrong symlink): back it up.
  if [ -e "${dest}" ] || [ -L "${dest}" ]; then
    backup="${dest}.bak-$(date +%Y%m%d-%H%M%S)"
    mv "${dest}" "${backup}"
    echo "backed up: ${dest} -> ${backup}"
  fi

  ln -s "${src}" "${dest}"
  echo "linked: ${dest} -> ${src}"
done

echo "done."
