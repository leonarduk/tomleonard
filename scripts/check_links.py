#!/usr/bin/env python3
"""Utility to verify that local href/src links in HTML files exist.

This script scans the given root directory (default: ``s3/``) for HTML files and
checks that every ``href`` or ``src`` attribute that refers to a local file
points to something present on disk.

The check is purposely limited to common static file extensions; links with
schemes (``http:``, ``mailto:``, etc.) or with extensions outside the allowlist
are ignored.
"""
from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
from typing import Iterable, List, Tuple

# Common static file extensions we care about.
ALLOWED_EXTENSIONS = {
    '.html', '.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.svg',
    '.mp3', '.mp4', '.pdf', '.txt', '.ico', '.wav', '.ogg', '.zip',
    '.xml', '.webm', '.mpg', '.mpeg', '.mov', '.mkv', '.json'
}


class LinkCollector(HTMLParser):
    """Collects href and src attributes while parsing HTML."""

    def __init__(self) -> None:
        super().__init__()
        self.links: List[str] = []

    def handle_starttag(self, tag: str, attrs: Iterable[Tuple[str, str]]) -> None:
        for attr, value in attrs:
            if attr in {"href", "src"}:
                self.links.append(value)


def is_local(url: str) -> bool:
    """Return True if *url* looks like a local file reference."""
    if not url or url.startswith('#'):
        return False
    parsed = urlparse(url)
    if parsed.scheme or url.startswith('//'):
        return False
    return True


def find_missing(root: Path) -> List[Tuple[Path, str]]:
    """Return list of (html_file_relative_path, broken_link)."""
    missing: List[Tuple[Path, str]] = []
    for html in root.rglob('*.html'):
        parser = LinkCollector()
        parser.feed(html.read_text(encoding='utf-8'))
        for link in parser.links:
            if not is_local(link):
                continue
            parsed = urlparse(link)
            path = parsed.path
            suffix = Path(path).suffix.lower()
            if suffix and suffix not in ALLOWED_EXTENSIONS:
                # Skip non-static extensions like .php
                continue
            target = (root / path.lstrip('/')) if path.startswith('/') else (html.parent / path)
            if not target.exists():
                missing.append((html.relative_to(root), link))
    return missing


def main(argv: List[str]) -> int:
    root = Path(argv[1]) if len(argv) > 1 else Path('s3')
    broken = find_missing(root)
    if broken:
        for html, link in broken:
            print(f"{html}: {link}")
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
