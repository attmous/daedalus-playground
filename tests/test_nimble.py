import pytest

from playground.nimble import split_commands


def test_split_commands_splits_simple_semicolon_delimited_commands() -> None:
    assert split_commands("build;test;deploy") == ["build", "test", "deploy"]


def test_split_commands_keeps_semicolons_inside_single_quotes() -> None:
    assert split_commands("say 'hello; there'; run") == [
        "say 'hello; there'",
        "run",
    ]


def test_split_commands_keeps_semicolons_inside_double_quotes() -> None:
    assert split_commands('say "hello; there"; run') == [
        'say "hello; there"',
        "run",
    ]


def test_split_commands_handles_mixed_quote_types() -> None:
    text = 'alpha "keep; this"; beta \'and "this; too"\'; gamma'

    assert split_commands(text) == [
        'alpha "keep; this"',
        'beta \'and "this; too"\'',
        "gamma",
    ]


def test_split_commands_drops_empty_entries() -> None:
    assert split_commands("alpha;; ; beta;") == ["alpha", "beta"]


def test_split_commands_strips_whitespace_around_commands() -> None:
    assert split_commands("  alpha  ;\n beta\t ; gamma  ") == [
        "alpha",
        "beta",
        "gamma",
    ]


@pytest.mark.parametrize("text", ["alpha 'unterminated", 'alpha "unterminated'])
def test_split_commands_raises_for_unmatched_quotes(text: str) -> None:
    with pytest.raises(ValueError):
        split_commands(text)
