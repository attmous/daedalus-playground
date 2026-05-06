from playground.emberly import parse_headers


def test_parse_headers_ignores_blank_no_colon_and_blank_keys() -> None:
    assert parse_headers(["", "   ", "No colon", "  : value", "Host: example.com"]) == {
        "host": "example.com",
    }


def test_parse_headers_trims_and_normalizes_keys_and_values() -> None:
    assert parse_headers(["  Content-Type  :  text/plain  "]) == {
        "content-type": "text/plain",
    }


def test_parse_headers_last_duplicate_key_wins() -> None:
    assert parse_headers(["X-Mode: first", " x-mode : second"]) == {
        "x-mode": "second",
    }


def test_parse_headers_keeps_colons_inside_values() -> None:
    assert parse_headers(["Location: https://example.com/a:b"]) == {
        "location": "https://example.com/a:b",
    }
