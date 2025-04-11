# --- Basic Function ---
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")


# --- Task vs Value Returning ---
def log_user(user_id):
    print(f"Logging in user {user_id}")
    return 0  # task only


def add(x, y):
    return x + y  # returns value


print("Add:", add(5, 3))


# --- Positional vs Keyword Args ---
def register(name, age, city):
    print(f"{name}, {age}, from {city}")


register("Alice", 25, "Zurich")
register(age=30, name="Bob", city="Berlin")


# --- Optional Parameters (Defaults) ---
def greet_with_title(name, title="Ms."):
    print(f"Hello, {title} {name}")


greet_with_title("Claire")
greet_with_title("David", title="Dr.")


# --- *args (Variable Positional Arguments) ---
def multiply(*numbers):
    result = 1
    for n in numbers:
        result *= n
    return result


print("Product:", multiply(2, 3, 4))  # 24


# --- **kwargs (Variable Keyword Arguments) ---
def save_user(**user):
    print("Saved:", user)


save_user(id=1, name="Alice", active=True)


# --- Combining all types ---
def demo(a, b=2, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)


demo(1, 5, 10, 20, x=99, y=100)

# --- Scope Example ---
x = 10


def update():
    global x
    x += 5


update()
print("Global x:", x)


# --- Invalid Scope (Accessing Local Outside) ---
def local_scope_demo():
    y = 42


local_scope_demo()
# print(y)  # Uncommenting this will raise: NameError


# --- Ternary Usage Inside a Function ---
def is_eligible(age):
    return "Eligible" if age >= 18 else "Ineligible"


print("Age 20:", is_eligible(20))
print("Age 15:", is_eligible(15))