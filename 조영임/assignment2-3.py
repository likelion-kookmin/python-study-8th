space=5
for i in range(1,10,2):
    space-=1 #space=space-1
    print(' '*space+i*'*')

space=0
for i in range(7,0,-2):
    space+=1

    print(space*' '+i*'*')