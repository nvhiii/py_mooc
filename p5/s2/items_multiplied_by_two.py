# Please write a function named double_items(numbers: list), which takes a list of integers as its argument.

# The function should return a new list, which contains all values from the original list doubled. The function should not change the original list.

# An example of the function at work:

# if __name__ == "__main__":
#     numbers = [2, 4, 5, 3, 11, -4]
#     numbers_doubled = double_items(numbers)
#     print("original:", numbers)
#     print("doubled:", numbers_doubled)

# original: [2, 4, 5, 3, 11, -4]
# doubled: [4, 8, 10, 6, 22, -8]

def double_items(numbers: list) -> list:
    new_list = []
    for num in numbers:
        new_list.append(num*2)
    return new_list