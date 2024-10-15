# Q3 - Differentiate between append () and extend () methods?

# append()

# adds a single element to end of the list.
#Ex.

list1= [1,2,3]
list1.append(4)
print(list1)   # outupt = [1, 2, 3, 4]

# Extend()

# add each elemnt to the list indvidually.

list2 = [1,2,3]
list2.extend(['x','y','z'])
print(list2)     # output - [1, 2, 3, 'x', 'y', 'z']
