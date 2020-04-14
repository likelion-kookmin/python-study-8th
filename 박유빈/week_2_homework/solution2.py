# Baekjoon 2443

N = int(input())

# solution 1
for i in range(N) :
    for j in range(i) :
        print(' ', end='')
    
    for j in range(2 * N - (2 * i + 1)) :
        print('*', end='')
    
    print()

# # solution 2
# for i in range(N) :
#     print(' ' * i, \
#           '*' * (2 * N - (2 * i + 1)), sep='')