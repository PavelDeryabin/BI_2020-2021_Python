print("Hello! This is a simple calculator")
print("Please, provide two numbers and one needed operation from the following: +, -, *, /")

number1 = float(input("Enter first number: "))
operation = input("Indicate operation (+, -, *, /): ")
number2 = float(input("Enter second number: "))

if operation == "+":
    print("Result: ", number1 + number2)
elif operation == "-":
    print("Result: ", number1 - number2)
elif operation == "*":
    print("Result: ", number1 * number2)
elif operation == "/":
    print("Result: ", number1 / number2)
else:
    print("Result:", "Indicated operation isn\'t valid, try again")
