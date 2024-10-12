# Please create a class named Recording which models a single recording. The class should have one private variable: __length of type integer.

# Please implement the following:

# a constructor which takes the length as an argument
# a getter method length which returns the length of the recording
# a setter method which sets the length of the recording
# It should be possible to make use of the class as follows:

# the_wall = Recording(43)
# print(the_wall.length)
# the_wall.length = 44
# print(the_wall.length)

# 43
# 44

# If the argument for either the constructor or the setter method is below zero, this should raise a ValueError.

# If you need a refresher on raising exceptions, please see part 6 of the course materials.

class Recording:

    def __init__(self, length: int):
        if length >= 0:
            self.__length = length
        else:
            raise ValueError("Length cannot be negative")

    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, new_length: int):
        if new_length >= 0:
            self.__length = new_length
        else:
            raise ValueError("Length cannot be a negative value")