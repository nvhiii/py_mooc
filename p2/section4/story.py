# Write your solution here
# empty story string to concat strings
story = ""
temp = ""

# part 1
while True:
    word = input("Please type in a word: ")
    # always remember that order of stmnts matter
    if word == "end" or word == temp:
        break
    story += word + " "
    temp = word

print(story)