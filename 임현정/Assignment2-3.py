num = int(input('별 개수 커몬  '))
for i in range(2*num-1):
    if i+1 <= 5:
        print(' '*(5-i),'*'*(2*(i+1)-1))
    else:
        a = 2*(10-(i+1))-1
        print(' '*(i-3),'*'*a)
        a -= 2