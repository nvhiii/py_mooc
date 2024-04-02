from math import sqrt
# Write your solution here

while True:
    num = int(input("Please type in a number: "))

    if num == 0:
        break
    elif num < 0:
        print(f"Invalid number")
    else:
        print(sqrt(num))

print(f"Exiting...")