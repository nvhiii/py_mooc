# The file matrix.txt contains a matrix in the format specified in the example below:

# 1,0,2,8,2,1,3,2,5,2,2,2
# 9,2,4,5,2,4,2,4,1,10,4,2
# ...etc...

# Please write two functions, named matrix_sum and matrix_max. Both go through the matrix in the file, and then return the sum of the elements or the element with the greatest value, as the names of the functions imply.

# Please also write the function row_sums, which returns a list containing the sum of each row in the matrix. For example, calling row_sums when the matrix in the file is defined as

# 1,2,3
# 2,3,4

# the function should return the list [6, 9].

# Hint: you can also include other helper functions in your program. It is very worthwhile to spend a moment considering which functionalities are shared by the three functions you are asked to write. Notice that the three functions named above do not take any arguments, but any helper functions you write may take arguments. The file you are working with is always named matrix.txt.

# NB: If Visual Studio Code can't find the file and you have checked that there are no spelling errors, take a look at the instructions before this exercise.

def matrix_sum():
    with open("matrix.txt") as new_file:
        for line in new_file:
            parts = line.strip().split(",")

    int_list = [int(x) for x in parts]
    total = sum(int_list)
    return total


def matrix_max():
    with open("matrix.txt") as new_file:
        for line in new_file:
            parts = line.split(",")

    int_list = [int(x) for x in parts]
    biggest = max(int_list)
    return biggest

def row_sums() -> list:
    sums = []
    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n")
            line = line.split(",")
            sums.append(sum(int(x) for x in line))

    return sums
            

