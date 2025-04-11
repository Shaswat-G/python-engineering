#!/usr/bin/env python3
"""
A demo script to illustrate Python’s core data structures and related operations.
Each section demonstrates creation, manipulation, and real-world usage patterns.
"""

from collections import deque
from sys import getsizeof


# -------------------------------
# 1. Lists
# -------------------------------
def demo_lists():
    print("=== Lists ===")

    # Creating a list: dynamic array; used for dynamic, ordered data.
    demo_list = [1] * 10 + [0] * 10
    print("Initial demo_list (10 ones + 10 zeros):", demo_list)

    # Slicing & Indexing
    print("First element:", demo_list[0])
    print("Every 2nd element:", demo_list[::2])
    print("Reversed list:", demo_list[::-1])

    # Unpacking: get first, second elements and rest of list
    data = [1, 2, 4, 4, 4, 4, 4, 4, 6]
    first, second, *others = data
    print("Unpacked (first, second, others):", first, second, others)
    first, *others, last = data
    print("Unpacked (first, others, last):", first, others, last)

    # Looping with enumerate (common in DSA when index matters)
    for idx, val in enumerate(demo_list[:5]):
        print(f"Index {idx} -> Value: {val}")

    # Modification methods: append, extend, pop, insert, remove, count, sort, and reverse.
    demo_list.append(1)
    new_list = [3, 4, 5]
    demo_list.extend(new_list)
    print("After append and extend:", demo_list)

    popped_element = demo_list.pop(-2)
    print("Popped element at index -2:", popped_element)

    demo_list.sort()  # In-place sort; used in many CP problems.
    print("Sorted list:", demo_list)

    demo_list.reverse()  # Reverse the sorted list.
    print("Reversed list:", demo_list)

    demo_list.insert(-2, 42)
    print("After inserting 42 at -2 index:", demo_list)

    demo_list.remove(1)  # Remove first occurrence of 1.
    print("After removing first occurrence of 1:", demo_list)
    print("Count of 42 in list:", demo_list.count(42))

    # List Comprehension: Fast, readable; common in DSA for filtering/mapping.
    squares = [x**2 for x in range(10) if x % 2 == 0]
    print("Squares (even numbers) using comprehension:", squares)

    # Stacks (LIFO): For undo-redo, balanced parentheses, etc.
    stack = []
    stack.append("a")
    stack.append("b")
    print("Stack after pushes:", stack)
    popped_stack = stack.pop()
    print("Stack after pop:", stack, "; Popped:", popped_stack)

    # Queues (FIFO): For message or task processing.
    queue = deque(["first", "second", "third"])
    print("Initial queue:", queue)
    queue.append("fourth")
    print("Queue after appending:", queue)
    dequeued = queue.popleft()
    print("Queue after popleft (dequeued):", dequeued, "; Current queue:", queue)

    # Zip: Combine two iterables (e.g., merging parallel arrays in tech data pipelines).
    another_list = [1, 2, 4, 5, 1, 5, 3, 2, 9, 10]
    zipped = list(zip(demo_list, another_list))
    print("Result of zip(demo_list, another_list):", zipped)
    print()  # Blank line for separation


# -------------------------------
# 2. Tuples
# -------------------------------
def demo_tuples():
    print("=== Tuples ===")

    # Fixed, immutable data; ideal for keys, fixed config, or records in DSA.
    t = (1, 2, 3, 4)
    print("Tuple t:", t)

    # Creating a tuple from any iterable.
    t2 = tuple(["a", "b", "c"])
    print("Tuple t2 from list:", t2)

    # Concatenation & repetition.
    t3 = t + t2
    print("Concatenated tuple (t + t2):", t3)
    print("Repeated tuple t * 3:", t * 3)

    # Membership test.
    print("Is 3 in tuple t?", 3 in t)

    # Swapping variables efficiently.
    a, b = 10, 20
    print("Before swap: a =", a, ", b =", b)
    a, b = b, a
    print("After swap: a =", a, ", b =", b)
    print()


# -------------------------------
# 3. Sets
# -------------------------------
def demo_sets():
    print("=== Sets ===")

    # Sets store unique, unordered items; crucial for deduplication and fast lookups.
    s = {1, 2, 3, 2, 4}
    print("Set s (duplicates dropped):", s)

    # Basic modification.
    s.add(5)
    print("After adding 5:", s)
    s.remove(2)
    print("After removing 2:", s)

    # Set operations: intersection, union, difference, symmetric difference.
    t = {3, 4, 6, 7}
    print("Set t:", t)
    print("Intersection (s & t):", s & t)
    print("Union (s | t):", s | t)
    print("Difference (s - t):", s - t)
    print("Symmetric difference (s ^ t):", s ^ t)
    print()


# -------------------------------
# 4. Dictionaries
# -------------------------------
def demo_dictionaries():
    print("=== Dictionaries ===")

    # Dictionaries use key-value pairs; fast lookups and essential for caching, indexing, etc.
    d = {"name": "Alice", "age": 25, "city": "Zurich"}
    print("Dictionary d:", d)

    # Accessing elements safely.
    print("Name from dictionary:", d.get("name"))
    print("Non-existent key with default:", d.get("country", "Unknown"))

    # Iterate through key-value pairs.
    for key, value in d.items():
        print(f"{key}: {value}")

    # Dictionary Comprehension: Generate mappings quickly.
    squares = {x: x**2 for x in range(5)}
    print("Dictionary comprehension (squares):", squares)
    print()


# -------------------------------
# 5. Generator Expressions
# -------------------------------
def demo_generators():
    print("=== Generator Expressions ===")

    # Generators yield one item at a time for memory efficiency (often used in big data or streams).
    gen = (x**2 for x in range(1000))
    print("Generator object (gen):", gen)
    print("Memory size of generator (bytes):", getsizeof(gen))

    # Use next() or a loop to iterate; here, convert first 10 items to list.
    first_ten = [next(gen) for _ in range(10)]
    print("First 10 values from generator:", first_ten)
    print()


# -------------------------------
# 6. Unpacking Operators
# -------------------------------
def demo_unpacking():
    print("=== Unpacking Operators ===")

    # Unpack iterable into a list.
    values = [*range(5), *"Hello"]
    print("Unpacked list from range and string:", values)

    # Unpack dictionaries: merge two dictionaries.
    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3, "d": 4}
    merged = {**d1, **d2}
    print("Merged dictionary using unpacking:", merged)
    print()


# -------------------------------
# Main function
# -------------------------------
def main():
    demo_lists()
    demo_tuples()
    demo_sets()
    demo_dictionaries()
    demo_generators()
    demo_unpacking()


if __name__ == "__main__":
    main()