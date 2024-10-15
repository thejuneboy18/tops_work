# Q-34 Write a Python script to check if a given key already exists in a dictionary. 


my_dict = {'cars': 10, 'bikes': 5, 'trucks': 20}

key_to_check = 'bikes'


if key_to_check in my_dict:
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")
