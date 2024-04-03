# Write your solution here
upper_lim = int(input("Upper limit: "))
base = int(input("Base: "))
power = 0

while base ** power <= upper_lim:
    print(f"{base ** power}")
    power += 1