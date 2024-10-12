# Write your solution here:

class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

# The database of a real estate agency keeps records of available properties with objects defined by the following class:

# Your task is to implement methods which allow for comparison between available properties.

# Is it bigger?
# Please write a method named bigger(self, compared_to) which returns True if the RealProperty object itself is bigger than the one it is compared to.

# An example of how the function should work:

# central_studio = RealProperty(1, 16, 5500)
# downtown_two_bedroom = RealProperty(2, 38, 4200)
# suburbs_three_bedroom = RealProperty(3, 78, 2500)

# print(central_studio.bigger(downtown_two_bedroom))
# print(suburbs_three_bedroom.bigger(downtown_two_bedroom))

# False
# True

# Price difference
# Please write a method named price_difference(self, compared_to) which returns the difference in price between the RealProperty object itself and the one it is compared to. The price difference is the absolute value of the difference between the total prices of the two properties. The total price of a property is its price per square metre multiplied by the amount of square metres in the property.

# An example of how the function should work:

# central_studio = RealProperty(1, 16, 5500)
# downtown_two_bedroom = RealProperty(2, 38, 4200)
# suburbs_three_bedroom = RealProperty(3, 78, 2500)

# print(central_studio.price_difference(downtown_two_bedroom))
# print(suburbs_three_bedroom.price_difference(downtown_two_bedroom))

# 71600
# 35400

# Is it more expensive?
# Please write a method named more_expensive(self, compared_to) which returns True if the RealProperty object itself is more expensive that the one it is compared to.

# An example of how the function should work:

# central_studio = RealProperty(1, 16, 5500)
# downtown_two_bedroom = RealProperty(2, 38, 4200)
# suburbs_three_bedroom = RealProperty(3, 78, 2500)

# print(central_studio.more_expensive(downtown_two_bedroom))
# print(suburbs_three_bedroom.more_expensive(downtown_two_bedroom))

# False
# True

    def bigger(self, compared_to: "RealProperty"):
        return self.square_metres > compared_to.square_metres
    
    def price_difference(self, compared_to: "RealProperty"):
        total_price_self = self.square_metres * self.price_per_sqm
        total_price_other = compared_to.square_metres * compared_to.price_per_sqm
        return abs(total_price_self - total_price_other)
    
    def more_expensive(self, compared_to: "RealProperty"):
        return self.rooms * self.square_metres * self.price_per_sqm > compared_to.rooms * compared_to.square_metres * compared_to.price_per_sqm