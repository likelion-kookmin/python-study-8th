def calculator(num1, 기호, num2):
    if 기호 == "+" :
        return num1 + num2
    if 기호 == "-" :
        return num1 - num2
    if 기호 == "*" :
        return num1 * num2
    if 기호 == "/" :
        return num1 / num2
    if 기호 == "**" :
        return num1 ** num2
    if 기호 == "//" :
        return num1 // num2   
    if 기호 == "%" :
        return num1 % num2


a = int(input("첫 번째 숫자 > "))
b = input("사칙연산 기호 > ")
c = int(input("두 번째 숫자 > "))
print(calculator(a,b,c))