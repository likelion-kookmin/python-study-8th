N = int(input("N :"))
for i in range(N, 0,-1):
     for j in range(1,N+1-i):
         print(" ", end='')
     for k in range(2*i-1):
         print("*", end='' )
     print()
