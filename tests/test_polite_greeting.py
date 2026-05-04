from daedalus_playground import polite_greeting


def test_polite_greeting_uses_default_name() -> None:
    assert polite_greeting() == "Good day, Daedalus."


def test_polite_greeting_trims_custom_name() -> None:
    assert polite_greeting("  Hermes  ") == "Good day, Hermes."


def test_polite_greeting_uses_default_for_blank_name() -> None:
    assert polite_greeting("   ") == "Good day, Daedalus."
