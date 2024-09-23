# Please write a program which asks for the name of the user and then creates an "inscription" in a file specified by the user. Please see the example below.

# Whom should I sign this to: Ada
# Where shall I save it: inscribed.txt

# The contents of the file inscribed.txt would be

# Hi Ada, we hope you enjoy learning Python with us! Best, Mooc.fi Team

# NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.

def inscription():
    recipient = input("Whom should I sign this to: ")
    address = input("Where shall I save it: ")
    with open(address, "w") as new_file:
        new_file.write(f"Hi {recipient}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")

inscription()