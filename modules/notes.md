Real programs and software can contain tens of thousands of lines of code.
We have to split puur codes across multiple files (modules) that function as sections for eacy of use and maintanability.
Each module should contain highly related cocepts (functions and classes)
For Eg: in a DL repo
custom dataset classes - for handling different datasets
custom datal loaders - for different datasets
model class
loss function
utils
training scripts
evaluation / performance becnhmarking
cross validation
visualizations etc
[This was a DL example, add more from popular use cases]


By keeping script sin the same directory you can import classes and functions by using from script_name import class!, functionB etc
Simply importing with a * is bad practice, This is becuase it might override the functionality of objects and methods in the current script with the same name.
So its good practive to only import what is being used.
Yoiu can either also import the entire module as an object : import script_name and call its functionality using script_name.function()

You will __pycache__ which contains the compiled version of the modules that you are importing. These are .pyc file (c python, remember?). This is Python Byte Code.
This only speeds up imports and does not actually improve the rruntime performance of tyour application. They are refreshed everytime you make a chaneg in the module.

You can see the path vairable by import sys and then doing print(sys.path)

Since we create many modules in a project having them in the same directory will complicate things -> 20+ modules say.
Its better to organize modules into subfolder and package them into a package.
A files is mapped to a module and a subfolder (wchih contains multiple modules) is mapped to a package.
To instruct the python interpreter to see a subfolder as a package of modules, you have to include hte __inti__.py script in the same folder.
This is where you can define the behavior of import * etc.

You can break an exsiitng package into subpackages by creating a subfolder and including a __init__.py script in that subfolder.
While importing you can jsut use the . operator. 
Eg: 
from ecommerce.shopping.sales import funcA
or from ecommerce.shopping import sales and then call sales.fincA

exommerce is the package, shopping is the subpackage and sales is the module.

We can use absolut (best practicve) or relative improts to import finctionality from differently nested sub-subspackaeges etc. this is called intra package references.