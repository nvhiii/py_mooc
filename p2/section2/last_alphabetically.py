# Write your solution here
word1 = input("Please type in the 1st word: ")
word2 = input("Please type in the 2nd word: ")

# greater means index of chara comes later, hence last alphabetically
if word1 > word2:
    print(f"{word1} comes alphabetically last")
elif word2 > word1:
    print(f"{word2} comes alphabetically last")
else:
    print(f"You gave the same word twice.")