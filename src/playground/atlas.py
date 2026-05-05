def classify_path(value: str) -> dict[str, object]:
    """Classify a POSIX-style path for smoke tests."""
    clean_value = value.strip()

    if clean_value == "":
        return {
            "kind": "empty",
            "depth": 0,
            "basename": "",
            "extension": "",
            "segments": [],
        }

    kind = "absolute" if clean_value.startswith("/") else "relative"
    segments = [segment for segment in clean_value.split("/") if segment]
    basename = segments[-1] if segments else ""
    extension = _extension_for(basename)

    return {
        "kind": kind,
        "depth": len(segments),
        "basename": basename,
        "extension": extension,
        "segments": segments,
    }


def _extension_for(basename: str) -> str:
    stem, separator, extension = basename.rpartition(".")
    if separator and stem:
        return extension
    return ""
