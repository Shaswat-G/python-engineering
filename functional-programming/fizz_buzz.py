def fizz_buzz(input):
    if input % 15 == 0:
        print("FizzBuzz")
    elif input % 3 == 0:
        print("Fizz")
    elif input % 5 == 0:
        print("Buzz")
    else:
        print(input)
    return 0    
    
fizz_buzz(int(input("Enter a number: ")))