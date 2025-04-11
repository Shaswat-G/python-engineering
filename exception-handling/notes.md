Erorrs can arise due to many reasons:
1. Programming error (we did not program right)
2. User error (user sent bad data)
3. Resource issue (out of resources)

{expand on this list and suggest a better MECE framework for errors in python programming.}

IndexError
TypeError
ValueError
ZeroDivisionError
{expand on this list include all built-in python exceptions with the class hierarchy}


Use try and except blocks with errors that you can anticiapte. you can also put multiple error messages in one tuple
except (ValueError, ZeroDivisionError):
do something

try:

except ValueError as ex:
    print(ex)
    print(type(ex))
else:
do something



Releasing resources:
use context maganers like with.
with open(file1, "r") as file1, open(file2, "w") as file2:
do something.

Objects that support __enter__ and __exit__ magic methods this means that they can be used swith teh with context managememnt protocol!

Use a final clause. This is where you close all network connections, all files, etc.


Raising Exceptions:
Eg: raise ValueError("ABC is the problem")


Raiding exceptions has a cost. we use import timeit from timeit
see if the exception can be handled with a simple if statement and not by rasining exceptions (4 times longer than with just an if)
and so if scalability for users is important then think twice before raising exceptions.
