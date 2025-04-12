class Animal:
    def __init__(self):
        self.age = 1
        
    def eat(self):
        print("Eating...")
class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 2
        
    def walk(self):
        print("Walking...")
             
class Fish(Animal):
    def swim(self):
        print("Swimming...")
        
class Bird(Animal):
    def fly(self):
        print("Flying...")
        
        
# Animal : Parent Class
# Mammal : Child Class of Animal
# Fish : Child Class of Animal
        
        
        
m = Mammal()
m.eat()  # Inherited from Animal class
m.walk()  # Defined in Mammal class
print(m.age)  # Inherited from Animal class


print(isinstance(m, Mammal))  # True
print(isinstance(m, Animal))  # True
print(isinstance(Animal, object))
print(isinstance(Mammal, object))  # True
print(issubclass(Mammal, Animal))  # True


print(m.weight)