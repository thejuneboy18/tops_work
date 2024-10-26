# What is Instantiation in terms of OOP terminology?

"""
Instantiation in Object-Oriented Programming (OOP) refers to the process of creating a specific 
instance (object) of a class. When a class is defined, it serves as a blueprint for objects, but it 
does not occupy memory or represent any specific data until it is instantiated.

"""

class Dog:
    def __init__(self, name):
        self.name = name 

    def bark(self):
        return f"{self.name} says Woof!"


my_dog = Dog("Buddy")  
print(my_dog.bark())   
