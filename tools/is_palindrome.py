# tool: is_palindrome
# description: Checks if a string is a palindrome
# author: @bitbox
# example: is_palindrome "racecar" → "True"


def run(*args) -> str:
    text = args[0].lower().strip()
    cleaned = "".join(c for c in text if c.isalnum())
    return str(cleaned == cleaned[::-1])
