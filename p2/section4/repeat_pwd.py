# Write your solution here
pwd = input("Password: ")
while True:
    repeat = input("Repeat password: ")
    if repeat != pwd:
        print(f"They do not match!")
    if repeat == pwd:
        break

print(f"User account created!")