import re


_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def allocate_slug(title: str, existing: set[str]) -> str:
    """Return a normalized slug that is not present in existing."""
    base_slug = _NON_ALNUM.sub("-", title.strip().lower()).strip("-") or "item"

    if base_slug not in existing:
        return base_slug

    suffix = 2
    while True:
        candidate = f"{base_slug}-{suffix}"
        if candidate not in existing:
            return candidate
        suffix += 1


__all__ = ["allocate_slug"]
