#!/usr/bin/env python3
"""Regenerate the WXCode marketplace catalog from plugin manifests.

Walks ``<repo>/plugins/*/open-design.json`` (sorted) and rebuilds the
``registry/wxcode-marketplace.json`` catalog deterministically, preserving the
existing top-level metadata and restamping ``metadata.updatedAt``. This is the
file-based port of the inline generator documented in od-plugin-forge
SKILL.md §4.5 ("Marketplace catalog regeneration").

Usage:
    python3 forge/tools/regen-catalog.py [--marketplace-repo <path>]
                                         [--catalog <relpath>]
                                         [--fork-catalog <path> | --no-fork-catalog]
                                         [--check]

Defaults:
    --marketplace-repo  the repo root (two levels up from this script:
                        forge/tools/ -> repo root)
    --catalog           registry/wxcode-marketplace.json
    --fork-catalog      auto-detected sibling open-design repo
                        (../open-design/plugins/registry/wxcode/
                        open-design-marketplace.json) — the catalog tenants
                        actually read. Synced alongside the authoring catalog;
                        a missing fork catalog is WARNED, never silently skipped.
                        See the "Dual-catalog sync" note below.

Determinism: ``metadata.updatedAt`` is read from the ``OD_REGEN_NOW`` env var
(an ISO-8601 string) when set, otherwise the current UTC time is used. Tests
set ``OD_REGEN_NOW`` so two runs produce byte-identical output.

Modes:
    default   write the catalog (pretty 2-space JSON + trailing newline) and
              print ``wrote <path> · <N> entries``.
    --check   regenerate in memory and compare to the on-disk catalog IGNORING
              ``metadata.updatedAt``; exit 1 if they differ (stale), 0 if
              current. Prints a clear status line.

stdlib only.
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import pathlib
import sys
from typing import Any

PUBLISHER_ID = "wxcode"
PUBLISHER_GITHUB = "GilbertoAbrao"
PUBLISHER_URL = "https://github.com/GilbertoAbrao/wxcode-design-plugins"
SOURCE_PREFIX = "github:GilbertoAbrao/wxcode-design-plugins@main/plugins/"
HOMEPAGE_PREFIX = (
    "https://github.com/GilbertoAbrao/wxcode-design-plugins/tree/main/plugins/"
)

# --- Dual-catalog sync ---------------------------------------------------
# Tenants do NOT read this repo's registry/wxcode-marketplace.json directly.
# The Open Design daemon only accepts a marketplace source whose repo is on its
# allowlist (the OD official repo OR ``OD_MARKETPLACE_REPO``), and that source
# file must be named ``open-design-marketplace.json`` under
# ``plugins/registry/<id>/``. WXCode tenants set
# ``OD_MARKETPLACE_REPO=GilbertoAbrao/open-design`` and read the catalog from
# the *open-design fork* at the path below. ``wxcode-design-plugins`` is NOT
# allowlisted, so a plugin that lands only in this repo's catalog can only be
# installed via a direct ``github:`` source — which defaults to the
# ``restricted`` trust tier (the Restricted-badge bug). Keeping BOTH catalogs in
# sync is therefore mandatory: this repo's catalog is the authoring home; the
# fork catalog is what every tenant actually consumes (and the marketplace-trust
# path that yields ``trusted`` installs).
FORK_SIBLING_DIRNAME = "open-design"
FORK_CATALOG_RELPATH = "plugins/registry/wxcode/open-design-marketplace.json"


def default_fork_catalog(repo: pathlib.Path) -> pathlib.Path:
    """Conventional fork-catalog path: the ``open-design`` repo checked out as a
    sibling of this repo (``<repo>/../open-design/<FORK_CATALOG_RELPATH>``)."""
    return (repo.parent / FORK_SIBLING_DIRNAME / FORK_CATALOG_RELPATH).resolve()

# Seed values for a fresh catalog (mirrors the existing
# registry/wxcode-marketplace.json top-level metadata).
SEED_CATALOG: dict[str, Any] = {
    "$schema": "https://open-design.ai/schemas/marketplace.v1.json",
    "specVersion": "1.0.0",
    "name": "wxcode-design-plugins",
    "version": "0.1.0",
    "owner": "GilbertoAbrao",
    "trust": "community",
    "metadata": {
        "title": "WXCode Design Plugins",
        "description": (
            "First-party plugins curated by WXCode for Open Design daemons."
        ),
        "homepage": "https://github.com/GilbertoAbrao/wxcode-design-plugins",
        "updatedAt": None,  # stamped at build time
    },
    "plugins": [],
}


def _now_iso() -> str:
    """ISO-8601 UTC timestamp, overridable via ``OD_REGEN_NOW`` for tests."""
    injected = os.environ.get("OD_REGEN_NOW")
    if injected:
        return injected
    return datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )


def build_entries(repo: pathlib.Path) -> list[dict[str, Any]]:
    """Build catalog entries by walking ``<repo>/plugins/*/open-design.json``.

    Sorted by directory name so output order is deterministic. Each entry is
    shaped exactly like the live committed catalog (publisher carries the
    ``github`` field; keys follow the live key order).
    """
    entries: list[dict[str, Any]] = []
    plugins_dir = repo / "plugins"
    if not plugins_dir.is_dir():
        return entries
    for plugin_dir in sorted(plugins_dir.iterdir()):
        if not plugin_dir.is_dir():
            continue
        manifest_path = plugin_dir / "open-design.json"
        if not manifest_path.exists():
            continue
        mf = json.loads(manifest_path.read_text(encoding="utf-8"))
        od = mf.get("od", {})
        slug = plugin_dir.name
        # Key order mirrors the live catalog exactly:
        # name, title, version, source, publisher, homepage, license,
        # capabilitiesSummary, description, tags, mode.
        entries.append(
            {
                "name": mf["name"],
                "title": mf["title"],
                "version": mf["version"],
                "source": f"{SOURCE_PREFIX}{slug}",
                "publisher": {
                    "id": PUBLISHER_ID,
                    "github": PUBLISHER_GITHUB,
                    "url": PUBLISHER_URL,
                },
                "homepage": f"{HOMEPAGE_PREFIX}{slug}",
                "license": mf.get("license", "MIT"),
                "capabilitiesSummary": od.get("capabilities", []),
                "description": mf["description"],
                "tags": mf.get("tags", []),
                "mode": od.get("mode"),
            }
        )
    return entries


def build_catalog(repo: pathlib.Path, catalog_path: pathlib.Path) -> dict[str, Any]:
    """Regenerate the full catalog dict (entries + preserved metadata)."""
    entries = build_entries(repo)
    if catalog_path.exists():
        existing = json.loads(catalog_path.read_text(encoding="utf-8"))
        catalog = {**existing, "plugins": entries}
        catalog.setdefault("metadata", {})
    else:
        catalog = json.loads(json.dumps(SEED_CATALOG))  # deep copy
        catalog["plugins"] = entries
    catalog["metadata"]["updatedAt"] = _now_iso()
    return catalog


def _strip_updated_at(catalog: dict[str, Any]) -> dict[str, Any]:
    """Return a copy of the catalog with ``metadata.updatedAt`` removed."""
    clone = json.loads(json.dumps(catalog))
    meta = clone.get("metadata")
    if isinstance(meta, dict):
        meta.pop("updatedAt", None)
    return clone


def _serialize(catalog: dict[str, Any]) -> str:
    return json.dumps(catalog, indent=2) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--marketplace-repo",
        default=None,
        help="path to the marketplace repo root (default: two levels up from "
        "this script)",
    )
    parser.add_argument(
        "--catalog",
        default="registry/wxcode-marketplace.json",
        help="catalog path relative to the repo root",
    )
    parser.add_argument(
        "--fork-catalog",
        default=None,
        help="explicit path to the open-design fork catalog "
        "(plugins/registry/wxcode/open-design-marketplace.json) — the file "
        "tenants actually read. Defaults to the sibling open-design repo. The "
        "file must already exist (its top-level metadata is preserved); a "
        "missing fork catalog is reported, never silently skipped.",
    )
    parser.add_argument(
        "--no-fork-catalog",
        action="store_true",
        help="do not sync the open-design fork catalog (suppresses the "
        "not-synced warning). Use only when intentionally regenerating just "
        "this repo's catalog.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="report whether the on-disk catalog is in sync (ignoring "
        "metadata.updatedAt); exit 1 if stale",
    )
    args = parser.parse_args(argv)

    if args.marketplace_repo:
        repo = pathlib.Path(args.marketplace_repo).resolve()
    else:
        # forge/tools/regen-catalog.py -> repo root is two levels up.
        repo = pathlib.Path(__file__).resolve().parents[2]

    catalog_path = (repo / args.catalog).resolve()

    # Resolve the fork catalog target. Both catalogs index the SAME plugin
    # sources (build_entries), so they receive identical entries; only the file
    # location + preserved top-level metadata differ. Tenants read the fork
    # catalog, so failing to sync it is the Restricted-badge bug — never skip it
    # silently.
    fork_path: pathlib.Path | None = None
    fork_explicit = False
    if not args.no_fork_catalog:
        if args.fork_catalog:
            fork_path = pathlib.Path(args.fork_catalog).resolve()
            fork_explicit = True
        else:
            fork_path = default_fork_catalog(repo)

    # A fork target is actionable only if its file already exists (its own
    # top-level metadata — owner/version/trust — must be preserved, never seeded
    # from this repo's defaults).
    fork_actionable = fork_path is not None and fork_path.exists()
    fork_missing = (
        fork_path is not None and not fork_path.exists() and not args.no_fork_catalog
    )

    # (path, label) pairs to process, primary first.
    targets: list[tuple[pathlib.Path, str]] = [(catalog_path, "this repo")]
    if fork_actionable:
        targets.append((fork_path, "open-design fork"))

    if args.check:
        stale = False
        for path, label in targets:
            regen = build_catalog(repo, path)
            n = len(regen["plugins"])
            if not path.exists():
                print(f"stale: {path} does not exist ({n} entries expected) [{label}]")
                stale = True
                continue
            on_disk = json.loads(path.read_text(encoding="utf-8"))
            if _strip_updated_at(on_disk) == _strip_updated_at(regen):
                print(f"in sync: {path} · {n} entries [{label}]")
            else:
                print(f"stale: {path} differs from regenerated catalog · {n} entries [{label}]")
                stale = True
        if fork_missing:
            # Surfaced, not fatal: an absent local fork checkout cannot be
            # verified, but a misconfigured run must still see the warning.
            _warn_fork_missing(fork_path, fork_explicit)
        return 1 if stale else 0

    wrote_fork = False
    for path, label in targets:
        regen = build_catalog(repo, path)
        n = len(regen["plugins"])
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(_serialize(regen), encoding="utf-8")
        print(f"wrote {path} · {n} entries [{label}]")
        if label == "open-design fork":
            wrote_fork = True

    if fork_missing:
        _warn_fork_missing(fork_path, fork_explicit)
    elif wrote_fork:
        print(
            "note: the open-design fork catalog was updated in a SEPARATE repo; "
            "commit + push it there too (raw.githubusercontent reads it at @main)."
        )
    return 0


def _warn_fork_missing(fork_path: pathlib.Path, explicit: bool) -> None:
    """Loud, non-fatal warning when the fork catalog could not be synced.

    Tenants read ONLY the open-design fork catalog, so a plugin that lands in
    this repo's catalog but not the fork's is installable only via a direct
    github: source -> the `restricted` trust tier. Never let that pass silently.
    """
    hint = (
        "pass --fork-catalog <path>"
        if not explicit
        else "the file must already exist (seed it once in the fork repo)"
    )
    print(
        "WARNING: open-design fork catalog NOT synced "
        f"({fork_path} not found). Tenants reading the open-design fork will "
        "NOT see new/updated plugins, and direct installs default to the "
        f"'restricted' trust tier. Check out the open-design repo as a sibling "
        f"or {hint}. Use --no-fork-catalog to silence this intentionally.",
        file=sys.stderr,
    )


if __name__ == "__main__":
    raise SystemExit(main())
