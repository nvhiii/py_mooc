# Write your solution here
letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

# assuming letters will all be the same case, whether it is upper or all lower

# 3 * 2 * 1 options
# the comparison operators can be used for strings

if letter1 > letter2 and letter2 > letter3:
    print(f"The letter in the middle is {letter2}")
elif letter3 > letter2 and letter2 > letter1:
    print(f"The letter in the middle is {letter2}")
elif letter1 > letter3 and letter3 > letter2:
    print(f"The letter in the middle is {letter3}")
elif letter2 > letter3 and letter3 > letter1:
    print(f"The letter in the middle is {letter3}")
else:
    print(f"The letter in the middle is {letter1}")
