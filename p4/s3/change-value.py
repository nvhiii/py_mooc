# Please write a program which initialises a list \
# with the values [1, 2, 3, 4, 5]. Then the 
# program should ask the user for an index and 
# a new value, replace the value at the given index,
#  and print the list again. This should be looped 
#over until the user gives -1 for the index. 
# You can assume all given index values will 
# fall within your list.

my_list = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index:"))

    # handle -1 index here
    if index == -1:
        break

    new_val = int(input("New value:"))
    my_list[index] = new_val
    print(my_list)
