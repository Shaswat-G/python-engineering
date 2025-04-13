# Python OOP Essentials

## Classes and Objects

Programming models real-world scenarios by defining:
- **Classes**: Blueprints/templates for objects.
- **Objects**: Instances of classes, encapsulating attributes (data) and methods (behaviors).

**Example:**
```python
class Human:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def talk(self):
        print(f"{self.name} says hello!")

john = Human("John", 180, 75)
john.talk()  # John says hello!
```

## Naming Conventions
- Class names use **PascalCase** (e.g., `MyClass`).
- Methods and attributes use lowercase and underscores (`my_method`).

## Special Methods
- `__init__`: Constructor, initializes object attributes upon creation.
- Magic methods (`__magic__`) enhance built-in functionality (e.g., `__str__`, `__len__`, `__eq__`).

**Example (Magic Method):**
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

book = Book("1984", "George Orwell")
print(book)  # '1984' by George Orwell
```

- [Full Magic Method Reference](https://rszalski.github.io/magicmethods/)

## Attributes
### Class vs. Instance Attributes
- **Class Attributes**: Common to all instances (e.g., humans have `1 head`).
  ```python
  class Human:
      num_heads = 1

  john = Human()
  print(john.num_heads)  # 1
  ```
- **Instance Attributes**: Unique per object (e.g., `skin_color`). Defined within `__init__` or dynamically:
  ```python
  def __init__(self, skin_color):
      self.skin_color = skin_color

  mary = Human("tan")
  print(mary.skin_color)  # tan
  ```

### Private Attributes
- Defined using double underscores (`__private_attr`).
- Prevents accidental external access but not secure.
- Accessed internally via: `obj._ClassName__private_attr`

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

account = Account(1000)
# account.__balance  # raises AttributeError
print(account.get_balance())  # 1000
```

## Methods
- Instance methods have `self` as their first argument.
- Class methods (`@classmethod`) act on class-level data, used for factory methods:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def origin(cls):
        return cls(0, 0)

p = Point.origin()
```

## Type Checking
- Check object instantiation: `isinstance(obj, ClassName)`
- Get object's class: `type(obj)` returns `<class '__main__.ClassName'>`

```python
print(isinstance(john, Human))  # True
print(type(john))  # <class '__main__.Human'>
```

## Custom Containers
Define custom containers by overriding magic methods:
```python
class MyList:
    def __init__(self):
        self.data = []

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

my_list = MyList()
my_list.data = [1, 2, 3]
print(my_list[0])  # 1
```

## Inheritance
Avoid duplication by inheriting common attributes/methods from a parent class.

### Single Inheritance
```python
class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def __init__(self, breed):
        super().__init__('dog')
        self.breed = breed

    def speak(self):  # Method overriding
        print("Woof!")

my_dog = Dog("Labrador")
my_dog.speak()  # Woof!
```

### Multilevel Inheritance
Multiple inheritance levels (grandparent → parent → child). Limit to 1-2 levels to avoid complexity.

### Multiple Inheritance
Child inherits from multiple parents. Python resolves methods left to right.

## Abstract Classes & Methods
- Enforce a common interface without direct implementation.
- Use `abc` module:
```python
from abc import ABC, abstractmethod

class Stream(ABC):
    @abstractmethod
    def open(self): pass

class FileStream(Stream):
    def open(self):
        print("File opened")
```
- Cannot instantiate abstract classes directly.

## Polymorphism
- Use different class instances interchangeably through a common interface.
- Behavior determined at runtime.

### Duck Typing
Python checks object behavior, not strict inheritance.

```python
class Duck:
    def quack(self): print("Quack!")

class Person:
    def quack(self): print("I'm pretending to quack!")

def make_it_quack(obj):
    obj.quack()

make_it_quack(Duck())  # Quack!
make_it_quack(Person())  # I'm pretending to quack!
```

## Extending Built-in Types
Subclass built-in types for additional behaviors:

```python
class TrackableList(list):
    def append(self, item):
        print(f"Adding {item}")
        super().append(item)

my_list = TrackableList()
my_list.append(3)  # Adding 3
```

## Data Classes
Simplify data-only classes:

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(x=1, y=2)
```
Immutable: attributes cannot change post-creation.