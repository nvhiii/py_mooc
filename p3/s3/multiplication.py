# Please write a program which asks the user for a positive integer
#  number. The program then prints out a list of multiplication operations 
# until both operands reach the number given by the user. See the examples 
# below for details:

# Please type in a number: 2
# 1 x 1 = 1
# 1 x 2 = 2
# 2 x 1 = 2
# 2 x 2 = 4

# Please type in a number: 3
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9

num = int(input("Please type in a number: "))
iterator = 1

while iterator <= num:

    operand = 1
    while operand <= num:
        print(f"{iterator} x {operand} = {iterator * operand}")
        operand += 1

    iterator += 1



