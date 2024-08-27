# Please write a program which asks the user for a string. The program 
# then prints out a message based on whether the second character and 
# the second to last character are the same or not. See the examples below.

# Please type in a string: python
# The second and the second to last characters are different

# Please type in a string: pascal
# The second and the second to last characters are a

ustr = input("Please type in a string: ")

if ustr[1] == ustr[-2]:
    print(f"The second and the second to last characters are {ustr[1]}")
else:
    print("The second and the second to last characters are different")