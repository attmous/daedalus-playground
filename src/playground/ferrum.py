def retry_delays(
    attempts: int,
    initial: int = 1,
    multiplier: int = 2,
    maximum: int = 60,
) -> list[int]:
    """Return capped exponential retry delays."""
    safe_attempts = max(0, attempts)
    delay = max(1, initial)
    factor = max(1, multiplier)
    cap = max(1, maximum)

    delays = []
    for _ in range(safe_attempts):
        delays.append(min(delay, cap))
        delay *= factor

    return delays
