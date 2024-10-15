""" Write a Python program to find the maximum and minimum numbers
from the specified decimal numbers. """


try:
    numbers = input("Enter decimal numbers separated by spaces: ")
    
    
    decimal_numbers = [float(num) for num in numbers.split()]
    
    
    max_number = max(decimal_numbers)
    min_number = min(decimal_numbers)
    
    
    print(f"The maximum number is: {max_number}")
    print(f"The minimum number is: {min_number}")

except ValueError:
    print("Please enter valid decimal numbers.")
