# Please write a program which asks the user to type in a string and a 
# single character. The program then prints the first three character 
# slice which begins with the character specified by the user. You may 
# assume the input string is at least three 
# characters long. The program must print out three characters, or else nothing.

# Pay special attention to when there are less than two characters left
#  in the string after the first occurrence of the character looked for. 
# In that case nothing should be printed out, and there should not be any 
# indexing errors when executing the program.

# Please type in a word: mammoth
# Please type in a character: m
# mam

# Please type in a word: banana
# Please type in a character: n
# nan

# Please type in a word: tomato
# Please type in a character: x

# Please type in a word: python
# Please type in a character: n

ustr = input("Please type in a word: ")
uchar = input("Please type in a character: ")

# bool check if it is here
if uchar in ustr:
    found = ustr.find(uchar)
    if (len(ustr) - found >= 3):
        print(ustr[found:found+3])