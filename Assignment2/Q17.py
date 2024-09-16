# Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string

string_1 = input("Enter the first string: ")
string_2 = input("Enter the second string: ")


if len(string_1) < 2 or len(string_2) < 2 :
    print("String length is too short enter atleast 2 characters.")

str1 = string_2[:2] + string_1[2:]
str2 = string_1[:2] + string_2[2:]

new_string = str1 + " " + str2
print(new_string)