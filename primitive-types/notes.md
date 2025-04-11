Variables are used to assign values to names that can be accessed in the program
they aer stored in moemory locations (program stack) [give a brief intro to prgram stack, direction of push pop, memory addresses, and parts of the stack, memories etc]


Primktive types:
Built in types
Boolean - True, Flase, 
integer, float (give the byte size also)
string = "AELKFJLFKJ"

Type conversion
Expand on this section.
int(), float(), str(), bool()
empty strings are flasy, 0 is falsy. None is flasy everything else is true. Eg: bool("False") will be true.

Variable names:
Descriptiv and meaningful. We want elegance and readability.
Lower case - no camel case, no upper case.
underscore to separate words in a variable name.
Space across assignments.
We want clean code that is beatiful, Ill formatted and badly designed code is smelly.


Strings:
Double and single quotes work.
Triple quotes for doc strings and huge strings.
Strings are 0-indexed.
Negative INdices are from the back.
Slicing - first 3 charactes : list[0:3] the last index is not includeded.
Escape Characters using backslash. (\\, \n etc)
Concatenation with +. (We use format strings much moremodern. curly braces in f"{expression}")
String methods: [expand on all the functions, and give a very short example for each]
len
.isdigit
.islower
.isnumeric
.lower
.upper
.title
.strip
.rstrip
.lstrip
.startswith
.endswith
.find
.replace
.format
.zfill
.split
can use "in" to check for existence of a substring.
.count('character or substring')


Numbers:
int and float.
we use j for complex numbers.
All standard operations supported. +, -, *, /, // (integer division), % (modulus), ** (exponent)
x += 3
y *= 3
round()
abs()
USe math module which includes functionalities built on top of promitive types allowing you for scientific calculations.
import math
[Expand on all the useful funcitons in the math modeule]
ceil, floor, log, degrees, radians, cos, atan, dist, factorial, gcd, sqrt and many many more

Built-in Function primitives:
len(string)
print()
type() 
