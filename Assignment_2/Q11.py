#  Write a python program to sum of the first n positive integers.

inp = int(input("Enter any number="))
sum = 0
if inp >= 1:
     for num in range(1, inp + 1):
          sum += num
     print(f"Sum of the {inp} is {sum}")
else:
    print("Please enter positive number.")
