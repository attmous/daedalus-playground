def orbit_token(name: str = "Sprints") -> str:
    clean_name = name.strip() or "Sprints"
    return f"Orbit: {clean_name}"
