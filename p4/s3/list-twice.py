# Write your solution here
# Please write a program which asks the user to 
# type in values and adds them to a list. After 
# each addition, the list is printed out in two different ways:

# in the order the items were added
# ordered from smallest to greatest
# The program exits when the user types in 0.

my_list = []

while True:

    # prompt input for list
    value = int(input("New item: "))
    if value == 0:
        print("Bye!")
        break
    
    my_list.append(value)
    sortList = sorted(my_list)
    print(f"The list now: {my_list}")
    print(f"The list in order: {sortList}")