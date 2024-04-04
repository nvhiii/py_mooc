# Write your solution here
user_string = input("Please type in a string: ")
ast = "*"

if len(user_string) < 20:
    diff = 20 - len(user_string) # calculation of asteriks to print
    print(f"{diff * ast}{user_string}")