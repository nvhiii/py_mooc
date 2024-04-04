# Write your solution here
width = int(input("Width: "))
height = int(input("Height: "))
# need to declare in var, cannot use literal inside expression for f-string
hash_str = "#"
x = 0
y = 0

# iterate height, print #s based on specified width
while y < height:
    print(f"{hash_str * width}")
    y += 1

