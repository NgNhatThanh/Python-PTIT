def solve(i, mp, lim, str):
    if i == lim:
        if mp['A'] > mp['B'] or mp['B'] > mp['C']:
            return
        if mp['A'] > 0 and mp['B'] > 0:
            print(str)
        return
    for c in 'ABC':
        mp[c] += 1
        solve(i + 1, mp, lim, str + c)
        mp[c] -= 1

n = int(input())
for i in range(3, n + 1):
    mp = {'A': 0, 'B': 0, 'C': 0}
    solve(0, mp, i, '')
