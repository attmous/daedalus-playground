from playground.cipher import redact_secrets


def test_redacts_token_assignment() -> None:
    assert redact_secrets("token=abc123") == "token=[REDACTED]"


def test_redacts_api_key_assignment_case_insensitively() -> None:
    assert redact_secrets("API_KEY=secret-value") == "API_KEY=[REDACTED]"


def test_redacts_secret_colon_assignment() -> None:
    assert redact_secrets("secret: hunter2") == "secret: [REDACTED]"


def test_redacts_mixed_text_without_changing_other_content() -> None:
    text = "start token=one middle api_key=two end secret: three"
    assert (
        redact_secrets(text)
        == "start token=[REDACTED] middle api_key=[REDACTED] end secret: [REDACTED]"
    )


def test_preserves_punctuation_boundaries() -> None:
    text = "token=one, api_key=two; secret: three done"
    assert (
        redact_secrets(text)
        == "token=[REDACTED], api_key=[REDACTED]; secret: [REDACTED] done"
    )


def test_leaves_non_secret_text_unchanged() -> None:
    text = "username=ada password: open-sesame note tokenless"
    assert redact_secrets(text) == text
