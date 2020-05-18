def calculator (num1,num2,op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1-num2
    elif op == "/":
        return num1/num2
    elif op == "*":
        return num1*num2


num1,num2,op=input("num1,num2,연산자를 입력해주세요: ").split()
num1=int(num1)
num2=int(num2)
print(num1,op,num2)


print(calculator(num1,num2,op))
 