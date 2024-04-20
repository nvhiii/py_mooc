# Write your solution here
# Please write a program which first asks 
# the user for the number of items to be added.
# Then the program should ask for the 
# given number of values, one by one, and 
# add them to a list in the order they were 
# typed in. Finally, the list is printed out.

items = []
num_items = int(input("How many items:"))
iterator = 1

while iterator <= num_items:
    item = int(input(f"Item {iterator}:"))
    items.append(item)
    iterator += 1

print(items)