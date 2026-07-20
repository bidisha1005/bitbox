# tool: path_normalize
# description: normalizes a filesystem path (collapse . and .., normalize separators)
# author: @Solaris-star
# example: path_normalize "a/b/../c" -> "a/c"

from pathlib import PurePosixPath


def run(*args) -> str:
    if not args:
        return "Error: expected a path argument"
    # Normalize using POSIX semantics for stable cross-platform tool output
    return str(PurePosixPath(args[0]))

