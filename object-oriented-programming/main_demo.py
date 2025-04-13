#!/usr/bin/env python3
from abc import ABC, abstractmethod
from collections import namedtuple
from dataclasses import dataclass

# ---------------------------------------
# Classes, Instances, and Constructors
# ---------------------------------------
class Human:
    species = "Homo sapiens"  # Class-level attribute

    def __init__(self, name, height, gender):
        self.name = name
        self.height = height
        self.gender = gender

    def talk(self):
        print(f"Hello, I'm {self.name}.")


john = Human("John", 180, "Male")
john.talk()
print(isinstance(john, Human), type(john))

# ---------------------------------------
# Private attributes (encapsulation)
# ---------------------------------------
class BankAccount:
    def __init__(self, balance):
        self.__set_balance(balance)

    def __set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            raise ValueError("Balance can't be negative.")

    def get_balance(self):
        return self.__balance

acc = BankAccount(100)
print(acc.get_balance())
# print(acc.__balance) # AttributeError
print(acc._BankAccount__balance)  # accessing private attribute (discouraged)

# ---------------------------------------
# Class and Static Methods
# ---------------------------------------
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    @classmethod
    def origin(cls):
        return cls(0, 0)

p = Point.origin()
print(p.x, p.y)

# ---------------------------------------
# Magic Methods (custom container)
# ---------------------------------------
class CustomList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

mylist = CustomList([1, 2, 3])
print(mylist[1], len(mylist))

# ---------------------------------------
# Inheritance and Method Overriding
# ---------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic animal sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Woof!"

dog = Dog("Rex", "Labrador")
print(dog.speak(), dog.name)

# ---------------------------------------
# Multiple Inheritance
# ---------------------------------------
class Flyer:
    def fly(self):
        return "I'm flying"

class Swimmer:
    def swim(self):
        return "I'm swimming"

class Duck(Animal, Flyer, Swimmer):
    pass

duck = Duck("Donald")
print(duck.fly(), duck.swim(), duck.speak())

# ---------------------------------------
# Abstract Base Classes (ABC) & Polymorphism
# ---------------------------------------
class Stream(ABC):
    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        return "File data read."

class NetworkStream(Stream):
    def read(self):
        return "Network data read."

def read_stream(stream):
    print(stream.read())

fs = FileStream()
ns = NetworkStream()
read_stream(fs)
read_stream(ns)

# ---------------------------------------
# Duck Typing
# ---------------------------------------
class Cat:
    def speak(self):
        return "Meow!"

def make_speak(animal):
    print(animal.speak())

make_speak(Dog("Buddy", "Beagle"))
make_speak(Cat())

# ---------------------------------------
# Extending Built-in Types
# ---------------------------------------
class TrackableList(list):
    def append(self, item):
        print(f"Appending {item}")
        super().append(item)

lst = TrackableList()
lst.append(5)
print(lst)

# ---------------------------------------
# Data Classes
# ---------------------------------------
@dataclass
class DataPoint:
    x: int
    y: int

dp1 = DataPoint(1, 2)
dp2 = DataPoint(1, 2)
print(dp1 == dp2)  # True, checks for equality by data

# namedtuple for immutable data bundles
PointTuple = namedtuple("PointTuple", ["x", "y"])
pt1 = PointTuple(10, 20)
print(pt1.x, pt1.y)