import re

content = "as busy as a bee b"

# * - zero or more
# ? - one or zero
# + - one or more
# {2,3} - specific number of characters

r = re.compile(r"b[a-z]{2,3}")

# match the regular expression from the start of the content
# print(r.match(content))

# searches the string for a match
# print(r.search(content))

# returns a list of the matches
# print(r.findall(content))

# returns all matches as match objects
print(list(r.finditer(content)))
