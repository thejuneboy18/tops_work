# Q-33 Write a Python script to concatenate following dictionaries to create a new one.

dict1 = {'apple': 10, 'banana': 5}
dict2 = {'cherry': 20, 'date': 15}
dict3 = {'fig': 25, 'grape': 30}

result={}
for n in (dict1,dict2,dict3):
    result.update(n)
    
print("Result:",result)