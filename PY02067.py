n = int(input())
lst = list(map(int, input().split()))
res = 10000000000
for i in range(1, lst[0] + 1):
    sum = 0
    ok = 1
    for j in range(n):
        k = lst[j] // (i + 1) + 1
        if lst[j] // k != i:
            ok = 0
            break
        sum += k
    if ok == 1:
        res = min(res, sum)
print(res)
