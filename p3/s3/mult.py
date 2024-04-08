product = 1
# prompt for infinite input until break cond is met
while True:

    # prompt num
    num = int(input("Please type in a number: "))
    temp = num

    if num == 0 or num < 0:
        break

    # calculate factorial
    while num >= 1:
        product *= num
        num -= 1
    
    # prnt
    print(f"The factorial of the number {temp} is {product}")
    product = 1 # IMPORTANT TO INCLUDE, NEED TO RESET VALUE OF PRODUCT

print(f"Thanks and bye!")