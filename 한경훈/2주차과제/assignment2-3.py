num=input()
num=int(num)
for i in range(1,num+1):
    for j in range(1,num-i+1):
        print(' ',end='')
    for j in range(1,i+1):
        print('*',end ='')
    if i != 1:
        for j in range(1,i):
            print('*',end='')
    print(' ')

for i in range(1,num+1):
    for j in range(1,i+1):
        print(' ',end='')
    for j in range(1,num-i+1):
        print('*',end='')
    if i != num:
        for j in range(1,num-i):
            print('*', end='')
    print('')
