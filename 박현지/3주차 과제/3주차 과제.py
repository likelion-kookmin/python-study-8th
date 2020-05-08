def calculate (a, b, c):
    if c == '+':
        return a + b
    elif c == '-': 
        return a - b 
    elif c == '%': 
        return a % b 
    elif c == '곱하기': 
        return a * b
    else:
        print(input("다시입력해주세요"))

a = int(input("숫자를 입력하세요: "))
b = int(input("숫자를 입력하세요: "))
c = input('사칙연산을 입력해주세요: ')

print(calculate(a, b, c))
