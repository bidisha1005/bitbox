# tool: reverse_string
# description: Reverses a string input
# author: @bitbox
# example: reverse_string "hello" → "olleh"


def run(*args) -> str:
    text = args[0]
    return text[::-1]
