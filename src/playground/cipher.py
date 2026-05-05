import re


_SECRET_ASSIGNMENT = re.compile(
    r"(?P<prefix>\b(?:token|api_key)\s*=\s*|\bsecret\s*:\s*)[^\s,;]+",
    re.IGNORECASE,
)


def redact_secrets(text: str) -> str:
    """Redact known secret assignment values from text."""
    return _SECRET_ASSIGNMENT.sub(r"\g<prefix>[REDACTED]", text)
