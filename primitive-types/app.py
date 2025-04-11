import math

# Variables and Types
name = "Alice"
age = 30
height = 5.7
is_student = True

# Type Checking
print(type(name), type(age), type(height), type(is_student))

# Type Conversion
age_str = str(age)
height_int = int(height)
empty_string = ""
print(bool(empty_string), bool("False"))  # False, True

# Variable Naming Convention
user_score = 95
final_result = True

# String Operations
bio = f"My name is {name}. I'm {age} years old."
print(bio)

sample = "  Hello, Python 123!  "
print("Length:", len(sample))
print("Lowercase:", sample.lower())
print("Digits only?", sample.isdigit())
print("Stripped:", sample.strip())
print("Starts with '  He'?", sample.startswith("  He"))
print("Split on comma:", sample.split(","))

# String Slicing
print("First 5 chars:", sample[:5])
print("Last char:", sample[-1])

# String Formatting
print("Score: {:.2f}".format(95.678))  # 95.68

# Numeric Operations
x = 10
y = 3
print("Add:", x + y, "Div:", x / y, "Floor Div:", x // y, "Mod:", x % y, "Pow:", x**y)

# Compound Assignment
x += 5
y *= 2
print("Updated x:", x, "Updated y:", y)

# Math Module Usage
angle = math.radians(90)
print("cos(90°):", math.cos(angle))
print("ceil(4.2):", math.ceil(4.2))
print("sqrt(16):", math.sqrt(16))
print("gcd(48, 180):", math.gcd(48, 180))
print("factorial(5):", math.factorial(5))

# Built-ins
print("Length of name:", len(name))
print("Absolute:", abs(-42))
print("Round:", round(3.756, 2))

# Truthiness
values = ["", " ", 0, 1, None, "False"]
truths = [bool(v) for v in values]
print("Truthiness:", dict(zip(values, truths)))