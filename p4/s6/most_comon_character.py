def most_common_character(s: str) -> str:
    # Step 1: Initialize a dictionary to count character frequencies
    frequency = {}
    
    # Step 2: Count the frequency of each character in the string
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    # Step 3: Find the most common character
    max_count = 0
    most_common_char = ''
    
    for char in s:
        if frequency[char] > max_count:
            max_count = frequency[char]
            most_common_char = char
    
    # Step 4: Return the most common character
    return most_common_char