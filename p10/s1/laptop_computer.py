# Write your solution here:
class Computer:
    def __init__(self, model: str, speed: int):
        self.__model = model
        self.__speed = speed

    @property
    def model(self):
        return self.__model

    @property
    def speed(self):
        return self.__speed

# The exercise template contains a class definition for a Computer, which has the attributes model and speed.

# Please define a class named LaptopComputer which inherits the class Computer. The constructor of the new class should take a third argument: weight, of type integer.

# Please also include a __str__ method in your class definition. See the example below for the expected format of the string representation printed out.

# laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
# print(laptop)

# NoteBook Pro15, 1500 MHz, 2 kg

class LaptopComputer(Computer):
    def __init__(self, model: str, speed: int, weight: int):
        super().__init__(model, speed) # since same attr
        self.__weight = weight

    @property
    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{super().model}, {super().speed} MHz, {self.weight} kg"