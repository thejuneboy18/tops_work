# Write a Python program to read a file line by line and store it into a list

file = open("sample.txt","r")
read_lines = file.readlines()
print(read_lines)
result=[x.strip() for x in read_lines]
print(result)