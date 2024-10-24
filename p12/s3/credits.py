from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

# In this exercise we will work with a slightly modified version of the CourseAttempt class. The name of the student is omitted, but the number of credits is included. The class works as follows:

# attempt = CourseAttempt("Data Structures and Algorithms", 3, 10)
# print(attempt)
# print(attempt.course_name)
# print(attempt.credits)
# print(attempt.grade)

# Data Structures and Algorithms (10 cr) grade 3
# Data Structures and Algorithms
# 10
# 3

# The sum of all credits
# Please implement a function named sum_of_all_credits which takes a list of course attempts as its argument. The function sums up the total number of study credits covered by the courses. It should work like this:

# s1 = CourseAttempt("Introduction to Programming", 5, 5)
# s2 = CourseAttempt("Advanced Course in Programming", 4, 5)
# s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
# credit_sum = sum_of_all_credits([s1, s2, s3])
# print(credit_sum)

# 20

# Please implement the function using the reduce function.

# The sum of passed credits
# Please implement a function named sum_of_passed_credits which takes a list of course attempts as its argument. The function sums up the credits for the course attempts with grade 1 or above. It should work like this:

# s1 = CourseAttempt("Introduction to Programming", 5, 5)
# s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
# s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
# credit_sum = sum_of_passed_credits([s1, s2, s3])
# print(credit_sum)

# 15

# Please implement the function using the reduce and filter functions.

# Average grade for passed courses
# Please implement a function named average which takes a list of course attempts as its argument. The function calculates the average grade for the course attempts with grade 1 or above. It should work like this:

# s1 = CourseAttempt("Introduction to Programming", 5, 5)
# s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
# s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
# ag = average([s1, s2, s3])
# print(ag)

# 4.0

# Please implement the function using the reduce and filter functions. NB: the exercise asks for a simple mean value, not a weighted average.

# While working on this exercise, it is likely worth remembering that the return value of filter is an iterator.

def sum_of_all_credits(course_list: list):
    return reduce(lambda total_sum, course: total_sum + course.credits, course_list, 0)

def sum_of_passed_credits(course_list: list):
    filtered = filter(lambda course: course.grade >= 1, course_list)
    return reduce(lambda total, course: total + course.credits, filtered, 0)

def average(course_list: list):
    filtered = list(filter(lambda course: course.grade >= 1, course_list))
    t = reduce(lambda total, course: total + course.grade, filtered, 0)
    return t / len(filtered)