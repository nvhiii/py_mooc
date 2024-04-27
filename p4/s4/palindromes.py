# Write your solution here
# Please write a function named palindromes, which 
# takes a string argument and returns True if the string 
# is a palindrome. Palindromes are words which are spelled 
# exactly the same backwards and forwards.

def palindromes(str):
    
    return str == str[::-1]

def main():
    
    while True:
        word = input("Please type in a palindrome: ")

        if palindromes(word):
            print(f"{word} is a palindrome!")
            break
        else:
            print("that wasn't a palindrome")

# dont forget to invoke the main method!
main()

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
