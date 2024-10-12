# In this exercise you will practice wrapping presents. You will write two classes: Present and Box. A present has a name and a weight, and a box contains presents.

# The Present class
# Please define the class Present which can be used to represent different kinds of presents. The class definition should contain attributes for the name and the weight (in kg) of the present. Instances of the class should work as follows:

# book = Present("ABC Book", 2)

# print("The name of the present:", book.name)
# print("The weight of the present:", book.weight)
# print("Present:", book)

# This should print out

# The name of the present: ABC Book
# The weight of the present: 2
# Present: ABC Book (2 kg)

# The Box class
# Please define the class Box. You should be able to add presents to the box, and the box should keep track of the combined weight of the presents within. The class definition should contain these methods:

# add_present(self, present: Present) which adds the present given as an argument to the box. The method has no return value.
# total_weight(self) which returns the combined weight of the presents in the box.
# You may use the following code to test your class:
    
# book = Present("ABC Book", 2)

# box = Box()
# box.add_present(book)
# print(box.total_weight())

# cd = Present("Pink Floyd: Dark Side of the Moon", 1)
# box.add_present(cd)
# print(box.total_weight())

class Present:

    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

class Box:

    def __init__(self):
        self.presents = []
        self.weigh = 0

    def add_present(self, present: Present):
        self.presents.append(present)
        self.weigh += present.weight

    def total_weight(self):
        return self.weigh