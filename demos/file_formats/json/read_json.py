""" read json file module """

import json

with open("colors.json", "r", encoding="UTF-8") as colors_json_file:

    colors = json.load(colors_json_file)
    print(colors)
