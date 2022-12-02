""" write json string module """

import json

colors = [
    {"id": 4, "name": "yellow", "hexcode": "00ffff"},
    {"id": 5, "name": "orange", "hexcode": "ffff00"},
    {"id": 6, "name": "purple", "hexcode": "ff00ff"}
]

print(json.dumps(colors))
