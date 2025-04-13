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