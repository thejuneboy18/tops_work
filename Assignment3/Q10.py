# Q10 - Write a Python program to generate and print a list of first and last 5
# elements where the values are square of numbers between 1 and 30. 
 

list1 = []
for n in range(1,30 +1):
    sqaure = n**2
    list1.append(sqaure)    
first_five = list1[:5]
last_five = list1[-5:]

print(f"First five elements:{first_five}, Last five elements:{last_five}")