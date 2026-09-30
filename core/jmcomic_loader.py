"""
JMComic optional dependency loader.
"""

from typing import Any


def import_jmcomic() -> Any | None:
    """Import jmcomic lazily and safely.

    Returns the module, or None if jmcomic is not installed. Plugin startup
    must not require jmcomic, so every caller goes through this single entry
    point instead of importing jmcomic directly.
    """
    try:
        import jmcomic
    except ImportError:
        return None
    return jmcomic
