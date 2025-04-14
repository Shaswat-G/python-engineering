# Python Package Management and Environments

## Python Community and Package Ecosystem
The Python community is large, active, and produces a wide variety of high-quality packages across domains such as web development, data science, automation, and machine learning.

To choose the right package:
- Search repositories like GitHub, discussions on StackOverflow, and package stats on [PyPI](https://pypi.org)
- Assess popularity, maintenance activity, and compatibility
- Use your judgment based on documentation and community adoption

---

## Virtual Environments
A **virtual environment** isolates a project's dependencies (including Python version) from the global environment.

### Common tools:
- `venv` (built-in since Python 3.3)
- `pipenv` (manages `Pipfile`, integrates pip + virtualenv)
- `conda` (alternative environment and package manager)

### venv Example:
```bash
python -m venv env
source env/bin/activate  # or .\env\Scripts\activate on Windows
pip install some-package
pip freeze > requirements.txt
```

---

## pip: Python Package Installer
`pip` is the standard tool for installing packages from PyPI.

### Common Commands:
```bash
pip install requests
pip uninstall requests
pip list                    # List installed packages
pip show requests           # Show package details
pip freeze > requirements.txt
pip install -r requirements.txt
```

### Semantic Versioning:
Format: `MAJOR.MINOR.PATCH` (e.g., `2.4.67`)
- MAJOR: Breaking changes
- MINOR: New features (backward-compatible)
- PATCH: Bug fixes

To install specific versions:
```bash
pip install requests==2.28.1
```

---

## pipenv: Dependency Manager
Combines pip and virtualenv with Pipfile tracking.

### Commands:
```bash
pipenv install requests     # Install package & create environment
pipenv shell                # Activate environment
exit                        # Exit environment
pipenv --venv               # Get venv path
pipenv graph                # Show dependency tree
pipenv update --outdated    # Show outdated packages
pipenv install              # Recreates env from Pipfile
```

### VSCode Tip:
Use `Ctrl+Shift+P` → "Python: Select Interpreter" to choose the right environment.

---

## Publishing Your Own Package to PyPI

### Steps:
1. **Create project structure**
```
your-package/
├── your_package/            # Contains __init__.py and module code
├── tests/
├── data/
├── README.md
├── LICENSE
├── setup.py
```

2. **setup.py Example**:
```python
import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="your-package",
    version="0.1.0",
    author="Your Name",
    description="Short summary",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=["tests", "data"]),
    classifiers=["Programming Language :: Python :: 3"],
    python_requires='>=3.6'
)
```

3. **Build and Upload**:
```bash
python setup.py sdist bdist_wheel
pip install twine

twine upload dist/*
```

---

## Documentation with Docstrings

### Structure:
```python
def square(x):
    """
    Calculate square of a number.

    Parameters:
        x (int | float): Number to be squared.

    Returns:
        int | float: Square of x.
    """
    return x * x
```

- Short summary (first line)
- Blank line
- Detailed explanation with inputs and outputs

Place module-level docstrings at the top of `.py` files.

---

## pydoc: View Python Docs

- View documentation in terminal:
```bash
pydoc math
```

- Serve local documentation via browser:
```bash
pydoc -p 1234   # Opens docs at http://localhost:1234
```

- Export to HTML:
```bash
pydoc -w math   # Generates math.html
```

---

## Anaconda vs Miniconda

### Definitions:
- **Anaconda**: Full Python distribution with 1,500+ preinstalled data science packages
- **Miniconda**: Minimal installer with `conda`, Python, and basic tools. Lightweight, customizable

### Use Cases:
- **Anaconda**: Ideal for beginners or out-of-box data science environment
- **Miniconda**: Preferred by advanced users who want control and minimal bloat

### Installation:
- Download from: [Anaconda](https://www.anaconda.com), [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

### Common Commands:
```bash
conda create --name myenv python=3.10
conda activate myenv
conda install numpy pandas
conda list
conda remove package-name
conda env export > environment.yml
conda env create -f environment.yml
conda config --add channels conda-forge
```

### What is conda-forge?
A community-maintained collection of high-quality `conda` packages. Often more up-to-date and widely used than the default channel.

---