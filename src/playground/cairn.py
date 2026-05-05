import re


_HEADING_PATTERN = re.compile(r"^(#+) (.*)$")
_FENCE_MARKER = "```"


def markdown_outline(text: str) -> list[dict[str, object]]:
    """Return ATX headings found outside triple-backtick fenced code blocks."""
    outline: list[dict[str, object]] = []
    in_fence = False

    for line in text.splitlines():
        if line.strip().startswith(_FENCE_MARKER):
            in_fence = not in_fence
            continue

        if in_fence:
            continue

        match = _HEADING_PATTERN.match(line)
        if match is None:
            continue

        level = len(match.group(1))
        if level > 6:
            continue

        title = match.group(2).strip().rstrip("#").strip()
        outline.append({"level": level, "title": title})

    return outline
