# Define functions for basic calculator operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# User interface for the calculator
def calculator():
    print("Welcome to the Simple Calculator!")
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '5':
            print("Exiting the calculator. Have a great day!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid input. Please try again.")
            continue
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"The result of addition is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result of subtraction is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result of multiplication is: {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            if result == "Cannot divide by zero":
                print(result)
            else:
                print(f"The result of division is: {result}")

# Run the calculator
calculator()