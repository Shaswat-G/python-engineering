#!/usr/bin/env python3

from timeit import timeit
from collections import defaultdict


# --------------------------------
# 1. Common Built-in Exceptions
# --------------------------------
def demo_common_exceptions():
    print("=== Common Exceptions ===")
    try:
        lst = [1, 2, 3]
        print(lst[5])  # IndexError
    except IndexError as ex:
        print("Caught IndexError:", ex)

    try:
        a = 5 + "5"  # TypeError
    except TypeError as ex:
        print("Caught TypeError:", ex)

    try:
        int("abc")  # ValueError
    except ValueError as ex:
        print("Caught ValueError:", ex)

    try:
        x = 1 / 0  # ZeroDivisionError
    except ZeroDivisionError as ex:
        print("Caught ZeroDivisionError:", ex)
    print()


# --------------------------------
# 2. Multiple Exception Handling
# --------------------------------
def demo_multiple_exceptions():
    print("=== Multiple Exceptions ===")
    try:
        value = int("0")
        result = 10 / value
    except (ValueError, ZeroDivisionError) as ex:
        print("Handled ValueError or ZeroDivisionError:", ex)
    else:
        print("Division successful:", result)
    print()


# --------------------------------
# 3. Raising Exceptions
# --------------------------------
def demo_raising_exception():
    print("=== Raising Exceptions ===")

    def set_age(age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        return f"Age set to {age}"

    try:
        print(set_age(-5))
    except ValueError as ex:
        print("Caught custom exception:", ex)
    print()


# --------------------------------
# 4. Finally Block
# --------------------------------
def demo_finally_cleanup():
    print("=== Finally Cleanup ===")
    try:
        file = open("nonexistent.txt", "r")
    except FileNotFoundError:
        print("File not found.")
    finally:
        print("Cleanup executed in finally block.\n")


# --------------------------------
# 5. Context Manager with `with`
# --------------------------------
def demo_context_manager():
    print("=== Context Manager ===")
    try:
        with open("sample.txt", "w") as file:
            file.write("Hello from context manager.\n")
        print("File written successfully with `with`.")
    except IOError as ex:
        print("IO error:", ex)
    print()


# --------------------------------
# 6. Performance: Try-Except vs If-Check
# --------------------------------
def demo_performance_comparison():
    print("=== Exception vs If Performance ===")
    try_time = timeit('try:\n int("abc")\nexcept:\n pass', number=10000)
    if_time = timeit('s = "abc"\nif s.isdigit():\n int(s)', number=10000)

    print("Try-Except time:", try_time)
    print("If-Check time:  ", if_time)
    print("Try/Except is ~{:.1f}x slower".format(try_time / if_time))
    print()


# --------------------------------
# Main runner
# --------------------------------
def main():
    demo_common_exceptions()
    demo_multiple_exceptions()
    demo_raising_exception()
    demo_finally_cleanup()
    demo_context_manager()
    demo_performance_comparison()


if __name__ == "__main__":
    main()
