# tool: line_count
# description: counts the number of lines in a string
# author: @Solaris-star
# example: line_count "a\\nb\\nc" -> "3"


def run(*args) -> str:
    if not args:
        return "Error: expected a string argument"
    text = args[0]
    if text == "":
        return "0"
    # Count newlines + 1 unless trailing newline-only semantics: splitlines handles no trailing
    return str(len(text.splitlines()) if text.endswith("\n") is False else len(text.splitlines()))

