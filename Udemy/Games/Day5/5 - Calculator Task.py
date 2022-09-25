from Games.Day5.calculator_art import logo

print(logo)


# add:
def add(n1, n2):
    return n1 + n2


# subtract:
def subtract(n1, n2):
    return n1 - n2


# multiply:
def multiply(n1, n2):
    return n1 * n2


# divide:
def divide(n1, n2):
    return n1 / n2


signs = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    num1 = float(input("What's the number?:\n"))
    for symbol in signs:
        print(symbol)
    restart = False

    while not restart:

        selected_symbol = input("Pick a symbol from the line above:\n")
        num2 = float(input("What's the next number?:\n"))
        calculation_function = signs[selected_symbol]
        answer = float(calculation_function(num1, num2))
        print(f"Your answer is: {answer}")

        selected_symbol = input("\nPick another symbol:\n")
        num3 = int(input("What's the next number?:\n"))
        calculation_function = signs[selected_symbol]
        answer = float(calculation_function(answer, num3))
        print(f"Your answer is: {answer}")
        again = input(f"Type 'y' to continue calculating with {answer} or type 'n' for a new calculation screen:\n").lower()
        if again == "yes" or "y":
            num1 = answer
            restart = False
        elif again == "no" or restart == "n":
            restart = True
            quit()
        else:
            restart = False
            calculator()


calculator()
