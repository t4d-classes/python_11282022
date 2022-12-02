""" read json string """

import json

colors_json = """
    [
        {"id": 1, "name": "red", "hexcode": "ff0000"},
        {"id": 2, "name": "green", "hexcode": "00ff00"},
        {"id": 3, "name": "blue", "hexcode": "0000ff"}
    ]
"""

print(json.loads(colors_json))
