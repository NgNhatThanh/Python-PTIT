n = int(input())
b = [list(map(int, input().split())) for i in range(n)]
if n == 2:
    print(0, n, sep = ' ')
else:
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += b[i][j]
    sum //= 2 * (n - 1)
    for i in range(n):
        tmp = 0
        for j in range(n):
            tmp += b[i][j]
        print(str((tmp - sum) // (n - 2)), end = ' ')