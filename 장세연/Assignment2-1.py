n = int(input("원하는 층 수를 입력하세요:"))

for i in range(1, n+1):
    print(" "*(n-i), "*"*(2*i-1))