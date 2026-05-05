def lumen_token(name: str = "Sprints") -> str:
    """Return the Lumen token for smoke tests."""
    clean_name = name.strip()
    return f"Lumen: {clean_name or 'Sprints'}"
