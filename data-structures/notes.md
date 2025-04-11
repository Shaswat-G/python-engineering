# Python Data Structures: Lists, Tuples, Sets, and Dictionaries

## Lists

**Definition:**  
A list is a mutable, ordered collection of elements. It is iterable, supports duplicates, and offers powerful operations such as slicing, indexing, concatenation, and more.

### Creating Lists
- **From Literals & Repetition:**
  ```python
  demo_list = [1] * 10 + [0] * 10
  print(demo_list)  # [1, 1, ..., 0, 0]
  ```
- **From Iterables:**
  ```python
  list(range(20))
  list("Any string")
  ```
- **Length:** Use `len(list)`.

### List Operations

#### Indexing & Slicing
- **Basic Indexing:**
  ```python
  lst = [0, 1, 2, 3, 4]
  print(lst[2])         # 2
  ```
- **Slicing:**
  - Every second element: `lst[::2]`
  - Reverse list: `lst[::-1]`
  - Copying: `lst.copy()`
  
- **Unpacking:**
  ```python
  first, second, *others = [1, 2, 4, 4, 4, 4, 4, 4, 6]
  first, *others, last = [1, 2, 4, 4, 4, 4, 4, 4, 6]
  ```

#### Looping Over a List
- **Direct Iteration:**
  ```python
  for x in demo_list:
      print(x)
  ```
- **Using `enumerate`:**
  ```python
  for idx, value in enumerate(demo_list):
      print(idx, value)
  ```

#### List Modification Methods
- **Appending & Extending:**
  ```python
  demo_list.append(1)
  new_list = [3, 4, 5]
  demo_list.extend(new_list)
  ```
- **Pop & Remove:**
  ```python
  demo_list.pop(-2)       # Remove element at index -2
  demo_list.remove(1)     # Removes first occurrence of 1
  ```
- **Insert, Reverse, and Clear:**
  ```python
  demo_list.insert(-2, 42)
  demo_list.reverse()
  demo_list.clear()       # Empty list
  del demo_list[0:3]      # Delete slice from index 0 to 2
  ```
- **Searching:**
  ```python
  idx = demo_list.index("object")   # Returns index of the first match
  count = demo_list.count("item")     # Counts occurrences
  ```

#### Additional Useful Methods
- **Sorting:** Use `list.sort()` (in-place) or `sorted(iterable, reverse=True)` (returns a new sorted list). For complex objects, pass a key function:
  ```python
  demo_list.sort(key=lambda x: x)  # Customize as needed
  ```
- **List Comprehensions:** An idiomatic, readable way to create lists.
  ```python
  squares = [x ** 2 for x in range(10) if x % 2 == 0]
  ```

#### Lambda Functions and `map`/`filter`
- **Lambda:** Anonymous, single-expression functions.
  ```python
  # Sorting using a lambda key:
  demo_list.sort(key=lambda x: x)
  ```
- **Map Function:**
  ```python
  items = [("P1", 10), ("P2", 4), ("P3", 23)]
  doubled = map(lambda x: (x[0], x[1] * 2), items)
  print(list(doubled))
  ```
- **Filter and Sorted Combined:**
  ```python
  items = [
      ("P1", 10), ("P2", 4), ("P3", 23),
      ("P4", 12), ("P5", 54), ("P6", 47),
      ("P7", 3), ("P8", 97), ("P9", 96), ("P10", 43)
  ]
  filtered_items = filter(lambda x: x[1] > 20, items)
  sorted_items = sorted(filtered_items, key=lambda x: x[1], reverse=True)
  mapped_items = map(lambda x: (x[0], x[1] * 2), sorted_items)
  print(list(mapped_items))
  ```
- **Recommendation:** List comprehensions are generally more readable:
  ```python
  [item[1] for item in items if item[1] > 20]
  ```

#### Stacks and Queues
- **Stacks (LIFO):**  
  Use lists with `.append()` for push and `.pop()` for pop.  
  _Application:_ Undo-redo systems, back-forward navigation, matching parentheses.
  ```python
  stack = []
  stack.append(1)  # Push
  stack.pop()      # Pop
  ```
- **Queues (FIFO):**  
  Use `deque` from the `collections` module.
  ```python
  from collections import deque
  queue = deque([1, 2, 3])
  queue.append(4)       # Enqueue
  queue.popleft()       # Dequeue
  if not queue:
      print("Queue is empty")
  ```
  
**Note:** Empty lists, empty strings, and the integer `0` are all falsy, so you can use conditions like:
```python
if not demo_list:
    print("List is empty")
```

---

## Tuples

**Definition:**  
Tuples are immutable, ordered collections. They are read-only lists, useful when you want to ensure data cannot be modified.

- **Creation:**  
  ```python
  t = (1, 2, 3)
  t2 = tuple([4, 5, 6])
  ```
- **Operations:**  
  - Concatenation: `t + t2`
  - Repetition: `t * 3`
  - Existence check: `if item in t: ...`
- **Usage:**  
  Tuples are often used for fixed data, to ensure integrity and for performance in loops or as dictionary keys.

#### Swapping Variables
```python
x, y = y, x
```
This unpacks a tuple for swapping without a temporary variable.

---

## Sets

**Definition:**  
Sets are unordered collections of unique elements. They are efficient for membership tests and mathematical set operations.

- **Creation:**  
  ```python
  s = {1, 2, 3, 3}  # Duplicate '3' is ignored
  ```
- **Operations:**  
  - Membership: `if 2 in s: ...`
  - Add/Remove elements:  
    ```python
    s.add(4)
    s.remove(1)  # Raises KeyError if not found
    ```
  - Length: `len(s)`
- **Set Operations:**  
  - **Intersection:** `s1 & s2` or `s1.intersection(s2)`
  - **Union:** `s1 | s2` or `s1.union(s2)`
  - **Difference:** `s1 - s2`
  - **Symmetric Difference:** `s1 ^ s2`
- **Applications:**  
  Duplicates removal, membership testing, and solving problems in competitive programming (DSA).

---

## Dictionaries

**Definition:**  
Dictionaries are key-value pairs, analogous to JSON objects. They offer fast lookups and are a core data structure in Python.

- **Creation:**  
  ```python
  d = {'name': "Alice", 'age': 25}
  ```
- **Access & Update:**
  ```python
  if 'name' in d:
      print(d['name'])
  # Or safely using:
  print(d.get('name', "Unknown"))
  ```
- **Iteration:**
  ```python
  for key, value in d.items():
      print(key, value)
  ```
- **Dictionary Comprehensions:**  
  ```python
  squares = {x: x ** 2 for x in range(5)}
  ```

---

## Generator Expressions

**Definition:**  
Generators are memory-efficient iterables that yield items one at a time rather than storing the entire sequence in memory.

- **Creation:**
  ```python
  from sys import getsizeof
  values = (x ** 2 for x in range(1000))
  print(getsizeof(values))  # Very small size, independent of 1000 elements
  ```
- **Usage Note:**  
  Length (`len()`) cannot be used because generators do not store values; iterate to process or convert to a list if needed.

---

## Unpacking Operators

- **For Iterables:**  
  Use a single asterisk (`*`) to unpack any iterable.
  ```python
  values = [*range(5), *"Hello"]
  # Results in a list with elements from range and each character from "Hello"
  ```

- **For Dictionaries:**  
  Use double asterisks (`**`) to unpack dictionaries.
  ```python
  d1 = {'a': 1, 'b': 2}
  d2 = {'c': 3}
  merged = {**d1, **d2}
  ```

---