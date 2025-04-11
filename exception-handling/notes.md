# ⚠️ Errors and Exception Handling in Python

## Categories of Errors (MECE Framework)

Errors in Python can be categorized into three **disjoint** and **exhaustive** buckets:

### 1. **Developer Errors (Bugs)**
- Programming mistakes during development.
- Can be caught during testing, linting, or static analysis.
- **Examples:** `SyntaxError`, `NameError`, `IndentationError`, `TypeError`

### 2. **External Input Errors (User or Data Issues)**
- Bad user inputs, invalid file paths, missing config.
- Should be anticipated and gracefully handled.
- **Examples:** `ValueError`, `FileNotFoundError`, `UnicodeDecodeError`

### 3. **System/Resource Failures**
- Caused by resource limits or environment.
- Often unavoidable but should be recoverable.
- **Examples:** `MemoryError`, `TimeoutError`, `OSError`, `ConnectionError`

> Use this classification to systematically approach exception handling.

---

## Common Python Built-in Exceptions

Here’s a non-redundant but representative set from Python’s [exception hierarchy](https://docs.python.org/3/library/exceptions.html):

### ⚙️ **BaseException**
- Root of all exceptions (don't catch this unless you're building a framework)

### ⚙️ **Exception (inherits BaseException)**
The most common subclass for application-level errors.

#### 🛠 Subclasses of `Exception`:

| Exception               | Description |
|-------------------------|-------------|
| `TypeError`             | Wrong type used (e.g., adding str to int) |
| `ValueError`            | Right type but invalid value |
| `IndexError`            | Index out of bounds |
| `KeyError`              | Missing key in a dictionary |
| `AttributeError`        | Attribute doesn’t exist |
| `ZeroDivisionError`     | Division by zero |
| `FileNotFoundError`     | File or directory not found |
| `PermissionError`       | File exists but access denied |
| `ImportError` / `ModuleNotFoundError` | Module or symbol import failure |
| `StopIteration`         | End of iterator |
| `AssertionError`        | Raised by failed assert |
| `RuntimeError`          | General runtime error not caught by other categories |
| `NotImplementedError`   | Method not implemented in base class |
| `TimeoutError`          | Operation exceeded the allowed time |
| `MemoryError`           | System ran out of memory |
| `RecursionError`        | Max recursion depth exceeded |
| `UnicodeEncodeError` / `UnicodeDecodeError` | String encoding/decoding failed |

> You can view the full class hierarchy using:
```python
help("exceptions")
```

---

## Try–Except Blocks

Use `try-except` blocks to **catch known exceptions** and handle them gracefully.

```python
try:
    result = int("abc")
except ValueError as ex:
    print("Conversion failed:", ex)
    print("Exception type:", type(ex))
else:
    print("Success:", result)
```

### Catching Multiple Exceptions
```python
try:
    x = 1 / int("0")
except (ValueError, ZeroDivisionError) as ex:
    print("Bad input or divide by zero:", ex)
```

---

## Context Managers: `with`

Python's `with` statement ensures resources are **automatically cleaned up** (e.g., file handles, network sockets).

```python
with open("file1.txt", "r") as file1, open("file2.txt", "w") as file2:
    for line in file1:
        file2.write(line)
```

- Any object with `__enter__` and `__exit__` methods can be used with `with`.
- Example use cases:
  - File I/O
  - DB transactions
  - Locks, mutexes
  - Temporary directories

---

## The `finally` Block

Use `finally` for **cleanup actions**, regardless of whether an exception was raised.

```python
try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("Missing file.")
finally:
    file.close()  # Always runs
```

---

## Raising Exceptions

You can raise exceptions intentionally when detecting invalid state:

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
```

### Performance Consideration

Raising and catching exceptions is **slow**. Avoid using exceptions for control flow.

```python
from timeit import timeit

print("Try-Except block (with exception):")
print(timeit('try:\n int("abc")\nexcept:\n pass', number=10000))

print("If-check instead:")
print(timeit('s = "abc"\nif s.isdigit():\n int(s)', number=10000))
```

- Exceptions are **~3–5x slower** than regular logic.
- For performance-sensitive code (e.g., APIs, ML pipelines), **prefer if-checks** over try-except if errors can be predicted.

---

## Best Practices Summary

- Handle only expected exceptions.
- Be specific in what you catch.
- Use `with` for managing resources.
- Use `finally` to ensure cleanup.
- Avoid using exceptions as flow control.
- Log and re-raise when necessary (especially in layered systems).

---