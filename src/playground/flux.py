def retry_delays(attempts: int, base: int = 2, cap: int = 60) -> list[int]:
    """Return capped exponential retry delays."""
    if attempts < 0:
        raise ValueError("attempts must be non-negative")
    if base <= 0:
        raise ValueError("base must be positive")
    if cap <= 0:
        raise ValueError("cap must be positive")

    return [min(base * 2**index, cap) for index in range(attempts)]
