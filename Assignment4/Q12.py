# Write a Python program to copy the contents of a file to another file.

file1 = 'sample1.txt'
file2 = 'sample2.txt'
file = open("sample.txt",'r')
data = file.read()
file.close()
with open("sample2.txt",'a')as file:
    file.write(data)