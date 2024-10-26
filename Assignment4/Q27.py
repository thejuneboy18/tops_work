# What is used to check whether an object o is an instance of class A?

"""
Ans -> To check whether an object o is an instance of class A in Python, you use the isinstance() function.

"""

class Animal:
    pass

class Dog(Animal):
    pass

my_dog = Dog()

print(isinstance(my_dog, Dog))       
print(isinstance(my_dog, Animal))    
print(isinstance(my_dog, str))        
