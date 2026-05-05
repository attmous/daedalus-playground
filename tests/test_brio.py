from playground.brio import parse_priority


def test_parse_priority_numeric_forms() -> None:
    assert parse_priority("P0") == {"level": 0, "label": "p0", "urgent": True}
    assert parse_priority(" p1 ") == {"level": 1, "label": "p1", "urgent": True}
    assert parse_priority("2") == {"level": 2, "label": "p2", "urgent": False}


def test_parse_priority_prefix_form() -> None:
    assert parse_priority("priority:2") == {"level": 2, "label": "p2", "urgent": False}


def test_parse_priority_normal_fallback() -> None:
    assert parse_priority(" NORMAL ") == {
        "level": 3,
        "label": "normal",
        "urgent": False,
    }


def test_parse_priority_unknown_fallback() -> None:
    assert parse_priority("soon") == {"level": 3, "label": "normal", "urgent": False}


def test_parse_priority_urgent_calculation() -> None:
    assert parse_priority("priority:0")["urgent"] is True
    assert parse_priority("priority:1")["urgent"] is True
    assert parse_priority("priority:2")["urgent"] is False
