# tool: json_minify
# description: minifies a JSON string
# author: @Solaris-star
# example: json_minify "{\"a\": 1}" -> "{\"a\":1}"

import json


def run(*args) -> str:
    if not args:
        return "Error: expected a JSON string"
    try:
        return json.dumps(json.loads(args[0]), separators=(",", ":"), ensure_ascii=False)
    except json.JSONDecodeError as exc:
        return f"Error: {exc}"

