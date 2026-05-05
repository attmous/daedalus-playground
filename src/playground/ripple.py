def ripple_token(name: str = "Sprints") -> str:
    """Return the Ripple token for smoke tests."""
    clean_name = name.strip()
    return f"Ripple: {clean_name or 'Sprints'}"
