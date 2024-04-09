# Write your solution here
# this is the singular input for the num of nums printed
total = int(input("Please type in a number: "))
index = 1

#  iterate all num
if index == total:
    print(index)
else:
    while index < total:
        # print first
        print(index)
        index += 1
        # last num
        print(total)
        total -= 1
        if index == total:
            print(index)
