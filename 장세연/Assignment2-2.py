n= int(input("원하는 층 수를 입력하세요:"))

for i in range(n) :
    print(" "*(n+i)+"*"*(2*(n-i)-1))