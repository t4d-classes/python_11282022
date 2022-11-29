
from typing import Generator
import itertools


def fibonacci() -> Generator[int, None, None]:
    """ generate an infinite fibonacci sequence """

    num_1 = 0
    num_2 = 1

    yield 0

    while True:

        next_num = num_1 + num_2
        yield next_num
        num_1 = num_2
        num_2 = next_num

# for fib_num in itertools.islice(fibonacci(), 5):
#     print(fib_num)


# nums = [1, 2, 3, 4, 5]

# always producing a new list

# double_nums = []
#
# for num in nums:
#     double_nums.append(num * 2)
#
# double_nums = [num * 2 for num in nums]

# producing a generator


def double_num(num: int) -> int:
    """ double num """
    print(f"called double num for: {num}")
    return num * 2


nums = list(range(1, 11))

print(nums)

# def my_map(transform_fn, items):
#     transformed_items = []
#     for item in items:
#         transformed_items.append(transform_fn(item))
#     return transformed_items
#
#


def my_map2(transform_fn, items):
    for item in items:
        yield transform_fn(item)


#
#
double_nums = my_map2(double_num, nums)

print(double_nums)

for num in itertools.islice(double_nums, 20):
    print(num)

# for num in double_nums:
#     print(num)

# print(list(double_nums))

# double_nums = (num * 2 for num in nums)

# for num in double_nums:
#     print(num)

#
# print(nums)
# print(double_nums)
