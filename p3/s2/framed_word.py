# Please write a program which asks the user for a string and then prints 
# out a frame of * characters with the word in 
# the centre. The width of the frame should be 30 characters. You may assume 
# the input string will always fit inside the frame.

# If the length of the input string is an odd number, you may print out 
# the word in either of the two possible centre locations.

# Word: testing

# ******************************
# *          testing           *
# ******************************

# Word: python

# ******************************
# *           python           *
# ******************************

ustr = input("Word: ")

# frame top
print(30*"*")

# frame on right and left of word
whitespace = 30 - 2 - len(ustr) # the 30 is max, 2 is the right and left borders w/ width of 1 each

if len(ustr) % 2 == 0:
    blanks = (whitespace//2) * " "
    print(f"*{blanks}{ustr}{blanks}*")
else:
    blanks_l = (whitespace//2 + 1) * " "
    blanks_r = (whitespace//2) * " "
    middle = f"*{blanks_l}{ustr}{blanks_r}*"
    print(f"{middle}")

# frame bottom
print(30*"*")