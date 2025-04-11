# --- Comparison Operators ---
print("== Comparison Operators ==")
print(5 > 3, 2 < 1, 4 >= 4, 7 != 10)  # Basic comparisons
print("abc" < "abd", "A" < "a")  # Lexicographic order
print(5 == "5", int("5") == 5)  # Type strict vs conversion

# --- Conditionals ---
print("\n== Conditionals ==")
age = 22
if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# --- Ternary Operator ---
print("\n== Ternary Operator ==")
eligibility = "Eligible" if age >= 18 else "Ineligible"
print(eligibility)

# --- Logical Operators & Short-Circuiting ---
print("\n== Logical Operators ==")
x = 10
print(x > 5 and x < 20)  # True
print(x < 5 or x > 15)  # False
print(not (x == 10))  # False

print(False and print("Won't run"))  # Short-circuit: right side not executed
print(True or print("Skipped"))  # Same here

# --- Operator Chaining ---
print("\n== Operator Chaining ==")
if 18 <= age < 65:
    print("Chained Comparison Passed")

# --- String Comparison (Lexicographic) ---
print("\n== String Comparison ==")
print("apple" < "banana")  # True
print("Zebra" > "apple")  # False

# --- For Loops with Range ---
print("\n== For Loops ==")
for i in range(3):
    print(f"Range 0-2: {i}")

for i in range(1, 4):
    print(f"Range 1-3: {i}")

for i in range(1, 10, 2):
    print(f"Range with step 2: {i}")

# --- Nested Loops ---
print("\n== Nested Loops ==")
for i in range(2):
    for j in range(3):
        print(f"({i},{j})", end=" ")
    print()

# --- Iterables (String, Tuple) ---
print("\n== Iterables ==")
for char in "Py":
    print(f"Char: {char}")

for val in (10, 20, 30):
    print(f"Tuple value: {val}")

# --- While Loop ---
print("\n== While Loop ==")
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1

# --- Infinite Loop with Break ---
print("\n== Infinite Loop with Break ==")
i = 0
while True:
    if i >= 3:
        break
    print(f"i = {i}")
    i += 1
