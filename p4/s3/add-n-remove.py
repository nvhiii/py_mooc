# Please write a program which asks the user to choose 
# between addition and removal. Depending on the choice,
#  the program adds an item to or removes an item from 
# the end of a list. The item that is added must always 
# be one greater than the last item in the list. The first 
# item to be added must be 1.

# initialize empty list
my_list = []
print(f"The list is now {my_list}")
iterator = 1

while True:
    prompt = input("a(d)d, (r)emove or e(x)it:")
    if prompt == "d":
        my_list.append(iterator)
        print(f"The list is now {my_list}")
        iterator += 1
    elif prompt == "r":
        my_list.pop(len(my_list)-1)
        print(f"The list is now {my_list}")
        iterator -= 1
    else:
        print("Bye!")
        break