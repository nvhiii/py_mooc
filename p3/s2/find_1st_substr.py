# Write your solution here
word = input("Please type in a word: ")
chara = input("Pease type in a character: ")

index_found = word.find(chara)
# need to create new var to hold index, since we
# cannot increment on var getting value from method
temp = index_found
num = 0

# first check if chara is in word
if chara in word:

    if len(word) - temp >= 3:
        print(f"{word[temp]}{word[temp+1]}{word[temp+2]}")
    else:
        print(f"")