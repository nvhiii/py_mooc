# This is the very last sudoku task. This time we will create a slightly different version of the function for adding new numbers to the grid.

# The function copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) takes a two-dimensional array representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. The function should return a copy of the original grid with the new digit added in the correct location. The function should not change the original grid received as a parameter.

# The print_sudoku function from the previous exercise could be useful for testing, and it is used in the example below:

# sudoku  = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

# grid_copy = copy_and_add(sudoku, 0, 0, 2)
# print("Original:")
# print_sudoku(sudoku)
# print()
# print("Copy:")
# print_sudoku(grid_copy)

def print_sudoku(sudoku: list):
    
    for i, row in enumerate(sudoku):
        for j, num in enumerate(row):
            if num == 0:
                print("_", end=" ")
            else:
                print(num, end=" ")
            
            if (j + 1) % 3 == 0 and j != 8:
                print(" ", end="")

        print()
        if (i + 1) % 3 == 0 and i != 8:
            print()

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku = [row[:] for row in sudoku] # cannot do sudoku[:]
    new_sudoku[row_no][column_no] = number
    return new_sudoku