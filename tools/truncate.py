# tool: truncate
# description: Truncates a string to a given length and appends "..."
# author: @bitbox
# example: truncate "Hello World" "5" → "Hello..."


def run(*args) -> str:
    text = args[0]
    length = int(args[1])
    if len(text) <= length:
        return text
    return text[:length] + "..."
