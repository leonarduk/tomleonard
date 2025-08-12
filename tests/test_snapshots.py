from __future__ import annotations

import hashlib
import json
from pathlib import Path

from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parents[1]
S3_DIR = BASE_DIR / "s3"
CHECKSUM_FILE = Path(__file__).with_name("expected_checksums.json")


def rendered_text(path: Path) -> str:
    """Return visible text for ``path`` as a browser would render."""
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    return soup.get_text(separator="\n", strip=True)


def compute_checksums() -> dict[str, str]:
    """Return SHA256 checksums for rendered text of all HTML files under ``s3``."""
    checksums: dict[str, str] = {}
    for path in sorted(S3_DIR.rglob("*.html")):
        rel_path = path.relative_to(BASE_DIR).as_posix()
        text = rendered_text(path)
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
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
