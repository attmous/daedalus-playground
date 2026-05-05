from playground.cairn import markdown_outline


def test_markdown_outline_parses_heading_levels() -> None:
    text = "\n".join(
        [
            "# Page",
            "## Section",
            "### Subsection",
            "#### Detail",
            "##### Note",
            "###### Fine print",
        ]
    )

    assert markdown_outline(text) == [
        {"level": 1, "title": "Page"},
        {"level": 2, "title": "Section"},
        {"level": 3, "title": "Subsection"},
        {"level": 4, "title": "Detail"},
        {"level": 5, "title": "Note"},
        {"level": 6, "title": "Fine print"},
    ]


def test_markdown_outline_ignores_invalid_headings() -> None:
    text = "\n".join(
        [
            "#Valid without required space",
            "####### Too deep",
            " ## Indented",
            "# Valid",
        ]
    )

    assert markdown_outline(text) == [{"level": 1, "title": "Valid"}]


def test_markdown_outline_ignores_headings_inside_fenced_code() -> None:
    text = "\n".join(
        [
            "# Outside",
            "```python",
            "## Inside",
            "```",
            "### Outside again",
        ]
    )

    assert markdown_outline(text) == [
        {"level": 1, "title": "Outside"},
        {"level": 3, "title": "Outside again"},
    ]


def test_markdown_outline_strips_trailing_hash_markers() -> None:
    assert markdown_outline("## Section ###") == [
        {"level": 2, "title": "Section"}
    ]


def test_markdown_outline_strips_surrounding_title_whitespace() -> None:
    assert markdown_outline("###   Spaced title   ###   ") == [
        {"level": 3, "title": "Spaced title"}
    ]


def test_markdown_outline_returns_empty_list_for_empty_text() -> None:
    assert markdown_outline("") == []
