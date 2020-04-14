l=int(input())
for i in range(l):
    for j in range(l-i-1): print(" ",end=" ")
    for j in range(i*2+1): 
        if j==i*2 : print("*")
        else : print("*",end=" ")