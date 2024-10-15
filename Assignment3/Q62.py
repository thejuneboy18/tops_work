""" Write a Python program to calculate the area of a parallelogram """


try:
    base = float(input("Enter the base of the parallelogram: "))
    height = float(input("Enter the height of the parallelogram: "))
    
    
    area = base * height
    
    print(f"The area of the parallelogram is: {area}")

except ValueError:
    print("Please enter valid numerical values for base and height.")
