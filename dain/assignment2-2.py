N=int(input())
if(1<=N<=100):
    for i in range(0, N):
        print(" "*i+"*"*(2*N-2*i-1))