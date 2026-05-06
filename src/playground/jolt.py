def percentile_bucket(
    value: float, boundaries: list[float] | tuple[float, ...]
) -> str:
    """Return the percentile bucket label for a value and boundary set."""
    sorted_boundaries = sorted(boundaries)

    for index, boundary in enumerate(sorted_boundaries):
        if value <= boundary:
            return f"p{index}"

    return f"p{len(sorted_boundaries)}"
