# In this exercise you will write two different classes, which will in turn form the backbone of the programming exercise which follows this one, where you will write an interactive application.

# Task
# Please write a class named Task which models a single task in a software company's list of tasks. Tasks have

# a description
# an estimate of the hours required for completing the task
# the name of the programmer assigned to the task
# a field for keeping track of whether the task is finished
# a unique identifier
# The class is used as follows:

# t1 = Task("program hello world", "Eric", 3)
# print(t1.id, t1.description, t1.programmer, t1.workload)
# print(t1)
# print(t1.is_finished())
# t1.mark_finished()
# print(t1)
# print(t1.is_finished())
# t2 = Task("program webstore", "Adele", 10)
# t3 = Task("program mobile app for workload accounting", "Eric", 25)
# print(t2)
# print(t3)

# 1 program hello world Eric 3
# 1: program hello world (3 hours), programmer Eric NOT FINISHED
# False
# 1: program hello world (3 hours), programmer Eric FINISHED
# True
# 2: program webstore (10 hours), programmer Adele NOT FINISHED
# 3: program mobile app for workload accounting (25 hours), programmer Eric NOT FINISHED
    
# Some clarifications:

# the state of the task (finished or not yet finished) can be checked with the function is_finished(self) which returns a Boolean value
# a task is not finished when it is created
# a task is marked as finished by calling the method mark_finished(self)
# the id of a task is a running number which starts with 1. The id of the first task is 1, the id of the second is 2, and so forth.
# Hint: id can be implemented as a class variable.

# OrderBook
# Please write a class named OrderBook which collects all the tasks ordered from the software company. The tasks should be modelled with the class Task you just wrote.

# The basic version of an OrderBook is used as follows:

# orders = OrderBook()
# orders.add_order("program webstore", "Adele", 10)
# orders.add_order("program mobile app for workload accounting", "Eric", 25)
# orders.add_order("program app for practising mathematics", "Adele", 100)

# for order in orders.all_orders():
#     print(order)

# print()

# for programmer in orders.programmers():
#     print(programmer)

# 1: program webstore (10 hours), programmer Adele NOT FINISHED
# 2: program mobile app for workload accounting (25 hours), programmer Eric NOT FINISHED
# 3: program app for practising mathematics (100 hours), programmer Adele NOT FINISHED

# Adele
# Eric

# At this stage your OrderBook should provide three methods:

# add_order(self, description, programmer, workload) which adds a new order to the OrderBook. An OrderBook stores the orders internally as Task objects. NB: the method should take exactly the arguments mentioned, or else the automated tests will not work correctly.
# all_orders(self) returns a list of all the tasks stored in the OrderBook
# programmers(self) returns a list of the names of all the programmers with tasks stored in the OrderBook. The list should contain each programmer only once
# Hint: an easy method for removing duplicates is handling the list initially as a set. A set is a collection of items where each unique item appears only once. A set can be then converted back into a list, and we can then be sure each item is now unique:
    
# my_list = [1,1,3,6,4,1,3]
# my_list2 = list(set(my_list))
# print(my_list)
# print(my_list2)

# [1, 1, 3, 6, 4, 1, 3]
# [1, 3, 4, 6]

# Some more features for OrderBook
# Please write three more methods in your OrderBook class.

# The method mark_finished(self, id: int) takes the id of the task as its argument and marks the relevant task as finished:

# orders = OrderBook()
# orders.add_order("program webstore", "Adele", 10)
# orders.add_order("program mobile app for workload accounting", "Eric", 25)
# orders.add_order("program app for practising mathematics", "Adele", 100)

# orders.mark_finished(1)
# orders.mark_finished(2)

# for order in orders.all_orders():
#     print(order)

# 1: program webstore (10 hours), programmer Adele FINISHED
# 2: program mobile app for workload accounting (25 hours), programmer Eric FINISHED
# 3: program app for practising mathematics (100 hours), programmer Adele NOT FINISHED
    
# If there is no task with the given id, the method should raise a ValueError exception. If you need a refresher on raising exceptions, please have a look at part 6.

# The methods finished_orders(self) and unfinished_orders(self) work as expected: both return a list containing the relevant tasks from the OrderBook.

# Finishing touches to OrderBook
# Please write one last method in your OrderBook class: status_of_programmer(self, programmer: str) which returns a tuple. The tuple should contain the number of finished and unfinished tasks the programmer has assigned to them, along with the estimated hours in both categories.
    
# orders = OrderBook()
# orders.add_order("program webstore", "Adele", 10)
# orders.add_order("program mobile app for workload accounting", "Adele", 25)
# orders.add_order("program app for practising mathematics", "Adele", 100)
# orders.add_order("program the next facebook", "Eric", 1000)

# orders.mark_finished(1)
# orders.mark_finished(2)

# status = orders.status_of_programmer("Adele")
# print(status)

# (2, 1, 35, 100)

# The first item in the tuple is the number of finished tasks, while the second item is the number of unfinished tasks. The third and fourth items are the sums of workload estimates for the finished and unfinished tasks, respectively.

# If there is no programmer with the given name, the method should raise a ValueError exception.

class Task:
    next_id = 1
    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False
        self.id = Task.next_id
        Task.next_id += 1

    def is_finished(self):
        return self.finished
    
    def mark_finished(self):
        self.finished = True

    def __str__(self):
        status = "FINISHED" if self.finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"
    
class OrderBook:
    def __init__(self):
        self.task_list = []

    def add_order(self, description, programmer, workload):
        order = Task(description, programmer, workload)
        self.task_list.append(order)

    def all_orders(self):
        return self.task_list
    
    def programmers(self):
        return list(set([task.programmer for task in self.task_list]))
    
    def mark_finished(self, id: int):
        # handle error
        task_found = False
        for task in self.task_list:
            if task.id == id:
                task.mark_finished()
                task_found = True
                break
        if not task_found:
            raise ValueError()

    def finished_orders(self):
        return [order for order in self.task_list if order.finished]
    
    def unfinished_orders(self):
        return [order for order in self.task_list if order.finished == False]
    
    def status_of_programmer(self, programmer: str):
        finished_tasks = []
        unfinished_tasks = []
        fin_wrk = 0
        unfin_wrk = 0
        programmer_found = False

        for task in self.task_list:
            if task.programmer == programmer:
                programmer_found = True
                if task.finished:
                    finished_tasks.append(task)
                    fin_wrk += task.workload
                elif not task.finished:
                    unfinished_tasks.append(task)
                    unfin_wrk += task.workload

        if not programmer_found:
            raise ValueError()

        return len(finished_tasks), len(unfinished_tasks), fin_wrk, unfin_wrk

        # finished, unfinished, finishedworkload, unfinishedworkload



    