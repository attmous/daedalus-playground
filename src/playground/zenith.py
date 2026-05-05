"""Zenith score band helpers."""

BAND_KEYS = ("low", "medium", "high", "elite")


def score_band(score: float) -> str:
    """Return the zenith band for a score between 0 and 100 inclusive."""
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100 inclusive")

    if score < 50:
        return "low"
    if score < 80:
        return "medium"
    if score < 95:
        return "high"
    return "elite"


def summarize_bands(scores: list[float]) -> dict[str, int]:
    """Count zenith score bands for the provided scores."""
    summary = dict.fromkeys(BAND_KEYS, 0)
    for score in scores:
        summary[score_band(score)] += 1
    return summary
