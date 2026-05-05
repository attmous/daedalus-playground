import re


def match_policy(path: str, rules: dict[str, str]) -> str | None:
    """Return the policy for the most specific matching vault path rule."""
    normalized_path = _normalize_path(path)
    matches = [
        pattern for pattern in rules if _pattern_matches(pattern, normalized_path)
    ]
    if not matches:
        return None

    best_pattern = min(matches, key=lambda pattern: (-len(pattern), pattern))
    return rules[best_pattern]


def _normalize_path(path: str) -> str:
    return re.sub(r"/+", "/", path)


def _pattern_matches(pattern: str, path: str) -> bool:
    pattern_segments = pattern.split("/")
    path_segments = path.split("/")

    def matches_from(pattern_index: int, path_index: int) -> bool:
        if pattern_index == len(pattern_segments):
            return path_index == len(path_segments)

        pattern_segment = pattern_segments[pattern_index]
        if pattern_segment == "**":
            if pattern_index == len(pattern_segments) - 1:
                return True
            return any(
                matches_from(pattern_index + 1, next_path_index)
                for next_path_index in range(path_index, len(path_segments) + 1)
            )

        if path_index == len(path_segments):
            return False

        return _segment_matches(
            pattern_segment,
            path_segments[path_index],
        ) and matches_from(pattern_index + 1, path_index + 1)

    return matches_from(0, 0)


def _segment_matches(pattern: str, segment: str) -> bool:
    regex = "".join(
        "[^/]*" if character == "*" else re.escape(character)
        for character in pattern
    )
    return re.fullmatch(regex, segment) is not None
