def greeting(name: str = "Daedalus") -> str:
    """Return a predictable greeting for smoke tests."""
    clean_name = name.strip() or "Daedalus"
    return f"Hello, {clean_name}!"


def salutation(name: str = "Daedalus") -> str:
    """Return the requested salutation helper."""
    return f"Salutations, {name}."


def polite_greeting(name: str = "Daedalus") -> str:
    """Return a polite greeting with a fallback name."""
    clean_name = name.strip() or "Daedalus"
    return f"Good day, {clean_name}."
