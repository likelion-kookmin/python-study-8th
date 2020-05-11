def calculator(num1,num2,a) : 
    if a == '+' : print(num1+num2)
    elif a == '-' : print(num1-num2)
    elif a == '*' : print(num1*num2)
    else : print('error')

num1 = int(input())
num2 = int(input())
mod = input()
calculator(num1,num2,mod)



