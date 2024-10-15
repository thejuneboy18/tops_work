# Q-29 Write a Python program to unzip a list of tuples into individual lists.

tuple_list = [(1, 2), (3, 4), (5, 6), (7, 8)]

list1, list2 = zip(*tuple_list)

list1 = list(list1)
list2 = list(list2)

print("List 1:", list1)
print("List 2:", list2)
