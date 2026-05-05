from heapq import heappop, heappush


def sort_dependencies(graph: dict[str, list[str]]) -> list[str]:
    """Return a deterministic topological order for a dependency graph."""
    nodes: set[str] = set(graph)
    dependency_counts: dict[str, int] = {node: 0 for node in graph}
    dependents: dict[str, set[str]] = {node: set() for node in graph}

    for node, dependencies in graph.items():
        unique_dependencies = set(dependencies)
        nodes.update(unique_dependencies)
        dependency_counts.setdefault(node, 0)

        for dependency in unique_dependencies:
            dependency_counts.setdefault(dependency, 0)
            dependents.setdefault(dependency, set()).add(node)
            dependency_counts[node] += 1

    for node in nodes:
        dependency_counts.setdefault(node, 0)
        dependents.setdefault(node, set())

    available: list[str] = []
    for node in sorted(nodes):
        if dependency_counts[node] == 0:
            heappush(available, node)

    ordered: list[str] = []
    while available:
        node = heappop(available)
        ordered.append(node)

        for dependent in dependents[node]:
            dependency_counts[dependent] -= 1
            if dependency_counts[dependent] == 0:
                heappush(available, dependent)

    if len(ordered) != len(nodes):
        cycle_nodes = sorted(node for node in nodes if dependency_counts[node] > 0)
        raise ValueError(
            "cycle detected in dependency graph involving: "
            + ", ".join(cycle_nodes)
        )

    return ordered


__all__ = ["sort_dependencies"]
