# Please write a program which asks the user for words.
#  If the user types in a word for the second time, 
# the program should print out the number of different 
# words typed in, and exit.

words = []
iterator = 1

while True:

    word = input("Word:")
    if word in words:
        break
    words.append(word)
    iterator += 1

print(f"You typed in {iterator} different words")