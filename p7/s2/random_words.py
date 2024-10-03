# The exercise template contains the file words.txt, which contains some English language words, one on each line.

# Please write a function named words(n: int, beginning: str), which returns a list containing n random words from the words.txt file. All words should begin with the string specified by the second argument.

# The same word should not appear twice in the list. If there are not enough words beginning with the specified string, the function should raise a ValueError exception.

# An example of the function in action:

# word_list = words(3, "ca")
# for word in word_list:
#     print(word)

# cat
# car
# carbon

from random import sample
def words(n: int, beginning: str):
    try:
        valid_words = []
        with open("words.txt") as new_file:
            for line in new_file:
                try:
                    line = line.strip()
                    if line.startswith(beginning):
                        valid_words.append(line)
                except ValueError as e:
                    print(f"Value error raised: {e}")

    except FileNotFoundError:
        pass

    if len(valid_words) < n:
        raise ValueError("Not enough words beginning with the specified string")
    
    return sample(valid_words, n)