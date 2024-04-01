# Write your solution here
num = int(input("Number: "))

if num % 3 == 0 and num % 5 == 0:
    print(f"FizzBuzz")
elif num % 3 == 0:
    print(f"Fizz")
elif num % 5 == 0:
    print(f"Buzz")