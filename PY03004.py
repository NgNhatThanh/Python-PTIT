import re

n = int(input())
mp = {}
for i in range(n):
    s = re.split('[^a-z0-9]', input().lower())
    for w in s:
        if len(w) > 0:
            mp[w] = mp.get(w, 0) + 1
lst = list(mp.keys())
lst.sort(key = lambda x: (-mp[x], x))
for w in lst:
    print(w, mp[w])