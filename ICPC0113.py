import math

maxN = 1000005
nt = [0] * maxN
mark = [False] * maxN

def sang():
    nt[1] = 1
    for i in range(2, int(math.sqrt(maxN))):
        if nt[i] == 0:
            for j in range(i * i, maxN, i):
                nt[j] = 1
    for i in range(13, maxN // 2):
        if nt[i] == 0 and check(i) and mark[int(str(i)[::-1])] == False:
            mark[i] = True
    return

def check(n):
    rev = int(str(n)[::-1])
    return rev != n and nt[rev] == 0

def solve():
    n = int(input())
    for i in range(13, n):
        rev = int(str(i)[::-1])
        if mark[i] and rev < n:
            print(i, rev, sep = ' ', end = ' ')
    print()
    return


def main():
    sang()
    t = 1
    t = int(input())
    for T in range(t):
        solve()
    return
main()