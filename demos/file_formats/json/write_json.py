""" write json file module """

import json

colors = [
    {"id": 4, "name": "yellow", "hexcode": "00ffff"},
    {"id": 5, "name": "orange", "hexcode": "ffff00"},
    {"id": 6, "name": "purple", "hexcode": "ff00ff"}
]

with open("colors2.json", "w", encoding="UTF-8") as colors2_json_file:
    # No Formatting
    # json.dump(colors, colors2_json_file)
    # Formatted
    json.dump(colors, colors2_json_file, indent=2)
