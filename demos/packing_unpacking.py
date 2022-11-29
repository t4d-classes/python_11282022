

letters = ['a', 'b', 'c', 'd', 'e', 'f']

print(letters)

print('a', 'b', 'c')

# * - unpacking operator
print(*letters)

# * - packing operator
first, *middle, last = letters

print(f"first: {first}")
print(f"middle: {middle}")
print(f"last: {last}")
