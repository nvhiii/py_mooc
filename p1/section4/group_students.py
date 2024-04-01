# Write your solution here
students = int(input("How many students on the course? "))
size = int(input("Desired group size? "))

if students % size != 0:
    groups = (students // size) + 1
    print(f"Number of groups formed: {groups}")

if students % size == 0:
    groups = students / size
    print(f"Number of groups formed: {groups}")