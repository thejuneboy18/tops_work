# Write a Python program to get a string made of the first 2 and the last
# 2 chars from a given a string. If the string length is less than 2, return
# instead of the empty string.

inp = str(input("Enter your string ="))

if len(inp) < 2:
    result = "String length should be more then 2 words."
else:
    result = inp[:2] + inp[-2:]    

print(result)