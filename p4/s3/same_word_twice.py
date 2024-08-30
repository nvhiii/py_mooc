# Please write a program which asks the user for words. If the user 
# types in a word for the second time, the program should print out 
# the number of different words typed in, and exit.

# Word: once
# Word: upon
# Word: a
# Word: time
# Word: upon
# You typed in 4 different words

words = []

while True:

    word = input("Word: ")

    if word in words:
        break

    words.append(word)

print(f"You typed in {len(words)} different words")