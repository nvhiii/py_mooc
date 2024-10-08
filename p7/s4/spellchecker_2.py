# In this exercise you will write an improved version of the Spell checker from the previous part.

# Just like in the previous version, the program should ask the user to type in a line of text. Your program should then perform a spell check, and print out feedback to the user, so that all misspelled words have stars around them. Additionally, the program should print out a list of suggestions for the misspelled words.

# Please have a look at the following two examples.

# write text: We use ptython to make a spell checker

# We use *ptython* to make a spell checker
# suggestions:
# ptython: python, pythons, typhon

# write text: this is acually a good and usefull program

# this is *acually* a good and *usefull* program
# suggestions:
# acually: actually, tactually, factually
# usefull: usefully, useful, museful

from difflib import get_close_matches
def spell_checker():

    # first load + store data from the text file
    dictionary = []
    with open("wordlist.txt") as word_bank:
        for line in word_bank:
            line = line.strip()
            word = line.lower()
            dictionary.append(word)

    # first line input
    text = input("write text: ")
    # now turn into list
    words = text.strip()
    words = words.split(" ")

    wrong_words = []
    for i, word in enumerate(words):
        if word.lower() not in dictionary:
            wrong_words.append(word)
            words[i] = f"*{word}*"
            

    # highlight wrong words
    wrong_sentence = " ".join(words)
    print(wrong_sentence)

    # suggestions
    print("suggestions:")
    for w in wrong_words:
        print(f"{w}: {', '.join(get_close_matches(w, dictionary, 3))}")

spell_checker()