# Quest 26 - Simple Calculator
# Each math operation is its own function so the code is organized and reusable.

# Adds two numbers and returns the result
def add(a, b):
    return a + b

# Subtracts the second number from the first
def subtract(a, b):
    return a - b

# Multiplies two numbers together
def multiply(a, b):
    return a * b

# Divides the first number by the second
def divide(a, b):
    # Guard against dividing by zero, which would crash the program
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b

print("Simple Calculator")

# float() lets the calculator handle decimals, not just whole numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask which operation the user wants to perform
operation = input("Choose an operation (add, subtract, multiply, divide): ")

# The if-elif-else chain checks the choice and calls the matching function
if operation == "add":
    print(f"Result: {add(num1, num2)}")
elif operation == "subtract":
    print(f"Result: {subtract(num1, num2)}")
elif operation == "multiply":
    print(f"Result: {multiply(num1, num2)}")
elif operation == "divide":
    print(f"Result: {divide(num1, num2)}")
else:
    # Runs if the user typed something that isn't a valid operation
    print("Unknown operation. Please choose add, subtract, multiply, or divide.")
