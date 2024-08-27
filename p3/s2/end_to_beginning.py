# Please write a program which asks the user for a string. The program 
# then prints out the input string in reversed order, from end to 
# beginning. Each character should be on a separate line.

# An example of expected behaviour:

# Please type in a string: hiya
# a
# y
# i
# h

ustr = input("Please type in a string: ")
num = len(ustr) # gives us length of user string

while num > 0:
    print(ustr[num-1]) # print last chara every iter
    num -= 1