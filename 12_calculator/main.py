from replit import clear
from art import logo

# Mathematical operations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Cannot divide by zero"

# Dictionary mapping symbols to corresponding functions
operations ={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Calculator function
def calculator():
    print(logo)

    # Get the first number from the user
    num1 = float(input("What's the first number?: "))

    # Display available operations
    for symbol in operations:
        print(symbol)

    should_continue = True
    
    while should_continue: 
        # Get the operation symbol from the user
        operation_symbol = input("Pick an operation: ")

        # Get the second number from the user
        num2 = float(input("What's the next number?: "))

        # Check if the operation symbol is valid
        if operation_symbol in operations:
            # Get the corresponding function for the chosen operation
            calculation_function = operations[operation_symbol]

            # Perform the calculation
            answer = calculation_function(num1, num2)

            # Display the result
            print(f"{num1} {operation_symbol} {num2} = {answer}")

            # Check if the user wants to continue with the result or start a new calculation
            if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower() == 'y':
                num1 = answer
            else:
                should_continue = False
                clear()
                calculator()
        else:
            print("Invalid operation. Please choose a valid operator.")

# Start the calculator
calculator()
