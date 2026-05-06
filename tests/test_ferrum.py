from playground.ferrum import retry_delays


def test_retry_delays_returns_empty_list_for_zero_attempts() -> None:
    assert retry_delays(0) == []


def test_retry_delays_clamps_negative_attempts_to_zero() -> None:
    assert retry_delays(-3) == []


def test_retry_delays_uses_default_exponential_growth() -> None:
    assert retry_delays(5) == [1, 2, 4, 8, 16]


def test_retry_delays_caps_delays_at_maximum() -> None:
    assert retry_delays(5, initial=10, multiplier=3, maximum=25) == [
        10,
        25,
        25,
        25,
        25,
    ]


def test_retry_delays_clamps_parameters_to_at_least_one() -> None:
    assert retry_delays(4, initial=0, multiplier=0, maximum=0) == [1, 1, 1, 1]
