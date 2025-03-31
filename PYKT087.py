mod = int(1e9 + 7)
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    bit = []
    while k > 0:
        bit.append(k % 2)
        k //= 2
    res = 0
    for i in range(len(bit)):
        if bit[i] == 1:
            res = (res + n ** i) % mod
    print(res)