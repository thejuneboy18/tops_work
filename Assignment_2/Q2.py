# Write a Python program to get the Factorial number of given number.

num = int(input("Enter your input ="))
factorial = 1

if num >= 1:
    for num in range (1,num + 1):
        factorial = factorial * num
    print("Your factorial number is", factorial)    