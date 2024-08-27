# Please modify the previous program so that it also asks for 
# the height, and prints out a rectangle of hash characters accordingly.

width = int(input("Width: "))
height = int(input("Height: "))
row = width * "#"
iterator = 0

while iterator < height:
    print(row)
    iterator += 1