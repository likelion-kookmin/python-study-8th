N = int(input("N :"))
 
for i in range(N):
     for j in range(N-1-i):
         print(" ", end='')
     for k in range(2*i+1):
         print("*", end='' )
     print()
