# Write your solution here
num = int(input("Please type in a number: "))
if num < 1000:
    print(f"This number is smaller than 1000")
    if num < 100:
        print(f"This number is smaller than 100")
        if num < 10:
            print(f"This number is smaller than 10")

print(f"Thank you!")