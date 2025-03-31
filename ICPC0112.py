import math

maxN = 1000005
nt = [0] * maxN
cnt = [0] * maxN

def sang():
    nt[1] = 1
    for i in range(2, int(math.sqrt(maxN))):
        if nt[i] == 0:
            for j in range(i * i, maxN, i):
                nt[j] = 1
    for i in range(11, maxN):
        cnt[i] = cnt[i - 1]
        if nt[i] == 0 and nt[i - 6] == 0 and (nt[i - 2] == 0 or nt[i - 4] == 0):
            cnt[i] += 1
    return

def solve():
    n = int(input())
    print(cnt[n - 1])
    return


def main():
    sang()
    t = 1
    t = int(input())
    for T in range(t):
        solve()
    return
main()