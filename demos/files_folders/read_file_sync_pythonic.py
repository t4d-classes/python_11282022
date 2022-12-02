try:
    with open("colors.txt", "r", encoding="UTF-8") as colors_file:

        for color in colors_file:
            print(color.rstrip())

except IOError as exc:
    print(exc)
