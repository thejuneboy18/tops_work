"""
Q-46 Write a Python program to combine values in python list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
300}, o {'item': 'item1', 'amount': 750}]
Expected Output:
Counter ({'item1': 1150, 'item2': 300}) """ 

data=[{'item': 'item1', 'amount': 400},
      {'item': 'item2', 'amount':300}, 
      {'item': 'item1', 'amount': 750}]
result={}
for r in data:
    item=r['item']
    amount=r['amount']
    if item in result:
        result[item]+=amount
    else:
        result[item]=amount
print("Result:",result)