import pytest

from playground.zenith import score_band, summarize_bands


@pytest.mark.parametrize(
    ("score", "expected"),
    [
        (0, "low"),
        (49.999, "low"),
        (50, "medium"),
        (79.999, "medium"),
        (80, "high"),
        (94.999, "high"),
        (95, "elite"),
        (100, "elite"),
    ],
)
def test_score_band_boundaries(score, expected):
    assert score_band(score) == expected


@pytest.mark.parametrize("score", [-0.001, 100.001])
def test_score_band_rejects_scores_outside_inclusive_range(score):
    with pytest.raises(ValueError, match="between 0 and 100"):
        score_band(score)


def test_summarize_bands_counts_scores_by_band():
    assert summarize_bands([10, 49.999, 50, 80, 94.999, 95, 100]) == {
        "low": 2,
        "medium": 1,
        "high": 2,
        "elite": 2,
    }


def test_summarize_bands_empty_summary_includes_all_bands():
    assert summarize_bands([]) == {
        "low": 0,
        "medium": 0,
        "high": 0,
        "elite": 0,
    }


def test_summarize_bands_returns_all_band_keys_when_counts_are_zero():
    assert set(summarize_bands([100])) == {"low", "medium", "high", "elite"}
