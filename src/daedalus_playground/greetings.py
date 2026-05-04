def _normalize_name(name: str) -> str:
    clean_name = name.strip()
    return clean_name or "Daedalus"


def greeting(name: str = "Daedalus") -> str:
    """Return a predictable greeting for smoke tests."""
    clean_name = _normalize_name(name)
    return f"Hello, {clean_name}!"


def salutation(name: str = "Daedalus") -> str:
    """Return the requested salutation helper."""
    clean_name = _normalize_name(name)
    return f"Salutations, {clean_name}."
