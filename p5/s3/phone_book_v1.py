# Please write a phone book application. It should work as follows:

# command (1 search, 2 add, 3 quit): 2
# name: peter
# number: 040-5466745
# ok!
# command (1 search, 2 add, 3 quit): 2
# name: emily
# number: 045-1212344
# ok!
# command (1 search, 2 add, 3 quit): 1
# name: peter
# 040-5466745
# command (1 search, 2 add, 3 quit): 1
# name: mary
# no number
# command (1 search, 2 add, 3 quit): 2
# name: peter
# number: 09-22223333
# ok!
# command (1 search, 2 add, 3 quit): 1
# name: peter
# 09-22223333
# command (1 search, 2 add, 3 quit): 3
# quitting...

# As you can see above, each name can be attached to a single number only. If a new entry with the same name is added, the number attached to the old entry is replaced with the new number.

# NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.

def add(pb: dict, name: str, num: str):  # 'num' should be a string, not an int
    pb[name] = num

def search(pb: dict, name: str):
    if name in pb:
        print(pb[name])
    else:
        print("no number")

def main():
    pb = {}  # Initialize an empty phonebook
    while True:
        val = int(input("command (1 search, 2 add, 3 quit): "))
        if val == 3:
            print("quitting...")
            break
        elif val == 2:
            name = input("name: ")
            number = input("number: ")
            add(pb, name, number)  # Call the 'add' function directly
            print("ok!")
        elif val == 1:
            name = input("name: ")
            search(pb, name)  # Call the 'search' function directly

if __name__ == "__main__":
    main()
