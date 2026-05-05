from playground.onyx import normalize_scores


def test_normalize_scores_scales_values() -> None:
    scores = {"low": 2.0, "middle": 4.0, "high": 6.0}

    assert normalize_scores(scores) == {
        "low": 0.0,
        "middle": 0.5,
        "high": 1.0,
    }


def test_normalize_scores_handles_negative_values() -> None:
    scores = {"cold": -10.0, "mild": 0.0, "hot": 10.0}

    assert normalize_scores(scores) == {
        "cold": 0.0,
        "mild": 0.5,
        "hot": 1.0,
    }


def test_normalize_scores_returns_zeroes_when_values_are_equal() -> None:
    scores = {"first": 7.0, "second": 7.0, "third": 7.0}

    assert normalize_scores(scores) == {
        "first": 0.0,
        "second": 0.0,
        "third": 0.0,
    }


def test_normalize_scores_returns_empty_dictionary_for_empty_input() -> None:
    assert normalize_scores({}) == {}


def test_normalize_scores_preserves_keys() -> None:
    scores = {"onyx": 3.0, "slate": 9.0, "jet": 6.0}

    result = normalize_scores(scores)

    assert result.keys() == scores.keys()


def test_normalize_scores_does_not_mutate_input() -> None:
    scores = {"onyx": 3.0, "slate": 9.0}
    original = scores.copy()

    result = normalize_scores(scores)

    assert scores == original
    assert result is not scores
