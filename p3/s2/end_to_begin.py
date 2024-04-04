# Write your solution here
user_str = input("Please type in a string: ")
size = len(user_str)
index = -1


while size > 0:
    print(f"{user_str[index]}")
    # decrease size of word
    index -= 1
    size -= 1

