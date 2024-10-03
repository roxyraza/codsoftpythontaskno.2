def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    print("Welcome to the Simple Calculator!")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter the operation number (1/2/3/4): ")

    if choice == '1':
        result = add(num1, num2)
        operation = "Addition"
    elif choice == '2':
        result = subtract(num1, num2)
        operation = "Subtraction"
    elif choice == '3':
        result = multiply(num1, num2)
        operation = "Multiplication"
    elif choice == '4':
        result = divide(num1, num2)
        operation = "Division"
    else:
        result = "Invalid operation chosen."
        operation = ""

    if operation:
        print(f"\n{operation} of {num1} and {num2} = {result}")
    else:
        print(result)

if __name__ == "__main__":
    main()
