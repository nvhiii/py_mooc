# Write your solution here
ustring = input("Please type in a string: ")
upper_lim = -1

# will have substrings as much as length always
while upper_lim >= -len(ustring):
    print(ustring[upper_lim:]) # from -1 index to end of string
    upper_lim -= 1