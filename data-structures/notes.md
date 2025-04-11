## List
Mutable colleciton of any type of objects. Its an iterbale, allows for duplicates, slicign, indexing, composing and many things.

[1]*100 to create a list with 100 ones. USe plus for concatenation. You can use .append and .extend
demo_list = [1]*10 + [0]*10
print(demo_list)
demo_list = [1] * 10 + [0] * 10
print(demo_list)

You can also pass any iterabel and convert it to a list.
list(range(20))
list("ANy string")
use len for length.


Operations on list:
Expand on Indexing (special steps also [::2] for every other element, [::-1] for reverse order), slicing, copying (.copy)
Unpacking:

first, second, *others = [1,2,4,4,4,4,4,4,6]
first, *others, last = [1,2,4,4,4,4,4,4,6]

Looping over list:
for x in list:
iterate.

for idx, value in enumerate(list):

This is tuple unpacked into idx and balues. enumerate generates a iteratble tuples of loop index and values.


demo_list.append(1)
print(demo_list)

new_list = [3, 4, 5]
demo_list.extend(new_list)
print(demo_list)

demo_list.pop(-2)
print(demo_list)

For sorting. We can set reverse=True.
demo_list.sort()
print(demo_list)
You can also use a predefined function called sorted() that sorts any iterable. It also accpts the recerse kwarg.
For lists of complex objects, you have to define a function that takes in one of the items and returns a numerical value.
This fcuntion is passed in the sort and sorted method as an argument (as a reference) and the list is sorted in the order of the numerical value.

demo_list.reverse()
print(demo_list)

demo_list.remove(1)
print(demo_list)
Only removes the first occurence.

demo_list.insert(-2, 42)
print(demo_list)

demo_list.clear()
print(demo_list)

del demo_list[0:3]

demo_list.index("object in the list") returns its index.
demo_list.count("item") returns the number of occurences.

[expand on other useful list methods with examples and short descriptions.]


Lambda functions are name-less (anonymous) one-liner functions that we can pass to other functions.
Eg: list.sort(key = lambda <paramters>:<expression>)

The map function.
The map function applies a function on each item in an titerable. SO it takes two arguments, first the funciton ,second the iterable.
and then it returns an iterable map object.

Eg: y=  map(lambda x:x[1], items)
print(list(y))

items = [
    ("P1", 10),
    ("P2", 4),
    ("P3",23),
    ("P4", 12),
    ("P5", 54),
    ("P6", 47),
    ("P7", 3),
    ("P8", 97),
    ("P9", 96),
    ("P10", 43)
]

filtered_items = filter(lambda x: x[1] > 20, items)
sorted_items = sorted(filtered_items, key=lambda x: x[1], reverse=True)
mapped_items = map(lambda x: (x[0], x[1] * 2), sorted_items)
print(list(mapped_items))

List comprehensions:
[item[1] for item in items if item[1]>20]
This is more readable, recommended to use over map and filter.

Zip function:
Combined multiple iterables (of any objects, any type but of same length) into a tuple based iterable.

another_list = [1, 2, 4, 5, 1, 5, 3, 2, 9, 10]
print(list(zip(items, another_list)))

Stacks:
LIFO based push and pop. USed for undo-redo, back and forward in browser, etc.
This can be implemented using lists with used with append for push and pop for pop. USed for parenthesis checking. [expand on all of the applications in tech, DSA problems and CP questions]

Trick: empty lists, empty strgins, the value 0 are all falsy values. SO you can use
if not an_empty_list: #this evalutats to true ig the lsit is empty.
    do sometheing.


Queues:
FIFO. Used for message queying, operation queying, etc. [expand on all of the applications in tech, DSA problems and CP questions]
from collections import deque
queue = deque([1,2,3]) #wrap an empty list into the deque function to make it a queue.
print(queue)  # print the queue
queue.append(4) #add to the end of the queue
queue.append(5) #add to the end of the queue
queue.append(6) #add to the end of the queue
print(queue) #print the queue
queue.popleft() #remove from the front of the queue
queue.popleft() #remove from the front of the queue
print(queue) #print the queue

if not queue:
    print("Queue is empty")

Tuples: [expand on all of the applications in tech, DSA problems and CP questions]
ZImmutable, read-only type list.
Concatenation with plus.
REpeating with *
tuple(list or any iterable)
if item in tuple (for existence check)
does not suppoort insert, remove, append, etc.


Swapping variables

x, y = y,x 

its basically packing unpacking a tuple for variable swapping without a third vairable.

a, b = 1,2 

Arrays: [expand on all of the applications in tech, DSA problems and CP questions]
Lists can be inefficient for larger streams. As a thumbrule, if you have 10,000 or more elements, use an array, otw list.
from array import array
my_array = array("i", range(1000))
the first argument is called type code which is a code for what type of data you want to store in the array sicne they are of homogenoue linear data strucuture.
They support all of the same functionality of a list.


Sets: [expand on all of the applications in tech, DSA problems and CP questions]
Unique and are unordered -> cannot index.
can check for existence using in.

add, remove, len
intersection, union, subtraction. (union - intersection is done by caret. ^)

Dictionaries: [expand on all of the applications in tech, DSA problems and CP questions]
Very powerful DS : key value pairs -> json objects.

You can check if a key is in a dict and access the element

if key in dict:
use dict[key] in something.

Or you can use the get method.
dict.get("key", None) This is super useful.

Iterating over a dict
for key, value in dict.items():


Dicitonary Compreshensions:
You can have a set comprehension
set = {x**2 for x in range(5)}
Tis is dict comprehension
dict = {x:x**2 for x in range(5)}


Generator expressions:
generator items do not store things in memery but are iterable.
These are much more memory efficient and have the same size irrespective of the length in the generator expression.
Using len wont work it will give an error.

from sys import getsizeof
values = (x**2 for x in range(1000))
print(values)
print(getsizeof(values)) # 112 bytes



Unpacking operator
You just have to unpack by putting a simple asterisk *list.
It can unpack any iterable into a string.

values = [*range(5), *"Hello"]

We can use ** for unpacking a dictionary.








## Tuple
## Set
## Dictionaries