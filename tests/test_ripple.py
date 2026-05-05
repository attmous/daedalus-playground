from playground.ripple import ripple_token


def test_ripple_token_uses_default_name() -> None:
    assert ripple_token() == "Ripple: Sprints"


def test_ripple_token_trims_custom_name() -> None:
    assert ripple_token("  Hermes  ") == "Ripple: Hermes"


def test_ripple_token_uses_default_for_blank_name() -> None:
    assert ripple_token("   ") == "Ripple: Sprints"
