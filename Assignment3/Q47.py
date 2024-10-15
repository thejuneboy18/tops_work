""" Q-47  Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string: 'w3resource' 
""""


sample_string = 'w3resource'

char_count = {}

for char in sample_string:
    if char in char_count:
        char_count[char] += 1  
    else:
        char_count[char] = 1  

print("Character count dictionary:", char_count)
