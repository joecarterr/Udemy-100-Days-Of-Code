# welcome:
print("\nWelcome to the Prime Number Checker!\n")


# checking if inputted number is a prime number:
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Your number is a prime number")
    else:
        print("It is not a prime number")


n = int(input("Check this number:\n"))

# call def:
prime_checker(number=n)  # setting user input to max number to go up to in number argument
