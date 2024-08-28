# Please write a program which asks the user to type in values 
# and adds them to a list. After each addition, the list is printed out 
# in two different ways:

# in the order the items were added
# ordered from smallest to greatest
# The program exits when the user types in 0.

# An example of expected behaviour:

# New item: 3
# The list now: [3]
# The list in order: [3]
# New item: 1
# The list now: [3, 1]
# The list in order: [1, 3]
# New item: 9
# The list now: [3, 1, 9]
# The list in order: [1, 3, 9]
# New item: 5
# The list now: [3, 1, 9, 5]
# The list in order: [1, 3, 5, 9]
# New item: 0
# Bye!

my_list = []

while True:

    num = int(input("New item: "))
    if num == 0:
        print("Bye!")
        break

    my_list.append(num)
    sort_list = sorted(my_list)
    print(f"The list now: {my_list}")
    print(f"The list in order: {sort_list}")
        


