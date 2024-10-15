# Q-32 Write a Python script to sort (ascending and descending) a dictionary by value. 

my_dict = {'apple': 10, 'banana': 5, 'cherry': 20, 'date': 15}

ascending_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))

descending_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Dictionary sorted by value (ascending):", ascending_sorted)
print("Dictionary sorted by value (descending):", descending_sorted)
