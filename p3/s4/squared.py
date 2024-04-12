def squared(str_input, num):
    # create num x num square first
    # rows loop
    i = 0 # start @ 0 bc of string indexing, same w/ j var
    while i < num:
        # col loop
        j = 0
        while j < num: # iterate loop while j less than num
            carry_index = (i * num + j) % len(str_input) # very cool logic, find specific location of each chara given vars
            print(f"{str_input[carry_index]}", end="")
            carry_index += 1
            j += 1

        print() # "iterate" to next line
        i += 1

if __name__ == "__main__":
    squared("python", 15) # test case