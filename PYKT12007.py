t = int(input())
for _ in range(t):
    n = int(input())
    u = float(input())
    lst = list(map(float, input().split()))
    mp = {}
    for x in lst:
        mp[x] = mp.get(x, 0) + 1
    mp = [[x, mp[x]] for x in sorted(mp)]
    while len(mp) > 1:
        d = mp[1][0] - mp[0][0]
        if u >= mp[0][1] * d:
            u -= mp[0][1] * d
            mp[1][1] += mp[0][1]
            mp.pop(0)
        else:
            break
    mp[0][0] += u / mp[0][1]
    res = 1
    for x in mp:
        res *= x[0] ** x[1]
    print(f'{min(1, res):.6f}')