from daedalus_playground import farewell


def test_farewell_uses_default_name() -> None:
    assert farewell() == "Goodbye, Daedalus."


def test_farewell_trims_custom_name() -> None:
    assert farewell("  Hermes  ") == "Goodbye, Hermes."


def test_farewell_falls_back_for_blank_name() -> None:
    assert farewell("   ") == "Goodbye, Daedalus."
