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

### Public, Protected, and Private Attributes & Methods

Python uses naming conventions to indicate the intended visibility of attributes and methods:

- **Public**: No underscore prefix. Accessible from anywhere.
- **Protected**: Single underscore prefix (`_attr`). Should only be accessed within the class and its subclasses (child classes). Not enforced by Python, but signals to developers that direct access is discouraged.
- **Private**: Double underscore prefix (`__attr`). Intended to be accessed only within the defining class. Python performs name mangling to make accidental access harder, but not impossible.

#### Public Attributes and Methods

Accessible from anywhere.

```python
class Car:
    def __init__(self, brand):
        self.brand = brand  # public attribute

    def drive(self):        # public method
        print(f"Driving {self.brand}")

car = Car("Toyota")
print(car.brand)  # Toyota
car.drive()       # Driving Toyota
```

#### Protected Attributes and Methods

Intended for internal use within the class and its subclasses. Prefix with a single underscore.

```python
class SuperHero:
    def __init__(self, name: str, power_level: int):
        self._name = name                # protected attribute
        self._power_level = power_level  # protected attribute

    def get_name(self) -> str:           # public method
        return self._name

    def _some_protected_method(self) -> None:  # protected method
        print("This is a protected method.")

    def some_public_method(self) -> None:
        self._some_protected_method()

spider_man = SuperHero("Spider-Man", 85)
print(spider_man._name)      # Allowed but discouraged
print(spider_man.get_name()) # Recommended

spider_man._some_protected_method() # Allowed but discouraged
spider_man.some_public_method()     # Recommended
```

- **Use Case**: When you want to allow subclasses to access or override an attribute/method, but discourage external access.

#### Private Attributes and Methods

Prefix with double underscores. Intended to be used only within the defining class. Not accessible from subclasses.

```python
class SuperHero:
    def __init__(self, name: str, power_level: int):
        self.__name = name                # private attribute
        self.__power_level = power_level  # private attribute

    def __secret_power(self) -> str:      # private method
        return f"Using {self.__name}'s secret power!"

    def use_power(self) -> str:           # public method to access private method
        return self.__secret_power()

    def get_power_level(self) -> int:     # public method to access private attribute
        return self.__power_level

hero = SuperHero("Iron Man", 95)
# print(hero.__name)           # AttributeError
print(hero.get_power_level())   # 95
print(hero.use_power())         # Using Iron Man's secret power!
```

- **Use Case**: For sensitive data or internal logic that should not be accessed or overridden outside the class.

##### Name Mangling

Private attributes are internally renamed to `_ClassName__attr`, making accidental access harder:

```python
print(hero._SuperHero__name)  # Iron Man  (not recommended)
```

#### Summary Table

| Visibility | Prefix | Accessible From        | Use Case                          |
| ---------- | ------ | ---------------------- | --------------------------------- |
| Public     | none   | Anywhere               | General use                       |
| Protected  | \_     | Class & subclasses     | Internal use, allow inheritance   |
| Private    | \_\_   | Only in defining class | Sensitive/internal implementation |

#### Example Use Cases

- **Public**: Methods and attributes meant for external use (API).
- **Protected**: Helper methods/attributes for subclasses (e.g., `_calculate_bonus`).
- **Private**: Passwords, internal counters, or logic not meant to be exposed.

#### Challenge Example

```python
class BankAccount:
    def __init__(self, title, balance):
        self.title = title        # public attribute
        self._balance = balance   # protected attribute

    def display_balance(self):
        print(f"Balance: ${self._balance}")

account = BankAccount("Savings", 1000)
account.display_balance()  # Balance: $1000
```

#### Private Attribute Challenge

```python
class PasswordManager:
    def __init__(self, password):
        self.__password = password  # private attribute

    def verify_password(self, input_password):
        return self.__password == input_password

pm = PasswordManager("secret123")
print(pm.verify_password("secret123"))  # True
print(pm.verify_password("wrong"))      # False
```

> **Note:** Python relies on conventions for access control ("we're all consenting adults here"). These are not enforced by the language, but following them helps maintain code clarity and safety.

---

### Getter and Setter Methods, Validation, and the `@property` Decorator

#### Why Use Getters and Setters?

- **Encapsulation**: Control access to private/protected attributes.
- **Validation**: Ensure only valid data is set.
- **Flexibility**: Change internal implementation without affecting external code.

#### Classic Getter and Setter Methods

```python
class SuperHero:
    def __init__(self, name: str, power_level: int):
        self.__name = name
        self.__power_level = power_level

    def get_power_level(self) -> int:      # Getter
        return self.__power_level

    def set_power_level(self, new_level: int) -> None:  # Setter with validation
        if 0 <= new_level <= 100:
            self.__power_level = new_level
        else:
            print("Power level must be between 0 and 100!")

hero = SuperHero("Thor", 80)
print(hero.get_power_level())   # 80
hero.set_power_level(90)        # OK
hero.set_power_level(150)       # Error: Power level must be between 0 and 100!
```

#### Typical Use Cases

- Sensitive data (e.g., passwords, balances)
- Attributes requiring validation (e.g., age, scores)
- Read-only or computed properties

#### Challenge Example

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def get_balance(self) -> int:
        return self.__balance

    def set_balance(self, new_balance: int) -> None:
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Cannot set negative balance!")

account = BankAccount(1000)
print(account.get_balance())    # 1000
account.set_balance(-50)        # Cannot set negative balance!
print(account.get_balance())    # 1000
account.set_balance(100)
print(account.get_balance())    # 100
```

#### Pythonic Approach: `@property` and Setter Decorators

Python provides a cleaner, more idiomatic way to define getters and setters using the `@property` and `@<property>.setter` decorators.

```python
class Hero:
    def __init__(self, name: str):
        self.__name = name    # private attribute

    @property
    def name(self) -> str:    # Getter
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:  # Setter with validation
        if new_name:
            self.__name = new_name
        else:
            print("Name cannot be empty!")

hero = Hero("Batman")
print(hero.name)        # Batman (calls getter)
hero.name = "Superman"  # OK (calls setter)
hero.name = ""          # Name cannot be empty!
```

- **Advantages**:
  - Attribute access syntax (`obj.name`) with validation/control.
  - Cleaner and more Pythonic than explicit get/set methods.

#### Challenge: Use `@property` for BankAccount

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Balance cannot be negative!")

account = BankAccount(1000)
print(account.balance)      # 1000
account.balance = -50       # Balance cannot be negative!
```

> **Tip:** Use `@property` for attributes that need validation or computed values, but should be accessed like regular attributes.

---

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

### Class Methods

- **Class methods** operate on the class itself, not on instances.
- Defined with the `@classmethod` decorator and take `cls` as the first parameter.
- Used to modify class attributes or create alternative constructors.

```python
class Superhero:
    training_level = 1  # Class attribute

    def __init__(self, name: str, power: str):
        self.name = name         # Instance attribute
        self.power = power       # Instance attribute

    @classmethod
    def upgrade_training(cls) -> None:
        cls.training_level += 1
        print(f"All heroes now at training level {cls.training_level}")

Superhero.upgrade_training()     # Recommended
print(Superhero.training_level)  # 2

iron_man = Superhero("Iron Man", "Flying")
iron_man.upgrade_training()      # Works, but not recommended
print(iron_man.training_level)   # 3
```

- **Use Case**: Modify class-level data, alternative constructors, or factory methods.

#### Challenge Example

```python
class Library:
    books_available = 100

    @classmethod
    def lend_books(cls, number):
        cls.books_available -= number

    @classmethod
    def return_books(cls, number):
        cls.books_available += number

print(f"Initial status: {Library.books_available} books available")
Library.lend_books(30)
print(f"After lending: {Library.books_available} books available")
Library.return_books(10)
print(f"After return: {Library.books_available} books available")
```

---

### Static Methods

- **Static methods** are utility functions inside a class that do not access instance (`self`) or class (`cls`) data.
- Defined with the `@staticmethod` decorator.
- Used for logic related to the class, but not dependent on class or instance state.

```python
class Superhero:
    def __init__(self, name: str, power: str):
        if not self.is_valid_power(power):
            raise ValueError(f"Invalid power: {power}")
        self.name = name
        self.power = power

    @staticmethod
    def is_valid_power(power: str) -> bool:
        valid_powers = ['Flying', 'Strength', 'Speed', 'Intelligence']
        return power in valid_powers

print(Superhero.is_valid_power('Flying'))         # True
print(Superhero.is_valid_power('Mind Reading'))   # False

iron_man = Superhero("Iron Man", "Flying")        # Works
# mind_reader = Superhero("Hero", "Mind Reading") # Raises ValueError
```

- **Use Case**: Utility functions, validation, or helpers that conceptually belong to the class.

#### Challenge Example

```python
class CurrencyConverter:
    rates = {
        'EUR': 1.2,   # 1 EUR = 1.2 USD
        'JPY': 0.01,  # 1 JPY = 0.01 USD
        'USD': 1.0
    }

    @staticmethod
    def to_usd(amount, currency):
        return amount * CurrencyConverter.rates[currency]

print(f"100 EUR = {CurrencyConverter.to_usd(100, 'EUR')} USD")
print(f"100 JPY = {CurrencyConverter.to_usd(100, 'JPY')} USD")
```

---

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
