# Q-38 Write a Python program to check multiple keys exists in a dictionary

dict = {'bananna':10,'apple':20,'kiwi':30,'dates':40}

def is_key_present(x):
    if x in dict:
        print(f"key {x} exist")
    else:
        print(f"key {x} dosen't exist")

is_key_present('bananna')
is_key_present('apple')
is_key_present('kiwi')
is_key_present('dates')