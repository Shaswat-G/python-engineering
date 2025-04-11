Functions:
expand on why we create functions in programming - reusability, clean, not-repreatingthe same thing, abstracting out complexity, readability, etc and so much mroe.

The same naming conventions apply to functions and that apply to variable names - meaningful, descriptive, oower case and underscores.
def function_name():

Arguments vs params:
Parameters are the inputs you define for your functions. Arguments are the values with which you call the function with.

Function types:

1. EIther perform a task. Return 0 for successful execution or error message if not. WIhtout a return statement, all functions return a None.
2. Or Return a value.

While callsing a function with multiple arguments, you have to floow the positional arguments. If not, ues keyword arguments - prefix the argument witht eh input paramter name.
[expand on this with examples]

Optional Parameters:
You can give a default value to paramters, then even if you dont pass it implicityly or explicityly it will use its default value defined in the functipn defiinotion.
ALso, all of the oprtional parameters as a rule have to come after the required arguments. No reqiored argument can come after aan optioanl argument in the funciton def.
[expand on this with examples]

\*args:
lets say we are defining a multiply function with a variable set of parameters that are all multiplied.

def multiply(\*numbers):
this actually defines a iterable tuple.
for number in numbers:
do something
return some

def save_user(**user)
we can pass arbitrary keyword arguments with this.
This is actually a dictionary.
[Expand by commbining both \*args, **args and differnt ways of defining and calling paramters]

Scope:
All parameter variables and variables inside are function are entirely inaccessible by anyone else, these are local vairables can only be accessed or referenced withing the scoep of the function. Global vairables can be accessed from anywhere, as a best bractive never use gloabl variables.

We can use the gloabl keyword to modify global variables inside of a function. We usually avoid it [give an example]

Debugging:
pNavigate to a project elevl clas or function using ctrl + shit + o or use vtrl + nT for local hierarchy navigatin in the file.
search for a function or symbol. Press f12 to reach its defiintoin. press ctrl + g to reach a particular line.
start debuggin with ctrl shift D, select python debugger.
set break points using f9, run till breakpoint with f5, run the next line with f10, step into a function with f11 and then keep doing f10 and inspecting the vairables.
You dont have to execute the function line by line you can always exit a dunction using shift+f11.

