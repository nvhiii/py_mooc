# Write your solution here
user_string = input("Please type in a string: ")
index = 0 # start at 0
reverse_index = -1 # start at -1
size = len(user_string)

if user_string[1] == user_string[len(user_string) - 2]:
    print(f"The second and the second to last characters are {user_string[1]}")
else:
    print(f"The second and the second to last characters are different")
