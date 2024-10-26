#Can one block of except statements handle multiple exception?
"""
Ans - Yes, a single except block can handle multiple exceptions by specifying them as a tuple. 
This allows you to catch and handle different exceptions in the same block.

"""

try:
    num = int(input("Enter a number: "))
    result = 100 / num
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero!")
