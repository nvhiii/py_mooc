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

def matrix_list(file_name="matrix.txt"):
    with open(file_name) as new_file:
        m = [int(x) for line in new_file for x in line.strip().split(",")]
    return m

def matrix_rows(file_name="matrix.txt"):
    with open(file_name) as new_file:
        m = [[int(x) for x in line.strip().split(",")] for line in new_file]
    return m

def matrix_sum():
    return sum(matrix_list())

def matrix_max():
    return max(matrix_list())

def row_sums():
    m = matrix_rows()
    return [sum(row) for row in m]

def main():
    matrix()

if __name__ == "__main__":
    main()

