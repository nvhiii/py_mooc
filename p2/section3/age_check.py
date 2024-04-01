# Write your solution here
age = int(input("What is your age? "))

if age >= 5:
    print(f"Ok, you're {age} years old")
elif age >= 0 and age <= 4:
    print(f"I suspect you can't write quite yet...")
else:
    print(f"That must be a mistake")