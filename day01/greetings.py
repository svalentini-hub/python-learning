#greeting script
name = input("Hello, what is your name? ")

age = int(input("How old are you? "))
#had to use int to convert the answer(a string) to an int(integer=number)
age_future = age + 10

print(f"Hello {name}, you will be {age_future} in 10 years")