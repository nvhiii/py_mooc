# Please write a program which asks the user for a string and then prints 
# it out so that exactly 20 characters are displayed. If the input is 
# shorter than 20 characters, the beginning of the line is filled in 
# with * characters.

# You may assume the input string is at most 20 characters long.

# Please type in a string: python

# **************python

# Please type in a string: alongerstring

# *******alongerstring

# Please type in a string: averyverylongstring

# *averyverylongstring

ustr = input("Please type in a string: ")

if len(ustr) < 20:

    whitespace = 20 - len(ustr) # calc whitespace we need to fill in
    stars = whitespace * "*"
    print(f"{stars}{ustr}")