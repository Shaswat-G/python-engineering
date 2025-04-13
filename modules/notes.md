# Organizing Python Code: Modules and Packages

Real-world software projects often have tens of thousands of lines of code. Proper organization is crucial for readability, maintainability, and scalability. Python organizes code using modules and packages.

## Modules

A module is simply a Python file (`.py`) containing functions, classes, and variables that share a related purpose.

### Best Practices for Modules:
- Group related functionality closely.
- Avoid overly large files; split logically into multiple modules.

### Example Module Structure (Deep Learning project):
- `datasets.py`: Custom dataset classes.
- `dataloaders.py`: Data loaders for batching.
- `models.py`: Neural network models.
- `loss.py`: Custom loss functions.
- `train.py`: Training scripts.
- `evaluate.py`: Model evaluation and benchmarking.
- `cross_validation.py`: Cross-validation utilities.
- `visualize.py`: Visualization utilities.
- `utils.py`: General utility functions.

Other common examples include:
- Web applications (Flask/Django): Separate modules for routes, database models, authentication, utilities, and templates.
- Data Science projects: Modules for preprocessing, feature engineering, modeling, evaluation, and visualization.

## Importing Modules

### Direct Import (Recommended)
Explicitly importing specific items is clean and clear:
```python
from dataset import CustomDataset
from models import CNN
```

### Avoid Wildcard Imports
Importing everything (`import *`) is discouraged:
- Leads to namespace pollution.
- May override local names unintentionally.

### Importing Module as an Object
```python
import utils
utils.some_function()
```

## `__pycache__` and Bytecode
- Python compiles modules to bytecode (`.pyc`) in `__pycache__` upon first import.
- Bytecode speeds up subsequent imports but doesn't affect runtime performance.
- Bytecode is regenerated when source code changes.

## Inspecting the Python Path
Python looks for modules in directories listed in the system path (`sys.path`):
```python
import sys
print(sys.path)
```

## Packages

A package is a collection of modules organized in subdirectories. Packages help manage large codebases by grouping modules logically.

### Creating Packages:
- Add an empty `__init__.py` file in a directory to signify it's a Python package.
- `__init__.py` can also control import behavior (like importing all submodules).

**Example:**
```
ecommerce/
│
├── __init__.py
├── shopping/
│   ├── __init__.py
│   ├── sales.py
│   └── cart.py
└── payments/
    ├── __init__.py
    └── gateway.py
```

### Subpackages
Organize complex packages by nesting subpackages:
```
ecommerce.shopping.sales
```

Importing from nested subpackages:
```python
from ecommerce.shopping.sales import calculate_discount
# or
from ecommerce.shopping import sales
sales.calculate_discount()
```

### Absolute vs. Relative Imports
- **Absolute imports** (recommended) clearly specify module locations:
  ```python
  from ecommerce.shopping import sales
  ```
- **Relative imports** (`.` and `..`) are concise but less clear:
  ```python
  from . import sales
  from ..payments import gateway
  ```

## The `dir()` Function
Useful for debugging complex modules:
```python
import sales
print(dir(sales))
```
Lists methods, attributes, and magic methods (`__name__`, `__package__`, `__file__`).

## Executing Modules as Scripts
When a module is imported, Python executes its top-level statements once (on the first import). Subsequent imports retrieve the cached module without re-executing the code.

### Entry Point with `__main__`
Use the following to distinguish between running a file as a script or importing it:
```python
if __name__ == "__main__":
    print("Running as script")
else:
    print("Imported as module")
```

- When run directly, Python sets `__name__` to `'__main__'`.
- If imported, `__name__` is set to the module's filename.

**Practical Usage Example:**
```python
# utils.py
def greet(name):
    print(f"Hello, {name}")

if __name__ == "__main__":
    greet("Developer")
```
- Running `python utils.py` outputs: `Hello, Developer`
- Importing `greet` function in another module:
```python
from utils import greet
greet("User")  # Outputs: Hello, User
```

This approach provides both modularity and flexibility in your code structure.