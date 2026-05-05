"""
Basic Calculator Application
A simple command-line calculator that performs basic arithmetic operations.
"""

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def calculator():
    """Main calculator loop"""
    print("\n" + "="*40)
    print("Welcome to BasicCal - Simple Calculator")
    print("="*40)
    
    while True:
        try:
            # Get user input
            print("\nOperations:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")
            
            choice = input("\nEnter operation (1/2/3/4/5): ").strip()
            
            if choice == '5':
                print("Thank you for using BasicCal! Goodbye!")
                break
            
            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
                continue
            
            # Get numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Perform operation
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"
            
            # Display result
            print(f"\n{num1} {operation} {num2} = {result}")
        
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculator()
