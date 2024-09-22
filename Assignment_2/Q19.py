# Q.19 - Write a Python program to find the first appearance of the substring
# 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
# whole 'not'...'poor' substring with 'good'. Return the resulting string

ent_string = str(input("Enter any string = "))

string1 = ent_string.find('not')
string2 = ent_string.find('poor')

if string1 != -1 or string2 != -1 and string1 < string2:
    result_str = ent_string[:string1] + 'good' + ent_string[string2 + 4:]
else:
    result_str = ent_string

print(result_str)        