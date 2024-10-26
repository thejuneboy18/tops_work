# Write a python program to find the longest words

file = open("sample.txt","r")
read = file.read()
data = read.split()
longest_word =""
max_length = 0
for word in data:
    if len(word) > max_length:
        max_length=len(word)
        longest_word=word    

print(f"The longest word is: {longest_word}")
print(f"The max length of  word is: {max_length}")

file.close
    