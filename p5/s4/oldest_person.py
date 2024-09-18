# Please write a function named oldest_person(people: list), which takes a list of tuples as its argument. In each tuple, the first element is the name of a person, and the second element is their year of birth. The function should find the oldest person on the list and return their name.

# An example of the function in action:

# p1 = ("Adam", 1977)
# p2 = ("Ellen", 1985)
# p3 = ("Mary", 1953)
# p4 = ("Ernest", 1997)
# people = [p1, p2, p3, p4]

# print(oldest_person(people))

# Mary

def oldest_person(people: list):
    for idx, person in enumerate(people):
        if idx == 0:
            oldest_year = person[1]
            oldest = person[0]
        else:
            oldest_year = min(oldest_year, person[1])
            if oldest_year == person[1]:
                oldest = person[0]
            
    oldest_year = min(oldest_year, person[1])
    if oldest_year == person[1]:
         oldest = person[0]

    return oldest