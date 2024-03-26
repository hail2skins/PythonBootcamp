# Calculator

# Import logo from art.py
from art import logo
print(logo)

# Addition function
def add(n1, n2):
    return n1 + n2

# Subtraction function
def subtract(n1, n2):
    return n1 - n2

# Multiplication function
def multiply(n1, n2):
    return n1 * n2

# Division function
def divide(n1, n2):
    return n1 / n2

# Operations dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Calculator function
def calculator():
    print(logo)

    num1 = float(input("+"))
    for symbol in operations:
      print(symbol)
    should_continue = True
 
    while should_continue:
      operation_symbol = input("Pick an operation: ")
      num2 = float(input("What's the next number?: "))
      calculation_function = operations[operation_symbol]
      answer = calculation_function(num1, num2)
      print(f"{num1} {operation_symbol} {num2} = {answer}")

      if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
        num1 = answer
      else:
        should_continue = False
        #clear the console
        print("\033[H\033[J")
        calculator()

calculator()