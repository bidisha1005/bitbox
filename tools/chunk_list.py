# tool: chunk_list
# description: splits a comma-separated list into chunks of size n
# author: @Solaris-star
# example: chunk_list "a,b,c,d" "2" -> "a,b|c,d"


def run(*args) -> str:
    if len(args) != 2:
        return "Error: expected list and chunk size"
    items = [x.strip() for x in args[0].split(",")] if args[0] != "" else []
    try:
        size = int(args[1])
    except ValueError:
        return "Error: chunk size must be an integer"
    if size < 1:
        return "Error: chunk size must be >= 1"
    chunks = [",".join(items[i:i + size]) for i in range(0, len(items), size)]
    return "|".join(chunks)
