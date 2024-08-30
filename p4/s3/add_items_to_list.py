# Please write a program which first asks the user for the number 
# of items to be added. Then the program should ask for the given 
# number of values, one by one, and add them to a list in the order 
# they were typed in. Finally, the list is printed out.

# An example of expected behaviour:

# How many items: 3
# Item 1: 10
# Item 2: 250
# Item 3: 34
# [10, 250, 34]

items = int(input("How many items: "))
item_list = []
num = 1

while num <= items:

    item = int(input(f"Item {num}: "))
    item_list.append(item)
    num += 1

print(item_list)