# Write your solution after the class Car
# Do not make changes to the class!
class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

    def __str__(self):
        return f"Car (make: {self.make}, top speed: {self.top_speed})"

# WRITE YOUR SOLUTION HERE:

# The exercise template contains a class named Car which represents the features of a car through two attributes: make (str) and top_speed (int).

# Please write a function named fastest_car(cars: list) which takes a list of Car objects as its argument.

# The function should return the make of the fastest car. You may assume there will always be a single car with the highest top speed. Do not change the list given as an argument, or make any changes to the Car class definition.

# You may use the following code to test your function:

# if __name__ == "__main__":
#     car1 = Car("Saab", 195)
#     car2 = Car("Lada", 110)
#     car3 = Car("Ferrari", 280)
#     car4 = Car("Trabant", 85)

#     cars = [car1, car2, car3, car4]
#     print(fastest_car(cars))

# Ferrari
def fastest_car(cars: list):
    fastest = cars[0].top_speed # gets make from first car obj
    fastest_car = cars[0].make
    for car in cars:
        if car.top_speed > fastest:
            fastest = car.top_speed
            fastest_car = car.make

    return fastest_car