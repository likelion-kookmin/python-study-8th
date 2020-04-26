def calculator(num1, num2, op):
    if op == '+':
        return num1 + num2

    elif op == '-':
        return num1 - num2

    elif op == '*':
        return num1 * num2

    elif op == '/':
        if num2 == 0 :
            print("0으로 나눌 수 없습니다!")
            return None
        else :
            return num1 / num2

    elif op == '//':
        return num1 // nun2
    
    elif op == '%':
        return num1 % num2
    
    elif op == '**':
        return num1 ** num2

    else:
        print("{} : 지원되지 않는 연산자".format(op))


if __name__ == '__main__':
    cmd = input("입력: ").split()
    n1, n2 = map(int, cmd[:2])
    op = cmd[2]
    
    print("출력: {}".format(calculator(n1, n2, op)))