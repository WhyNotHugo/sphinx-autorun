# Changelog

## v2.0.0

- Update supported Pythons to 3.9 to 3.13.
- Prefer sys.executable over `python`.
- Return extension metadata on `setup()`. This enabled handling multiple files
  in parallel.
- Switch from `setup.py` to `pyproject.toml`.
- Remove bogus argument `bufsize=1` from `Popen` call, which resulted in a
  `RuntimeWarning`.
