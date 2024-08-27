# Please write a program which keeps asking the user for a PIN code 
# until they type in the correct one, which is 4321. The program should 
# then print out the number of times the user tried different codes.

# PIN: 3245
# Wrong
# PIN: 1234
# Wrong
# PIN: 0000
# Wrong
# PIN: 4321
# Correct! It took you 4 attempts

attempts = 0

while True:

    pin = int(input("PIN: "))
    attempts += 1 # increment here bc each time input, that is an attempt

    # break stmnt
    if pin == 4321:
        break
    else:
        print("Wrong")

print("Correct! It only took you one single attempt!") if attempts == 1 else print(f"Correct! It took you {attempts} attempts")
