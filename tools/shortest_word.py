# tool: shortest_word
# description: Finds the shortest word in a given text
# author: @PurpleSwtr
# example: shortest_word "the quick brown fox" -> "the"


def run(text: str) -> str:
    return min(text.split(), key=len, default="")
