t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    k = []
    for i in range(3):
        k.append(list(map(int, input().split())))
    res = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            sum = 0
            for z in range(3):
                for o in range(3):
                   sum += k[z][o] * a[i - 1 + z][j - 1 + o]
            res += sum
    print(res)
