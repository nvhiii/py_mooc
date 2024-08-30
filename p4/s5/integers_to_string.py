# Please write a function named formatted, which takes a list of 
# floating point numbers as its argument. The function returns a 
# new list, which contains each element of the original list in 
# string format, rounded to two decimal points. The order of the 
# items in the list should remain unchanged.

# Hint: use f-strings to format the floating point numbers into suitable strings.

# An example of expected beahviour:

# my_list = [1.234, 0.3333, 0.11111, 3.446]
# new_list = formatted(my_list)
# print(new_list)

# ['1.23', '0.33', '0.11', '3.45']

def formatted(my_list: list) -> list:
    new_list = []
    for i in my_list:
        formatter = f"{i:.2f}"
        new_list.append(formatter)

    return new_list