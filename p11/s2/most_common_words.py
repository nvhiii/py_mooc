# Please write a function named most_common_words(filename: str, lower_limit: int) which takes a filename and an integer value for a lower limit as its arguments. The function should return a dictionary containing the occurrences of the words which appear at least the number of times specified in the lower_limit parameter.

# For example, say the function was used to process a file named comprehensions.txt with the following contents:

# List comprehension is an elegant way to define and create lists based on existing lists.
# List comprehension is generally more compact and faster than normal functions and loops for creating list.
# However, we should avoid writing very long list comprehensions in one line to ensure that code is user-friendly.
# Remember, every list comprehension can be rewritten in for loop, but every for loop can’t be rewritten in the form of list comprehension.

# When the function is called with the arguments most_common_words("comprehensions.txt", 3) it should return

# {'comprehension': 4, 'is': 3, 'and': 3, 'for': 3, 'list': 4, 'in': 3}

# NB: the case of letters affects the results, and all inflected forms are unique words in this exercise. That is, the words List, lists and list are each separate words here, and only list has enough occurrences to make it to the returned list. All punctutation should be removed before counting up the occurrences.

# It is up to you to decide how to implement this. The easiest way would likely be to make use of list and dictionary comprehensions.

def most_common_words(filename: str, lower_limit: int):
    punc = "!?:,."
    all_words = []
    with open(filename) as new_file:
        for line in new_file:
            line = line.strip() # get rid of newline
            listified_line = list(line) # splits everything including whitespacec into list
            no_punc = "".join([item for item in listified_line if item not in punc])
            [all_words.append(word) for word in no_punc.split()] # populates all words

    return {word : all_words.count(word) for word in all_words if all_words.count(word) >= lower_limit}
            
