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
