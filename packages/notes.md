Python community is rich and thriving ans is full of very useful packages and modules implementing a lot of functionality you can think ouf.

To know whether to use what package for what task you can searh the internet and see what other poeple are using and use your onw judgement.

Virtual environments are used to package all the dependencies of a project otgethet into one isolated environement with a particular version of python interpreter and packages.
Most contain a way to install, uninstall (manage) to activate, deactivate and export etc.

##
pip is a tool that is used to use pypi to install packages.
Eg: pip install requests (to send http requests)
These apckages are maintaned and upgraded indepently and so you need to upgrade from time to time.

pip list to list all packages.
Semantic versioning : Eg: 2.4.67 will represent 2nd major version 4th minor version and 67th patch (for bug fixes)
You can check the release history to see what is the release history and install the versuon you want (newer may not always be better, it may have bugs plus you need compatibility with rest of your code). by defualt it installs the latest compatible version.

use pip uninstall requests. You should cover all the useful and essential commands for the tool pip like pip list and others.

## pipenv is a dependey manager that uses pip and env under the hood
pipenv install requests
pipenv --venv (directory of the virtual env) its goofd that the venv is separaete from theproject directory (not the case with using pip and venv separately.)

pipenv shell
execute python code scripts then exit to exit.

you can use ctrl shift p to select python interpreter while running on vscode. You may use jupyter, anaconda, venv, pipenv and others.
You can export a pipfile and simply run pipenv install it will find the pipfule and install all the dependencies.

pipenv graph
pipenv update --outdated

## Publishing a package
Create a new account on pypi.
setuptools, while and twine

Create a new directory (which will be the root of your project) with the dame name as your package.
Create folders for data, tests and your package directory (same name). 
Add __init__.py and modules with code.

Now you need to add setup.py  in the root, a Readme.md and a License. You can ghot to license.com and aget basic license agreements. copy paste.

import setuptools
setuptools.setup(name, version, long_description= read the readmen and put its content here, packages =setuptools.find_packages(exclude=["tests", "data"]))

then run python setup.py sdist bdist_wheel that is short for source distribution and a build distribution (2 distributions) -> whl and tar.gz files
use twine to upload the files on the dist directory twine upload

## Docstrings:
Docuemneing is important to guide users.  The intellisense shows docstrings in the tooltips while writing.
what does it do, with inputs and outputs, parameters and returns. FOr the module you wirte the docstringon the top

sohrt summary 
blak like
a more detailed explanation. with explainign each class and method.

## Pydoc
You can see the docuemntation for any moduel using pydoc followed by the module name.
You can also export the docuemntation to an html file and render it with a browswe.
You can also load it up in a local server and navigage the docuemntsation of python stl.





Anaconda vs Miniconda
Define what are anacona and miniconda and their pros concs and use case persona.
link, installation walkthrough steps, and major commands of creating an env, naming it, listing packages, installing packages, unistalling, creating adn env file, exporting env file, imstaling form an env file using conda forge, what is conda forge. 