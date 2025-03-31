from sys import stdin
import re

lst = stdin.read().splitlines()
res = ''
for s in lst:
    res += s
    if res[-1] not in '.!?':
        res += '.'
ls = re.split('[.!?]', res)
dau = []
for i in range(len(res)):
    if res[i] in '.!?':
        dau.append(res[i])
for i in range(len(ls)):
    if len(ls[i]) > 0:
        w = ls[i].lower().capitalize().split()
        print(*w, end = '')
        print(dau[i])
