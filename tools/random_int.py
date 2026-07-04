# tool: random_int
# description: generates a random integer between two given numbers
# author: @navaneethsankar07
# example: random_int "1" "10" -> "7"


import random


def run(*args) -> str:
    min_val = int(args[0])
    max_val = int(args[1])
    return str(random.randint(min_val, max_val))
