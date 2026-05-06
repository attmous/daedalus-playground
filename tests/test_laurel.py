from copy import deepcopy

import pytest

from playground.laurel import expand_aliases


def test_expand_aliases_replaces_simple_alias() -> None:
    aliases = {"warm": ["sun", "ember"]}

    assert expand_aliases(["warm"], aliases) == ["sun", "ember"]


def test_expand_aliases_recursively_expands_aliases() -> None:
    aliases = {
        "bouquet": ["laurel", "sage"],
        "laurel": ["leaf", "crown"],
    }

    assert expand_aliases(["bouquet"], aliases) == ["leaf", "crown", "sage"]


def test_expand_aliases_passes_through_values_without_aliases() -> None:
    aliases = {"known": ["expanded"]}

    assert expand_aliases(["start", "known", "end"], aliases) == [
        "start",
        "expanded",
        "end",
    ]


def test_expand_aliases_preserves_duplicate_expanded_values() -> None:
    aliases = {
        "pair": ["leaf", "leaf"],
        "bundle": ["pair", "leaf"],
    }

    assert expand_aliases(["bundle", "pair"], aliases) == [
        "leaf",
        "leaf",
        "leaf",
        "leaf",
        "leaf",
    ]


def test_expand_aliases_detects_cycles() -> None:
    aliases = {
        "a": ["b"],
        "b": ["c"],
        "c": ["a"],
    }

    with pytest.raises(ValueError, match="alias cycle detected"):
        expand_aliases(["a"], aliases)


def test_expand_aliases_passes_through_missing_alias_targets() -> None:
    aliases = {"root": ["known", "missing"], "known": ["leaf"]}

    assert expand_aliases(["root"], aliases) == ["leaf", "missing"]


def test_expand_aliases_does_not_mutate_inputs() -> None:
    items = ["root", "plain"]
    aliases = {"root": ["branch"], "branch": ["leaf"]}
    original_items = list(items)
    original_aliases = deepcopy(aliases)

    expand_aliases(items, aliases)

    assert items == original_items
    assert aliases == original_aliases
