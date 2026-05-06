def expand_aliases(items: list[str], aliases: dict[str, list[str]]) -> list[str]:
    """Expand aliases recursively while preserving item order."""
    expanded: list[str] = []

    def expand_item(item: str, path: tuple[str, ...]) -> list[str]:
        if item not in aliases:
            return [item]
        if item in path:
            cycle = " -> ".join((*path, item))
            raise ValueError(f"alias cycle detected: {cycle}")

        result: list[str] = []
        for alias_item in aliases[item]:
            result.extend(expand_item(alias_item, (*path, item)))

        return result

    for item in items:
        expanded.extend(expand_item(item, ()))

    return expanded
