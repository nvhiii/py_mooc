# Please write a function named new_person(name: str, age: int), which creates and returns a tuple containing the data in the arguments. The first element should be the name and the second the age.

# If the values stored in the parameter variables are not valid, the function should throw a ValueError exception.

# Invalid parameters in this case include:

# name is an empty string
# name contains less than two words
# name is longer than 40 characters
# age is a negative number
# age is greater than 150

def new_person(name: str, age: int):
    
    if not name:
        raise ValueError("Name cannot be empty")
    
    if len(name.strip().split(" ")) < 2:
        raise ValueError("Name cannot be less than 2 words")

    if len(name) > 40:
        raise ValueError("Name cannot be greater than 40 characters")
    
    if age < 0:
        raise ValueError("Age cannot be negative")
    
    if age > 150:
        raise ValueError("Age cannot be greater than 150")
    
    return name, age