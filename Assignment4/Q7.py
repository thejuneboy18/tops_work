# Write a Python program to read a file line by line store it into a variable.

line=[]

with open("sample.txt", 'r')  as file:
    line= [x.strip() for x in file]

print("line stored in variables")
for x in line:
    print(x)
