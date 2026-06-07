a = int(input("ENTER FIRST NUMBER: "))
b = int(input("ENTER SECOND NUMBER: "))

operator = input("Enter operator (+,-,*,/,%,): ")

if operator == "+":
    print("result =", a + b)
elif operator == "-":
    print("result =", a - b)
elif operator == "*":
    print("result =", a * b)
elif operator == "/":
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("result =", a / b)
elif operator == "%":
    print("result =", a % b)
else:
    print("invalid operator")