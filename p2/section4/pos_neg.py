# Write your solution here
print(f"Please type in integer numbers. Type in 0 to finish.")
count = 0
total = 0
positive = 0
negative = 0

while True:
    num = int(input("Number: "))

    if num == 0:
        break

    if num > 0:
        positive += 1
    else:
        negative += 1

    count += 1
    total += num

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {total}")
print(f"The mean of the numbers is {total / count}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")


