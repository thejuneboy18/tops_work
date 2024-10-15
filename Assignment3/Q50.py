# Q-50  Write a Python function to check whether a number is perfect or not. 

def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum
        

n=int(input("Enter number:"))
s=perfect(n)
if n == s:
    print("Entered number is perfect number.")
else:
    print("Entered number is not perfect number.")