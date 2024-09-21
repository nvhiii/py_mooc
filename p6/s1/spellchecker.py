# Please write a program which asks the user to type in some text. Your program should then perform a spell check, and print out feedback to the user, so that all misspelled words have stars around them. Please see the two examples below:

# Write text: We use ptython to make a spell checker

# We use *ptython* to make a spell checker

# Write text: This is acually a good and usefull program

# This is *acually* good and *usefull* program

# The case of the letters should be irrelevant to the functioning of your program.

# The exercise template includes the file wordlist.txt, which contains all the words the spell checker should accept as correct.

# NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.

# NB2 If Visual Studio can't find the file and you have checked that there are no spelling errors, take a look at these instructions.

def spell_check():
    # Store values from file as list of valid words
    dictionary = []
    with open("wordlist.txt") as new_file:
        for line in new_file:
            line = line.strip().lower()  # Make dictionary words lowercase
            dictionary.append(line)

    user = input("Write text: ")
    user = user.strip()
    words = user.split(" ")

    for i in range(len(words)):
        if words[i].lower() not in dictionary:
            words[i] = f"*{words[i]}*"

    result = " ".join(words)
    print(result)

# Example usage
spell_check()
