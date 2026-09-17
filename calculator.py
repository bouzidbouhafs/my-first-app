# calculator.py - my first real project

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero!"
    return a / b

if __name__ == "__main__":
    print("=== My Calculator ===")
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", subtract(5, 2))
    print("4 * 3 =", multiply(4, 3))
    print("10 / 2 =", divide(10, 2))

    # interactive part
    try:
        x = float(input("Enter first number: "))
        op = input("Enter operation (+ - * /): ")
        y = float(input("Enter second number: "))
        if op == "+":
            print("Result:", add(x, y))
        elif op == "-":
            print("Result:", subtract(x, y))
        elif op == "*":
            print("Result:", multiply(x, y))
        elif op == "/":
            print("Result:", divide(x, y))
        else:
            print("Unknown operation!")
    except ValueError:
        print("Please enter valid numbers!")
