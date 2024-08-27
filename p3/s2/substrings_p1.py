# Please write a program which asks the user to type in a string. The 
# program then prints out all the substrings which begin with the first 
# character, from the shortest to the longest. Have a look at the 
# example below.

# Please type in a string: test
# t
# te
# tes
# test

ustr = input("Please type in a string: ")
num = 1

while not num > len(ustr):

    print(ustr[:num])
    num += 1