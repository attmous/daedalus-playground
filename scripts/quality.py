from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_ci() -> int:
    env = os.environ.copy()
    src_path = str(ROOT / "src")
    existing = env.get("PYTHONPATH")
    env["PYTHONPATH"] = src_path if not existing else os.pathsep.join([src_path, existing])
    return subprocess.call([sys.executable, "-m", "pytest", "-q"], cwd=ROOT, env=env)


def main() -> int:
    parser = argparse.ArgumentParser(description="Repository quality checks.")
    parser.add_argument("command", choices=["ci"])
    args = parser.parse_args()
    if args.command == "ci":
        return run_ci()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
