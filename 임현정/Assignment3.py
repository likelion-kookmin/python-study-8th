def calculator(num1, num2, oper):
    num1 = int(num1)
    num2 = int(num2)
    if oper=="+":
        return num1+num2
    elif oper=="-":
        return num1-num2
    elif oper=="*": 
        return num1*num2
    elif oper=="/":
        return num1/num2
    else:
        return "Error"

number1, operation, number2 = list(input("식을 입력해주세요: "))
print(calculator(number1,number2,operation))