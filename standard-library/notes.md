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

# File and Data Handling Cheat Sheet

---

## Working with ZIP Files

ZIP archives are commonly used for compressing multiple files and directories.

**Basic Operations:**
```python
from zipfile import ZipFile

# Reading a zip file
with ZipFile('file.zip', 'r') as zip:
    print(zip.namelist())  # List files
    zip.extractall('output_directory')  # Extract all files
    info = zip.getinfo('specific_file.txt')  # Get file metadata

# Writing a zip file
with ZipFile('file.zip', 'w') as zip:
    zip.write('file.txt')  # Add files
```

---

## Working with CSV Files

CSV (Comma Separated Values) files are simple, widely-used formats for tabular data.

### Using Python's built-in CSV module:
```python
import csv

# Writing to a CSV
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])  # Write header
    writer.writerow(['Alice', 30, 'London'])  # Write data

# Reading from a CSV
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

### Using Pandas (recommended for larger datasets):
```python
import pandas as pd

# Reading CSV
df = pd.read_csv('data.csv')

# Writing CSV
df.to_csv('output.csv', index=False)
```

---

## Working with JSON Files

JSON (JavaScript Object Notation) is the standard for data exchange, especially with APIs and configuration files.

```python
import json

# Reading JSON
with open('data.json', 'r') as file:
    data = json.load(file)

# Writing JSON
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# JSON to string (serialization)
json_string = json.dumps(data, indent=4)

# String to JSON (deserialization)
data = json.loads(json_string)

# Safe access using .get()
name = data.get('name', 'Default Name')
```

**Error Handling:**
```python
try:
    data = json.loads(invalid_json_string)
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
```

---

## Working with XML Files

XML is often used for data interchange in complex hierarchical structures.

### Using ElementTree (built-in):
```python
import xml.etree.ElementTree as ET

# Parsing XML
root = ET.parse('file.xml').getroot()

# Traversing XML
data = []
for child in root.findall('element'):
    item = child.find('sub_element').text
    data.append(item)

# Creating XML
data = ET.Element('data')
item = ET.SubElement(data, 'item')
item.text = 'Value'

# Writing XML
ET.ElementTree(data).write('output.xml', encoding='utf-8', xml_declaration=True)
```

---

## Working with YAML Files

YAML (YAML Ain't Markup Language) is commonly used for human-readable configuration files.

### Using PyYAML (Third-party library):
Install with `pip install pyyaml`:

```python
import yaml

# Reading YAML
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

# Writing YAML
with open('config.yml', 'w') as file:
    yaml.dump(config, file)
```

---

## Working with Excel (XLSX) Files

Excel files are standard in business and data analytics.

### Using Pandas (recommended):
Install dependencies with `pip install openpyxl pandas`:

```python
import pandas as pd

# Reading Excel
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Writing Excel
df.to_excel('output.xlsx', sheet_name='Results', index=False)
```

### Using openpyxl for advanced control:
```python
from openpyxl import Workbook, load_workbook

# Writing to Excel
wb = Workbook()
sheet = wb.active
sheet.title = "Data"
sheet.append(['Name', 'Age', 'City'])
sheet.append(['Bob', 25, 'Paris'])
wb.save('output.xlsx')

# Reading from Excel
wb = load_workbook('data.xlsx')
sheet = wb['Sheet1']
for row in sheet.iter_rows(values_only=True):
    print(row)
```

---

# SQLite Databases with Python

SQLite is ideal for lightweight applications, particularly on mobile devices and embedded systems. It offers a self-contained, serverless, zero-configuration SQL database engine.

## Setup

Download a GUI tool for exploring SQLite databases from [DB Browser for SQLite](https://sqlitebrowser.org/).

---

## Connecting to a Database

```python
import sqlite3

# Establish a connection
with sqlite3.connect("db.sqlite3") as connection:
    cursor = connection.cursor()
```

---

## Creating Tables

```python
with sqlite3.connect("db.sqlite3") as connection:
    connection.execute('''CREATE TABLE IF NOT EXISTS Movies
                          (id INTEGER PRIMARY KEY, title TEXT, year INTEGER)''')
    connection.commit()
```

---

## Inserting Data

Use parameterized queries (`?`) to avoid SQL injection:

```python
movies = [
    {'id': 1, 'title': 'Inception', 'year': 2010},
    {'id': 2, 'title': 'Interstellar', 'year': 2014}
]

with sqlite3.connect("db.sqlite3") as connection:
    command = "INSERT INTO Movies VALUES (?, ?, ?)"
    for movie in movies:
        connection.execute(command, tuple(movie.values()))
    connection.commit()
```

- `commit()` saves your changes permanently to the database.

---

## Querying Data

Fetch data using `fetchone()`, `fetchmany()`, and `fetchall()`:

```python
with sqlite3.connect("db.sqlite3") as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Movies")

    # Fetch all records
    records = cursor.fetchall()
    for record in records:
        print(record)

    # Fetch one record
    cursor.execute("SELECT * FROM Movies WHERE id=?", (1,))
    movie = cursor.fetchone()
    print(movie)
```

---

## Updating Data

```python
with sqlite3.connect("db.sqlite3") as connection:
    connection.execute("UPDATE Movies SET year = ? WHERE id = ?", (2022, 1))
    connection.commit()
```

---

## Deleting Data

```python
with sqlite3.connect("db.sqlite3") as connection:
    connection.execute("DELETE FROM Movies WHERE id = ?", (2,))
    connection.commit()
```

---

## Advanced Features

### Transaction Handling
```python
with sqlite3.connect("db.sqlite3") as connection:
    try:
        connection.execute("INSERT INTO Movies VALUES (?, ?, ?)", (3, 'Dunkirk', 2017))
        connection.commit()
    except sqlite3.Error as e:
        connection.rollback()
        print(f"Transaction failed: {e}")
```

### Using Context Managers
SQLite connections and cursors are best handled with context managers (`with`) to ensure proper cleanup:

```python
with sqlite3.connect("db.sqlite3") as conn:
    with conn:
        conn.execute("INSERT INTO Movies VALUES (?, ?, ?)", (4, 'Tenet', 2020))
```

---

## Handling SQLite Errors

```python
try:
    with sqlite3.connect("db.sqlite3") as connection:
        connection.execute("INVALID SQL")
except sqlite3.Error as e:
    print(f"SQLite error: {e}")
```

---

SQLite provides a robust, simple, yet powerful way to handle data storage and retrieval in Python-based applications.