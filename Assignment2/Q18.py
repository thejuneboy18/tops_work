# Q.18- Write a Python program to add 'ing' at the end of a given string (length
# should be at least 3). If the given string already ends with 'ing' then add
# 'ly' instead if the string length of the given string is less than 3, leave it
# unchanged.

string1 = input("Enter any name = ")

if len(string1) >= 3 :
    if string1.endswith("ing"):
        result = string1 + "ly"
    else :
        result = string1 + "ing"
else:
    result = "Character length should be atleast three characters." 
          
print(result)        