x = input("Enter a number: ")
try:
    x = int(x)
    print(f"Your number is {x}")
    exit(1)
except ValueError:
    print("That's not a number!")
    exit(-1)