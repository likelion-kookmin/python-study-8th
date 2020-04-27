def calculator(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    elif op == '%':
        return num1 % num2
    else:
        print("다시 입력해 주세요")

    
num1 = int(input("첫 번째 숫자를 입력해 주세요: "))
num2 = int(input("두 번째 숫자를 입력해 주세요: "))
op = input("사칙연산을 입력해 주세요(예시: +, -, *, /, %): ")

print("결과값: " + calculator(num1, num2, op))