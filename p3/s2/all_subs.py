# Write your solution here
word = input("Please type in a word: ")
chara = input("Please type in a character: ")
index = 0

while index < len(word) - 2:
    if word[index] == chara:
        print(f"{word[index:index+3]}")
    index += 1
    
