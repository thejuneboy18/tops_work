# Q14 - Write a Python program to find the second smallest number in a list.

def second_smallest(numbers):

    unique_numbers = list(set(numbers))


    if len(numbers) < 2:
        return None
    
    unique_numbers.sort()
    return unique_numbers[1]
    


numbers = [1,2,5,4,3,8,9,6]
result = second_smallest(numbers)

if result is not None:
    print(f"Here is second smallest digit from list: {result}")
else:
    print("List does not contain enough numbers")    