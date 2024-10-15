# Q-56 How will you set the starting value in generating random numbers?

import random


random.seed(42)

print(random.random()) 
print(random.randint(1, 10)) 
print(random.choice([100, 200, 300]))  