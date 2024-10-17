# Please write an interactive application for keeping track of your studies. The internal structure is up to you, but this would be a good opportunity to practice creating a similar structure as in the PhoneBook example above.

# Your program should work as follows:

# 1 add course
# 2 get course data
# 3 statistics
# 0 exit

# command: 1
# course: ItP
# grade: 3
# credits: 5

# command: 2
# course: ItP
# ItP (5 cr) grade 3

# command: 1
# course: ItP
# grade: 5
# credits: 5

# command: 2
# course: ItP
# ItP (5 cr) grade 5

# command: 1
# course: ItP
# grade: 1
# credits: 5

# command: 2
# course: ItP
# ItP (5 cr) grade 5

# command: 2
# course: Introduction to Java
# no entry for this course

# command: 1
# course: ACiP
# grade: 1
# credits: 10

# command: 1
# course: ItAI
# grade: 2
# credits: 5

# command: 1
# course: Algo101
# grade: 4
# credits: 1

# command: 1
# course: CompModels
# grade: 5
# credits: 8

# command: 3
# 5 completed courses, a total of 29 credits
# mean 3.4
# grade distribution
# 5: xx
# 4: x
# 3:
# 2: x
# 1: x

# command: 0

# Each course name should result in a single entry in the records. A grade may be raised by re-entering the course details, but the grade should never be lowered.

# This exercise is worth two exercise points. The first is granted after the commands 1, 2 and 0 work correctly in your program. The second is granted if command 3 also works as expected.

class Course():
    def __init__(self, cname: str, grade: int, credits: int):
        self.__cname = cname
        self.__grade = grade
        self.__credits = credits

    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, val: int):
        self.__grade = val

    def __str__(self):
        return f"{self.__cname} ({self.__credits} cr) grade {self.__grade}"

class CourseList():
    def __init__(self):
        self.__courses = {} # since each course name only should appear once, use dict
    
    def add_c(self, name: str, grade: int, creds: int):
        # increment grade 
        if name in self.__courses:
            if self.__courses[name].grade < grade:
                self.__courses[name].grade = grade
        else:
            self.__courses[name] = Course(name, grade, creds)

    def get_c(self, name: str):
        if name not in self.__courses:
            return None
        return self.__courses[name] # return entire course obj

class CourseRecordsApplication():
    def __init__(self):
        self.__cl = CourseList()

    def prompts(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        # since exercise didnt specify to raise error, neither will i here
        course = input("course: ")
        grade = int(input("grade: "))
        creds = int(input("credits: "))
        self.__cl.add_c(course, grade, creds)

    def get_course_data(self):
        course = input("course: ")
        entire_course = self.__cl.get_c(course)
        if entire_course == None:
            print("no entry for this course")
        print(entire_course)

    def execute(self):
        self.prompts()
        while True:
            print("")
            cmd = input("command: ")
            if cmd == "0":
                break
            if cmd == "1":
                self.add_course()
            if cmd == "2":
                self.get_course_data()
            
app = CourseRecordsApplication()
app.execute()
