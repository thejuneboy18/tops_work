# Q - 45 Write a Python program to find the highest 3 values in a dictionary


my_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 150, 'e': 250}


highest_values = sorted(my_dict.values())[-3:]

print("The highest three values are:", highest_values)
