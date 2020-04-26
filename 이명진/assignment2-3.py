n = int(input("숫자를 입력하세요:"))
for i in range(n//2,-1,-1):
    print(' '*i + '*'*(n -2*i))
for i in range(1, n//2 +1):
    print(' '*i + '*'*(n -2*i))