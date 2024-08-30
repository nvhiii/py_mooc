# Please write a function named palindromes, which takes a string argument 
# and returns True if the string is a palindrome. Palindromes are words 
# which are spelled exactly the same backwards and forwards.

# Please also write a main program which asks the user to type in words 
# until they type in a palindrome:

# Please type in a palindrome: python
# that wasn't a palindrome
# Please type in a palindrome: java
# that wasn't a palindrome
# Please type in a palindrome: oddoreven
# that wasn't a palindrome
# Please type in a palindrome: neveroddoreven
# neveroddoreven is a palindrome!

# logic to check if palindrome
def palindromes(val: str) -> bool:
    return val == val[::-1]

def main():

    while True:

        ustr = input("Please type in a palindrome: ")

        if palindromes(ustr):
            break

        print("that wasn't a palindrome")

    print(f"{ustr} is a palindrome!")

main()