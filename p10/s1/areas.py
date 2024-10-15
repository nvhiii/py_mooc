# Write your solution here!
class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        return f"rectangle {self.width}x{self.height}"

    def area(self):
        return self.width * self.height

# The exercise template contains a class definition for a Rectangle. It represents a rectangle shape. A Rectangle works like this:

# rectangle = Rectangle(2, 3)
# print(rectangle)
# print("area:", rectangle.area())

# rectangle 2x3
# area: 6

# Square
# Please define a class named Square which inherits the Rectangle class. The sides of a square are all of equal length, which makes the square a special case of the rectangle. The new class should not contain any new attributes.

# A Square object is used as follows:

# square = Square(4)
# print(square)
# print("area:", square.area())

# square 4x4
# area: 16

class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)

    def __str__(self):
        return f"square {self.width}x{self.height}"