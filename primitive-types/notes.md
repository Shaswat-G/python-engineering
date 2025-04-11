Here's your expanded, structured, and elegant markdown version of the second part of your notes, with explanations, examples, and best practices — all kept concise and functional:

---

# 📦 Python Core: Variables, Types, Strings, Numbers, and Built-ins

## 🔹 Variables & Memory

### What is a Variable?
A **variable** is a name that **refers to a value** stored in memory. It's how we assign and access data in a program.

```python
age = 25
name = "Alice"
```

### How Variables Work Internally
- Variables point to **memory locations** on the program **stack** or **heap**.
- The **stack** is a structured memory region for storing local variables and function calls.
  - **Push** = add to stack (grows downward in memory)
  - **Pop** = remove from top
  - Fast access, LIFO (Last In First Out)
- The **heap** holds objects like large data structures and class instances.
- Python abstracts memory management, but understanding stack/heap helps with performance and references.

---

## 🔹 Primitive Data Types

### Built-in Types

| Type     | Description               | Example           | Size (approx)   |
|----------|---------------------------|-------------------|-----------------|
| `bool`   | Boolean                   | `True`, `False`   | 1 byte          |
| `int`    | Integer                   | `42`, `-5`        | Arbitrary (no fixed size in Python 3) |
| `float`  | Floating point number     | `3.14`, `-2.0`    | 8 bytes (64-bit IEEE-754) |
| `str`    | String                    | `"hello"`         | Size depends on content |

---

## 🔹 Type Conversion

Convert between types using constructors:

```python
int("42")       # 42
float("3.14")   # 3.14
str(100)        # "100"
bool(0)         # False
```

### Truthiness in Python

| Value          | Boolean Value |
|----------------|----------------|
| `""`, `0`, `None`, `[]`, `{}` | `False` |
| Everything else               | `True`  |

```python
bool("False")  # True – non-empty strings are truthy
```

---

## 🔹 Variable Naming Conventions

- Use **descriptive**, **elegant**, and **readable** names:
  ```python
  user_age = 30
  is_logged_in = True
  ```
- Best practices:
  - **lowercase** names
  - **underscores** instead of camelCase
  - Add **spaces around operators** (`x = y + 3`)

> 💡 Messy code is "code smell" — clean syntax reflects clean logic.

---

## 🔹 Strings

### Basics

```python
name = "Alice"
bio = '''Multiline
string using triple quotes'''
```

- Strings are **0-indexed**
- Negative indices count from the **end**
- **Slicing**: `text[0:3]` → characters at 0, 1, 2
- **Escape characters**: `\n`, `\\`, `\'`, `\"`, `\t`

### Formatting

```python
f"Name: {name}, Age: {age}"
```

### String Methods

| Method          | Example                   | Description                      |
|-----------------|---------------------------|----------------------------------|
| `len()`         | `len("hello")` → 5        | Length of string                 |
| `.isdigit()`    | `"123".isdigit()`         | All characters are digits        |
| `.islower()`    | `"abc".islower()`         | All lowercase                    |
| `.isnumeric()`  | `"42".isnumeric()`        | All numeric                      |
| `.lower()`      | `"ABC".lower()`           | To lowercase                     |
| `.upper()`      | `"abc".upper()`           | To uppercase                     |
| `.title()`      | `"hello world".title()`   | Capitalize each word             |
| `.strip()`      | `" hello ".strip()`       | Remove leading/trailing spaces   |
| `.rstrip()`     | `"test \n".rstrip()`      | Remove trailing whitespace       |
| `.lstrip()`     | `"  start".lstrip()`      | Remove leading whitespace        |
| `.startswith()` | `"python".startswith("py")` | Check prefix                  |
| `.endswith()`   | `"data.csv".endswith(".csv")` | Check suffix                 |
| `.find()`       | `"abcabc".find("b")`      | First occurrence index           |
| `.replace()`    | `"yes no".replace("no", "yes")` | Replace substrings         |
| `.format()`     | `"{} + {}".format(1, 2)`  | Format placeholders              |
| `.zfill()`      | `"42".zfill(5)` → `00042` | Pad with zeros                   |
| `.split()`      | `"a,b,c".split(",")`      | Split by delimiter               |
| `"in"`          | `"py" in "python"`        | Substring check                  |
| `.count()`      | `"hello".count("l")` → 2  | Count substring occurrence       |

---

## 🔹 Numbers

```python
x = 10       # int
y = 3.14     # float
z = 2 + 3j   # complex
```

### Operations

| Operator | Function                 |
|----------|--------------------------|
| `+`      | Addition                 |
| `-`      | Subtraction              |
| `*`      | Multiplication           |
| `/`      | Division (float)         |
| `//`     | Integer division         |
| `%`      | Modulus                  |
| `**`     | Exponentiation           |
| `+=`, `*=` | Augmented assignment  |

### Built-in Functions

```python
round(3.75)    # → 4
abs(-7)        # → 7
```

---

## 🔹 Math Module

```python
import math
```

| Function        | Description                            |
|-----------------|----------------------------------------|
| `math.ceil(x)`  | Smallest integer ≥ x                  |
| `math.floor(x)` | Largest integer ≤ x                   |
| `math.sqrt(x)`  | Square root                            |
| `math.factorial(n)` | Factorial                          |
| `math.log(x)`   | Natural log                            |
| `math.log(x, base)` | Log with custom base               |
| `math.degrees(x)` | Radians to degrees                  |
| `math.radians(x)` | Degrees to radians                  |
| `math.cos(x)`   | Cosine (x in radians)                  |
| `math.atan(x)`  | Arctangent                             |
| `math.dist([x1, y1], [x2, y2])` | Euclidean distance     |
| `math.gcd(a, b)`| Greatest common divisor                |

---

## 🔹 Essential Built-in Functions

| Function     | Usage                    |
|--------------|--------------------------|
| `print()`    | Display output           |
| `len(obj)`   | Length of string, list, etc. |
| `type(obj)`  | Returns the type         |

---