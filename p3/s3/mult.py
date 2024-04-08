# Write your solution here
# Please write a program which asks the user for a positive integer number. The program then prints out a list of multiplication operations until both operands reach the number given by the user. See the examples below for details:
num = int(input("Please type in a number: "))
first_operand = 1
second_operand = 1

while first_operand <= num:
    print(f"{first_operand} x {second_operand} = {first_operand * second_operand}")
    first_operand += 1
    second_operand += 1

    
# WIP