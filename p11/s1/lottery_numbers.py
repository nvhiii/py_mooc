# LotteryNumbers matched
# Please write a class named LotteryNumbers which takes the week number (an integer value) and a list of seven integers as its constructor arguments. The list should contain the correct lottery numbers for the given week.

# Please also write a method named number_of_hits(numbers: list) which takes a list of integers as its argument. The method returns the number of correct entries in the parameter list.

# The method should use a list comprehension to achieve this. The maximum length of the function is two lines of code, including the header line beginning with the def keyword.

# An example of how the class and function are used:

# week5 = LotteryNumbers(5, [1,2,3,4,5,6,7])
# my_numbers = [1,4,7,11,13,19,24]

# print(week5.number_of_hits(my_numbers))

# 3

# LotteryNumbers matched in place
# Please write a method named hits_in_place(numbers) which takes a list of seven integers as its argument, and returns a new list of seven integers. The new list contains only those items from the original list which match the week's correct numbers. These must remain at the same indexes as they were in the original list. The rest of the indexes should be filled with values -1.

# The method should use a list comprehension to achieve this. The maximum length of the function is two lines of code, including the header line beginning with the def keyword.

# Please take a look at the example below:

# week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
# my_numbers = [1,4,7,10,11,20,30]

# print(week8.hits_in_place(my_numbers))

# [1, -1, -1, 10, -1, 20, 30]

class LotteryNumbers:
    def __init__(self, week_number: int, seven_numbers: list):
        self.week_number = week_number
        self.seven_numbers = seven_numbers
    
    def number_of_hits(self, numbers: list):
        return len([num for num in numbers if num in self.seven_numbers])
    
    def hits_in_place(self, numbers: list):
        return [hit if hit in self.seven_numbers else -1 for hit in numbers]