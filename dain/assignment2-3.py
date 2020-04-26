N=int(input())
if 1<=N<=100:
    for i in range(1, N):
        print(" "*abs(N-i)+"*"*abs(2*i-1))
    for i in range(1,N+1):
        print(" "*abs(i-1)+"*"*abs(2*N-(2*i-1)))
      
