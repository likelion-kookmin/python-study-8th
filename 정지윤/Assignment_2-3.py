n = int(input(''))

for i in range(2*n):
    if n>i :
        print(" "*(abs(n-i-1)) + "*"*(2*i+1))
    elif n==i:
        continue
    else :
        print(" "*(abs(n-i-1)-1)+"*"*(2*(n+(n-i))-1))