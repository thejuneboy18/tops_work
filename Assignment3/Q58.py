# Q-58 Write a Python program to read a random line from a file.


import random

def read_random_line(file_path):
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    
    random_line = random.choice(lines).strip()  
    return random_line


file_path = 'example.txt' 
print(f"Random line from file: {read_random_line(file_path)}")
