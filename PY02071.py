res = []

def Try(prev, n, lst, sum = 0):
    global res
    if sum > n:
        return
    if sum == n:
        res.append(list(lst))
        return
    for i in range(prev, 0, -1):
        lst.append(i)
        Try(i, n, lst, sum + i)
        lst.pop()

t = int(input())
for _ in range(t):
    n = int(input())
    Try(n, n, [])
    print(len(res))
    for ls in res:
        print('(', end = '')
        print(*ls, end = ') ')
    print()
    res.clear()
