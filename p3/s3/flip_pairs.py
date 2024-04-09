# Please write a program which asks the user to 
# type in a number. The program then prints out 
# all the positive integer values from 1 up to the 
# number. However, the order of the numbers is 
# changed so that each pair or numbers is flipped. 
# That is, 2 comes before 1, 4 before 3 and so forth.
# See the examples below for details.

# Please type in a number: 5
# 2
# 1
# 4
# 3
# 5

# Write your solution here
num = int(input("Please type in a number: "))
iterator = 1

# prints all nums from 1 to the num specified by user
while iterator <= num:

    # now group all contiguous nums in pairs of 2
    if iterator + 1 <= num:
        print(iterator + 1)

    print(iterator) # else

    iterator += 2 # increment by 2 bc we swap two contiguous values, and next pair starts at index + 2  

    

