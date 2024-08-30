# Please write a program which asks the user to type in a string. 
# The program then prints each input character on a separate line. 
# After each character there should be a star (*) printed on its own line.

# This is how it should work:

# Please type in a string: Python
# P
# *
# y
# *
# t
# *
# h
# *
# o
# *
# n
# *

ustr = input("Please type in a string: ")

for char in ustr:
    print(char)
    print("*")