# tool: path_basename
# description: Returns the final component of a file path
# author: @isaac-sun
# example: path_basename "/home/user/docs/file.txt" → "file.txt"

from pathlib import PurePath


def run(*args) -> str:
    if not args:
        raise ValueError("path_basename requires a path argument")
    path = str(args[0])
    return PurePath(path).name
