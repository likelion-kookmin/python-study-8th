a = int(input("input number:"))
for i in range(1, a+1):
    print(' ' * (a -i), end ='')
    print('*' * (2*i-1))