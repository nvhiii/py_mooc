# Please write a function named dict_of_numbers(), which returns a new dictionary. The dictionary should have the numbers from 0 to 99 as its keys. The value attached to each key should be the number spelled out in words. Please have a look at the example below:

# numbers = dict_of_numbers()
# print(numbers[2])
# print(numbers[11])
# print(numbers[45])
# print(numbers[99])
# print(numbers[0])

# two
# eleven
# forty-five
# ninety-nine
# zero

def dict_of_numbers():
    num_to_words = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
        20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
    }
    
    result = {}
    
    for num in range(100):
        if num < 20:
            result[num] = num_to_words[num]
        else:
            tens, ones = divmod(num, 10)
            if ones == 0:
                result[num] = num_to_words[tens * 10]
            else:
                result[num] = num_to_words[tens * 10] + "-" + num_to_words[ones]
    
    return result
