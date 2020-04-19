n = int(input("n:"))
for i in range(n//2,-1,-1):
    print(' '*i + '*'*(n -2*i))
for i in range(1, n//2 +1):
    print(' '*i + '*'*(n -2*i))
