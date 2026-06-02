#!/usr/bin/env python3
"""Smoke test for regen-catalog.py.

Run:
    python3 forge/tools/regen-catalog.test.py
    # or
    python3 -m unittest -v forge/tools/regen-catalog.test.py

Builds a throwaway marketplace repo in a tempdir (two plugin manifests + a
seed catalog) and drives the real ``regen-catalog.py`` via subprocess so the
test exercises the actual CLI behavior: entry shape, sort order, idempotency,
and ``--check`` exit codes. Never touches the real
``registry/wxcode-marketplace.json``.
"""

from __future__ import annotations

import json
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parent / "regen-catalog.py"
FIXED_NOW = "2026-01-02T03:04:05Z"


def _manifest(name: str, title: str, mode: str, tags: list[str]) -> dict:
    return {
        "$schema": "https://open-design.ai/schemas/plugin.v1.json",
        "specVersion": "1.0.0",
        "name": name,
        "title": title,
        "version": "0.1.0",
        "description": f"{title} test plugin.",
        "license": "MIT",
        "author": {"name": "WXCode", "url": "https://example.invalid"},
        "homepage": "https://example.invalid",
        "tags": tags,
        "od": {
            "mode": mode,
            "capabilities": ["prompt:inject", "fs:write"],
        },
    }


def _seed_catalog() -> dict:
    return {
        "$schema": "https://open-design.ai/schemas/marketplace.v1.json",
        "specVersion": "1.0.0",
        "name": "wxcode-design-plugins",
        "version": "0.1.0",
        "owner": "GilbertoAbrao",
        "trust": "community",
        "metadata": {
            "title": "WXCode Design Plugins",
            "description": "Test seed.",
            "homepage": "https://github.com/GilbertoAbrao/wxcode-design-plugins",
            "updatedAt": "2000-01-01T00:00:00Z",
        },
        "plugins": [],
    }


class RegenCatalogTest(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = pathlib.Path(self._tmp.name)
        plugins = self.repo / "plugins"
        # Create beta before alpha to prove the generator sorts, not relies on
        # filesystem creation order.
        for slug, name, title, mode, tags in (
            ("beta", "wxcode-beta", "Beta Plugin", "deck", ["wxcode-plugin", "b-tag"]),
            ("alpha", "wxcode-alpha", "Alpha Plugin", "prototype", ["wxcode-plugin", "a-tag"]),
        ):
            d = plugins / slug
            d.mkdir(parents=True)
            (d / "open-design.json").write_text(
                json.dumps(_manifest(name, title, mode, tags)),
                encoding="utf-8",
            )
        registry = self.repo / "registry"
        registry.mkdir()
        self.catalog_path = registry / "wxcode-marketplace.json"
        self.catalog_path.write_text(json.dumps(_seed_catalog()), encoding="utf-8")

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def _run(self, *extra: str, now: str = FIXED_NOW) -> subprocess.CompletedProcess:
        env = dict(os.environ)
        env["OD_REGEN_NOW"] = now
        return subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--marketplace-repo",
                str(self.repo),
                "--catalog",
                "registry/wxcode-marketplace.json",
                *extra,
            ],
            env=env,
            capture_output=True,
            text=True,
        )

    def test_writes_two_sorted_entries_with_correct_shape(self) -> None:
        res = self._run()
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("2 entries", res.stdout)

        catalog = json.loads(self.catalog_path.read_text(encoding="utf-8"))
        plugins = catalog["plugins"]
        self.assertEqual(len(plugins), 2)

        # Sorted by slug: alpha before beta.
        self.assertEqual([p["name"] for p in plugins], ["wxcode-alpha", "wxcode-beta"])
        self.assertEqual(
            plugins[0]["source"],
            "github:GilbertoAbrao/wxcode-design-plugins@main/plugins/alpha",
        )
        self.assertEqual(
            plugins[1]["source"],
            "github:GilbertoAbrao/wxcode-design-plugins@main/plugins/beta",
        )
        self.assertEqual(
            plugins[0]["homepage"],
            "https://github.com/GilbertoAbrao/wxcode-design-plugins/tree/main/plugins/alpha",
        )
        self.assertEqual(plugins[0]["mode"], "prototype")
        self.assertEqual(plugins[1]["mode"], "deck")
        self.assertEqual(
            plugins[0]["publisher"],
            {
                "id": "wxcode",
                "github": "GilbertoAbrao",
                "url": "https://github.com/GilbertoAbrao/wxcode-design-plugins",
            },
        )
        self.assertEqual(
            plugins[0]["capabilitiesSummary"], ["prompt:inject", "fs:write"]
        )
        self.assertEqual(plugins[0]["license"], "MIT")

        # Preserved top-level metadata + restamped updatedAt.
        self.assertEqual(catalog["owner"], "GilbertoAbrao")
        self.assertEqual(catalog["trust"], "community")
        self.assertEqual(catalog["metadata"]["updatedAt"], FIXED_NOW)
        self.assertEqual(catalog["metadata"]["title"], "WXCode Design Plugins")

    def test_idempotent_byte_identical(self) -> None:
        self._run()
        first = self.catalog_path.read_bytes()
        self._run()
        second = self.catalog_path.read_bytes()
        self.assertEqual(first, second, "second run must be byte-identical")
        # Trailing newline + 2-space indent contract.
        self.assertTrue(second.endswith(b"\n"))
        self.assertIn(b'\n  "plugins"', second)

    def test_check_in_sync_then_stale(self) -> None:
        self._run()  # make catalog current

        # --check with a DIFFERENT now must still pass (updatedAt ignored).
        ok = self._run("--check", now="2099-12-31T23:59:59Z")
        self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)
        self.assertIn("in sync", ok.stdout)

        # Mutate a plugin manifest -> catalog is now stale.
        manifest_path = self.repo / "plugins" / "alpha" / "open-design.json"
        mf = json.loads(manifest_path.read_text(encoding="utf-8"))
        mf["title"] = "Alpha Plugin RENAMED"
        manifest_path.write_text(json.dumps(mf), encoding="utf-8")

        stale = self._run("--check")
        self.assertEqual(stale.returncode, 1, stale.stdout + stale.stderr)
        self.assertIn("stale", stale.stdout)


class RealCatalogRegressionTest(unittest.TestCase):
    """Guards that the regenerator is a faithful no-op against the live repo.

    Runs ``regen-catalog.py --check`` against the actual committed
    ``registry/wxcode-marketplace.json`` (NOT a tempdir). ``--check`` is
    read-only: it regenerates in memory and compares (ignoring
    ``metadata.updatedAt``) without ever writing the catalog. If this fails,
    the tool's entry shape has drifted from the live catalog.
    """

    def test_check_against_real_catalog_is_in_sync(self) -> None:
        # forge/tools/regen-catalog.test.py -> repo root is two levels up.
        repo_root = pathlib.Path(__file__).resolve().parents[2]
        catalog = repo_root / "registry" / "wxcode-marketplace.json"
        self.assertTrue(
            catalog.exists(),
            f"expected real catalog at {catalog}",
        )

        res = subprocess.run(
            [sys.executable, str(SCRIPT), "--check"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            res.returncode,
            0,
            f"regen-catalog.py --check reported the live catalog as stale "
            f"(the tool is not a faithful no-op):\n{res.stdout}\n{res.stderr}",
        )
        self.assertIn("in sync", res.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
