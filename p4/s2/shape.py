# Please write a function named shape, which takes four arguments. 
# The first two parameters specify a triangle, as above, and the 
# character used to draw it. The first parameter also specifies the 
# width of a rectangle, while the third parameter specifies its height. 
# The fourth parameter specifies the filler character of the rectangle.
# The function prints first the triangle, and then the rectangle below it.

# The function should call the function line from the exercise above 
# for the actual printing out. Copy your solution to that exercise 
# above the code for this exercise. Please don't change anything in 
# the line function.

# Some examples:

# shape(5, "X", 3, "*")
# print()
# shape(2, "o", 4, "+")
# print()
# shape(3, ".", 0, ",")

# X
# XX
# XXX
# XXXX
# XXXXX
# *****
# *****
# *****

# o
# oo
# ++
# ++
# ++
# ++

# .
# ..
# ...

def line(times, ustr):

    if ustr=="":
        print(f"*" * times)
    else:
        print(times*ustr[0])

def shape(dim, ustr1, height, ustr2):

    # print out triangle then square
    num = 1
    while num <= dim:
        line(num, ustr1)
        num += 1

    num_rect = 0
    while num_rect < height:
        line(dim, ustr2)
        num_rect += 1