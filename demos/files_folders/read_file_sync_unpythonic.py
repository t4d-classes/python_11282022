colors_file = None

try:
    colors_file = open("colors.txt", "r", encoding="UTF-8")

    for color in colors_file:
        print(color.rstrip())

except IOError as exc:
    print(exc)

finally:
    if colors_file:
        colors_file.close()
