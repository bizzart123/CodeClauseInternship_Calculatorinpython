# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main program loop
while True:
    # Display menu
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to exit the program")

    user_choice = input(": ")

    if user_choice == "quit":
        break
    elif user_choice in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_choice == "add":
            print("Result:", add(num1, num2))
        elif user_choice == "subtract":
            print("Result:", subtract(num1, num2))
        elif user_choice == "multiply":
            print("Result:", multiply(num1, num2))
        elif user_choice == "divide":
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input. Please choose a valid operation.")
