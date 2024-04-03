# Write your solution here
limit = int(input("Limit: ")) # this is the in
first = 0
incrementer = 1

while first < limit:
    first += incrementer
    incrementer += 1

print(f"{first}")