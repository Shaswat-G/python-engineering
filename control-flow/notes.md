Here’s a clean, expanded, and **operational** markdown version of your next block of notes, covering comparisons, control flow, and iteration — all distilled for clarity and utility:

---

# ⚙️ Python Control Flow & Comparisons

## 🔹 Comparison Operators

Used to evaluate relationships between values. Result is always a `bool` (`True` or `False`).

| Operator | Meaning       | Example             | Result     |
|----------|----------------|---------------------|------------|
| `>`      | Greater than   | `5 > 3`             | `True`     |
| `<`      | Less than      | `2 < 1`             | `False`    |
| `>=`     | Greater or equal | `4 >= 4`          | `True`     |
| `<=`     | Less or equal  | `6 <= 3`            | `False`    |
| `==`     | Equal to       | `"a" == "a"`        | `True`     |
| `!=`     | Not equal to   | `7 != 10`           | `True`     |

### Examples with Strings and Type Conversions

```python
print("abc" < "abd")      # True — lexicographic order
print("A" < "a")          # True — 'A' has lower Unicode value than 'a'
print(5 == "5")           # False — no implicit conversion
print(int("5") == 5)      # True — explicit conversion
```

---

## 🔹 Conditionals

### Basic Structure
```python
if condition:
    # indented block runs if condition is True
elif another_condition:
    # runs if previous if fails and this one passes
else:
    # runs if all above conditions fail
```

### Example
```python
age = 20
if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")
```

> **Indentation is mandatory** after colons (`:`). Python uses indentation, not braces `{}`.

---

## 🔹 Ternary Operator (Conditional Expression)

Compact one-liner version of an if-else:
```python
message = "Eligible" if age >= 18 else "Ineligible"
```

---

## 🔹 Logical Operators

| Operator | Meaning           | Example                  | Result     |
|----------|-------------------|--------------------------|------------|
| `and`    | Both must be True | `True and False`         | `False`    |
| `or`     | At least one True | `False or True`          | `True`     |
| `not`    | Inverts Boolean   | `not True`               | `False`    |

### Examples
```python
x = 10
print(x > 5 and x < 20)   # True
print(x < 5 or x > 15)    # False
print(not (x == 10))      # False
```

### Short-circuit Evaluation
```python
False and print("Won't run")  # Doesn't print
True or print("Also skipped") # Doesn't print
```

### Operator Chaining
Python supports chained comparisons:

```python
age = 22
if 18 <= age < 65:
    print("Eligible")  # Same as (age >= 18) and (age < 65)
```

---

## 🔹 String Comparison

Strings are compared using **lexicographic order**, based on Unicode values (like dictionary order).

```python
print("apple" < "banana")    # True
print("Zebra" > "apple")     # False
```

> Capital letters come **before** lowercase in Unicode.

---

## 🔹 `for` Loops

Iterate over a sequence or range.

```python
for number in range(3):
    print(number)   # 0, 1, 2
```

### Range Variants

```python
range(1, 4)       # 1, 2, 3
range(1, 10, 2)   # 1, 3, 5, 7, 9
```

### Nested Loops

```python
for i in range(2):
    for j in range(3):
        print(i, j)
```

---

## 🔹 Iterables

**Anything you can iterate over with `for` is an iterable.**

```python
for letter in "Python":
    print(letter)

for num in (1, 2, 3):
    print(num)
```

- `range`, `str`, `list`, `tuple`, `dict` — all are iterable.
- Custom iterables can be defined via `__iter__()` and `__next__()` (more on this in OOP).

---

## 🔹 `while` Loops

Repeatedly execute a block **while a condition is `True`**.

```python
x = 0
while x < 3:
    print(x)
    x += 1
```

### Infinite Loop with Exit Condition

```python
while True:
    command = input("Enter 'q' to quit: ")
    if command == 'q':
        break
```

---