# Q.26 - Write a Python program to replace last value of tuples in a list. 

list_of_tuples = [(2,4,6),(3,6,9),(4,8,13)]

new_value = 12

updated_list_of_tuple = []

for tup in list_of_tuples:
    temp_list = list(tup)

    temp_list[-1] = new_value
    
    updated_list_of_tuple.append(tuple(temp_list))

print("Original list of tuples:", list_of_tuples)
print("Updated list of tuples:", updated_list_of_tuple)