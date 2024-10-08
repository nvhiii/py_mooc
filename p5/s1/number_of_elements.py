# Please write a function named 
# count_matching_elements(my_matrix: list, element: int), which takes a 
# two-dimensional array of integers and a single integer value as its arguments. 
# The function then counts how many elements within the matrix match the argument 
# value.

# An example of how the function should work:

# m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
# print(count_matching_elements(m, 1))

# 3

def count_matching_elements(my_matrix: list, element: int) -> int:

    count = 0
    for row in my_matrix:
        for n in range(len(row)):
            if row[n] == element:
                count += 1

    return count