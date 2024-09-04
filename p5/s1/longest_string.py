# Please write a function named longest(strings: list), which takes a list of strings 
# as its argument. The function finds and returns the longest string in the list. You 
# may assume there is always a single longest string in the list.

# An example of expected behaviour:

# if __name__ == "__main__":
#     strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
#     print(longest(strings))

#     Sample output
# howdydoody

def longest(strings: list) -> str:
    current_longest = strings[0]
    for string in strings:
        if len(string) > len(current_longest):
            current_longest = string
    return current_longest