# Please write a function named square, which prints out a square of 
# characters, and takes two arguments. The first parameter specifies t
# he length of the side of the square. The second parameter specifies 
# he character used to draw the square.

# The function should call the function line from the exercise above 
# for the actual printing out. Copy your solution to that exercise above 
# the code for this exercise. Please don't change anything in the line 
# function.

# Some examples:

# square(5, "*")
# print()
# square(3, "o")

# *****
# *****
# *****
# *****
# *****

# ooo
# ooo
# ooo

def line(times, ustr):

    if ustr=="":
        print(f"*" * times)
    else:
        print(times*ustr[0])

def square(amt, ustr):

    num = 0
    while num < amt:
        line(amt, ustr) # width is amt, since this is a square
        num += 1