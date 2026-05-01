from daedalus_playground import salutation


def test_salutation_uses_default_name() -> None:
    assert salutation() == "Salutations, Daedalus."


def test_salutation_uses_custom_name() -> None:
    assert salutation("Hermes") == "Salutations, Hermes."
