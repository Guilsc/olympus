# Olympus project instructions

Follow the shared rules supplied by the execution host when available. Keep Olympus-specific architecture, decisions and validation guidance in this repository's `docs/` and `tests/`; use its README and Git history to understand existing conventions before changing behavior. Olympus role definitions remain in `config/`; its validation skill is scoped to `.agents/skills/` in this repository. Run `python3 -m unittest discover -s tests -v` for offline integrity checks; this does not authorize model-backed validation or production changes.
