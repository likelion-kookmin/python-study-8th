num=input()
num=int(num)
for i in range(1,num+1):
    for j in range(1,i):
        print(' ',end='')
    for j in range(1,num-i+2):
        print('*',end='')
    if i != num:
        for j in range(1,num-i+1):
            print('*', end='')
    print('')