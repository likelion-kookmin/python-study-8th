# Assignment 3-1

def calculator (val1, val2, opt):
    if opt == '+':
        return val1 + val2
    elif opt == '-':
        return val1 - val2
    elif opt == '*':
        return val1 * val2
    elif opt == '/':
        return val1 / val2
    elif opt == '//':
        return val1 // val2
    elif opt == '%':
        return val1 % val2
    elif opt == '**':
        return val1 ** val2
    else:
        print("다시 입력해주세요.")
        quit()

user_input = list(map(str, input().split(" ")))
print(calculator(int(user_input[0]), int(user_input[1]), user_input[2]))