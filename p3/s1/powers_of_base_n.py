# Please change the program from the previous exercise so that 
# the user gets to input also the base which is multiplied (in the previous 
# program the base was always 2).

# Upper limit: 27
# Base: 3
# 1
# 3
# 9
# 27

# init
upper = int(input("Upper limit: "))
base = int(input("Base: "))
exponent = 0

while base ** exponent <= upper:

    print(base**exponent)
    # increment exponent
    exponent += 1