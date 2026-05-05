from playground.willow import willow_token


def test_willow_token_uses_default_name() -> None:
    assert willow_token() == "Willow: Sprints"


def test_willow_token_trims_custom_name() -> None:
    assert willow_token("  Hermes  ") == "Willow: Hermes"


def test_willow_token_uses_default_for_blank_name() -> None:
    assert willow_token("   ") == "Willow: Sprints"
