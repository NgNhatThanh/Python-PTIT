from collections import deque

n = int(input())
ke = [[] for i in range(200001)]
d = [0] * (200001)
id = 1
mp = {}
for i in range(n):
    s = input()
    a, dau, b = s.split()
    if mp.get(a, 0) == 0:
        mp[a] = id
        id += 1
    if mp.get(b, 0) == 0:
        mp[b] = id
        id += 1
    if dau == '<':
        d[mp[a]] += 1
        ke[mp[b]].append(mp[a])
    else:
        d[mp[b]] += 1
        ke[mp[a]].append(mp[b])

q = deque()
for i in range(1, id):
    if d[i] == 0:
        q.append(i)
cnt = 0
while len(q) > 0:
    v = q[0]
    q.popleft()
    cnt += 1
    for x in ke[v]:
        d[x] -= 1
        if d[x] == 0:
            q.append(x)
if cnt == id - 1:
    print("possible")
else:
    print("impossible")
