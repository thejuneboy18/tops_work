# Q16 - Write a Python program to check whether a list contains a sub list 

list1 = [1, 2, 3, 4, 5, 6, 7]
sub_list = [4, 5, 6]
sub_len = len(sub_list)
list_len = len(list1)

is_sublist = False

for i in range(list_len - sub_len + 1):
    if list1[i:i + sub_len] == sub_list:
        is_sublist = True
        break

print(is_sublist)