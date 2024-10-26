#When is the finally block executed?

"""
Ans - The finally block is always executed, regardless of whether an exception occurs or not in the try block. 
It’s typically used for cleanup actions, like closing files or releasing resources.

"""

try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always execute.")
