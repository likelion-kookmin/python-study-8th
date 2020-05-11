def calculator(num1, num2, cal):
    if cal == "+" :
        return num1 + num2
    elif cal == "-":
        return num1 - num2
    elif cal == "/":
        return num1 / num2
    elif cal == "*":
        return num1 * num2

num1 = int(input("숫자1 :"))
num2 = int(input("숫자2 :"))
cal = input("사칙연산 :")
print(calculator(num1, num2, cal))
