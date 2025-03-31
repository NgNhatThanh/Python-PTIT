def solve():
    a, k, n = list(map(int, input().split()))
    d = n // k
    if d == 0:
        print(-1)
    else:
        cnt = 0
        for i in range(1, d + 1):
            if k * i - a > 0:
                cnt += 1
                print(k * i - a, end = ' ')
        if cnt == 0:
            print(-1)
    return


def main():
    t = 1
    # t = int(input())
    for T in range(t):
        solve()
    return
main()