#Python Calculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    if num2 == 0:
        print("Invalid!!!,Denominator can't be zero")
    else:
        result = num1 / num2
        print(result)
else:
    print("Invalid Operator,Try again")

"""
Additionally,
print(round(result))       # Round off to nearest decimal

print(round(result, 3))    # Upto 3 decimal places after answer if its there eg. 77.342

"""