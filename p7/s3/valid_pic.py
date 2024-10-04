# In this exercise you will validate Finnish Personal Identity Codes (PIC).

# Please write a function named is_it_valid(pic: str), which returns True or False based on whether the PIC given as an argument is valid or not. Finnish PICs follow the format ddmmyyXyyyz, where ddmmyy contains the date of birth, X is the marker for century, yyy is the personal identifier and z is a control character.

# The program should check the validity by these three criteria:

# The first half of the code is a valid, existing date in the format ddmmyy.
# The century marker is either + (1800s), - (1900s) or A (2000s).
# The control character is valid.
# The control character is calculated by taking the nine-digit number created by the date of birth and the personal identifier, dividing this by 31, and selecting the character at the index specified by the remainder from the string 0123456789ABCDEFHJKLMNPRSTUVWXY. For example, if the remainder was 12, the control character would be C.

# More examples and explanations of the uses of the PIC are available at the Digital and Population Data Services Agency.

# NB! Please make sure you do not share your own PIC, for example in the code you use for testing or through the course support channels.

# Here are some valid PICs you can use for testing:

# 230827-906F
# 120488+246L
# 310823A9877

from datetime import datetime
def is_it_valid(pic: str):
    # first split string given
    # ddmmyyXyyyz is expected
    day = pic[:2]
    month = pic[2:4]
    year = pic[4:6]

    if len(pic) != 11:
        return False

    # since need 4 digit century in order to use datetime constructor, need to do century logic first
     # fetch X from string
    century = pic[6]
    if century == "+":
        my_year = "18" + year
    elif century == "-":
        my_year = "19" + year
    elif century == "A":
        my_year = "20" + year
    else:
        return False

    # convert to int
    i_day = int(day)
    i_month = int(month)
    i_year = int(my_year)

    try:
        date = datetime(i_year, i_month, i_day)
    except ValueError:
        return False
    
    # fetch yyy from string
    identifier = pic[7:10]
    # Should i use a error here?

    # calc control
    dob_identifier = day + month + year + identifier # gives 9 digit string
    tester_string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    try:
        i_dob_identifier = int(dob_identifier)
    except ValueError:
        return False

    control = tester_string[i_dob_identifier%31] # calculate index then pick from string
    if control != pic[-1]:
        return False
    
    return True

    # keep in mind htis is a bool fxn, need to return false for the diff parts if fail
    # otherwise return true, THats what i need to fix