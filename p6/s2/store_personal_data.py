# Please write a function named store_personal_data(person: tuple), which takes a tuple containing some identifying information as its argument.

# The tuple contains the following elements:

# Name (string)
# Age (integer)
# Height (float)
# This should be processed and written into the file people.csv. The file may already contain some data; the new entry goes to the end of the file. The data should be written in the format

# name;age;height

# Each entry should be on a separate line. If we call the function with the argument ("Paul Paulson", 37, 175.5), the function should write this line to the end of the file:

# Paul Paulson;37;175.5

def store_personal_data(person: tuple):
    
    person_line = f"{person[0]};{int(person[1])};{float(person[2])}"

    with open("people.csv", "a") as working_file:
        working_file.write(f"{person_line}\n")