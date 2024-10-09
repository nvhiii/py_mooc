# Please write a function named smallest_average(person1: dict, person2: dict, person3: dict), which takes three dictionary objects as its arguments.

# Each dictionary object contains values mapped to the following keys:

# "name": The name of the contestant
# "result1": the first result of the contestant (an integer between 1 and 10)
# "result2": the second result of the contestant (as above)
# "result3": the third result of the contestant (as above)

# The function should calculate the average of the three results for each contestant, and then return the contestant whose average result was the smallest. The return value should be the entire dictionary object containing the contestant's information.

# You may assume there will be no ties, i.e. a single contestant will have the smallest average result.

# An example of the function in action:

# person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
# person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
# person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

# print(smallest_average(person1, person2, person3))

# {'name': 'Larry', 'result1': 3, 'result2': 1, 'result3': 1}

def smallest_average(person1: dict, person2: dict, person3: dict):
    avg_p1 = (person1["result1"] + person1["result2"] + person1["result3"]) / 3
    avg_p2 = (person2["result1"] + person2["result2"] + person2["result3"]) / 3
    avg_p3 = (person3["result1"] + person3["result2"] + person3["result3"]) / 3
    persons = [(person1, avg_p1), (person2, avg_p2), (person3, avg_p3)]
    
    min_avg = min(persons, key=lambda x: x[1])
    return min_avg[0]

