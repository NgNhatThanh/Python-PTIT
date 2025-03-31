def solve():
    n, d = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    for i in range(d, n):
        print(lst[i], end = ' ')
    for i in range(d):
        print(lst[i], end = ' ')
    print()
    return


def main():
    t = 1
    t = int(input())
    for T in range(t):
        solve()
    return
main()