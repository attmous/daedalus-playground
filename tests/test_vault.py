from playground.vault import match_policy


def test_match_policy_returns_exact_match() -> None:
    rules = {
        "secret/app/config": "app-config",
        "secret/app/token": "app-token",
    }

    assert match_policy("secret/app/config", rules) == "app-config"


def test_match_policy_supports_single_star_within_one_segment() -> None:
    rules = {
        "secret/app-*/config": "app-config",
    }

    assert match_policy("secret/app-prod/config", rules) == "app-config"
    assert match_policy("secret/app-prod/us/config", rules) is None


def test_match_policy_supports_double_star_across_segments() -> None:
    rules = {
        "secret/**/config": "nested-config",
    }

    assert match_policy("secret/team/app/config", rules) == "nested-config"
    assert match_policy("secret/config", rules) == "nested-config"


def test_match_policy_chooses_longest_matching_pattern() -> None:
    rules = {
        "secret/**": "broad",
        "secret/app/*": "app",
        "secret/app/config": "config",
    }

    assert match_policy("secret/app/config", rules) == "config"


def test_match_policy_uses_alphabetical_tie_breaker() -> None:
    rules = {
        "secret/a*": "prefix",
        "secret/*a": "suffix",
    }

    assert match_policy("secret/aa", rules) == "suffix"


def test_match_policy_returns_none_when_nothing_matches() -> None:
    rules = {
        "secret/app/*": "app",
    }

    assert match_policy("secret/app/prod/config", rules) is None


def test_match_policy_normalizes_repeated_slashes_in_input_path() -> None:
    rules = {
        "secret/app/config": "app-config",
    }

    assert match_policy("secret//app///config", rules) == "app-config"
