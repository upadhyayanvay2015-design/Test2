from secrets import choice


def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a/b
("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplicaprinttion")
print("4. Division")
choice = input("Enter choice (1/2/3/4): ")
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

try:
    if choice == '1':
        result = addition(a, b)
    elif choice == '2':
        result = subtraction(a, b)
    elif choice == '3':
        result = multiplication(a, b)
    elif choice == '4':
        result = division(a, b)
    else:
        print("Invalid choice. Please enter a valid operation.")
        exit()
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")