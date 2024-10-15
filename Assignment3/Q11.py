# Q-11 - Write a Python function that takes a list and returns a new list with unique
# elements of the first list.

def unique_list(list1):
    return list(set(list1))

list1 = [1,1,2,2,3,4,5,5,6]
new_list = unique_list(list1)
print(new_list)
        