# tool: is_email
# description: checks whether a string looks like an email address
# author: @Solaris-star
# example: is_email "a@b.com" -> "true"

import re

_EMAIL = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def run(*args) -> str:
    if not args:
        return "Error: expected a string argument"
    return "true" if _EMAIL.match(args[0].strip()) else "false"

