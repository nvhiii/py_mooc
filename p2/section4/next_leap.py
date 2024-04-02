# for some reason, only this format of submission worked on mooc. Used sources found readily available
# on reddit, disclaimer that this code is based on someone elses code to address
# bug in mooc

year = int(input("Year:"))
nextYear = year + 1

while True:
    if nextYear % 4 == 0 and nextYear % 100 != 0 or nextYear % 400 == 0:
        break
    nextYear += 1
print(f"The next leap year after {year} is {nextYear}")