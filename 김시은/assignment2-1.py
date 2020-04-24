a = int(input("줄 수를 입력해주세요: "))

for i in range(1, a+1):
    print(" "*(a-i)+("*"*(2*i-1)))
