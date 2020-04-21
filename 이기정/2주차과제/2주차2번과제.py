l=int(input())
for i in range(l,0,-1):
    for j in range(l-i): print(" ",end=" ")
    for j in range(i*2-1): 
        if j==i*2-2 : print("*")
        else : print("*",end=" ")