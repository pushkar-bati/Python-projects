import math

todo = input("Enter the operation: ").lower()

# Zero-number operations
if todo == "pi":
    print("Result:", math.pi)

elif todo == "e":
    print("Result:", math.e)

# One-number operations
elif todo in ("sqrt", "square", "cube", "factorial"):

    num1 = float(input("Enter the number: "))

    if todo == "sqrt":
        if num1 >= 0:
            print("Result:", math.sqrt(num1))
        else:
            print("Error: Square root requires a non-negative number")

    elif todo == "square":
        print("Result:", num1 ** 2)

    elif todo == "cube":
        print("Result:", num1 ** 3)

    elif todo == "factorial":
        if num1 >= 0 and num1.is_integer():
            num = int(num1)
            print("Result:", math.factorial(num))
        else:
            print("Error: Factorial requires a non-negative integer")

# Two-number operations
else:

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if todo == "+":
        print("Result:", num1 + num2)

    elif todo == "-":
        print("Result:", num1 - num2)

    elif todo == "*":
        print("Result:", num1 * num2)

    elif todo == "/":
        try:
            print("Result:", num1 / num2)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero")

    elif todo == "%":
        try:
            print("Result:", num1 % num2)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero")

    elif todo == "**":
        print("Result:", num1 ** num2)

    elif todo == "//":
        try:
            print("Result:", num1 // num2)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero")

    else:
        print("Error: Invalid operation")