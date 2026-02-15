import os
from pathlib import Path

from github_actions.debug import debug


class ActionsCache:

    def __init__(self, cache_dir: Path, label: str=None):
        self._cache_dir = cache_dir
        self._label = label or self._cache_dir

    def _get_path(self, key: str) -> Path:
        """Get the full path for a cache key"""
        return Path(self._cache_dir) / key

    def __setitem__(self, key, value):
        if value is None:
            debug(f'Cache value for {key} should not be set to {value}')
            return

        path = self._get_path(key)

        os.makedirs(path.parent, exist_ok=True)
        with open(path, 'w') as f:
            f.write(value)
            debug(f'Wrote {key} to {self._label}')

    def __getitem__(self, key):
        path = self._get_path(key)
        if path.is_file():
            with open(path) as f:
                debug(f'Read {key} from {self._label}')
                return f.read()

        raise IndexError(key)

    def __contains__(self, key):
        return self._get_path(key).is_file()
