# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class
"""
In Python, a class is defined using the class keyword followed by the class name and a colon. 
Classes often contain an __init__ method (constructor) to initialize the class attributes.

"""


class Person:
    def __init__(self, name, age):
        self.name = name    
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


person1 = Person("Alice", 25)
person1.greet()  
