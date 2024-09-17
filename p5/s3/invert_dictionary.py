# Please write a function named invert(dictionary: dict), which takes a dictionary as its argument. The dictionary should be inverted in place so that values become keys and keys become values.

# An example of its use:

# s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
# invert(s)
# print(s)

# {"first": 1, "second": 2, "third": 3, "fourth": 4}

def invert(dictionary: dict):
    copy = {}
    for k, v in dictionary.items():
        copy[v] = k
    dictionary.clear()
    dictionary.update(copy)