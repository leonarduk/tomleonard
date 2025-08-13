from pathlib import Path

def test_stylesheet_snapshot():
    css = Path('s3/styles.css').read_text()
    snapshot = Path('tests/snapshots/styles.css.snap').read_text()
    assert css == snapshot
