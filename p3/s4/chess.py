# Please write a function named chessboard, 
# which prints out a chessboard made out of ones 
# and zeroes. The function takes an integer 
# argument, which specifies the length of the 
# side of the board. See the examples below for details:

# Write your solution here
def chessboard(num):
    i = 1
    while i <= num:

        # check if num line is odd
        if i % 2 == 1:
            x = 1
            while x <= num:
                if x % 2 == 1:
                    print(1, end="")
                else:
                    print(0, end="")
                x += 1
        else:
            x2 = 1
            while x2 <= num:
                if x2 % 2 == 1:
                    print(0, end="")
                else:
                    print(1, end="")
                x2 += 1

        i += 1
        print()

# Testing the function
if __name__ == "__main__":
    chessboard(6)