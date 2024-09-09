# In this exercise we will complete two more functions for the sudoku project from the previous section: print_sudoku and add_number.

# The function print_sudoku(sudoku: list) takes a two-dimensional array representing a sudoku grid as its argument. The function should print out the grid in the format specified in the examples below.

# The function add_number(sudoku: list, row_no: int, column_no: int, number:int) takes a two-dimensional array representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. The function should add the digit to the specified location in the grid.

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

# print_sudoku(sudoku)
# add_number(sudoku, 0, 0, 2)
# add_number(sudoku, 1, 2, 7)
# add_number(sudoku, 5, 7, 3)
# print()
# print("Three numbers added:")
# print()
# print_sudoku(sudoku)

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# Three numbers added:

# 2 _ _  _ _ _  _ _ _
# _ _ 7  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ 3 _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# Hint

# Remember it is possible to call the print function without causing a line change:

# print("characters ", end="")
# print("without carriage returns", end="")

# characters without carriage returns

# Sometimes you need just a new line, which a print statement without any argument will achieve:

# print()

def print_sudoku(sudoku: list):

    for i, row in enumerate(sudoku):
        for j, col in enumerate(row):
            if col == 0:
                print("_", end=" ")
            else:
                print(col, end=" ")

            # extra space every 3 col
            if (j+1)%3 == 0 and j != 8: # add 1 bc index starts at 0, and dont add space after 9th col
                print(" ", end="")

        print()
        if (i+1)%3 == 0 and i != 8:
            print()
    

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number