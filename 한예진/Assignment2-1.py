# 과제1-별찍기(피라미드 모양)
x=int(input("번호를 입력하세요: "))
for j in range(1,x+1):
    for i in range(x+1-j):
        print(" ",end="")
    for i in range(2*j-1):
        print("*",end="")
    print()