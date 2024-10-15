# Q-28 .Write a Python program to remove an empty tuple(s) from a list of tuples. 

tuple_list = [(1, 2), (), (3, 4, 5), (), (6,), ()]

new_list=[]
for n in tuple_list:
    if n:
        new_list.append(n)
print(f"New List after removing empty tuples:{new_list}")