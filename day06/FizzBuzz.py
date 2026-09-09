print("Hello and welcome to Fizz Buzz!")

for number in range(1, 51):
    if (number % 5 == 0 and number % 3 == 0):
            print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)