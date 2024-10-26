# How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.

# Ans -

try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution of the try-except-finally block is complete.")
