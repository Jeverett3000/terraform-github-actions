"""
Wraps python-hcl
"""

import hcl2  # type: ignore
import sys
from pathlib import Path

from github_actions.debug import debug


def try_load(path: Path) -> dict | None:
    """
    Try to load HCL file, returning None if it cannot be loaded.
    """
    try:
        with open(path) as f:
            return hcl2.load(f)
    except Exception:
        return None


def load(path: Path) -> dict:
    """
    Load HCL file directly without subprocess validation.
    This is more efficient as it avoids spawning a subprocess for validation.
    """
    result = try_load(path)
    if result is not None:
        return result

    debug(f'Unable to load {path}')
    raise ValueError(f'Unable to load {path}')


def loads(hcl: str) -> dict:
    """
    Load HCL from string directly without subprocess validation.
    """
    try:
        return hcl2.loads(hcl)
    except Exception as e:
        debug(f'Unable to load hcl: {e}')
        raise ValueError(f'Unable to load hcl') from e


if __name__ == '__main__':
    try_load(Path(sys.argv[1]))
