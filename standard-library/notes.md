Python is rich with features to make it easier to work with digital world.

## Working with paths:
from pathlib import Path
Path("C:\\Program Files\\Microsfot") or use a raw strinf r"" where you do not have to escape the backslash.

Expand on os module:
1. print(os.path.curdir())  # Prints the current working directory
print(os.path.abspath('.'))  # Prints the absolute path of the current directory
print(os.path.basename('/path/to/file.txt'))  # Prints 'file.txt'
print(os.path.dirname('/path/to/file.txt'))  # Prints '/path/to'
print(os.path.exists('/path/to/file.txt'))  # Checks if the file exists
print(os.path.join('/path', 'to', 'file.txt'))  # Joins paths correctly
print(os.path.split('/path/to/file.txt'))  # Splits the path into directory and file name
print(os.path.splitext('/path/to/file.txt'))  # Splits the file name and extension
print(os.path.getsize('/path/to/file.txt'))  # Gets the size of the file
print(os.path.isdir('/path/to/directory'))  # Checks if the path is a directory
print(os.path.isfile('/path/to/file.txt'))  # Checks if the path is a file
print(os.path.isabs('/path/to/file.txt'))  # Checks if the path is absolute
print(os.path.normpath('/path//to//file.txt'))  # Normalizes the path
print(os.environ)  # Prints the environment variables
print(os.getenv('HOME'))  # Prints the value of the HOME environment variable
print(os.getcwd())  # Prints the current working directory
print(os.chdir('/path/to/directory'))  # Changes the current working directory
print(os.listdir('.'))  # Lists the files in the current directory
print(os.mkdir('new_directory'))  # Creates a new directory
print(os.makedirs('new_directory/sub_directory'))  # Creates a new directory and its parent directories
print(os.remove('file.txt'))  # Removes a file
print(os.rmdir('new_directory'))  # Removes a directory
print(os.rename('old_file.txt', 'new_file.txt'))  # Renames a file
print(os.stat('file.txt'))  # Gets the status of a file
print(os.walk('.'))  # Walks through the directory tree
print(os.pathsep)  # Prints the path separator for the operating system
print(os.linesep)  # Prints the line separator for the operating system
print(os.sep)  # Prints the file path separator for the operating system
print(os.name)  # Prints the name of the operating system
print(os.system('echo Hello World'))  # Executes a system command
2. os.environ - get, pop, uodate, clear, items, keys, values
3. print(os.environ.keys())  # Prints the keys of the environment variables
print(os.environ.values())  # Prints the values of the environment variables
print(os.environ.items())  # Prints the items of the environment variables

Basically anything you want to do with files (check for existence, make, remove, list, globbing, rglob), directories, sizes, environement variables, system calls, executing commands, etc