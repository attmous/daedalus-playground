def split_commands(text: str) -> list[str]:
    """Split semicolon-delimited commands outside quoted text."""
    commands: list[str] = []
    current: list[str] = []
    quote: str | None = None

    for character in text:
        if character in {"'", '"'}:
            if quote is None:
                quote = character
            elif quote == character:
                quote = None
            current.append(character)
            continue

        if character == ";" and quote is None:
            command = "".join(current).strip()
            if command:
                commands.append(command)
            current = []
            continue

        current.append(character)

    if quote is not None:
        raise ValueError(f"unmatched {quote} quote")

    command = "".join(current).strip()
    if command:
        commands.append(command)

    return commands
