# tool: reverse_words
# description: Reverses the order of words in a string
# author: @Julito-Dev
# example: example_tool "Hello World" -> "World Hello"


def run(*args) -> str:
    return " ".join(args[0].split()[::-1])