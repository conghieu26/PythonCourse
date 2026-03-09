# Python calculator

opertator = input("Enter an operator (+ - * /): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if opertator == "+":
    result = num1 + num2
    print(round(result, 3))
elif opertator == "-":
    result = num1 - num2
    print(round(result, 3))
elif opertator == "*":
    result = num1 * num2
    print(round(result, 3))
elif opertator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{opertator} is not a valid operator")