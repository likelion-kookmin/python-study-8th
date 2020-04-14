# Baekjoon 2422

N = int(input())

# solution 1
for i in range(N) :
    for j in range(N-i-1) :
        print(' ', end='')

    for j in range(2 * (i+1) - 1) :
        print('*', end='')

    print()

# # solution2
# for i in range(N) :
#     print(' ' * (N-i-1), \
#           '*' * (2 *(i+1) - 1), sep='')