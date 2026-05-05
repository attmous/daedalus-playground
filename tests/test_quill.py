import pytest

from playground.quill import parse_front_matter


def test_parse_front_matter_parses_metadata_and_body() -> None:
    text = "---\ntitle: Hello\nslug: hello-world\n---\nBody text\n"

    metadata, body = parse_front_matter(text)

    assert metadata == {"title": "Hello", "slug": "hello-world"}
    assert body == "Body text\n"


def test_parse_front_matter_returns_original_text_without_opening_delimiter() -> None:
    text = "title: Hello\n---\nBody text\n"

    metadata, body = parse_front_matter(text)

    assert metadata == {}
    assert body == text


def test_parse_front_matter_ignores_blank_lines() -> None:
    text = "---\n\n title :  Hello  \n   \ncategory: Notes\n---\nBody\n"

    metadata, body = parse_front_matter(text)

    assert metadata == {"title": "Hello", "category": "Notes"}
    assert body == "Body\n"


def test_parse_front_matter_raises_for_malformed_nonblank_line() -> None:
    text = "---\ntitle Hello\n---\nBody\n"

    with pytest.raises(ValueError, match="malformed front matter line"):
        parse_front_matter(text)


def test_parse_front_matter_raises_for_missing_closing_delimiter() -> None:
    text = "---\ntitle: Hello\nsummary: Body\n"

    with pytest.raises(ValueError, match="missing closing front matter delimiter"):
        parse_front_matter(text)


def test_parse_front_matter_preserves_body_exactly_after_closing_delimiter() -> None:
    body = "\n# Heading\n\nBody: with colon\n---\n"
    text = f"---\ntitle: Hello\n---\n{body}"

    metadata, parsed_body = parse_front_matter(text)

    assert metadata == {"title": "Hello"}
    assert parsed_body == body
