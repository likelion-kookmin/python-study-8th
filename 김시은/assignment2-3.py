a = int(input("줄 수를 입력해주세요: "))

for i in range(1, a):
    print(" "*(a-i)+("*"*(2*i-1)))
for i in range(a-1, -1, -1):
    print(" "*(a-i-1)+("*"*(2*i+1)))
