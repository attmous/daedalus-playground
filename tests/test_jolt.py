from playground.jolt import percentile_bucket


def test_percentile_bucket_sorts_unsorted_boundaries() -> None:
    assert percentile_bucket(15.0, [30.0, 10.0, 20.0]) == "p1"


def test_percentile_bucket_uses_lower_bucket_for_exact_boundaries() -> None:
    boundaries = (10.0, 20.0, 30.0)

    assert percentile_bucket(10.0, boundaries) == "p0"
    assert percentile_bucket(20.0, boundaries) == "p1"
    assert percentile_bucket(30.0, boundaries) == "p2"


def test_percentile_bucket_returns_last_bucket_above_all_boundaries() -> None:
    assert percentile_bucket(31.0, [10.0, 20.0, 30.0]) == "p3"


def test_percentile_bucket_does_not_mutate_input_boundaries() -> None:
    boundaries = [30.0, 10.0, 20.0]

    assert percentile_bucket(15.0, boundaries) == "p1"
    assert boundaries == [30.0, 10.0, 20.0]
