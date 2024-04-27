# Write your solution here
# Please write a function named anagrams, which takes 
# two strings as arguments. The function returns True 
# if the strings are anagrams of each other. Two words 
# are anagrams if they contain exactly the same characters.

def anagrams(str1, str2):

    if sorted(str1) == sorted(str2):
        return True
    else:
        return False