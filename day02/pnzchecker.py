#positive, negative and zero number checker
user_number = int(input("Welcome to the number check, give me a number and I'll tell you if it is positive, negative or zero: "))

if user_number > 0:
    print(f"{user_number} is a positive number!")
elif user_number < 0:
    print(f"{user_number} is a negative number!")
else:
    print("You chose 0, that sort of speaks for itself, doesn't it?")