#!/usr/bin/env python3
"""Regenerate the WXCode marketplace catalog from plugin manifests.

Walks ``<repo>/plugins/*/open-design.json`` (sorted) and rebuilds the
``registry/wxcode-marketplace.json`` catalog deterministically, preserving the
existing top-level metadata and restamping ``metadata.updatedAt``. This is the
file-based port of the inline generator documented in od-plugin-forge
SKILL.md §4.5 ("Marketplace catalog regeneration").

Usage:
    python3 forge/tools/regen-catalog.py [--marketplace-repo <path>]
                                         [--catalog <relpath>] [--check]

Defaults:
    --marketplace-repo  the repo root (two levels up from this script:
                        forge/tools/ -> repo root)
    --catalog           registry/wxcode-marketplace.json

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
PUBLISHER_URL = "https://github.com/GilbertoAbrao/wxcode-design-plugins"
SOURCE_PREFIX = "github:GilbertoAbrao/wxcode-design-plugins@main/plugins/"
HOMEPAGE_PREFIX = (
    "https://github.com/GilbertoAbrao/wxcode-design-plugins/tree/main/plugins/"
)

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
    shaped exactly like the SKILL.md §4.5 generator.
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
        entries.append(
            {
                "name": mf["name"],
                "title": mf["title"],
                "version": mf["version"],
                "source": f"{SOURCE_PREFIX}{slug}",
                "publisher": {
                    "id": PUBLISHER_ID,
                    "url": PUBLISHER_URL,
                },
                "capabilitiesSummary": od.get("capabilities", []),
                "description": mf["description"],
                "tags": mf.get("tags", []),
                "homepage": f"{HOMEPAGE_PREFIX}{slug}",
                "license": mf.get("license", "MIT"),
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
    regenerated = build_catalog(repo, catalog_path)
    n = len(regenerated["plugins"])

    if args.check:
        if not catalog_path.exists():
            print(f"stale: {catalog_path} does not exist ({n} entries expected)")
            return 1
        on_disk = json.loads(catalog_path.read_text(encoding="utf-8"))
        if _strip_updated_at(on_disk) == _strip_updated_at(regenerated):
            print(f"in sync: {catalog_path} · {n} entries")
            return 0
        print(f"stale: {catalog_path} differs from regenerated catalog · {n} entries")
        return 1

    catalog_path.parent.mkdir(parents=True, exist_ok=True)
    catalog_path.write_text(_serialize(regenerated), encoding="utf-8")
    print(f"wrote {catalog_path} · {n} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
