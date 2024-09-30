# Please write a function named read_input, which asks the user for input until the user types in an integer which falls within the bounds given as arguments to the function. The function should return the final valid integer value typed in by the user.

# An example of the function in action:

# number = read_input("Please type in a number: ", 5, 10)
# print("You typed in:", number)

# Please type in a number: seven
# You must type in an integer between 5 and 10
# Please type in a number: -3
# You must type in an integer between 5 and 10
# Please type in a number: 8
# You typed in: 8

def read_input(user_num: int, lower: int, upper: int):
    while True:
        try:
            num = int(input("Please type in a number: "))
            if num >= lower and num <= upper:
                return num
        except ValueError:
            pass

        print(f"You must type in an integer between {lower} and {upper}")


