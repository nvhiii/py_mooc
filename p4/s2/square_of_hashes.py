# Please write a function named square_of_hashes, 
# which draws a square of hash characters. The 
# function takes one argument, which determines 
# the length of the side of the square.

# The function should call the function line from the 
# exercise above for the actual printing out. Copy your 
# solution to that exercise above the code for this exercise.
# Please don't change anything in the line function.

# Copy here code of line function from previous exercise
def line(num, str):
    
    if len(str) == 0:
        print(f"*" * num) # accounts for new lines, and better time efficiency
    else:
        print(f"{str[0]}" * num)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    i = 1
    while i <= size:
        line(size, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
