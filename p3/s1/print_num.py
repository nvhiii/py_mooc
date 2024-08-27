# Please write a program which prints out all the even numbers between 
# two and thirty, using a loop. Print each number on a separate line.

# The beginning of your output should look like this:

# 2
# 4
# 6
# 8
# etc...

num = 2

# includes 30 in the set
while num <= 30:

    if num % 2==0:
        print(num)
    
    num += 1