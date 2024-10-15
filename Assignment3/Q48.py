# Q-48 Write a Python function to calculate the factorial of a number

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = 9
print(f"The factorial of {num} is: {factorial(num)}")
