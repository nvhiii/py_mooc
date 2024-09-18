# In this series of exercises you will create a simple student database. Before diving in, please spend a moment reading through the instructions and thinking about what sort of data structures are necessary for organising the data stored by your program.

# adding students
# First write a function named add_student, which adds a new student to the database. Also write a preliminary version of the function print_student, which prints out the information of a single student.

# These function are used as follows:

# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# print_student(students, "Peter")
# print_student(students, "Eliza")
# print_student(students, "Jack")

# Your program should now print out

# Peter:
#  no completed courses
# Eliza:
#  no completed courses
# Jack: no such person in the database

# adding completed courses
# Please write a function named add_course, which adds a completed course to the information of a specific student in the database. The course data is a tuple consisting of the name of the course and the grade:

# students = {}
# add_student(students, "Peter")
# add_course(students, "Peter", ("Introduction to Programming", 3))
# add_course(students, "Peter", ("Advanced Course in Programming", 2))
# print_student(students, "Peter")

# When some courses have been added, the information printed out changes:

# Peter:
#  2 completed courses:
#   Introduction to Programming 3
#   Advanced Course in Programming 2
#  average grade 2.5

# repeating courses
# Courses with grade 0 should be ignored when adding course information. Additionally, if the course is already in the database in that specific student's information, the grade recorded in the database should never be lowered if the course is repeated.

# students = {}
# add_student(students, "Peter")
# add_course(students, "Peter", ("Introduction to Programming", 3))
# add_course(students, "Peter", ("Advanced Course in Programming", 2))
# add_course(students, "Peter", ("Data Structures and Algorithms", 0))
# add_course(students, "Peter", ("Introduction to Programming", 2))
# print_student(students, "Peter")

# Peter:
#  2 completed courses:
#   Introduction to Programming 3
#   Advanced Course in Programming 2
#  average grade 2.5

# summary of database
# Please write a function named summary, which prints out a summary based on all the information stored in the database.

# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# add_course(students, "Peter", ("Data Structures and Algorithms", 1))
# add_course(students, "Peter", ("Introduction to Programming", 1))
# add_course(students, "Peter", ("Advanced Course in Programming", 1))
# add_course(students, "Eliza", ("Introduction to Programming", 5))
# add_course(students, "Eliza", ("Introduction to Computer Science", 4))
# summary(students)

# This should print out

# students 2
# most courses completed 3 Peter
# best average grade 4.5 Eliza