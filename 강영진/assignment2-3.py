a = int(input("input number:"))
for i in range(a//2, -1, -1):
    print(' '*i + '*'*(a - 2*i))
for i in range(1, a//2 + 1):
    print(' '*i + '*'*(a - 2*i))