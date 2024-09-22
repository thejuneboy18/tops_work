# Write a Python function to reverses a string if its length is a multiple of 4

inp = str(input("Enter your string ="))

if len(inp) % 4 == 0:
    result = inp[::-1]
else:
    result = inp

print(result)
        