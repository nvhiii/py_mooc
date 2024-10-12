# Please create a class named ListHelper which contains the following two class methods.

# greatest_frequency(my_list: list) returns the most common item on the list
# doubles(my_list: list) returns the number of unique items which appear at least twice on the list
# It should be possible to use these methods without creating an instance of the class. An example of how the methods could be used:

# numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
# print(ListHelper.greatest_frequency(numbers))
# print(ListHelper.doubles(numbers))

# 5
# 3

class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list: list):
        counts = {}

        for item in my_list:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1

        highest_freq = 0
        common = 0
        for item, count in counts.items():
            if count > highest_freq:
                highest_freq = count
                common = item
        
        return common

    @classmethod
    def doubles(cls, my_list: list):
        counts = {}
        dupes = []

        for item in my_list:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1

        for k, count in counts.items():
            if count > 1:
                dupes.append(k)

        num_d = len(dupes)
        return num_d