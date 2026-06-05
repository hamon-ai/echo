import os


def service_root(anchor):
    """Return the service root. Pass the module's __file__ as anchor."""
    return os.path.dirname(os.path.dirname(os.path.abspath(anchor)))


def resolve_path(path, base):
    """Resolve a config path relative to base. Absolute or empty paths pass through."""
    if not path or os.path.isabs(path):
        return path
    return os.path.join(base, path)
