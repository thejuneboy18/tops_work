# Q.51 Write a Python function that checks whether a passed string is palindrome or not 

def is_palindrome(s):
    rev_string = s[::-1]  

inp = input("Enter a string: ")
def is_palindrome(s):
    rev_string = s[::-1] 
    if rev_string == s:
        return True
    else:
        return False

inp = input("Enter a string: ")
if is_palindrome(inp):
    print("Palindrome")
else:
    print("Not palindrome")