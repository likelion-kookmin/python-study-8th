def calculator(num1, num2, symbols):
    if symbols == '+':
        return num1 + num2
    elif symbols == '-':
        return num1 - num2
    elif symbols == '*':
        return num1 * num2
    elif symbols == '/':
        return num1 / num2
    elif symbols == '%':
        return num1 % num2
    else:
        print("x")

    
num1 = int(input("num1: "))
num2 = int(input("num2: "))
symbols = input("사칙연산: ")

print(calculator(num1, num2, symbols))