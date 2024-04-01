# Write your solution here
pts = int(input("How many points [0-100]: "))

if pts > 100 or pts < 0:
    print(f"Grade: impossible!")
elif pts >= 0 and pts <= 49:
    print(f"Grade: fail")
elif pts >= 50 and pts <= 59:
    print(f"Grade: 1")
elif pts >= 60 and pts <= 69:
    print(f"Grade: 2")
elif pts >= 70 and pts <= 79:
    print(f"Grade: 3")
elif pts >= 80 and pts <= 89:
    print(f"Grade: 4")
else:
    print(f"Grade: 5")