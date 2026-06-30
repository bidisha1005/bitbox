# tool: is_uppercase
# description: Checks if a string is all uppercase
# author: @bitbox
# example: is_uppercase "HELLO" -> "True"

def run(*args) -> str:
    text = args[0]
    if not text:
        return "False"
    return str(text.isupper())
