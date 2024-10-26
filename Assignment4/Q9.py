# Write a Python program to count the number of lines in a text file.

file = open("sample.txt","r")
count = 0
read = file.read()
data_list = read.split()
print(data_list)

for word in data_list:
    if word:
        count+=1

print(f"The number of line in text file is: {count}")