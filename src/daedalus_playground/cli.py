import argparse
import inspect
import sys
from collections.abc import Callable, Sequence

import daedalus_playground


def _is_simple_greeting_helper(helper: Callable[..., str]) -> bool:
    signature = inspect.signature(helper)
    positional_parameters = [
        parameter
        for parameter in signature.parameters.values()
        if parameter.kind
        in (parameter.POSITIONAL_ONLY, parameter.POSITIONAL_OR_KEYWORD)
    ]
    return len(positional_parameters) == 1


def _greeting_helpers() -> dict[str, Callable[[str], str]]:
    helpers = {}
    for name in daedalus_playground.__all__:
        helper = getattr(daedalus_playground, name)
        if callable(helper) and _is_simple_greeting_helper(helper):
            helpers[name] = helper
    return helpers


def main(argv: Sequence[str] | None = None) -> int:
    helpers = _greeting_helpers()
    parser = argparse.ArgumentParser(
        prog="daedalus-greet",
        description="Print a Daedalus greeting.",
    )
    parser.add_argument("kind", help="Greeting type to print.")
    parser.add_argument("name", nargs="?", default="Daedalus")
    args = parser.parse_args(argv)

    helper = helpers.get(args.kind)
    if helper is None:
        available = ", ".join(sorted(helpers))
        print(
            f"Unknown greeting type: {args.kind}. Available types: {available}.",
            file=sys.stderr,
        )
        return 2

    print(helper(args.name))
    return 0
