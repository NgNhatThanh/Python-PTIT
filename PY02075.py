t = int(input())
for _ in range(t):
    n = int(input())
    lst = [list(map(int, input().split())) for i in range(n)]
    lst.sort(key = lambda x: x[1])
    res = 0
    last = 0
    for p in lst:
        if p[0] >= last:
            res += 1
            last = p[1]
    print(res)