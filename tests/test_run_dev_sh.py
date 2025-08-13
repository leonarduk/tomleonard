import os
import subprocess
from pathlib import Path


def test_run_dev_requires_npm(tmp_path):
    # Create dummy package.json so the script progresses to npm check
    (tmp_path / 'package.json').write_text('{}')
    script = Path(__file__).resolve().parent.parent / 'run-dev.sh'
    env = os.environ.copy()
    env['PATH'] = '/nonexistent'
    result = subprocess.run(['/bin/bash', str(script)], cwd=tmp_path, capture_output=True, text=True, env=env)
    assert result.returncode != 0
    assert 'npm is not installed' in result.stderr
