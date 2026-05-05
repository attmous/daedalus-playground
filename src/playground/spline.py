def compress_ranges(values: list[int]) -> str:
    """Compress integer values into comma-delimited consecutive ranges."""
    sorted_values = sorted(set(values))
    if not sorted_values:
        return ""

    parts: list[str] = []
    start = previous = sorted_values[0]

    for value in sorted_values[1:]:
        if value == previous + 1:
            previous = value
            continue

        parts.append(_format_range(start, previous))
        start = previous = value

    parts.append(_format_range(start, previous))
    return ",".join(parts)


def _format_range(start: int, end: int) -> str:
    if start == end:
        return str(start)

    return f"{start}-{end}"
