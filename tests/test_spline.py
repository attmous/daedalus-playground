from playground.spline import compress_ranges


def test_compress_ranges_returns_empty_string_for_empty_input() -> None:
    assert compress_ranges([]) == ""


def test_compress_ranges_renders_singletons() -> None:
    assert compress_ranges([4]) == "4"


def test_compress_ranges_renders_consecutive_runs() -> None:
    assert compress_ranges([1, 2, 3, 4]) == "1-4"


def test_compress_ranges_sorts_and_deduplicates_values() -> None:
    assert compress_ranges([4, 2, 3, 3, 1, 2]) == "1-4"


def test_compress_ranges_handles_negative_values() -> None:
    assert compress_ranges([-3, -2, -1, 1]) == "-3--1,1"


def test_compress_ranges_renders_separated_ranges() -> None:
    assert compress_ranges([1, 2, 4, 6, 7, 8, 10]) == "1-2,4,6-8,10"


def test_compress_ranges_does_not_mutate_input() -> None:
    values = [3, 1, 2, 2]
    original = values.copy()

    result = compress_ranges(values)

    assert result == "1-3"
    assert values == original
