# Agent Instructions

## Package Manager
Use **npm** for JS tooling: `npm install`, `npm run test:readme`, `npm run test:fast`.
Use the project Python environment when available: `./venv/bin/python -m pytest ...`; otherwise use `python3 scripts/run_python.py -m pytest ...`.

## File-Scoped Commands
| Task | Command |
|------|---------|
| Python test | `python3 scripts/run_python.py -m pytest tests/path_to_test.py` |
| Focused tests | `python3 scripts/run_python.py tests/run_focus.py --area security -- --maxfail=1 -q` |
| JS tests | `npm run test:js` |
| README check | `npm run test:readme` |

## Project Metadata
- Keep `package.json` `name`, `version`, repository, and AGPL license aligned for this fork.
- Keep README maintainer links: Instagram `@monrars`, site `goldneuron.io`, GitHub `@monrars1995`.
- Preserve AGPL-3.0-or-later compatibility for code and dependencies.

## Commit Attribution
AI commits MUST include:
```
Co-Authored-By: Codex <noreply@openai.com>
```

## Key Conventions
- Keep changes small and focused; follow neighboring patterns in `src/`, `core/`, `services/`, `routes/`, and `companion/`.
- Do not commit secrets, `.env`, generated caches, virtualenvs, or local runtime data.
- Follow `tests/README.md` and `tests/TESTING_STANDARD.md` when adding or changing tests.
