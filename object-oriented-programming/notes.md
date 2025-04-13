WIth ptogramming we are usually solving problems in a contextual univese.
There are certain objects and operations that are intuitive and natural to model our universe.

So we define objects and their attributes and write up methods like nature's rules to manipulate and interact with them.
A class is a frmaework or a template for creating objects.
An object is an instance of a class.

Eg: Class: Human
Objects: John, Mary, etc.
Attributes: Height, weight, gender, appearance, charisma, etc
Methods: Walk, talk, eat, etc.


For defining classes we use the PascalCase which is no underscores, evey first letter of the word should be capital.
Each method should at least have one parameter that is the self, by convention.
We can use the isinstance(python_object, ClassName) to see if a python object is an instantiation of a class.
the type(object) retuns __main__.ClassName where main is our module.


Constructor:
It is a method that is called whenever an object of a class is instantiaded. It initilaised the attributes of the object.

Class vs instance attributes:
Class attributes are immutable and constant for all objects of a class. Eg: All humans will have 1 nose and 1 head (class attributes) but any skin color (instance attribute, which may not be necessarily defined in the constructor, can be dynamically done also). Class level attributs can also be modified by setting ClassName.class_attribute = "some_value"


Class vs Instance Methods:
Usually the methods in a class need to be called by objects of that class using the dot method. However there are class lebel functions which do not need to be called by an object.
One such category of functions is called a factory method which initializes a special case object of a class (like origin for a point class.)

Magic Methods:
__magicmethod__ : THey have double underscores. Check on google how magic methods are commonly used. The object already inherits a bunvh of magic methods that we did not define as it inherits them.

We can modify them.

Creating Custom containers and operations on them
Data structures are containers and lists, touples, dictionaries are sufficient ususlaly.
But sometime we need to define our own custom.


We can use a double underscore to any attribute in the calss to keep it private. This does not allow people to access these attributes externally.
This is not for security, just a warning for developers to prevent accidental access of these private members. You can use the __dict__ method to get all the attributes of the object. Copy the name of the private attribute you want
its usually prefized with an underscore followed by the classname and then the attribute name.
Eg: object._ClassName__private_attribute.

Instead of setting a private attribute in the class constructor, you can define a set_attribute(self, value): function that is called from within the constructore body and has the necessary checks.


A very useful reference on magic methods: https://rszalski.github.io/magicmethods/



Defining similar functions for different classes leads to code duplication (violation of the DRY principle). Any bug will need to be fixed everywhere else.
And so we use inheritance.

We define a common (more abstract class) that has the common function and inherit that in different classes. Ag: An animal class for mammal and fish classes.
After inheriting, the child class inherits all  functions and attributes form the paretn class. Isinstance shows true for all parents, grandparents etc. You can also use issublcass and isinstance methods.

Defining a oonstructor in the base class will override the constructor of the parent class. This is called method overloading. You need to use the super() function to call the initalizer of the parent class (or super class)

Super() in general can be used to call any method of the parent class. The order of calling the constructors can be changed bu changing the order of calling the constructor inside the base class.



## Multilevel Inheritance.

You can go as abstract and as granular as you want. But, the goal of writing software is to solve a problem, and we should restrict ourselves to 1-2 inheritance levels. Anything beyond that is firstly not needed, secondly adds unnecessary complexity in the code. Just because there can be a hierarchy defined, doesn't mean you should replicate it in code.
[expand on certain real world examples and issues here]


## Multiple Inheritance:
A child class inherits from multiple parent classes. The parent calsses may have the same methods -> python interpreter first tries to find the method in the child class, if not then moves to the first parent class, then the second and so on. Multiple inheritaance is useful, but you have to be careful that the parents and child class shuold not have things (methods) in common.

You can also inherit from existing calsses in python. FOr Eg: you can inherit from the exceptions class in python to define your own exceptions.

Sometimes exposing the mehtods of the parent class is not good. When you derive several calsses from a common parent calss,
say File and Network streams from a class called stream with an open and close method, this can be done by designing an abstract base class, this allows for having a common contract across its derivatives. We cannot create an instance of the abstract class.
This can be done by from abc import ABC, abstractmethod (decorator)
The abstraactmethod decoratoe tells that htese methods have to be implemented in the derivative calss, or else it will also be treated like an abstract class.

Polymorphism: Many forms.
Lets say you create an abstract base calss with a function decorates with the asbstract decorator . All its derivate classes have to implement this metods. you can create a function outside all theses clases which can call these abstract decoreated functions with any of the instacnes of the derivateve class. Whic funciton is actually called is dtermined at runtime when the actual object calls. it.

Ducktyping:
Python is a dynamically typed class. The existence of an abstract class just enforces a rule. EVen if you do not define a common behavior in the abstract class and do not inherit from that class, just simpley have the common behaviour (without that rule), we can achieve the polymorphic behavior. This is called ducktypeing - if it talks like a ducka dn walsk like a duck, it is a duck.


Extending builtin types.
class Text(str):
and can now add multiple things on it - mehtod slike duplicate.
class TrackableList(list):
overwrite the append method for logging say.


Dataclasses
We can use calsses to bundle data and funcitonality together. For classes that have no methods but only deal with data, you will have to define __eq__ magic methods among others for ordering, but this is a bit tedious. You can use a named touple instance. from collections import namedtuple.
Eg: Point = namedtuple("Point", ["x", "y"])
pa = Point(x=1,y=2)
pb = Point(x=3,y=4)

In this case, you can directly check for equality if all atteibutes are the same. However, you cannot change the attributes of the namedtuple after it is created.