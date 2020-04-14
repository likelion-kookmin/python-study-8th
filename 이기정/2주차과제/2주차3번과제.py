l=int(input())
for i in range(l):
    for j in range(l-i-1): print(" ",end=" ")
    for j in range(i*2+1): 
        if j==i*2 : print("*")
        else : print("*",end=" ")

for i in range(l-1,0,-1):
    for j in range(l-i): print(" ",end=" ")
    for j in range(i*2-1): 
        if j==i*2-2 : print("*")
        else : print("*",end=" ")