# When will the else part of try-except-else be executed?
"""
Ans - The else part of a try-except-else block runs only if no exceptions are raised in the try block.
If an exception occurs, the else block is skipped, and the except block is executed instead.


"""

try:
    num = int(input("Enter a number: "))
    result = 100 / num
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero!")
else:
    print("Result is:", result) 