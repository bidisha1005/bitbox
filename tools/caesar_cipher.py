# tool: caesar_cipher
# description: Applies a Caesar cipher shift to a string
# author: @Solaris-star
# example: caesar_cipher "abc" "1" -> "bcd"

def run(*args) -> str:
    if len(args) != 2:
        return "Error: Expected exactly 2 arguments."
    text = args[0]
    try:
        shift = int(args[1]) % 26
    except ValueError:
        return "Error: Shift must be an integer."
    out = []
    for ch in text:
        if "a" <= ch <= "z":
            out.append(chr((ord(ch) - 97 + shift) % 26 + 97))
        elif "A" <= ch <= "Z":
            out.append(chr((ord(ch) - 65 + shift) % 26 + 65))
        else:
            out.append(ch)
    return "".join(out)
