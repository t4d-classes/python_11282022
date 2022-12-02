import re

content = """apple
banana
apple
Banana
banana
apple   orange
avocado
"""

r = re.compile(r"^apple$", re.MULTILINE | re.IGNORECASE)

# r = re.compile(r"^a[a-z]*", re.MULTILINE)

fruits = ['apple', 'banana', 'apple', 'dates', 'avocado', 'apricot']

r = re.compile(r"^a[a-z]*[eo]{1}$")

matched_fruits = [fruit for fruit in fruits if r.match(fruit)]
print(matched_fruits)
# print(list(r.finditer(content)))
