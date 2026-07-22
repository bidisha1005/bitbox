# tool: power
# description: Raises a number to a power
# author: @Solaris-star
# example: power "2" "10" -> "1024"

def run(*args) -> str:
    if len(args) != 2:
        return "Error: Expected exactly 2 arguments."
    try:
        base = float(args[0])
        exp = float(args[1])
    except ValueError:
        return "Error: Both arguments must be valid numbers."
    result = base ** exp
    if result.is_integer():
        return str(int(result))
    return str(result)
