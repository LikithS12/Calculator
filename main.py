#Functions that have different math operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

#Print statement that allows a user 
print("Select operation:")
print("Add")
print("Subtract")
print("Multiply")
print("Divide")
print(" ")

while True:
    # Take input from the user
    choice = input("Enter choice (add/subtract/multiply/divide): ").lower()

    if choice in ('add', 'subtract', 'multiply', 'divide'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 'add':
            print("Result:", add(num1, num2))

        elif choice == 'subtract':
            print("Result:", subtract(num1, num2))

        elif choice == 'multiply':
            print("Result:", multiply(num1, num2))

        elif choice == 'divide':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid Input")

    # Check if the user wants to perform another calculation
    next_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
        print("come back later!")
        break
