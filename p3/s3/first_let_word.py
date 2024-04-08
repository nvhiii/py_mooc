# Write your solution here
sentence = input("Please type in a sentence: ")
word_index = 0
words = sentence.split()

while word_index < len(words):

    # using index, retrieve word then find first chara
    word = words[word_index]
    print(f"{word[0]}")

    # iterate to next word
    word_index += 1