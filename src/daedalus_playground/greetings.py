def greeting(name: str = "Daedalus") -> str:
    """Return a predictable greeting for smoke tests."""
    clean_name = name.strip() or "Daedalus"
    return f"Hello, {clean_name}!"


def salutation(name: str = "Daedalus") -> str:
    """Return the requested salutation helper."""
    return f"Salutations, {name}."
