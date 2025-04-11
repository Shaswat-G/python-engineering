comaprision operators
give examples with numbers and strings and some tricky sype conversions
>, <, >=, <=, ==, !=


Conditionals:
if alone, if - else, if -elif-else, : Expand on how you need to indent after a block.

Ternary Operator:
message = "Eligible" if age >=18 else "Ineligible"

Logical Operators 
and, or, not
Expand with examples.
They are shortcircuited.
A chain of ands is evaluated in a short circuit (in the same way in bash). The evaluation stops whenreer any argument in a chain of ands is Flase.
Similarly for finding a true in a or chain.

You can also chain operators.
age = "22"
if 18 <=age < 65:
print("Eligible")


Comaprision between strings happens in a sorted lexicgraphical manner. w A greather than is who occues later in a dictionary?

For loops:

Number goes from 0,1,2.
for number in range(3):
    print("something")

range(1,4) - 1,2,3
range(1,10,2) - 1, 3, 5, 7, 9

Can also use nesteed loops.


Iterables:
Range is a built in complex type that returns an interable.

Strings are also iterable:
for x in "Python"
print(x)

Similarly for lists and tuples. We will understand how to make iterable complex objects in classes later.

while loop.
WHile (some condition):
do something.


Infinite loops:
while(True):
do something with a break condition.

