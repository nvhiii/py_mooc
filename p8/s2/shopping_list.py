# DO NOT CHANGE THE CODE OF THE CLASS
# ShoppingList. Write yous solution under it!
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def item(self, n: int):
        return self.products[n - 1][0]

    def amount(self, n: int):
        return self.products[n - 1][1]

# -------------------------
# Write your solution here:
# -------------------------

# The exercise template contains a pre-defined ShoppingList class, which can be used to model a shopping list. Your task is to add a method to the class definition. You do not need to change any methods already defined.

# Assuming we have a ShoppingList object referenced in a variable named shopping_list, the object can be handled with the following methods:

# print(shopping_list.number_of_items())
# print(shopping_list.item(1))
# print(shopping_list.amount(1))
# print(shopping_list.item(2))
# print(shopping_list.amount(2))

# 2
# Bananas
# 4
# Milk
# 1

# We can also do this:

# # the items on the shopping list are indexed from 1
# for i in range(1, shopping_list.number_of_items()+1):
#     item = shopping_list.item(i)
#     amount = shopping_list.amount(i)
#     print(f"{item}: {amount} units")

# Bananas 4 units
# Milk 1 units

# As you can see, a ShoppingList works a bit like a normal list, but it is accessed via the methods provided by the ShoppingList class. Unlike normal Python lists, indexing starts from 1, not 0.

# Please write a function named total_units(my_list: ShoppingList), which takes a ShoppingList type object as its argument. The function should calculate the total number of units listed, and return the value.

# You can use the following code to test your function:

# if __name__ == "__main__":
#     my_list = ShoppingList()
#     my_list.add("bananas", 10)
#     my_list.add("apples", 5)
#     my_list.add("pineapple", 1)

#     print(total_units(my_list))

# 16

# NB: the definition of the ShoppingList class is already included in the exercise template. You do not need to use an import statement to import it, unlike in the examples above with the Python standard library classes Fraction and date.

def total_units(my_list: ShoppingList):
    # since this obj list is a list of tuples, and index starts at 1 for the outer list
    total = 0
    for i in range(my_list.number_of_items()):
        total += my_list.amount(i)

    return total
    