from playground.orbit import orbit_token


def test_orbit_token_uses_default_name() -> None:
    assert orbit_token() == "Orbit: Sprints"


def test_orbit_token_trims_custom_name() -> None:
    assert orbit_token("  Hermes  ") == "Orbit: Hermes"


def test_orbit_token_falls_back_for_blank_name() -> None:
    assert orbit_token("   ") == "Orbit: Sprints"
