limit = int(input("Limit: "))
total = 0
incrementer = 1
sum_string = ""

while total < limit:
    total += incrementer
    if incrementer == 1:
        sum_string += f"{incrementer}"
    else:
        sum_string += f" + {incrementer}"
    incrementer += 1

print(f"The consecutive sum: {sum_string} = {total}")