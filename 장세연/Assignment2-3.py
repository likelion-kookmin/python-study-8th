n = int(input("원하는 층 수를 입력하세요 : "))
n2 = int(n/2) +1
for i in range(1,2*n):
    if i <= n :
        for j in range(n - i):
            print(" ", end="")
        for j in range(2*i-1):
            print("*",end="")
        print()
    else:
        for j in range(i-n):
            print(" ",end="")
        for j in range((2*n-i)*2-1):
            print("*",end="")
        print()