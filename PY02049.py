t = int(input())
for _ in range(t):
    n, p = list(map(int, input().split()))
    res = 0
    k = p
    while n / k > 0:
        res += n // k
        k *= p
    print(res)