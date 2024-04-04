# Write your solution here
underline = "-"
while True:
    # every iteration for loop prompt input
    user_input = input("Please type in a string: ")
    if user_input == "":
        break

    print(f"{user_input}")
    print(f"{len(user_input) * underline}")