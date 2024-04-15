# Please write a function named greatest_number, 
# which takes three arguments. The function returns 
# the greatest in value of the three.

# Write your solution here

def greater(numA, numB):
    if numA > numB:
        return numA
    return numB

def greatest_number(num1, num2, num3):
    if num1 == num2 and num2 == num3:
        return num1
    else:
        great1 = greater(num1, num2)
        great2 = greater(great1, num3)
        return great2

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)