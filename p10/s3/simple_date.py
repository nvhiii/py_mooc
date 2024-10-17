# # WRITE YOUR SOLUTION HERE:

# In this exercise you are asked to implement the class SimpleDate which allows you to handle dates. For simplicity's sake we assume here that each month has 30 days.

# Because of this simplification you should not use the datetime module from the Python standard library. You will implement similar functionality by yourself instead.

# Comparisons
# Please implement the outline of the class, along with methods allowing for comparisons with the operators <, >, == and !=. You can use the following code to test your implementation:

# d1 = SimpleDate(4, 10, 2020)
# d2 = SimpleDate(28, 12, 1985)
# d3 = SimpleDate(28, 12, 1985)

# print(d1)
# print(d2)
# print(d1 == d2)
# print(d1 != d2)
# print(d1 == d3)
# print(d1 < d2)
# print(d1 > d2)

# 4.10.2020
# 28.12.1985
# False
# True
# False
# False
# True

# Increment
# Please implement the addition operator + which allows you to add a given number of days to a SimpleDate object. The operator should return a new SimpleDate object. The original object should not be changed.

# d1 = SimpleDate(4, 10, 2020)
# d2 = SimpleDate(28, 12, 1985)

# d3 = d1 + 3
# d4 = d2 + 400

# print(d1)
# print(d2)
# print(d3)
# print(d4)

# 4.10.2020
# 28.12.1985
# 7.10.2020
# 8.2.1987

# Difference
# Please implement the subtraction operator - which allows you to find out the difference in days between two SimpleDate objects. As we assumed each month to have 30 days, a year within the confines of this exercise is 12*30 = 360 days long.

# You can use the following code to test your program:

# d1 = SimpleDate(4, 10, 2020)
# d2 = SimpleDate(2, 11, 2020)
# d3 = SimpleDate(28, 12, 1985)

# print(d2-d1)
# print(d1-d2)
# print(d1-d3)

# 28
# 28
# 12516

class SimpleDate():
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"

    def __lt__(self, another: "SimpleDate"):
        if self.__year == another.__year:
            if self.__month == another.__month:
                return self.__day < another.__day
            return self.__month < another.__month
        # default condition to determine which date is "less"
        return self.__year < another.__year
    
    def __gt__(self, another: "SimpleDate"):
        if self.__year == another.__year:
            if self.__month == another.__month:
                return self.__day > another.__day
            return self.__month > another.__month
        # default condition to determine which date is "less"
        return self.__year > another.__year
    
    def __eq__(self, another: "SimpleDate"):
        return self.__year == another.__year and self.__month == another.__month and self.__day == another.__day
    
    def __ne__(self, another: "SimpleDate"):
        return self.__year != another.__year or self.__month != another.__month or self.__day != another.__day
    
    def __add__(self, num_days: int):
        if self.__day + num_days <= 30:
            new_day = self.__day + num_days
            new_date = SimpleDate(new_day, self.__month, self.__year)
            return new_date
        else:
            new_day = (self.__day + num_days) % 30
            num_month = (self.__day + num_days) // 30
            new_month = self.__month + num_month
            
            if new_month <= 12:
                new_date = SimpleDate(new_day, new_month, self.__year)
                return new_date
            else:
                # If months overflow past 12, adjust both month and year
                new_month = new_month % 12
                num_year = self.__year + (self.__month + num_month - 1) // 12
                new_date = SimpleDate(new_day, new_month, num_year)
                return new_date
            
    def __sub__(self, other):
        # Convert both dates to total days since day 0
        self_total_days = self.__year * 360 + self.__month * 30 + self.__day
        other_total_days = other.__year * 360 + other.__month * 30 + other.__day
        
        # Return the absolute difference in days
        return abs(self_total_days - other_total_days)
