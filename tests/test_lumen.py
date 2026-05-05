from playground.lumen import lumen_token


def test_lumen_token_uses_default_name() -> None:
    assert lumen_token() == "Lumen: Sprints"


def test_lumen_token_trims_custom_name() -> None:
    assert lumen_token("  Hermes  ") == "Lumen: Hermes"


def test_lumen_token_uses_default_for_blank_name() -> None:
    assert lumen_token("   ") == "Lumen: Sprints"
