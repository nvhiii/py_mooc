# Please write three functions: first_word, second_word and last_word. 
# Each function takes a string argument.

# As their names imply, the functions return either the first, the second 
# or the last word in the sentence they receive as their string argument.

# In each case you may assume the argument string contains at least two 
# separate words, and all words are separated by exactly one space 
# character. There will be no spaces in the beginning or at the end 
# of the argument strings.

# sentence = "it was a dark and stormy python"

# print(first_word(sentence)) # it
# print(second_word(sentence)) # was
# print(last_word(sentence)) # python

# it
# was
# python

# sentence = "it was"

# print(second_word(sentence)) # was
# print(last_word(sentence)) # was

def first_word(sentence: str) -> str:
    splitted = sentence.split(" ")
    return splitted[0] # return first word in string turned into list via split of spaces

def second_word(sentence: str) -> str:
    splitted = sentence.split(" ")
    return splitted[1]

def last_word(sentence: str) -> str:
    splitted = sentence.split(" ")
    return splitted[len(splitted)-1]

if __name__ == "__main__":
    ustr = input("Enter any string: ")
    print(first_word(ustr))
    print(second_word(ustr))
    print(last_word(ustr))