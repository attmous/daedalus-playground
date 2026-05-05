def yonder_token(name: str = "Sprints") -> str:
    """Return the Yonder token for smoke tests."""
    clean_name = name.strip()
    return f"Yonder: {clean_name or 'Sprints'}"
