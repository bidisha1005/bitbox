# tool: count_words
# description: Counts the number of words in a string
# author: @bitbox
# example: count_words "the quick brown fox" → "4"


def run(*args) -> str:
    text = args[0]
    return str(len(text.split()))
