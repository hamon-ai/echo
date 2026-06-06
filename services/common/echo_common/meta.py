import os
import tomllib


def service_version(anchor):
    """Read version from the service's pyproject.toml."""
    path = os.path.join(os.path.dirname(os.path.abspath(anchor)), "pyproject.toml")
    try:
        with open(path, "rb") as f:
            return str(tomllib.load(f).get("project", {}).get("version", "0.0"))
    except OSError:
        return "0.0"
