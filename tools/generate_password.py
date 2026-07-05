# description: Generates a random password of the given length

import random
import string


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    try:
        length = int(args[0])
    except ValueError:
        return "Error: Password length must be a positive integer."

    if length <= 0:
        return "Error: Password length must be greater than 0."

    characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        string.punctuation
    )

    password = []

    for _ in range(length):
        password.append(random.choice(characters))

    return "".join(password)