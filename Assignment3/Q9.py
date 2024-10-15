# Q9 - Write a Python function that takes two lists and returns true if they have
# at least one common member

def compare_list(list_a, list_b):
    for n in list_a:
        if n in list_b:
            print("list_a is present in list_b")
            return True
        
    print("list_a is not present in list_b.")
    return False
list_a = [1,2,3,4,5,6]
list_b = [9,7,6]
res = compare_list(list_a,list_b)
print(res)