#  Write a Python function to insert a string in the middle of a string.

og_string = str(input("Enter your string ="))
inp_string = str(input("Enter your string ="))

middle_index = len(og_string) // 2
result = og_string[:middle_index] + inp_string + og_string[middle_index:]

print(result)