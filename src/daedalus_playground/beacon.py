def beacon_token(name: str = "Daedalus") -> str:
    clean_name = name.strip() or "Daedalus"
    return f"Beacon: {clean_name}"
