# tool: json_keys
# description: Lists the top-level keys of a JSON object
# author: @zaid-brk
# example: json_keys '{"a":1,"b":2}' → '["a", "b"]'

import json


def run(*args) -> str:
    data = json.loads(args[0])
    return json.dumps(list(data.keys()))
