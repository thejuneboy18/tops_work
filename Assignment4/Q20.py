# Write python program that user to enter only odd numbers, else will raise an exception.

# Ans 

try:
    number = int(input("Enter an odd number: "))
    if number % 2 == 0:
        # Raise an exception if the number is even
        raise ValueError("This is not an odd number!")
except ValueError as e:
    print(e)
else:
    print("Thank you for entering an odd number.")
