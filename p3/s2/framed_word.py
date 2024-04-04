# Write your solution here
word = input("Word: ")
ast = "*"
blank = " "
height = 0
btwn_ast = 28
space_diff = btwn_ast - len(word)
w2a = space_diff // 2 # w2a = word-to-asterik

while height < 3:
    if height == 0 or height == 2:
        print(f"{ast * 30}")
    else:
        # check if dividing by 2 leaves float or int
        if space_diff % 2 == 0:
            print(f"{ast}{w2a * blank}{word}{w2a * blank}{ast}")
        else:
            print(f"{ast}{(w2a + 1) * blank}{word}{(w2a) * blank}{ast}")

    height += 1