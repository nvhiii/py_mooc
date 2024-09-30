# Please write a program which functions as a dictionary. The user can type in new entries or look for existing entries.

# The program should work as follows:

# 1 - Add word, 2 - Search, 3 - Quit
# Function: 1
# The word in Finnish: auto
# The word in English: car
# Dictionary entry added
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 1
# The word in Finnish: roska
# The word in English: garbage
# Dictionary entry added
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 1
# The word in Finnish: laukku
# The word in English: bag
# Dictionary entry added
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 2
# Search term: bag
# roska - garbage
# laukku - bag
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 2
# Search term: car
# auto - car
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 2
# Search term: laukku
# laukku - bag
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 3
# Bye!

# The dictionary entries should be written to a file called dictionary.txt. The program should first read the contents of the file. New entries are written to the end of the file whenever they are added to the dictionary.

# The format of the data stored in the dictionary is up to you.

# NB: the automatic tests for this exercise may change the contents of the file. If you want to keep its contents, first make a copy of the file under a different name.

# NB2: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.

def add_word(dictionary: dict, finnish: str, eng: str):
    dictionary[finnish] = eng  # add to dict
    with open("dictionary.txt", "a") as d:  # append to file
        d.write(f"{finnish} - {eng}\n")  # Add a newline after each entry


def search(dictionary: dict, term: str):
    found = False
    for k, v in dictionary.items():
        if term in k or term in v:
            print(f"{k} - {v}")
            found = True
    if not found:
        print(f"No entries found for: {term}")


def load_dictionary():
    dictionary = {}
    try:
        with open("dictionary.txt", "r") as d:
            for line in d:
                finnish, english = line.strip().split(" - ")
                dictionary[finnish] = english
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty dictionary
        pass
    return dictionary


def main():
    words = load_dictionary()
    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        fxn = int(input("Function: "))
        if fxn == 3:
            print("Bye!")
            break
        if fxn == 1:
            finnish_word = input("The word in Finnish: ")
            english_word = input("The word in English: ")
            add_word(words, finnish_word, english_word)
            print("Dictionary entry added")
        elif fxn == 2:
            search_term = input("Search term: ")
            search(words, search_term)


if __name__ == "__main__":
    main()
