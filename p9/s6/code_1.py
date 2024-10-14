# In this series of exercises you will create the classes Item, Suitcase and Cargo Hold, which will let you further practice working on objects which contain references to other objects.

# Item
# Please create a class named Item which is used to create items of different kinds. Each item has a name and a weight (in kilograms).

# You can use the following code to test your class:

# book = Item("ABC Book", 2)
# phone = Item("Nokia 3210", 1)

# print("Name of the book:", book.name())
# print("Weight of the book:", book.weight())

# print("Book:", book)
# print("Phone:", phone)

# Your program should print out this:

# Name of the book: ABC Book
# Weight of the book: 2
# Book: ABC Book (2 kg)
# Phone: Nokia 3210 (1 kg)

# An Item should provide the methods weight and name, which return the values stored in those attributes.

# The name and weight should be encapsulated within the class. The following code should not work:

# book = Item("ABC Book", 2)
# book.weight = 10

# Suitcase
# Please write a class named Suitcase. You should be able to pack items into a suitcase. A suitcase also has a maximum combined weight for the items stored within.

# Your class should contains the following members:

# a constructor which takes the maximum weight as an argument
# a method named add_item which adds the item given as an argument to the suitcase. The method has no return value.
# a __str__ method which returns a string in the format "x items (y kg)"
# The class should make sure that the combined weight of the items stored within any Suitcase does not exceed the maximum weight set for that instance. If the maximum weight would be exceeded when the add_item method is called, the new item should not be added to the suitcase.

# Your class should work as follows:

# book = Item("ABC Book", 2)
# phone = Item("Nokia 3210", 1)
# brick = Item("Brick", 4)

# suitcase = Suitcase(5)
# print(suitcase)

# suitcase.add_item(book)
# print(suitcase)

# suitcase.add_item(phone)
# print(suitcase)

# suitcase.add_item(brick)
# print(suitcase)

# Executing the above should print out

# 0 items (0 kg)
# 1 items (2 kg)
# 2 items (3 kg)
# 2 items (3 kg)

# Mind your language
# The notification "1 items" is not very grammatical. Instead, it should say "1 item". Please make the required changes to your __str__ method.

# The previous example should now print out

# 0 items (0 kg)
# 1 item (2 kg)
# 2 items (3 kg)
# 2 items (3 kg)

# All the items
# Please add the following methods to your Suitcase class definition:

# print_items prints out all the items stored in the suitcase
# weight returns an integer number representing the combined weight of all the items stored in the suitcase
# Your class should now work with the following program:

# book = Item("ABC Book", 2)
# phone = Item("Nokia 3210", 1)
# brick = Item("Brick", 4)

# suitcase = Suitcase(10)
# suitcase.add_item(book)
# suitcase.add_item(phone)
# suitcase.add_item(brick)

# print("The suitcase contains the following items:")
# suitcase.print_items()
# combined_weight = suitcase.weight()
# print(f"Combined weight: {combined_weight} kg")

# Executing the above program should print out this:

# The suitcase contains the following items:
# ABC Book (2 kg)
# Nokia 3210 (1 kg)
# Brick (4 kg)
# Combined weight: 7 kg

# If you have implemented your Suitcase class with more than two instance variables, please make the required changes so that each instance has only two data attributes: the maximum weight and a list of items within.

# The heaviest item
# Please add a new method to your Suitcase class: heaviest_item should return the Item which is the heaviest. If there are two or more items with the same, heaviest weight, the method may return any one of these. The method should return a reference to an object. If the suitcase is empty, the method should return None.

# Your class should now work with the following program:

# book = Item("ABC Book", 2)
# phone = Item("Nokia 3210", 1)
# brick = Item("Brick", 4)

# suitcase = Suitcase(10)
# suitcase.add_item(book)
# suitcase.add_item(phone)
# suitcase.add_item(brick)

# heaviest = suitcase.heaviest_item()
# print(f"The heaviest item: {heaviest}")

# Executing the above program should print out this:

# The heaviest item: Brick (4 kg)

# Cargo hold
# Please write a class named CargoHold with the following methods:

# a constructor which takes the maximum weight as an argument
# a method named add_suitcase which adds the suitcase given as an argument to the cargo hold
# a __str__ method which returns a string in the format "x suitcases, space for y kg"
# The class should make sure that the combined weight of the items stored within any CargoHold does not exceed the maximum weight set for that instance. If the maximum weight would be exceeded when the add_suitcase method is called, the new suitcase should not be added to the cargo hold.

# Your class should now work with the following program:

# cargo_hold = CargoHold(1000)
# print(cargo_hold)

# book = Item("ABC Book", 2)
# phone = Item("Nokia 3210", 1)
# brick = Item("Brick", 4)

# adas_suitcase = Suitcase(10)
# adas_suitcase.add_item(book)
# adas_suitcase.add_item(phone)

# peters_suitcase = Suitcase(10)
# peters_suitcase.add_item(brick)

# cargo_hold.add_suitcase(adas_suitcase)
# print(cargo_hold)

# cargo_hold.add_suitcase(peters_suitcase)
# print(cargo_hold)

# 0 suitcases, space for 1000 kg
# 1 suitcase, space for 997 kg
# 2 suitcases, space for 993 kg

# The contents of the cargo hold
# Please add a method named print_items to your CargoHold class. It should print out all the items in all the suitcases within the cargo hold.

# Your class should now work with the following program:

# book = Item("ABC Book", 2)
# phone = Item("Nokia 3210", 1)
# brick = Item("Brick", 4)

# adas_suitcase = Suitcase(10)
# adas_suitcase.add_item(book)
# adas_suitcase.add_item(phone)

# peters_suitcase = Suitcase(10)
# peters_suitcase.add_item(brick)

# cargo_hold = CargoHold(1000)
# cargo_hold.add_suitcase(adas_suitcase)
# cargo_hold.add_suitcase(peters_suitcase)

# print("The suitcases in the cargo hold contain the following items:")
# cargo_hold.print_items()

# Executing the above program should print out this:

# The suitcases in the cargo hold contain the following items:
# ABC Book (2 kg)
# Nokia 3210 (1 kg)
# Brick (4 kg)

class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    @property
    def weight(self):
        return self.__weight

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"  # formatted item instance


class Suitcase:
    def __init__(self, maximum_weight: int):
        self.__maximum_weight = maximum_weight
        self.__case = []

    def add_item(self, item: "Item"):
        curr = self.weight()
        if curr + item.weight <= self.__maximum_weight:  # Access weight as a property
            self.__case.append(item)

    def print_items(self):
        for item in self.__case:
            print(item)

    def weight(self):
        return sum([x.weight for x in self.__case])  # Directly sum the weights

    def heaviest_item(self):
        if not self.__case:
            return None
        return max(self.__case, key=lambda item: item.weight)  # Access weight as a property

    def __str__(self):
        weight_case = self.weight()
        num_items = len(self.__case)
        if num_items == 1:
            return f"{num_items} item ({weight_case} kg)"  # Correct plurality
        return f"{num_items} items ({weight_case} kg)"


class CargoHold:
    def __init__(self, maximum_weight: int):
        self.__maximum_weight = maximum_weight
        self.__hold = []

    def add_suitcase(self, case: "Suitcase"):
        curr = sum([x.weight() for x in self.__hold])  # Calculate the current weight in the hold
        if curr + case.weight() <= self.__maximum_weight:
            self.__hold.append(case)

    def print_items(self):
        for case in self.__hold:
            case.print_items()

    def __str__(self):
        curr_weight = sum([x.weight() for x in self.__hold])
        return f"{len(self.__hold)} suitcases, space for {self.__maximum_weight - curr_weight} kg"  # Use 'suitcases' for consistency
