# tomleonard

[![FTP](https://github.com/leonarduk/tomleonard/actions/workflows/ftp.yml/badge.svg)](https://github.com/leonarduk/tomleonard/actions/workflows/ftp.yml)
[![S3](https://github.com/leonarduk/tomleonard/actions/workflows/s3.yml/badge.svg)](https://github.com/leonarduk/tomleonard/actions/workflows/s3.yml)

This publishes to 
http://tomleonard.co.uk

All content owned by Tom Leonard Literary Estate

## Snapshot checks

HTML files under `s3/` are tracked with SHA256 digests. The expected values live in `tests/expected_checksums.json`.

When HTML changes are intentional, regenerate the snapshot file by running:

```bash
python tests/test_snapshots.py
```

This updates `tests/expected_checksums.json` so tests pass with the new content.
