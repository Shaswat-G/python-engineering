# Working with Paths and the OS

Python provides powerful modules like `os` and `pathlib` to interact with the operating system, work with file systems, manage environment variables, and execute system commands.

## Working with Paths using `pathlib`

```python
from pathlib import Path
```
- Use raw strings to handle Windows paths:
  ```python
  path = Path(r"C:\\Program Files\\Microsoft")
  ```
- Create platform-independent paths:
  ```python
  path = Path("/usr", "bin", "env")  # Unix
  ```
- Common operations:
  ```python
  path.exists()       # Check if path exists
  path.is_file()      # Check if it's a file
  path.is_dir()       # Check if it's a directory
  path.name           # File name
  path.stem           # Name without extension
  path.suffix         # File extension
  path.parent         # Parent directory
  path.resolve()      # Absolute path
  path.glob("*.txt")  # Glob for txt files
  ```

## OS Module — Full Toolkit

```python
import os
```

### Path Operations
```python
os.path.abspath('.')                   # Absolute path of current directory
os.path.basename('/a/b/c.txt')        # 'c.txt'
os.path.dirname('/a/b/c.txt')         # '/a/b'
os.path.exists('file.txt')            # True/False
os.path.join('folder', 'file.txt')    # 'folder/file.txt'
os.path.split('/a/b/c.txt')           # ('/a/b', 'c.txt')
os.path.splitext('file.txt')          # ('file', '.txt')
os.path.getsize('file.txt')           # File size in bytes
os.path.isdir('folder')               # True if folder
os.path.isfile('file.txt')            # True if file
os.path.isabs('/absolute/path')       # Check if path is absolute
os.path.normpath('/a//b///c')         # '/a/b/c'
```

### Working with Directories and Files
```python
os.getcwd()                            # Get current working directory
os.chdir('/new/path')                  # Change working directory
os.listdir('.')                        # List files in current directory
os.mkdir('new_dir')                    # Make single directory
os.makedirs('a/b/c')                   # Make nested directories
os.remove('file.txt')                  # Delete a file
os.rmdir('dir')                        # Remove empty directory
os.rename('old.txt', 'new.txt')        # Rename file or folder
```

### File Metadata
```python
os.stat('file.txt')                    # File statistics (size, modified time, etc.)
```

### Walking a Directory Tree
```python
for root, dirs, files in os.walk('.'):
    print(root, dirs, files)
```

### System Info and Commands
```python
os.name                                # OS name: 'posix', 'nt', etc.
os.sep                                 # Path separator: '/' or '\\'
os.pathsep                             # Path list separator: ':' or ';'
os.linesep                             # Line separator: '\n' or '\r\n'
os.system('echo Hello World')         # Run system command (Unix/Windows)
```

### Environment Variables
```python
import os

os.environ.get('HOME')                # Get variable
os.environ['HOME']                    # Access like a dictionary
os.environ['NEW_VAR'] = 'value'       # Set environment variable
os.environ.pop('NEW_VAR')             # Remove environment variable
os.environ.update({"MYAPP": "123"})   # Update multiple values
os.environ.clear()                    # Clear all environment variables
```

**Inspecting environment:**
```python
print(os.environ.keys())              # All variable names
print(os.environ.values())            # All values
print(os.environ.items())             # All key-value pairs
```

### Common Use-Cases
- Check file existence before reading
- Create temp directories
- Walk over files recursively
- Extract filenames or extensions
- Execute shell commands (automation)
- Manage project environments (e.g., `VIRTUAL_ENV`, `PATH`)

---