# tool: ordinal
# description: Converts an integer to its ordinal string (1 → 1st, 2 → 2nd)
# author: @bitbox
# example: ordinal "1" → "1st"


def run(*args) -> str:
    n = int(args[0])
    if 11 <= n % 100 <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"
