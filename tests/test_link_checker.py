from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))
from scripts.check_links import find_missing

def test_all_local_links_exist():
    missing = find_missing(Path('s3'))
    assert missing == [], f"Missing files: {missing}"
