def parse_priority(value: str) -> dict[str, object]:
    """Parse a Brio priority value into a normalized priority summary."""
    normalized = value.strip().lower()
    level = _parse_level(normalized)

    if level is None:
        level = 3

    label = "normal" if level == 3 else f"p{level}"
    return {
        "level": level,
        "label": label,
        "urgent": level in {0, 1},
    }


def _parse_level(value: str) -> int | None:
    if value == "normal":
        return 3

    if value.startswith("priority:"):
        return _parse_known_level(value.removeprefix("priority:").strip())

    if value.startswith("p"):
        return _parse_known_level(value.removeprefix("p").strip())

    return _parse_known_level(value)


def _parse_known_level(value: str) -> int | None:
    if not value.isdecimal():
        return None

    level = int(value)
    if level in {0, 1, 2, 3}:
        return level

    return None
