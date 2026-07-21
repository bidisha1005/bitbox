# tool: html_unescape
# description: unescapes HTML entities in a string
# author: @Solaris-star
# example: html_unescape "&lt;div&gt;" -> "<div>"

from html import unescape


def run(*args) -> str:
    if not args:
        return "Error: expected a string argument"
    return unescape(args[0])

