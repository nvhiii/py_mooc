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

from datetime import datetime, timedelta
def is_it_valid(pic: str):
    # split data
    dob = pic[0:6] # ddmmyy format
    century = pic[6] # X
    identifier = pic[7:10] # yyy
    control = pic[-1] # z

    # now since thats all strings, convert to int

    # then century market check

    # try except block

    # calc control using string ascii uppercase + digits or hardcode string from exercise