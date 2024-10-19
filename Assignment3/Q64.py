# Write a Python program to returns sum of all divisors of a number 

num = int(input("Enter a number: "))
sum_of_divisors = 0

for n in range(1, num + 1):
    if num % n == 0:  
        sum_of_divisors += n

print(f"The sum of all divisors of {num} is: {sum_of_divisors}")