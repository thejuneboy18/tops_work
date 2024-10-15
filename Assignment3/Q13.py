# Q13. - Write a Python program to select an item randomly from a list.


import random

fruits = ['Banana','apple','kiwi','dragon fruit','pineaple']
random_fruit = random.choice(fruits)

print(f"Randomly selected item: {random_fruit}")