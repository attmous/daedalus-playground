from playground.atlas import classify_path


def test_classify_path_handles_empty_input() -> None:
    assert classify_path("   ") == {
        "kind": "empty",
        "depth": 0,
        "basename": "",
        "extension": "",
        "segments": [],
    }


def test_classify_path_handles_absolute_path() -> None:
    assert classify_path(" /srv/app/config ") == {
        "kind": "absolute",
        "depth": 3,
        "basename": "config",
        "extension": "",
        "segments": ["srv", "app", "config"],
    }


def test_classify_path_handles_relative_path() -> None:
    assert classify_path("docs/readme") == {
        "kind": "relative",
        "depth": 2,
        "basename": "readme",
        "extension": "",
        "segments": ["docs", "readme"],
    }


def test_classify_path_collapses_repeated_slashes_for_segments() -> None:
    assert classify_path("//var///log/app/") == {
        "kind": "absolute",
        "depth": 3,
        "basename": "app",
        "extension": "",
        "segments": ["var", "log", "app"],
    }


def test_classify_path_extracts_extension_without_dot() -> None:
    assert classify_path("reports/summary.final.txt") == {
        "kind": "relative",
        "depth": 2,
        "basename": "summary.final.txt",
        "extension": "txt",
        "segments": ["reports", "summary.final.txt"],
    }
