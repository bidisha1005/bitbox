# tool: current_timestamp
# description: returns the current Unix timestamp in seconds
# author: @Solaris-star
# example: current_timestamp -> "1710000000"

import time


def run(*args) -> str:
    return str(int(time.time()))

