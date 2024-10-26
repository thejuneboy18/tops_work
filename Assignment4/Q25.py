# Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  
print(cat.speak())  
