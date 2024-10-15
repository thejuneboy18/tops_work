# Q-53 How can you pick a random item from a list or tuple?
""""
In Python, you can pick a random item from a list or tuple using the random.choice() function from 
the random module. Here's how to do it:
"""

import random

my_list = [1, 2, 3, 4, 5]
random_item_list = random.choice(my_list)
print(f"Random item from list: {random_item_list}")


my_tuple = ('apple', 'banana', 'cherry')
random_item_tuple = random.choice(my_tuple)
print(f"Random item from tuple: {random_item_tuple}")
