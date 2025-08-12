from __future__ import annotations

import hashlib
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
S3_DIR = BASE_DIR / "s3"
CHECKSUM_FILE = Path(__file__).with_name("expected_checksums.json")


def compute_checksums() -> dict[str, str]:
    """Return SHA256 checksums for all HTML files under ``s3``."""
    checksums: dict[str, str] = {}
    for path in sorted(S3_DIR.rglob("*.html")):
        rel_path = path.relative_to(BASE_DIR).as_posix()
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        checksums[rel_path] = digest
    return checksums


def write_checksums() -> None:
    """Recompute and write checksums to ``expected_checksums.json``."""
    data = compute_checksums()
    with CHECKSUM_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True)
        f.write("\n")


def test_html_snapshots() -> None:
    expected = json.loads(CHECKSUM_FILE.read_text(encoding="utf-8"))
    actual = compute_checksums()
    assert actual == expected


if __name__ == "__main__":  # pragma: no cover
    write_checksums()
    print("wrote", len(compute_checksums()), "checksums")
