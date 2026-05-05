from playground.yonder import yonder_token


def test_yonder_token_uses_default_name() -> None:
    assert yonder_token() == "Yonder: Sprints"


def test_yonder_token_trims_custom_name() -> None:
    assert yonder_token("  Hermes  ") == "Yonder: Hermes"


def test_yonder_token_uses_default_for_blank_name() -> None:
    assert yonder_token("   ") == "Yonder: Sprints"
