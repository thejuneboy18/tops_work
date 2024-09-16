# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

n1 = int(input("Emter number="))
n2 = int(input("Enter number="))
sum = n1 + n2 
sub = n1 - n2

if n1 == n2 or sum == 5 or sub == 5:
    print("True")
else:
    print("False")

