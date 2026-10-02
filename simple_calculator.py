# [simple_calculator.py]
# Author: [Obaid ur Rahman]
# Date: [29/09/2026]
# Description: [The script will take two numbers from user, ask him/her to select an operator and then print the output for the specific operation. It will also handle the wrong input and also handle the division by zero error.]

first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    result = first + second
elif operator == "-":
    result = first - second
elif operator == "*":
    result = first * second
elif operator == "/":
    if second != 0:
        result = first / second
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operator"

print(first, operator, second, "=", result)
