#!/usr/bin/env python3
"""Verify recovered CAD/binary artifacts against the 2026-08-26 checkpoint hashes.

By default missing files are reported but do not cause failure, because the
GitHub chat connector used for the original archival session could not upload
local binary files directly. Any file that *is* present and has a wrong size or
SHA-256 is an error.

Use --strict once all binary artifacts have been copied into the repository.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "BINARY_ARTIFACT_CHECKSUMS.json"

SEARCH_DIRS = [
    ROOT,
    ROOT / "cad",
    ROOT / "cad" / "current",
    ROOT / "cad" / "archive",
    ROOT / "simulation",
    ROOT / "artifacts",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def find_file(name: str) -> Path | None:
    for base in SEARCH_DIRS:
        candidate = base / name
        if candidate.is_file():
            return candidate
    # Allow organized subfolders under cad/artifacts without assuming names.
    for base in [ROOT / "cad", ROOT / "artifacts", ROOT / "simulation"]:
        if base.exists():
            matches = list(base.rglob(name))
            if matches:
                return matches[0]
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--strict",
        action="store_true",
        help="fail if any manifest artifact is missing",
    )
    args = parser.parse_args()

    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    artifacts = data["artifacts"]

    missing = []
    bad = []
    verified = []

    for item in artifacts:
        name = item["filename"]
        expected_bytes = int(item["bytes"])
        expected_sha = item["sha256"].lower()
        path = find_file(name)

        if path is None:
            missing.append(name)
            print(f"MISSING  {name}")
            continue

        actual_bytes = path.stat().st_size
        actual_sha = sha256(path)
        size_ok = actual_bytes == expected_bytes
        sha_ok = actual_sha == expected_sha

        if size_ok and sha_ok:
            verified.append(name)
            print(f"OK       {name}  [{path.relative_to(ROOT)}]")
        else:
            bad.append(name)
            print(f"BAD      {name}")
            print(f"         expected bytes: {expected_bytes}")
            print(f"         actual bytes  : {actual_bytes}")
            print(f"         expected sha  : {expected_sha}")
            print(f"         actual sha    : {actual_sha}")

    print()
    print(f"verified: {len(verified)}")
    print(f"missing : {len(missing)}")
    print(f"bad     : {len(bad)}")

    if bad:
        raise SystemExit("FAIL: one or more present artifacts do not match the archived checkpoint")
    if args.strict and missing:
        raise SystemExit("FAIL: --strict requested and one or more artifacts are missing")

    if missing:
        print("PASS (non-strict): all present files match; missing binaries are still awaiting upload")
    else:
        print("PASS: every archived binary artifact matches size and SHA-256")


if __name__ == "__main__":
    main()
