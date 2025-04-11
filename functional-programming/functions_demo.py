def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Main program
number = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {number} is {factorial(number)}")