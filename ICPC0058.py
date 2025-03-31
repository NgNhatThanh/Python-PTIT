ke = [[] for i in range(101)]
cnt = [0] * 101
trace = [0] * 101
vst = [0] * 101
pathCount = 0

def dfs(u, en):
    vst[u] = 1
    if u == en:
        global pathCount
        pathCount += 1
        while trace[u] != 0:
            cnt[u] += 1
            u = trace[u]
        return
    for ver in ke[u]:
        if vst[ver] == 0:
            trace[ver] = u
            dfs(ver, en)
            vst[ver] = 0

t = int(input())
for _ in range(t):
    n, m, u, v = list(map(int, input().split()))
    for i in range(m):
        x, y = list(map(int, input().split()))
        ke[x].append(y)
    dfs(u, v)
    res = 0
    for i in range(1, n + 1):
        if i != u and i != v and cnt[i] == pathCount:
            res += 1
        ke[i].clear()
        cnt[i] = 0
        trace[i] = 0
        vst[i] = 0
    pathCount = 0
    print(res)

