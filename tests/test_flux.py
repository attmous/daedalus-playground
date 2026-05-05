import pytest

from playground.flux import retry_delays


def test_retry_delays_returns_empty_list_for_zero_attempts() -> None:
    assert retry_delays(0) == []


def test_retry_delays_uses_basic_exponential_schedule() -> None:
    assert retry_delays(5) == [2, 4, 8, 16, 32]


def test_retry_delays_caps_each_delay() -> None:
    assert retry_delays(6, cap=10) == [2, 4, 8, 10, 10, 10]


def test_retry_delays_accepts_custom_base() -> None:
    assert retry_delays(4, base=3) == [3, 6, 12, 24]


@pytest.mark.parametrize(
    ("attempts", "base", "cap"),
    [
        (-1, 2, 60),
        (1, 0, 60),
        (1, 2, 0),
    ],
)
def test_retry_delays_rejects_invalid_arguments(
    attempts: int, base: int, cap: int
) -> None:
    with pytest.raises(ValueError):
        retry_delays(attempts, base=base, cap=cap)
