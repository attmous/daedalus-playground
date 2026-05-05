import pytest

from playground.pylon import sort_dependencies


def test_sort_dependencies_orders_simple_chain() -> None:
    graph = {
        "app": ["service"],
        "service": ["database"],
        "database": [],
    }

    assert sort_dependencies(graph) == ["database", "service", "app"]


def test_sort_dependencies_orders_branching_graph() -> None:
    graph = {
        "app": ["api", "worker"],
        "api": ["database"],
        "worker": ["database", "queue"],
        "database": [],
        "queue": [],
    }

    assert sort_dependencies(graph) == [
        "database",
        "api",
        "queue",
        "worker",
        "app",
    ]


def test_sort_dependencies_includes_dependency_only_nodes() -> None:
    assert sort_dependencies({"app": ["runtime"]}) == ["runtime", "app"]


def test_sort_dependencies_sorts_available_nodes_alphabetically() -> None:
    graph = {
        "zeta": [],
        "alpha": [],
        "release": ["zeta", "alpha"],
    }

    assert sort_dependencies(graph) == ["alpha", "zeta", "release"]


def test_sort_dependencies_raises_useful_error_for_cycles() -> None:
    graph = {
        "build": ["test"],
        "test": ["build"],
        "lint": [],
    }

    with pytest.raises(ValueError, match="cycle.*build.*test"):
        sort_dependencies(graph)


def test_sort_dependencies_does_not_mutate_input_graph_or_lists() -> None:
    dependencies = ["beta", "alpha"]
    graph = {
        "release": dependencies,
        "alpha": [],
        "beta": [],
    }
    original = {
        node: list(node_dependencies)
        for node, node_dependencies in graph.items()
    }

    sort_dependencies(graph)

    assert graph == original
    assert dependencies == ["beta", "alpha"]
