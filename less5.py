def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "Invalid operator"


num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operator = input("Введите оператор  (+, -, *, /): ")

result = calculate(num1, num2, operator)

print(f"{num1} {operator} {num2} = {result}")
