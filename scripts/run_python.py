#!/usr/bin/env python3
"""Run a Python command with the project's minimum supported Python version."""

from __future__ import annotations

import shutil
import subprocess
import sys


MIN_VERSION = (3, 11)
PYTHON_CANDIDATES = ("python3.14", "python3.13", "python3.12", "python3.11", "python3")


def _supports_project_python(executable: str) -> bool:
    try:
        result = subprocess.run(
            [
                executable,
                "-c",
                "import sys; raise SystemExit(0 if sys.version_info >= (3, 11) else 1)",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
    except OSError:
        return False
    return result.returncode == 0


def _select_python() -> str | None:
    if sys.version_info >= MIN_VERSION:
        return sys.executable

    for candidate in PYTHON_CANDIDATES:
        executable = shutil.which(candidate)
        if executable and _supports_project_python(executable):
            return executable

    return None


def main() -> int:
    if len(sys.argv) < 2:
        print(
            "usage: python3 scripts/run_python.py [-m module|script.py] [args...]",
            file=sys.stderr,
        )
        return 2

    executable = _select_python()
    if not executable:
        print(
            "Python 3.11+ is required. Install Python 3.11 or newer, or activate a compatible venv.",
            file=sys.stderr,
        )
        return 2

    return subprocess.call([executable, *sys.argv[1:]])


if __name__ == "__main__":
    raise SystemExit(main())
