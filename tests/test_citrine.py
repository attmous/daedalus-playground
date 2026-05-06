from playground.citrine import allocate_slug


def test_allocate_slug_normalizes_title() -> None:
    assert allocate_slug("  Hello, Citrine Slug!!  ", set()) == "hello-citrine-slug"


def test_allocate_slug_uses_item_for_blank_normalized_title() -> None:
    assert allocate_slug(" !!! ", set()) == "item"


def test_allocate_slug_numbers_collisions_until_unique() -> None:
    existing = {"release-notes", "release-notes-2", "release-notes-3"}

    assert allocate_slug("Release Notes", existing) == "release-notes-4"


def test_allocate_slug_does_not_mutate_existing() -> None:
    existing = {"item"}
    before = set(existing)

    assert allocate_slug(" ", existing) == "item-2"
    assert existing == before
