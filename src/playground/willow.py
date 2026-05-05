def willow_token(name: str = "Sprints") -> str:
    """Return the Willow token for smoke tests."""
    clean_name = name.strip()
    return f"Willow: {clean_name or 'Sprints'}"
