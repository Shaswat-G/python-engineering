## Why Python?
- Fastest growing programming language in terms of number of users.
- High level, easy to learn, easy to write and understand
- Huge community
- Large Exosystem
- Cross Platform

Python 2.0 is a legacy version, now it is python 3.x -> I am using puython 3.9

Expression - line of code that produces a value (evaluation)
Syntax - correct grammar according to the rules of the code.
Editors - any text editor - vim, notepad, sublime text, notepad++,
IDE - Editors with extra features like autocompletion, debugging, testing, version control etc - Jupyter Notebooks, PyCharm, Atom, VS Code, Colab


Install the Python extension in VS code it comes with the following features.
Linting - syntax checking for errors
Autocomplete - write code faster
code formatting - redability, pretty
unit testing - run automated test
code snippets - can use premade templates to not write them from scratch.



Python Enhancement Proposals:
People use PEP8 - it is a set of guidelines for python code. Allows for consistency with other people.
Autopep8 is a tool to automatically format your python code.

Can enabel format on save in the user settings from the command palette.
It helps to create a shortcut for running python code. I have changed it to ctrl + R to generally run


When we install python, we are actully installing a python implementation which can interprtest ccode writte4in the python languagte
the default is Cpython - written in C
there is also Jython (Java). IronPython (C#) and PyPy(wiritten in subset of python) certain features work in some, not in others. THey are different.
WHy this variety? Same since we have diff OS, diff  browsers, diff languages, etc.
Techincal reason for using one particular implementation - the Jython version will allow you to import some javascript if you want to use it and youa re a java developer.
SImiliarly for Ironlython.



How is Python interpreted and compiled?

Java code is compiled bu tis compiler into Java Bytecode that can be used cross-platform with diff cpus and processors. 
Java Bytcode is converted to Machine code (instrcution set) using Java Virtual Machine JVM converts to mchince code on run time.

Similary for Python to Python Bytecode to Python Virtual Machine to machine code.
However, Jython converts python code to Java bytecode and hence can be run with other java code.
