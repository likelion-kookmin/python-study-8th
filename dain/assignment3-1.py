def calculator(num1, num2,a):
    if a=="+":
        return num1+num2
    elif a=="-":
        return num1-num2
    elif a=="*":
        return num1*num2
    elif a=="/":
        return num1/num2

num1=int(input("숫자1을 입력하세요"))
num2=int(input("숫자2를 입력하세요"))
a=input("사칙연산을 입력하세요")
print(calculator(num1,num2,a))