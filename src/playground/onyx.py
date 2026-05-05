def normalize_scores(scores: dict[str, float]) -> dict[str, float]:
    """Scale score values into the 0.0 to 1.0 range."""
    if not scores:
        return {}

    minimum = min(scores.values())
    maximum = max(scores.values())

    if minimum == maximum:
        return {key: 0.0 for key in scores}

    spread = maximum - minimum
    return {key: (value - minimum) / spread for key, value in scores.items()}
