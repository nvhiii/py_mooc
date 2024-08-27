# Please write a new version of the program in the previous exercise. 
# In addition to the result it should also print out the 
# calculation performed:

# Limit: 2
# The consecutive sum: 1 + 2 = 3

# Limit: 10
# The consecutive sum: 1 + 2 + 3 + 4 = 10

# Limit: 18
# The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21

# init
limit = int(input("Limit: "))
num = 1
summation = 0
sum_string = ""

while not summation >= limit:

    summation += num
    if (summation < limit):
        sum_string += f"{num} + "
    else:
        sum_string += f"{num}"

    # increment number
    num += 1

print(f"The consecutive sum: {sum_string} = {summation}")



