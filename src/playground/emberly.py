def parse_headers(lines: list[str]) -> dict[str, str]:
    headers: dict[str, str] = {}

    for line in lines:
        if not line.strip() or ":" not in line:
            continue

        key, value = line.split(":", 1)
        clean_key = key.strip().lower()
        if not clean_key:
            continue

        headers[clean_key] = value.strip()

    return headers
