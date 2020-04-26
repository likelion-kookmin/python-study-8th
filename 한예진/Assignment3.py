# 함수를 이용한 단순 계산기 만들기
def calculator(num1, num2, oper):
    if oper=="+":
        return num1+num2
    elif oper=="-":
        return num1-num2
    elif oper=="*": 
        return num1*num2
    elif oper=="/":
        return num1/num2
    else:
        return "계산불가"

number1, number2, operation = input("입력해주세요: ").split()
number1=int(number1)
number2=int(number2)
print(calculator(number1, number2, operation))