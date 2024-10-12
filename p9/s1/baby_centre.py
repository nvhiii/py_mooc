
# WRITE YOUR SOLUTION HERE:
#Note! Do not change the class Person!

class Person:
    def __init__(self, name: str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class BabyCentre:
    def __init__(self):
        self.number_of_weigh_ins = 0

    def weigh(self, person: Person):
        # return the weight of the person passed as an argument
        self.number_of_weigh_ins += 1
        return person.weight
    
    def feed(self, person: Person):
        person.weight += 1

    def weigh_ins(self):
        return self.number_of_weigh_ins
    
# The exercise template contains a class named Person and a skeleton implementation for the class BabyCentre. A BabyCentre object performs various actions on a Person object. It may, for example, weigh or feed the person. In this exercise you will implement the rest of the BabyCentre class. Please do not change the class definition of Person in any way.

# Weighing persons
# The BabyCentre class definition contains an outline for the function weigh:

# The method takes a Person object as its argument. It should return the weight of the person. You can access the weight of a person through the appropriate attribute defined in the Person class. Please fill in the rest of the implementation for the method weigh.

# Below is an example of a main function where a BabyCentre weighs two separate Person objects:

# Feeding
# It is possible to change the state of an object passed as an argument. Please implement the method feed(person: Person) which increases by one the weight of the person passed as an argument.

# In the following example two persons are weighed, and then one of them is fed three times. Then the persons are weighed again:

# baby_centre = BabyCentre()

# eric = Person("Eric", 1, 110, 7)
# peter = Person("Peter", 33, 176, 85)

# print(f"{eric.name} weighs {baby_centre.weigh(eric)} kg")
# print(f"{peter.name} weighs {baby_centre.weigh(peter)} kg")
# print() 

# baby_centre.feed(eric)
# baby_centre.feed(eric)
# baby_centre.feed(eric)

# print(f"{eric.name} weighs {baby_centre.weigh(eric)} kg")
# print(f"{peter.name} weighs {baby_centre.weigh(peter)} kg")

# The printout should reveal that Eric's weight has increased by three:

# Eric weighs 7 kg
# Peter weighs 85 kg

# Eric weighs 10 kg
# Peter weighs 85 kg

# Counting weigh-ins
# Please implement the method weigh_ins() which returns the total number of weigh-ins a BabyCentre object has performed. NB: you will need a new attribute for keeping track of the number of weigh-ins. You can use the following code to test your method:
    
# baby_centre = BabyCentre()

# eric = Person("Eric", 1, 110, 7)
# peter = Person("Peter", 33, 176, 85)

# print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

# baby_centre.weigh(eric)
# baby_centre.weigh(eric)

# print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

# baby_centre.weigh(eric)
# baby_centre.weigh(eric)
# baby_centre.weigh(eric)
# baby_centre.weigh(eric)

# print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

# Total number of weigh-ins is 0
# Total number of weigh-ins is 2
# Total number of weigh-ins is 6
