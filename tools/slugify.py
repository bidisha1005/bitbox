# tool: slugify
# description: Converts a string to a URL-friendly slug
# author: @bitbox
# example: slugify "Hello World" → "hello-world"


def run(*args) -> str:
    import re

    text = args[0].lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")
