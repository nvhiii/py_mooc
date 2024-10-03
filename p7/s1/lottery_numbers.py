# Please write a function named lottery_numbers(amount: int, lower: int, upper: int), which generates as many random numbers as specified by the first argument. All numbers should fall within the bounds lower to upper. The numbers should be stored in a list and returned. The numbers should be in ascending order in the returned list.

# As these are lottery numbers, no number should appear twice in the list.

# An example of how the function should work:

# for number in lottery_numbers(7, 1, 40):
#     print(number)

# 4
# 7
# 11
# 16
# 22
# 29
# 38

from random import sample

def lottery_numbers(amount: int, lower: int, upper: int):
    num_pool = list(range(lower, upper))
    draw = sample(num_pool, amount)
    draw = sorted(draw)
    return draw