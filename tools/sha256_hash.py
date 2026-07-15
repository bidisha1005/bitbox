# tool: sha256_hash
# description: Computes the SHA-256 hex digest of a string
# author: @bidisha1005
# example: sha256_hash "hello" -> "2cf24dba5fb0a30e26e83b2ac5b9e29e1618c90837c5534c2e2ab4f55e16b1e"

import hashlib

def run(*args) -> str:
    text = " ".join(args)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
