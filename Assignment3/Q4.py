# Q4 - Write a Python function to get the largest number, smallest num and sum
# of all from a list.


def number_function(numbers):
    largest = max(numbers)
    smallest = min(numbers)
    total_sum = sum(numbers)

    return largest, smallest, total_sum

numbers_list = [1,5,4,2,3,8,9] 
largest, smallest, total_sum = number_function(numbers_list)
print(f"largest number: {largest} ")
print(f"smallest number: {smallest} ")
print(f"Total sum: {total_sum} ")
