# tool: word_wrap
# description: wraps text to a maximum line width
# author: @Solaris-star
# example: word_wrap "hello world again" "5" -> multi-line wrapped text

import textwrap


def run(*args) -> str:
    if len(args) < 1:
        return "Error: expected text and optional width"
    text = args[0]
    width = 80
    if len(args) >= 2:
        try:
            width = int(args[1])
        except ValueError:
            return "Error: width must be an integer"
    if width < 1:
        return "Error: width must be >= 1"
    return textwrap.fill(text, width=width)

