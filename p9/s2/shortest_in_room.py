# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.people = []

    def add(self, person: Person):
        self.people.append(person)

    def is_empty(self):
        if len(self.people) == 0:
            return True
        return False
    
    def print_contents(self):
        for person in self.people:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if not self.is_empty():
            smallest_height = self.people[0].height
            smallest = self.people[0]
            for person in self.people:
                if person.height < smallest_height:
                    smallest_height = person.height
                    smallest = person
            return smallest
        return None
    
    def remove_shortest(self):
        shortest_person = self.shortest()
        if not self.is_empty():
            self.people.remove(shortest_person)
            return shortest_person
        return None

# The exercise template contains the class Person. A person has a name and a height. In this exercise you will implement the class Room. You may add any number of persons to a room, and you may also search for and remove the shortest person in the room.

# Room
# Please define the class Room. It should have a list of persons as an attribute, and also contain the following methods:

# add(person: Person) adds the person given as an argument to the room.
# is_empty() returns True or False depending on whether the room is empty.
# print_contents() prints out the contents of the list of persons in the room.
# Please have a look at the following usage example:

# room = Room()
# print("Is the room empty?", room.is_empty())
# room.add(Person("Lea", 183))
# room.add(Person("Kenya", 172))
# room.add(Person("Ally", 166))
# room.add(Person("Nina", 162))
# room.add(Person("Dorothy", 155))
# print("Is the room empty?", room.is_empty())
# room.print_contents()

# Is the room empty? True
# Is the room empty? False
# There are 5 persons in the room, and their combined height is 838 cm
# Lea (183 cm)
# Kenya (172 cm)
# Ally (166 cm)
# Nina (162 cm)
# Dorothy (155 cm)

# The shortest person
# Please define the method shortest() within the Room class definition. The method should return the shortest person in the room it is called on. If the room is empty, the method should return None. The method should not remove the person fron the room.

# room = Room()

# print("Is the room empty?", room.is_empty())
# print("Shortest:", room.shortest())

# room.add(Person("Lea", 183))
# room.add(Person("Kenya", 172))
# room.add(Person("Nina", 162))
# room.add(Person("Ally", 166))

# print()

# print("Is the room empty?", room.is_empty())
# print("Shortest:", room.shortest())

# print()

# room.print_contents()

# Is the room empty? True
# Shortest: None

# Is the room empty? False
# Shortest: Nina

# There are 4 persons in the room, and their combined height is 683 cm
# Lea (183 cm)
# Kenya (172 cm)
# Nina (162 cm)
# Ally (166 cm)

# Removing a person from the room
# Please define the method remove_shortest() within the Room class definition. The method should remove the shortest Person object from the room and return the reference to the object. If the room is empty, the method should return None.

# room = Room()

# room.add(Person("Lea", 183))
# room.add(Person("Kenya", 172))
# room.add(Person("Nina", 162))
# room.add(Person("Ally", 166))
# room.print_contents()

# print()

# removed = room.remove_shortest()
# print(f"Removed from room: {removed.name}")

# print()

# room.print_contents()

# There are 4 persons in the room, and their combined height is 683 cm
# Lea (183 cm)
# Kenya (172 cm)
# Nina (162 cm)
# Ally (166 cm)

# Removed from room: Nina

# There are 3 persons in the room, and their combined height is 521 cm
# Lea (183 cm)
# Kenya (172 cm)
# Ally (166 cm)

# Hint: in part 4 you will find instructions for removing items from a list.

# Hint2: it is always possible to call another method of the same class from within a method. The following should work just fine:

# class Room:
#     # ...
#     def shortest(self):
#         # your code goes here

#     def remove_shortest(self):
#         shortest_person = self.shortest()
#         # ...