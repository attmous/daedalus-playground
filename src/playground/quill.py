def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    """Parse YAML-like front matter from the start of text."""
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip("\r\n") != "---":
        return {}, text

    metadata: dict[str, str] = {}

    for index, line in enumerate(lines[1:], start=1):
        content = line.rstrip("\r\n")
        if content == "---":
            return metadata, "".join(lines[index + 1 :])
        if not content.strip():
            continue
        if ":" not in content:
            raise ValueError(f"malformed front matter line: {content}")

        key, value = content.split(":", 1)
        key = key.strip()
        if not key:
            raise ValueError(f"malformed front matter line: {content}")
        metadata[key] = value.strip()

    raise ValueError("missing closing front matter delimiter")
